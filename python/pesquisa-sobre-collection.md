Em Python, coleções são estruturas de dados que permitem armazenar múltiplos valores em uma única variável. Existem quatro tipos principais de coleções em Python: listas, tuplas, dicionários e conjuntos. Cada um deles possui características distintas, tornando-os úteis em diferentes situações.

## Listas:
Coleção ordenada e mutável de elementos;
Permite armazenar itens duplicados;
Acessados através de índices (0, 1, 2, ...);
Utiliza colchetes [] para criação;
Exemplo:
```
lista = ['palavra', True, 13, 3.2]

print(lista) # ['palavra', True, 13, 3.2]
```
Caso queira acessar um item específico de sua lista, basta informar o índice correspondente dentro de colchetes:
```
lista = ('palavra', True, 13, 3.2)

print(lista) # ['palavra', True, 13, 3.2]
print(lista[1]) # True
```

## Tuplas:
Coleção ordenada e imutável de elementos;
Permite armazenar itens duplicados;
Acessados através de índices (0, 1, 2, ...);
Utiliza parênteses () para criação;

## Exemplo:
```
tupla = ('palavra', True, 13, 3.2)

print(tupla) # ('palavra', True, 13, 3.2)
```
Caso queira acessar um item específico de sua tupla, basta informar o índice correspondente dentro de colchetes:
```
tupla = ('palavra', True, 13, 3.2)

print(tupla) # ('palavra', True, 13, 3.2)
print(tupla[3]) # 3.2
```
## Dicionários:
Coleção ordenada e mutável de pares chave-valor;
Não permite chaves duplicadas, mas valores podem ser repetidos;
Acessados através das chaves, não por índices;
Utiliza chaves {} para criação;

Exemplo:
Caso queira acessar um item específico de seu dicionário, basta informar a chave correspondente ao valor que deseja dentro de colchetes:
```
dicionario = {'string': 'palavra', 'logico': True, 'numero': 13, 'flutuante': 3.2}

print(dicionario) # {'string': 'palavra', 'logico': True, 'numero': 13, 'flutuante': 3.2}

dicionario = {'string': 'palavra', 'logico': True, 'numero': 13, 'flutuante': 3.2}

print(dicionario) # {'string': 'palavra', 'logico': True, 'numero': 13, 'flutuante': 3.2}
print(dicionario['string']) # palavra
```

## Conjuntos (Sets):
Coleção não ordenada e não indexada de elementos;
Não permite itens duplicados;
Não possui acesso através de índices ou chaves;
Utiliza chaves {} para criação, mas sem pares chave-valor;

Exemplo:
Repare que a ordem de inserção dos itens foi mudada ao rodar o programa;
Como não há acesso direto aos itens de um conjunto, ao informar um índice dentro de colchetes, como nos exemplos anteriores, o terminal retorna um erro:

```
conjunto = {'palavra', True, 13, 3.2}

print(conjunto) # {'palavra', True, 3.2, 13}
conjunto = {'palavra', True, 13, 3.2}

print(conjunto)
print(conjunto[2])
```


```
ERROR!
{'palavra', 3.2, 13, True}
Traceback (most recent call last):
File "<string>", line 5, in <module>
TypeError: 'set' object is not subscriptable
```

## Conclusão
Cada tipo de coleção tem suas vantagens e usos específicos.

As listas são usadas quando a ordem dos elementos é importante e quando é necessário modificar a coleção após a criação.

As tuplas são úteis quando se quer uma coleção imutável, por exemplo, para definir coordenadas.

Os dicionários são ideais para associar valores a chaves e fazer buscas rápidas por essas chaves.

Por fim, os conjuntos são úteis quando não precisamos nos preocupar com a ordem e precisamos garantir que os itens sejam únicos.

De maneira simples, podemos dizer que as principais diferenças entre as coleções são:

Listas: Ordenadas, mutáveis e permitem duplicados.
Tuplas: Ordenadas, imutáveis e permitem duplicados.
Dicionários: Ordenados (a partir da versão 3.7), mutáveis e não permitem chaves duplicadas.
Conjuntos: Não ordenados, não indexados e não permitem itens duplicados.
