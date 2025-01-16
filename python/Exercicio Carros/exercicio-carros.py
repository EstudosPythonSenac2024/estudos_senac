'''
Desenvolva um software que modele um carro trazendo suas características como modelo, ano, 
marca, cor. 
Este software deve cadastrar as informações de cada carro e exibir em tela todas as informações 
de cada carro em tela.
Cadastre 10 carros com características diferentes.

Ao terminar, anexar o arquivo com a extensão .py2
'''

import json
import os

class Carro:
    def __init__(self, id_cadastro, modelo, ano, marca, cor, combustivel, quilometragem):
        self.id_cadastro = id_cadastro
        self.modelo = modelo
        self.ano = ano
        self.marca = marca
        self.cor = cor
        self.combustivel = combustivel
        self.quilometragem = quilometragem

    def to_dict(self):
        """Converte o objeto Carro para um dicionário para salvar em JSON."""
        return {
            "id_cadastro": self.id_cadastro,
            "modelo": self.modelo,
            "ano": self.ano,
            "marca": self.marca,
            "cor": self.cor,
            "combustivel": self.combustivel,
            "quilometragem": self.quilometragem
        }

    def __str__(self):
        return (f"{self.id_cadastro} - Modelo: {self.modelo} | Ano: {self.ano} | Marca: {self.marca} | "
                f"Cor: {self.cor} | Combustível: {self.combustivel} | Quilometragem: {self.quilometragem} km")


class SistemaCadastroCarros:
    def __init__(self, arquivo_json="carros.json"):
        self.carros = []
        self.arquivo_json = arquivo_json
        self.carregar_carros()

    def carregar_carros(self):
        """Carrega os carros do arquivo JSON, se ele existir."""
        if os.path.exists(self.arquivo_json):
            with open(self.arquivo_json, "r") as f:
                dados = json.load(f)
                for item in dados:
                    carro = Carro(**item)
                    self.carros.append(carro)

    def salvar_carros(self):
        """Salva os carros no arquivo JSON."""
        with open(self.arquivo_json, "w") as f:
            json.dump([carro.to_dict() for carro in self.carros], f, indent=4)
        print(f"Dados salvos no arquivo '{self.arquivo_json}'.")

    def gerar_id_cadastro(self):
        """Gera um número de cadastro único."""
        if not self.carros:
            return 1
        return max(carro.id_cadastro for carro in self.carros) + 1

    def cadastrar_carro(self):
        modelo = input("Modelo: ")
        ano = input("Ano: ")
        while not ano.isdigit() or len(ano) != 4:
            ano = input("Ano inválido! Insira um ano válido (ex: 2020): ")
        marca = input("Marca: ")
        cor = input("Cor: ")
        combustivel = input("Tipo de combustível (Gasolina, Etanol, Flex, Elétrico): ")
        quilometragem = input("Quilometragem (em km): ")

        while not quilometragem.isdigit():
            quilometragem = input("Quilometragem inválida! Insira um valor numérico: ")

        if modelo and marca and cor:
            id_cadastro = self.gerar_id_cadastro()
            novo_carro = Carro(id_cadastro, modelo, ano, marca, cor, combustivel, quilometragem)
            self.carros.append(novo_carro)
            print(f"Carro cadastrado com sucesso! Número de cadastro: {id_cadastro}")
            self.salvar_carros()
        else:
            print("Modelo, marca e cor são obrigatórios.")

    def exibir_carros(self):
        if self.carros:
            print("\n--- Lista de Carros Cadastrados ---")
            for carro in self.carros:
                print(carro)
            print("\n")
        else:
            print("Nenhum carro cadastrado.")

    def alterar_carro(self):
        if not self.carros:
            print("Nenhum carro cadastrado para alterar.")
            return

        self.exibir_carros()
        opcao = input("Informe o número de cadastro do carro que deseja alterar: ")

        if not opcao.isdigit():
            print("Opção inválida.")
            return

        id_cadastro = int(opcao)
        carro_selecionado = next((carro for carro in self.carros if carro.id_cadastro == id_cadastro), None)

        if not carro_selecionado:
            print("Carro com esse número de cadastro não encontrado.")
            return

        print(f"\nAlterando informações do carro {id_cadastro}:")
        print(carro_selecionado)

        # Atualiza informações
        novo_modelo = input(f"Novo Modelo (atual: {carro_selecionado.modelo}): ") or carro_selecionado.modelo
        novo_ano = input(f"Novo Ano (atual: {carro_selecionado.ano}): ") or carro_selecionado.ano
        while not novo_ano.isdigit() or len(novo_ano) != 4:
            novo_ano = input("Ano inválido! Insira um ano válido (ex: 2020): ") or carro_selecionado.ano

        nova_marca = input(f"Nova Marca (atual: {carro_selecionado.marca}): ") or carro_selecionado.marca
        nova_cor = input(f"Nova Cor (atual: {carro_selecionado.cor}): ") or carro_selecionado.cor
        novo_combustivel = input(f"Novo Combustível (atual: {carro_selecionado.combustivel}): ") or carro_selecionado.combustivel
        nova_quilometragem = input(f"Nova Quilometragem (atual: {carro_selecionado.quilometragem} km): ") or carro_selecionado.quilometragem

        while not nova_quilometragem.isdigit():
            nova_quilometragem = input("Quilometragem inválida! Insira um valor numérico: ") or carro_selecionado.quilometragem

        # Atualizando os atributos
        carro_selecionado.modelo = novo_modelo
        carro_selecionado.ano = novo_ano
        carro_selecionado.marca = nova_marca
        carro_selecionado.cor = nova_cor
        carro_selecionado.combustivel = novo_combustivel
        carro_selecionado.quilometragem = nova_quilometragem

        print("Informações do carro atualizadas com sucesso!")
        self.salvar_carros()

    def menu(self):
        while True:
            print("\n--- Menu de Cadastro de Carros ---")
            opcao = input("1. Cadastrar carro\n2. Exibir carros\n3. Alterar informações de um carro\n4. Sair\nEscolha: ")
            if opcao == "1":
                self.cadastrar_carro()
            elif opcao == "2":
                self.exibir_carros()
            elif opcao == "3":
                self.alterar_carro()
            elif opcao == "4":
                print("Encerrando o sistema.")
                break
            else:
                print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    SistemaCadastroCarros().menu()