//3 - Exercicios de decisão JavaScript //Instruções

//Exercício 1: Verificar se um número é par ou ímpar.
//Descrição: Dado um número estático (ex: let numero = 7;), crie uma estrutura de decisão que verifique se ele é par ou ímpar e exiba o resultado no console.

function testePar(Number) {
if (Number % 2 === 0) {
    console.log("Number " + Number + " é par.")
 } else {
    console.log("Numero " + Number + " é impar.")
 }
}
testePar(30)
testePar(50)