import os
import subprocess
import csv
import toml
import logging
import re

# Configuração do logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename="process_toml.log",
    filemode="w",  # Sobrescrever o arquivo de log a cada execução
)

def clone_repo(repo_url, target_dir):
    """
    Clona o repositório Git se o diretório não existir.
    """
    if not os.path.exists(target_dir):
        logging.info(f"Diretório '{target_dir}' não encontrado. Clonando o repositório...")
        subprocess.run(["git", "clone", repo_url, target_dir], check=True)
    else:
        logging.info(f"Diretório '{target_dir}' já existe. Pulando o clone.")

def extract_fields(filepath):
    """
    Extrai os campos 'name', 'tags', 'language', 'integration', 'technology' do arquivo TOML em caso de falha.
    """
    name = "N/A"
    tags = []
    language = "N/A"
    integration = ["N/A"]
    technology = os.path.relpath(os.path.dirname(filepath), "detection-rules").replace(os.sep, "/")

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        for line in lines:
            line = line.strip()
            if line.startswith('name ='):
                name = line.split('=', 1)[-1].strip().strip('"')
            if line.startswith('tags = ['):
                tag_block = line
                while not tag_block.strip().endswith(']'):
                    tag_block += next(f).strip()
                tags = re.findall(r'"(.*?)"', tag_block)
            if line.startswith('language ='):
                language = line.split('=', 1)[-1].strip().strip('"')
            if line.startswith('integration ='):
                integration_block = line
                while not integration_block.strip().endswith(']'):
                    integration_block += next(f).strip()
                integration = re.findall(r'"(.*?)"', integration_block)

    except Exception as e:
        logging.warning(f"Erro ao tentar extrair campos no arquivo {filepath}: {e}")

    return name, tags, language, integration, technology

def process_toml_files(directory, output_csv, failed_alerts_csv):
    """
    Processa arquivos TOML em múltiplos diretórios e salva os resultados.
    """
    data = []
    failed_alerts = []

    # Listar todas as pastas para processar
    directories_to_process = [
        os.path.join(directory, "rules"),
        os.path.join(directory, "rules_building_block"),
    ]

    for sub_dir in directories_to_process:
        if not os.path.exists(sub_dir):
            logging.warning(f"Pasta {sub_dir} não encontrada. Pulando.")
            continue

        for root, _, files in os.walk(sub_dir):
            for file in files:
                if file.endswith(".toml"):
                    filepath = os.path.join(root, file)

                    # Extrair campos antes do parsing completo
                    alert_name, alert_tags, alert_language, alert_integration, alert_technology = extract_fields(filepath)

                    try:
                        # Carregar o arquivo TOML completo
                        with open(filepath, 'r', encoding='utf-8') as f:
                            toml_data = toml.load(f)

                        # Processar campos principais
                        name = toml_data.get("rule", {}).get("name", "N/A")
                        language = toml_data.get("rule", {}).get("language", "N/A")
                        integration = toml_data.get("metadata", {}).get("integration", ["N/A"])
                        tags = toml_data.get("rule", {}).get("tags", ["N/A"])
                        technology = os.path.relpath(root, directory).replace(os.sep, "/")

                        # Processar MITRE fields (tactic name)
                        threats = toml_data.get("rule", {}).get("threat", [])
                        threat_names = [threat.get("tactic", {}).get("name", "N/A") for threat in threats if "tactic" in threat]

                        data.append({
                            "name": name,
                            "language": language,
                            "integration": integration,
                            "technology": technology,
                            "tags": tags,
                            "threat_names": threat_names if threat_names else ["N/A"]
                        })

                    except toml.TomlDecodeError as decode_error:
                        # Salvar alerta com falha na ordem especificada
                        failed_alerts.append({
                            "name": alert_name,
                            "language": alert_language,
                            "integration": ", ".join(alert_integration),
                            "technology": alert_technology,
                            "tags": ", ".join(alert_tags),
                        })
                        logging.error(f"Erro ao decodificar TOML no arquivo {filepath}: {decode_error}")

                    except Exception as e:
                        failed_alerts.append({
                            "name": alert_name,
                            "language": alert_language,
                            "integration": ", ".join(alert_integration),
                            "technology": alert_technology,
                            "tags": ", ".join(alert_tags),
                        })
                        logging.exception(f"Erro genérico ao processar {filepath}")

    # Salvar os dados em um CSV principal
    with open(output_csv, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ["name", "language", "integration", "technology", "tags", "threat_names"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow({
                "name": row["name"],
                "language": row["language"],
                "integration": ",".join(row["integration"]),
                "technology": row["technology"],
                "tags": ",".join(row["tags"]),
                "threat_names": "; ".join(row["threat_names"])
            })

    # Salvar alertas com falha em um CSV separado
    with open(failed_alerts_csv, 'w', newline='', encoding='utf-8') as failfile:
        fieldnames = ["name", "language", "integration", "technology", "tags"]  # Ordem desejada
        writer = csv.DictWriter(failfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in failed_alerts:
            writer.writerow(row)

    print(f"Processamento concluído. Dados salvos em {output_csv}.")
    print(f"Alertas com falha registrados em {failed_alerts_csv}.")

# URLs e diretórios
repo_url = "https://github.com/elastic/detection-rules.git"
repo_dir = "detection-rules"
output_csv = "rules_data.csv"
failed_alerts_csv = "failed_alerts.csv"

# Clonar o repositório e processar os arquivos
clone_repo(repo_url, repo_dir)
process_toml_files(repo_dir, output_csv, failed_alerts_csv)

print(f"Dados processados e salvos em {output_csv}.")
print(f"Alertas com falha salvos em {failed_alerts_csv}. Detalhes no arquivo 'process_toml.log'.")