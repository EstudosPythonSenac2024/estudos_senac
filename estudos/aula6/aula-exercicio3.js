//Exercício 3 :Verificar o tipo de triângulo.
//Descrição: Dado três lados de um triângulo (ex: let lado1 = 10; let lado2 = 10; let lado3 = 8;), determine se ele é equilátero (todos os lados iguais), isósceles (dois lados iguais) ou escaleno (todos os lados diferentes) e exiba o tipo no console. */


let lado1 = 0; 
let lado2 = 10; 
let lado3 = 8;

if ( lado1 === lado2 && lado1 === lado3 ) {
    console.log("Equilátero");
} else if ( lado1 != lado2 && lado1 === lado3  || lado1 === lado2 || lado2 === lado3 ) {
    console.log("Isósceles.");
} else if ( lado1 === 0 || lado2 === 0 || lado3 === 0) {
    console.log("Erro: Não existe Triangulo com Valor Zero.")
} else {
    console.log("Escaleno.");
}