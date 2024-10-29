//Exercício 2: Avaliar a aprovação de um aluno.
//Descrição: Considerando duas notas (ex: let nota1 = 7; let nota2 = 5;), calcule a média e use uma estrutura de decisão para exibir se o aluno foi aprovado (média >= 6), em recuperação (média entre 4 e 5.9) ou reprovado (média < 4).

let nota1 = 9;
let nota2 = 9;

let media = (nota1 + nota2) / 2;
if (media > 6) {
    console.log("Aluno aprovado com nota: " + media);
} else if (media >= 4 && media < 6) {
    console.log("Aluno em recuperação com media: " + media);
} else {
    console.log("Aluno foi reprovado: " + media);
}