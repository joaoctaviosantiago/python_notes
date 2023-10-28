# Capítulo 3: Tipos de dados collections

Existem tipos de dados mais avançados chamados de ```collections```, que funcionam como contêineres que pode armazenar um ou mais dados de tipos variados. Neste capítulo nós falaremos das collections que já vem com python, chamadas de _built-in collections_.

## Pensando como um programador

Antes de começarmos a ver o conteúdo de mais um capítulo, eu gostaria de falar sobre como pensar com um programador. E o que isso quer dizer, exatamente?

Bem, a cada exercício, nós estamos resolvendo problemas mais complexos. Nós começamos com problemas que só precisavam de variáveis e tipos de dados para serem resolvidos; depois resolvemos problemas que combinavam estes com controle de fluxo. Nós estamos aprendendo ferramentas e técnicas isoladas que podem ser combinadas para resolver um problema maior.

E é a isto que me refiro quando digo "pensar como um programador". Eu quero que você aprenda a olhar para problemas com outros olhos. Quero que divida problemas complexos em problemas menores, que possam ser resolvidos com as ferramentas que você tem a sua disposição.

Quando encontramos um problema grande e complexo, normalmente não sabemos nem por onde começar a resolvê-lo. O que devemos fazer é dividi-lo em problemas menores, de resolução mais simples, e resolvermos um por um; pedacinho por pedacinho.

Uma técnica bem útil pra este objetivo é utilizar o ```TODO```, que pode ser traduzido como "para fazer". Imagine que você foi contratado para fazer um programa. O primeiro passo, é definir quais serão as funcionalidades dele (dividindo um problema grande e complexo em problemas menores) e, para cada funcionalidade, definimos os ```TODO```, ou seja, definimos o que cada funcionalidade fará, quantas variáveis vai precisar, de que tipos de dados, como o controle de fluxo será, e assim sucessivamente.

Eu espero que, a partir de agora, você passe a olhar todos os problemas desta maneira. Pensando em quais passos você terá que dar para resolvê-los. E olhar para o que estamos aprendendo como novas ferramentas e novas maneiras de fazer o mesmo. Existem diversas formas de resolver o mesmo problema e cada um usará as ferramentas de sua maneira.

---

## Lista | List

A lista é um tipo de dado que contém um ou mais elementos ordenados. Dentro de uma lista nós podemos ter strings, números, outra listas, entre outros.

```python
my_list = ['Hello', 'World', 1, 2.0, 3]
print(my_list)
```

![[32 - lists_1.png]]

Neste exemplo temos uma lista com 5 elementos de diversos tipos. Quando a imprimimos, python imprime a lista inteira, incluindo os colchetes.

> **_Nota:_** Python reconhece uma lista por causa dos colchetes.

Antes de vermos exemplos práticos de uso de uma lista, primeiro precisamos aprender a manipulá-la.

### Acessando uma lista
#### Acessando os elementos da lista

Como falamos anteriormente, listas são ordenadas, ou seja, todos os elementos de uma lista estão em uma posição fixa dentro dela. Sabendo disso, nós podemos acessá-los através de seu índice (index em inglês).

```python
my_list = ['Hello', 'World', 1, 2.0, 3]
# indice:    [0]      [1]   [2] [3] [4]
print(my_list[0])
```

Aqui estamos dizendo para python imprimir o elemento que se encontra na posição 0 dentro da lista.

![[33 - list_index.png]]

> **_Importante:_** O índice sempre começa em 0. Então, numa lista de 5 elementos, nós teremos os índices 0, 1, 2, 3, 4. índices são sempre ```Int```.


#### Acessando lista dentro de uma lista

Como falamos anteriormente, uma lista pode conter elementos de qualquer tipo, incluindo ```lists``` , ```dictionaries``` e outros tipos de dados que veremos mais à frente.

```python
names_and_numbers = [['Rebeca', 'Chelsey', 'Caroline'], [21, 73, -102]]  
print(names_and_numbers[0])
```

Quando tentamos acessar o índice 0 da lista ```names_and_numbers```, python imprimirá a lista de nomes.

![[34 - list_names.png]]

Então como eu acesso a string ```'Rebeca'```?

```python
print(names_and_numbers[0][0])
```

Primeiro acessamos o elemento no índice 0 da lista ```names_and_numbers```, que é a lista de nomes, depois acessamos o elemento de índice 0 nela.

![[35 - list_rebeca.png]]

#### Acessando o ultimo elemento

Python lê os elementos de uma lista da esquerda pra direita.

```python
fruits = ['Apple', 'Banana', 'Grape', 'Strawberry', 'Orange']
#            [0]      [1]      [2]        [3]          [4]
```

Quando passamos um índice negativo, python passa a ler a lista da direita para a esquerda.

```python
fruits = ['Apple', 'Banana', 'Grape', 'Strawberry', 'Orange']
#           [-5]     [-4]      [-3]       [-2]        [-1]
```

Sendo assim, o elemento de índice ```-1``` é o ultimo elemento da lista.

### Modificando uma lista

Agora que nós sabemos como acessar cada elemento dentro de uma lista, vamos ver como modificá-los.

#### Substituindo elementos

Para substituir um elemento na lista, nós primeiro acessamos o elemento e então atribuímos um valor, como fizemos com variáveis anteriormente.

```python
fruits = ['Apple', 'Banana', 'Grape']
fruits[0] = 'Orange'
print(fruits)
```

![[36 - replacing_list_elements.png]]

#### Adicionando elementos no final

Para adicionar elementos no final de uma lista, nós utilizamos o método ```list_name.append()```.

```python
fruits = []
fruits.append('Orange')
fruits.append('Banana')
fruits.append('Grape')
print(fruits)
```

Neste exemplo, estamos criando uma lista vazia chamada ```fruits``` e, a seguir, utilizamos o método ```append()``` para adicionar elementos no seu final, resultando em:

![[37 - append.png]]

> **_Nota:_** Nós estudaremos métodos a fundo posteriormente. Por enquanto, apenas aprenda a usá-los.

#### Adicionando elementos em posições específicas

O método que utilizamos para adicionar um elemento em uma lista em uma posição especifica é o ```insert()```. Ao utilizá-lo, nós precisamos passar o índice e o dado que queremos adicionar.

```python
fruits = ['Orange', 'Banana', 'Grape']  
fruits.insert(1, "apple")  
print(fruits)
```

Nós estamos dizendo para python adicionar a ```string "apple"``` no índice 1 da lista ```fruits```. É importante ressaltar que python não vai substituir "Banana" por "apple", ele vai empurrar banana pra frente e adicionar "apple" onde "Banana" estava.

![[38 - insert.png]]

#### Removendo elementos por índice

Para remover elementos de uma lista nós utilizamos o comando ```del```.

```python
fruits = ['Orange', 'Banana', 'Grape']  
del fruits[1]  
print(fruits)
```

![[39 - del.png]]

Com o comando ```del``` nós simplesmente deletamos o elemento da lista.

#### Removendo e atribuindo um elemento da lista com pop()

O método ```pop()``` tem 3 usos. Ele pode:

1. remover o ultimo elemento da lista
2. remover um elemento específico da lista
3. remover o elemento e atribuí-lo a uma variável

Quando apenas utilizamos o método ```pop()```, ele removerá o ultimo elemento da lista:

```python
fruits = ['Orange', 'Banana', 'Grape']  
fruits.pop()  
print(fruits)
```

![[40 - pop_1.png]]

Quando passamos o índice do elemento como argumento, ele removerá o elemento especifico. No exemplo a seguir, removeremos o elemento do índice 0:

```python
fruits = ['Orange', 'Banana', 'Grape']  
fruits.pop(0)  
print(fruits)
```

![[41 - pop_2.png]]

Quando queremos remover o item de uma lista e atribuí-lo a uma variável, também utilizamos o ```pop()```

```python
fruits = ['Orange', 'Banana', 'Grape']  
my_favorite_fruit = fruits.pop(1)  
print(fruits)  
print(my_favorite_fruit)
```

Neste último caso, nós não estamos apenas acessando o elemento na lista e atribuindo-o à variável. Nós estamos removendo ```'Banana'``` e atribuindo à variável ```my_favorite_fruit```

![[42 - pop_2.png]]

#### Removendo um elemento por valor

Até agora só vimos maneiras de remover um elemento por índice.  Mas e quando sabemos o valor e não sabemos onde ele se encontra na lista? Para estes casos, utilizamos o método ```remove()```.

```python
fruits = ['Orange', 'Banana', 'Grape']  
fruits.remove('Banana')  
print(fruits)
```

![[43 - remove.png]]

Aqui estamos dizendo para python encontrar a palavra 'Banana' na lista e removê-la.

> **_Importante:_** O método ```remove()``` remove apenas o primeiro elemento com este valor!

```python
fruits = ['Orange', 'Banana', 'Grape', 'Banana']  
fruits.remove('Banana')  
print(fruits)
```

![[44 - remove_2.png]]

#### Combinando listas

Listas podem ser concatenadas, ou combinadas, com o operador ```+```:

```python
numbers = [1, 2, 3]  
animals = ['cat', 'dog', 'capybara']  
  
numbers_and_animals = numbers + animals  
  
print(numbers_and_animals)
```

![[45 - list_concatenation_1.png]]

#### Repetindo os valores

Quando multiplicamos uma lista por uma ```int```, repetimos seus elementos dentro dela, como vemos abaixo:

```python
animals = ['cat', 'dog', 'capybara']  
print(animals * 2)
```

![[46 - list_multiplication_1.png]]

### Loops e listas

Agora que já sabemos como manipular uma lista, nós podemos falar do seu verdadeiro poder. Nós podemos utilizar um loop para iterar por todos os elementos da lista e executar um bloco de código para cada um dos elementos. Calma, eu sei que tá começando a soar complicado de novo. Então vamos ver isso com calma.

Imagina que nós temos uma lista de nomes de convidados para uma festa. Nós queremos criar um programa que dirá "Olá" para todos os convidados. Com o que aprendemos até agora, fazer algo assim seria muito trabalhoso.

```python
print("Hello, Joseph!")
print("Hello, Johnny!")
print("Hello, Richard!")
print("Hello, Sabine!")
print("Hello, Jessica!")
```

Já que estamos lidando com uma grande quantidade de valores, podemos utilizar loops e listas em conjunto para lidar com isso.

```python
names = ["Joseph", 'Johnny', 'Richard', 'Sabine', 'Jessica']  
  
for name in names:  
    print(f"Hello, {name}!")
```

Neste código, o ```for``` loop vai começar e em sua primeira iteração, pegará o primeiro valor em ```names``` e atribuirá à variável ```name```, ou seja, na primeira iteração ```name = "joseph"```, python imprimirá a mensagem na tela, e o loop voltará ao começo, na segunda iteração, ```name = "Johnny"```, e assim sucessivamente até chegar ao final da lista, resultando em:

![[47 - loops_and_lists_1.png]]

Caso ainda não tenha ficado claro, tente ler o código da seguinte maneira: "para cada nome em ```names```, faça:".

Como você pode ver, com poucas linhas de código nós podemos modificar diversos valores de uma única vez combinando listas e loops!

### Os operadores ```in``` e ```not in```

Nós usamos os operadores ```in``` e ```not in``` para checar se um valor está na lista ou não, respectivamente.

```python
names = ["Joseph", 'Johnny', 'Richard', 'Sabine', 'Jessica']  
  
if "Johnny" in names:  
    print("yay")
```

Este código checa se a ```string``` "Johnny" faz parte da lista ```nomes``` e imprime "yay" caso faça.

![[48 - in_operator.png]]

```python
names = ["Joseph", 'Johnny', 'Richard', 'Sabine', 'Jessica']  

if "Rebeca" not in names:  
    print("boo")
```

Já este, checa se a ```string``` "Rebeca" não faz parte da lista ```names``` e, caso não faça, imprime "boo" na tela.

![[49 - not_in_operator.png]]

> **_Importante:_** Letras maiúsculas e minúsculas são vistas como diferentes pelo computador. Sendo assim ```"Rebeca"``` não é a mesma coisa que ```rebeca```.

### List Slices

Nós já sabemos como acessar um elemento dentro de uma lista, ou acessar todos os elementos de uma lista. Mas e quando nós quisermos acessar apenas alguns elementos dentro da lista? Uma opção seria criar um ```for```loop e utilizar condições para determinar quais elementos serão selecionados. Mas python nos permite fazer isso de uma forma: utilizando list slices.

```python
names = ["Joseph", 'Johnny', 'Richard', 'Sabine', 'Jessica']  
  
print(names[2:5])
```

Neste bloco de código, nós estamos dizendo à python para imprimir os elemento na lista ```names``` do índice 2 até o 5, não incluso, ou seja, índices 2, 3 e 4.

![[50 - list_slices_1.png]]

List slices funcionam da mesma forma que a função ```range()``` que aprendemos anteriormente.

```python
list_name[começo:fim:passo]
```

> **_Nota:_** O valor padrão para ```passo``` é 1, o que significa "de um em um".

> **_Importante:_**  Não esquecer que o slice vai de um número até o outro sem incluí-lo. Se eu digo ```[0:3]```, eu estou dizendo do 0 até o 3 sem incluí-lo, ou seja, 0, 1, 2.

Quando não colocamos um valor para o começo, estamos dizendo "comece do índice 0".

```python
numbers = [10, 20, 30, 40, 50, 60]  
my_lucky_numbers = numbers[:3]  
  
print(my_lucky_numbers)
```

Neste bloco de código nós temos um variável do tipo ```list``` chamada ```numbers```, e estamos criando uma nova variável chamada ```my_lucky_numbers``` que também será uma lista, e estamos atribuindo a ela os elementos do começo da lista ```numbers``` até o elemento de índice 3, não incluso.

![[51 - list_slices_2.png]]

Quando não colocamos um valor para o fim, estamos dizendo "vá até o final".

```python
numbers = [10, 20, 30, 40, 50, 60]  
my_lucky_numbers = numbers[2:]  
  
print(my_lucky_numbers)
```

![[52 - list_slices_3.png]]

Você consegue me dizer o que o bloco de código no próximo exemplo faz?

```python
numbers = [10, 20, 30, 40, 50, 60]  
my_lucky_numbers = numbers[::2]  
  
print(my_lucky_numbers)
```

Para descobrirmos, precisamos lembrar que list slices funcionam com três valores ```[começo:fim:passo]```. Não passamos nenhum número para o começo, então estamos dizendo "comece do índice 0"; também não passamos nenhum número para o fim, o que quer dizer "vá até o final"; e, por fim, estamos dizendo para ir de 2 em 2. Este código então irá ler toda a lista e atribuirá à ```my_lucky_numbers``` os elementos de índice 0, 2 e 4.

![[53 - list_slices_4.png]]

### Métodos mais comuns

Posteriormente nós veremos com calma o que são métodos e como criá-los. Por enquanto, só precisamos saber que eles são chamados utilizando a "Notação de ponto", em inglês, "Dot Notation", que nós já utilizamos:

```python
numbers = []
numbers.append(1)
```

Como podemos ver, dot notation nada mais é do que utilizar um ponto para chamar um método. Nós veremos outros métodos antes de aprender como criá-los, e todos eles serão chamados através da dot notation.

#### index()

O método ```index()``` retorna, ou seja, têm como resultado, o índice de um elemento da lista.

```python
names = ["Joseph", 'Johnny', 'Richard', 'Sabine', 'Jessica']  
jessica_index = names.index("Jessica")  
print(jessica_index)
```

![[54 - index_method.png]]

#### sort()

O método ```sort()``` organiza uma lista, seja em ordem do menor para o maior ou em ordem alfabética.

```python
names = ["Joseph", 'Johnny', 'Richard', 'Sabine', 'Jessica']  
names.sort()  
print(names)
```

![[55 - sort_method_1.png]]

Nós também podemos organizar a lista de maneira reversa com ele:

```python
names = ["Joseph", 'Johnny', 'Richard', 'Sabine', 'Jessica']  
names.sort(reverse=True)  
print(names)
```

![[56 - sorte_method_2.png]]

#### reverse()

O método ```reverse()``` reverte a ordem da lista.

```python
names = ["Joseph", 'Johnny', 'Richard', 'Sabine', 'Jessica']  
names.reverse()  
print(names)
```

![[57 - reverse_method.png]]

### função sorted()

A função ```sorted()``` organiza a lista sem alterar a original.

```python
names = ["Joseph", 'Johnny', 'Richard', 'Sabine', 'Jessica']  
  
print(f"Sorted: {sorted(names)}")  
print(f"Original: {names}")
```

![[58 - sorted_function.png]]

### função len()

A função ```len()``` verifica a quantidade de elementos em uma lista

```python
numbers = [1, 2, 3, 4, 5, 6]  
length_of_list = len(numbers)  
print(length_of_list)
```

![[59 - len_function.png]]

> **_Importante:_** Esta função também pode ser utilizada com outros tipos de dados, como ```dictionary```, ```tuple```, ```string```, entre outros.

### Embelezando listas

Pode acontecer de nossas listas serem muito grandes ou com muitos elementos, o que as tornam difíceis de ler. Nestes casos, podemos escrever a lista de uma maneira um pouco diferente, para facilitar a leitura.

```python
hello_list = [  
    "hello",  
    "World",  
    "This",  
    "Is",  
    "Doggo"  
]
```

A lista continuará funcionando perfeitamente.

> **_Importante:_** Não se esqueça da vírgula entre os elementos!

### Exercícios 5

1. Crie um programa que, dada a lista abaixo, encontre o maior e o menor número e imprima-os na tela.

```python
numbers = [191, 78, 67, 195, 51, 154, 28, 45, 186, 106]
```

2. Crie um programa que imprima a lista abaixo sem nenhum número repetido e em ordem crescente:

```python
numbers = [6, 2, 5, 6, 2, 7, 1, 9, 1, 7, 6, 4, 2, 6]
```

3. Ainda utilizando a lista anterior, crie um programa que ache o número que mais se repete na lista, imprima-o na tela, juntamente com quantas vezes ele se repete.

---

## Revisitando strings

Nós já sabemos o que são ```strings``` e como elas funcionam, entretanto, agora que aprendemos mais conceitos, podemos olhá-las de uma outra maneira. ```Strings``` são como listas de caracteres alfanuméricos. Sendo assim, nós podemos, por exemplo, acessar cada caractere através do seu índice:

```python
word = "hello"  
print(word[0])
```

aqui nós estamos acessando o elemento de índice 0 na ```string```.

![[60 - string_list_1.png]]

Nós também podemos acessar os elementos da ```string``` utilizando um ```for``` loop:

```python
word = "hello"  
  
for letter in word:  
    print(letter, end=" ")
```

![[61 - string_list_2.png]]

Ou usar a função ```len()``` para descobrir quantos elementos há na ```string```:

```python
word = "hello"  
  
letters = len(word)  
print(letters)
```

![[62 - string_list_3.png]]

Porém, ```string``` é um tipo de dado diferente de ```list```. Por conta disto, ele tem métodos diferentes. Neste módulo, nós veremos algumas outras formas de manipulação e métodos relacionados à ```string```.

### Aspas triplas

As ```string``` que vimos até agora estavam todas em uma unica linha. Nós podemos utilizar o que aprendemos até agora para construir strings com várias linhas, como, por exemplo, com quebras de linha, concatenação, ou até mesmo diversos ```print()```. Existe, porém, uma outra forma: as aspas tripas.

```python
text = """My dear,  
  
I'm sending you this text because I will not be able to get there on time. I'm stuck in traffic.  
Save me some cake!  
  
Love,  
me.  
"""

print(text)
```

![[63 - triple_quotes.png]]

> **_Nota:_** Podem ser usadas aspas únicas ```'''```  ou duplas ```"""```

### Raw strings

Nós vimos que podemos ignorar caracteres e adicionar caracteres especiais utilizando a barra inversa, ou _escape character_. Mas e se nós quisermos que o que quer que seja digitado pelo usuário seja mantido na ```string```, incluindo barras inversas. É aqui que entram as raw strings or ```r string```.

```python
print(r"hello, \"my friends\"!")
```

![[64 - raw_string.png]]

Na ```r string``` python trata tudo na string como parte dela, mesmo que você tente passar caracteres especiais.

### Métodos mais comuns

Existem outros métodos e você pode encontrá-los na documentação oficial,  livros, procurando no google ou perguntando a inteligências artificiais. Estes são apenas os mais comumente usados.

#### upper()

O método ```upper()``` faz com que as letras das palavras fiquem maiúsculas.

```python
name = "Fatma"  
name = name.upper()  
  
print(name)
```

Aqui nós estamos criando uma varável do tipo ```string``` com o valor "Fatma", depois estamos atribuindo à variável ```name``` o valor original modificado para que todas as letras estejam maiúsculas.

![[65 - upper_method.png]]

#### lower()

O método ```lower()``` faz com que as letras fiquem minúsculas.

```python
name = "Fatma"  
name = name.lower()  
  
print(name)
```

![[66 - lower_method.png]]

#### isupper() e islower()

Checam se os caracteres da ```string``` são todos maiúsculos ou minúsculos, respectivamente.

```python
word1 = "HELLO"  
word2 = "WORLD"  
  
print(f"{word1} is upper? = {word1.isupper()}")  
print(f"{word2} is lower? = {word2.islower()}")
```

![[67 - isupper_islower.png]]

#### capitalize()

Transforma a primeira letra da ```string``` em maiúscula.

```python
text = 'rodrigo has a blue car.'  
text = text.capitalize()  
  
print(text)
```

![[68 - capitalize_method.png]]

#### title()

Transforma todas as palavras da ```string```, colocando todas com letras maiúsculas.

```python
name = "james bond"  
name = name.title()  
  
print(name)
```

![[69 - title_method.png]]

#### startswith() and endswith()

Checam se o a ```string``` começa ou termina com os argumentos passados para eles, respectivamente.

```python
message = "Hello, world! I'm here to learn how to code in python."  
  
print(message.startswith("Hello"))  
print(message.endswith("world"))
```

![[70 - startswith_endswith.png]]

#### split()

O método ```split()``` pode separa uma string em elementos e retorna uma lista

```python
message = "Python is so much fun. I wish I had learned it sooner"  
message = message.split()  
  
print(message)
```

![[71 - split_method.png]]

Por padrão, ele separa a string pelos espaços, mas nós podemos alterar este comportamento passando o argumento pelo qual queremos separar a string. A seguir, vamos separar a mesma ```string``` pelo ponto final.

```python
message = "Python is so much fun. I wish I had learned it sooner"  
message = message.split(".")  
  
print(message)
```

![[72 - split_method_2.png]]

#### strip(), rstrip() and lstrip()

Os métodos ```strip()```, ```rstrip()``` e ```lstrip()``` removem elementos da string. ```strip()``` remove elementos dos dois lados, ```rstrip()``` remove apenas do lado direito e ```lstrip()``` remove apenas do lado esquerdo. Por padrão, eles removem espaços em branco no começo, no final ou em ambos os lados da string.

```python
message = "     hello, world!       "  
  
print(f"strip: {message.strip()}")  
print(f"rstrip: {message.rstrip()}")  
print(f"lstrip: {message.lstrip()}")
```

![[73 - strip_method.png]]

Porém, é possível passar como argumento o elemento que gostaríamos de remover. Talvez seu uso fique mais claro com o exemplo abaixo:

```python
message = "______hello, world!______"  
  
print(f"strip: {message.strip('_')}")  
print(f"rstrip: {message.rstrip('_')}")  
print(f"lstrip: {message.lstrip('_')}")
```

![[74 - strip_method_2.png]]

#### replace()

Este método troca um elemento da ```string``` por outro. Ele recebe dois argumentos: a palavra que você quer trocar e por qual você quer trocar.

```python
text = "oh no, my cat ate all my food!"  
print(text)  
  
text = text.replace("cat", "dog")  
# troca a palavra "cat" na string por "dog"
print(text)
```

![[75 - replace_method.png]]

#### join()

O método ```join()``` recebe uma lista ou tuple como argumento e concatena cada elemento usando a string como separador.

```python
words = ["Hello", "my", "friend", "Doug"]  
phrase = " - blah - ".join(words)  
print(phrase)
```

![[76 - join_method_1.png]]

Eu concordo que pareça um método um pouco estranho. Mas talvez um outro exemplo deixe seu uso mais claro. Imagine que você tem uma ```list``` e deseja colocar todos os seus elementos dentro de uma ```string```, separados por espaço.

```python
words = ["Hello", "world", "this", "is", "dog"]  
phrase = " ".join(words)  
print(phrase)
```

Python pegará cada uma das palavras com a ```string``` que passamos, neste caso, um espaço vazio ```" "```.

![[77 - join_method_2.png]]

#### count()

O método ```count()``` recebe uma ```string``` argumento e conta quantas vezes este argumento aparece na frase, semelhante ao programa que criamos no exercício 5-3.

```python
text = "oh no, my cat ate all my food!"  
  
my_counter = text.count("my")  
print(my_counter)
```

a palavra "my" aparece duas vezes na ```string``` dada.

![[78 - count_method.png]]

### Exercise 6

1. Crie um programa que recebe uma string do usuário e imprima na tela a mesma string, mas com a primeira metade toda em letras maiúsculas e a segunda metade toda em letras minúsculas.
2. Crie um programa que receba uma frase do usuário e imprima na tela a frase ao contrário. Ex: "Olá mundo" -> "mundo Olá"
3. Crie um programa que verifica se a palavra ou frase digitada pelo usuário é um palíndromo (palavra ou frase que se pode ler, indiferentemente, da esquerda para a direita ou vice-versa).

---

## Compreensão de lista | List comprehension

List comprehension é uma forma mais concisa de se criar listas, e é encontrada em apenas algumas linguagens. Em uma única linha, nós podemos criar um ```for``` loop, adicionar os elementos na lista e até utilizar condições.

Normalmente, nós criaríamos uma lista da seguinte maneira:

```python
numbers = []  
  
for number in range(1, 11):  
    numbers.append(number)  
  
print(numbers)
```

![[79 - list_comprehension_1.png]]

Porém, com list comprehension, nós podemos escrever a mesma coisa em apenas uma linha:

```python
numbers = [number for number in range(1, 11)]  
print(numbers)
```

![[80 - list_comprehension_2.png]]

O que nós estamos fazendo aqui? Primeiro, criamos uma variável ```numbers``` e dentro dos colchetes é onde colocamos a list comprehension. Ali, temos ```number for number in range(1, 11) ```, ou seja, adicione ```number``` à lista para cada valor de ```number``` de 1 até 11 (não incluso).

> **_Nota:_** O primeiro ```number``` dentro da list comprehension é a variável que será adicionada à lista.

Uma outra forma de **ler** a list comprehension é a seguinte:

```python
numbers = [numbers.append(number) for number in range(1, 11)]
```

A primeira variável dentro da list comprehension será adicionada à lista sendo criada.

Vamos ver outros exemplos. Criaremos uma lista apenas com números pares de 1 até 20 (não incluso).

Sem list comprehension:

```python
numbers = []  
  
for number in range(1, 20):  
    if number % 2 == 0:  
        numbers.append(number)  
  
print(numbers)
```

![[81 - list_comprehension_3.png]]

Com list comprehension:

```python
numbers = [number for number in range(1, 20) if number % 2 == 0]  
print(numbers)
```

![[82 - list_comprehension_4.png]]

No exemplo abaixo temos uma lista de nomes e queremos criar outra lista apenas com os nomes começados com a letra a.

Sem list comprehension:

```python
names = ["João", "Alice", "Janaína", "Ana", "Bruna", "Eduarda"]  
names_with_a = []  
  
for name in names:  
    if name.startswith('A'):  
        names_with_a.append(name)  
  
print(names_with_a)
```

![[83 - list_comprehension_5.png]]

Com list comprehension:

```python
names = ["João", "Alice", "Janaína", "Ana", "Bruna", "Eduarda"]  
names_with_a = [name for name in names if name.startswith('A')]  
print(names_with_a)
```

![[84 - list_comprehension_6.png]]

### Exercícios 7

> **_Nota:_** Utilize _list comprehension_ para resolver estas questões.

1. Dadas as listas abaixo, crie um programa que imprima na tela uma lista apenas com os números em comum entre elas.

```python
first_list = [2, 7, 33, 27, 92, 40, 3, 28, 56]  
second_list = [90, 12, 23, 7, 38, 29, 56, 13, 2]
```

2. Crie um programa que gere uma lista de 'par' ou 'ímpar'  para cada número de 1 até 20 (não incluso). Ex: \[ímpar, par, ímpar, par...]
3. Crie um programa que peça ao usuário uma frase e imprima uma lista de todas as palavras com 4 letras ou menos.

---

## Dicionário | Dictionary

```Dictionary``` é um tipo de dado que guarda diversos elementos, assim como uma lista, e são utilizados para guardar elementos que estão relacionados entre si. Eles são armazenados em pares chamados de "key" (palavra-chave) e "value" (valor), separados por dois pontos ```:```. Para criá-los, utilizamos chaves em vez de colchetes.

```python
# person = {key: value, key: value, key: value, ...}
person = {'name': 'Mario', 'age': 25, 'location': 'Mushroom Kingdom'}
```

Além de ser criado com chaves em vez de colchetes, outra grande diferença é que para acessarmos um valor, nós não usamos um índice numérico, nós usamos as palavras-chave.

```python
person = {'name': 'Mario', 'age': 25, 'location': 'Mushroom Kingdom'} 
print(person['name'])  
print(person['age'])
```

![[85 - dictionary_1.png]]

Uma outra diferença é que os elementos de um ```dictionary``` são desordenados, enquanto os de uma lista são ordenados.

```python
my_list = [1, 2, 3]  
my_other_list = [3, 2, 1]  
print(my_list == my_other_list)
```

Neste caso, o resultado é ```False``` pois os valores de alguns índices são diferentes. Listas são ordenada, ou seja, a ordem de cada valor é importante.

```python
my_dict = {'first': 1, 'second': 2, 'third': 3}  
my_other_dict = {'second': 2, 'third': 3, 'first': 1}  
print(my_dict == my_other_dict)
```

Já aqui, o resultado é ```True``` pois listas não são ordenadas. Python não se importa com a ordem dos elementos, apenas que eles sejam iguais.

### Acessando elementos

Apesar de termos acabado de ver como acessar os elementos de um ```dictionary```, eu quero explicar novamente para que, caso você queira relembrar, consiga encontrar facilmente.

Nós acessamos os elementos de um ```dictionary``` através das palavras-chave.

```python
doggo = {"name": "Nugget", "age": 3, "breed": "Golden Retriever"}
```

Neste ```dictionary``` nós temos 3 palavras-chave - ```name```, ```age``` e ```breed``` - e nós as usaremos para acessar seus respectivos valores.

```python
doggo = {"name": "Nugget", "age": 3, "breed": "Golden Retriever"} 

print(f"Name: {doggo['name']}")  
print(f"Age: {doggo['age']}")  
print(f"Breed: {doggo['breed']}")
```

![[86 - dict_accessing_elements.png]]

### Modificando um dicionário

#### Adicionando elementos

Para adicionar elementos, precisamos passar a palavra-chave a ser adicionada e seu respectivo valor:

```python
doggo = {"name": "Nugget", "age": 3, "breed": "Golden Retriever"}  
  
doggo["favorite_toy"] = "bone"  
print(doggo)
```

A palavra-chave "favorite_toy" não existe no ```dictionary```, então python adiciona a mesma e atribui a ela o valor de "bone".

![[87 - dict_adding_elements.png]]

#### Modificando elementos

Para modificar elementos, apenas atribuímos um novo valor ao mesmo.

```python
doggo = {"name": "Nugget", "age": 3, "breed": "Golden Retriever"}  
  
doggo["name"] = "Dorito"
print(doggo)
```

![[88 - dict_modifying_elements.png]]

#### Deletando elementos

Para deletarmos elementos, utilizamos o comando ```del```.

```python
doggo = {"name": "Nugget", "age": 3, "breed": "Golden Retriever"}  
  
del doggo["breed"]  
print(doggo)
```

![[89 - dict_deleting_elements.png]]

> **_Nota:_** O elemento é permanente deletado. 

### Loops e dicionários

Assim como fizemos com os dados de tipo ```list```, nós podemos utilizar loops para iterar por todos os elementos de um ```dictionary```. Mas, para isso, precisamos utilizar alguns métodos.

#### keys()

Este método nós da acesso apenas às palavras-chave de um ```dictionary```.

```python
catto = {"name": "KitKat", "age": 5, "color": "orange", "weight": 5.0}  

print(catto.keys())
```

![[90 - dict_method_keys_1.png]]

E, assim, podemos utilizar um for loop para acessar todas as palavras-chave.

```python
catto = {"name": "KitKat", "age": 5, "color": "orange", "weight": 5.0}  
  
for key in catto.keys():  
    print(key)
```

![[91 - dict_method_keys_2.png]]

#### values()

Assim como o método ```keys()```, o método ```values()``` nos dá acesso apenas aos valores do ```dictionary```.

```python
catto = {"name": "KitKat", "age": 5, "color": "orange", "weight": 5.0}  
  
print(catto.values())
```

![[92- dict_method_values_1.png]]

E com ele nós podemos utilizar um loop para acessar apenas os valores do ```dictionary```.

```python
catto = {"name": "KitKat", "age": 5, "color": "orange", "weight": 5.0}  
  
for values in catto.values():  
    print(values)
```

![[93- dict_method_values_2.png]]

#### items()

O método ```ìtems()``` nos dá acesso tanto às palavras-chave quanto aos valores.

```python
catto = {"name": "KitKat", "age": 5, "color": "orange", "weight": 5.0}  
  
print(catto.items())
```

![[94 - dict_method_items_1.png]]

Por conta disto, o ```for``` loop é um pouco diferente. Ele tem duas variáveis.

```python
catto = {"name": "KitKat", "age": 5, "color": "orange", "weight": 5.0}  
  
for key, value in catto.items():  
    print(f"Key: {key} -> Value: {value}")
```

![[95 - dict_method_items_2.png]]

Como este loop tem duas variáveis, uma para a palavra-chave (```key```) e a outra para o valor (```value```), nós podemos manipular as duas dentro do ```for``` loop.

> **_Nota:_** Assim como vimos anteriormente, o nome das variáveis passadas no ```for``` loop pode ser qualquer coisa. Eu escolhi "key" e "value".

### Métodos mais comuns

#### get()

O método ```get()``` pode ter um ou dois argumentos.  Quando tentamos acessar uma palavra-chave que não existe dentro do ```dictionary```, python levantará um erro. O método ```get()``` retornará o valor se a palavra-chave existir e, caso não exista, retornará o valor que passarmos como argumento.

```python
items = {"sword": 3, "shield": 1, "dagger": 2, "bow": 1}  
  
print(items.get("bow", 0))
```

Neste exemplo, estamos dizendo para python imprimir o valor da palavra-chave "bow", caso não exista no ```dictionary```, diga que o valor é 0. A palavra-chave existe no ```dictionary```, então python imprime seu valor.

![[96 - dict_method_get_1.png]]

```python
items = {"sword": 3, "shield": 1, "dagger": 2}  
  
print(items.get("bow", 0))
```

Já neste exemplo, a palavra-chave "bow" não existe no ```dictionary```, então python imprimirá o valor padrão (default).

![[97 - dict_method_get_2.png]]

> **_Nota:_** Caso você só passe um argumento, imprimirá o valor se a palavra-chave existir no ```dictionary``` e, caso não exista, imprimirá o valor ```None```, que é um tipo de dado que significa "nenhum valor existente".


#### copy()

Este método permite que nós criemos uma cópia de um ```dictionary```.

```python
items = {"sword": 3, "shield": 1, "dagger": 2}  
new_items = items.copy()  
  
print(f"Items: {items}")  
print(f"New items: {new_items}")
```

![[98 - dict_method_copy.png]]

#### clear()

```clear()``` remove todos os elementos de um ```dictionary```.

```python
items = {"sword": 3, "shield": 1, "dagger": 2}  
  
items.clear()  
print(f"Items: {items}")
```

![[99 - dict_method_clear.png]]

#### setdefault()

O método ```setdefault()``` faz com que o ```dictionary``` sempre tenha determinada palavra-chave e valor.

```python
items = {"sword": 3, "shield": 1, "dagger": 2}  
  
items.setdefault("heartstone", 1)  
print(f"Items: {items}")
```

No exemplo acima, nós definimos que o ```dictionary``` deve ter ao menos 1 "heartstone" obrigatoriamente. Como não colocamos no dicionário, python colocará.

![[100 - dict_method_setdefault().png]]

Caso já existisse uma palavra-chave "heartstone" no ```dictionary``` python não faria nada.

```python
items = {"sword": 3, "shield": 1, "dagger": 2, "heartstone": 3}  
  
items.setdefault("heartstone", 1)  
print(f"Items: {items}")
```

![[101 - dict_method_setdefault()_2.png]]

#### pop()

```pop()``` é um método que recebe uma palavra chave como argumento e remove o elemento do ```dictionary```.

```python
items = {"sword": 3, "shield": 1, "dagger": 2}  
  
items.pop("sword")  
print(f"Items: {items}")
```

![[102 - dict_method_pop().png]]

### Embelezando dicionários

Assim como como dados do tipo ```list```, nós podemos escrever dados do tipo ```dictionary``` de tal maneira que fiquem mais legíveis, como no exemplo abaixo:

```python
person = {  
    "name": "Luigi",  
    "age": 24,  
    "location": "Mushroom Kingdom"  
}  
  
print(person)
```

![[103 - beautifying_dict.png]]

> **_Importante:_** Não esqueça de colocar virgula entre os elementos!

### Exercícios 8

Utilize a lista abaixo para os exercícios 1 e 2:

```python
people = {  
    'James': 30,  
    'Mary': 23,  
    'Robert': 83,  
    'Patricia': 42,  
    'John': 19,  
    'Jennifer': 27,  
    'Michael': 36,  
    'Linda': 65,  
    'David': 76  
}
```

1. Encontre a pessoa mais velha e imprima-o na tela.
2. Encontre a média de idade das pessoas e imprima-a na tela com 2 casas decimais.
3. Você foi contratado para criar um programa para entrevistar 10 pessoas sobre o que preferem, pizza ou sushi. Crie um programa para esta pesquisa que ao final imprima na tela o que a maioria prefere e quantos votos o ganhador recebeu.

## Tuple

Também conhecidas como "tupla" no português, ```tuple``` são dados iteráveis, assim como ```list``` e ```dictionary```. Os elementos de um ```tuple``` são ordenados, então podemos acessá-los com índices, porém, um ```tuple``` é imutável. Uma vez criado, ele não pode ser modificado.

Um ```tuple``` é criado colocando os dados entre parênteses.

```python
numbers = (10, 20, 30)  
  
print(numbers)
```

![[104 - tuple.png]]

> **_Importante:_** Uma ```list``` ou um ```dictionary``` dentro de um ```tuple``` ainda pode ser modificados, porém, a estrutura do ```tuple``` não pode.

### Acessando elementos

Como ```tuple``` é ordenado, seus elementos podem ser acessados através de índices, assim como ```list```.

```python
numbers = (10, 20, 30)  
  
print(numbers[1])
```

![[105 - accessing_tuple.png]]

> **_Importante:_** Os índices começam sempre em 0.

### Tuple slices

Também podemos acessar os elementos de ```tuple``` com slices.

```python
numbers = (10, 20, 30, 40, 50)  
  
print(numbers[:3])
```

![[106 - tuple_slices_1.png]]

```python
numbers = ("Banana", "Apple", "Grape")  
  
print(numbers[::-1])
```

![[107 - tuple_slices_2.png]]

### Métodos

#### count()

Conta a quantidade de vezes que um elemento aparece no ```tuple```.

```python
numbers = (10, 20, 30, 30, 40, 20, 30, 10)  
  
print(numbers.count(30))
``` 

![[108 - tuple_method_count.png]]

#### index()

Mostra o índice do dado passado.

``` python
names = ("George", "Geoff", "Gob")  
  
print(names.index("Geoff"))
```

![[109 - tuple_method_index.png]]

### Unpacking tuple

Unpacking tuple significa colocar cada elemento da ```tuple``` dentro de uma variável. Python nos permite fazer isso de forma bem elegante.

```python
numbers = (10, 20, 30)  
a, b, c = numbers  
  
print(a)  
print(b)  
print(c)
```

![[110 - unpacking_tuple.png]]

### Trocando variáveis

Podemos também trocar o valor de variáveis com ```tuple```. Normalmente, se quiséssemos fazer isso, faríamos da forma abaixo:

```python
a = 10  
b = 20  
  
print(f"a: {a}, b: {b}")  
  
c = a  
a = b  
b = c  
  
print(f"a: {a}, b: {b}")
```

![[111 - swapping_variables_1.png]]

Temos duas variáveis ```a``` de valor 10 e ```b``` de valor 20 e queremos trocar seus valores para que ```a``` seja 20 e ```b``` seja 10. Para isto, criamos uma variável temporária ```c```, depois colocamos o valor de ```a``` em ```c```, o de ```b``` em ```a``` e o de ```c``` em ```b```. É como se tivéssemos dois copos e um com refrigerante de laranja no copo A e outro com refrigerante de uva B, e nós quiséssemos colocar o de uva no A e o de laranja no B. Para isso, nós usaríamos um terceiro copo vazio chamado de C. Colocaríamos o refrigerante de laranja no C, o de uva no copo A e o de laranja, que está no copo C, no copo B.

Com ```tuple``` podemos fazer esta troca de uma maneira muito mais simples.

```python
a = 10  
b = 20  
  
print(f"a: {a}, b: {b}")  
  
a, b = b, a  
  
print(f"a: {a}, b: {b}")
```

![[112 - swapping_variables_2.png]]

### Concatenando tuple

Apesar de não podermos modificar tuples, podemos concatená-las para criar novas tuples.

```python
numbers = (1, 2, 3)
numbers_total = numbers + (4, 5, 6)

print(numbers_total)
```

![[113 - tuple_concatenation.png]]

### Exercícios 9

Utilize a ```tuple``` abaixo para os exercícios:

```python
numbers = (7, 42, 93, 58, 12, 24, 30)
```

1. Imprima os três últimos números.
2. imprima a média de todos os elementos
3. imprima o tuple ao contrário

## Set

```set``` é um tipo de dado iterável que remove elementos duplicados. Seus elementos não são organizados, ou seja, não podemos acessá-los através de índices (é comum os elementos virem em ordens diferentes ao serem impressos).

```python
numbers = {10, 20, 10, 30, 10, 40}  
  
print(numbers)
```

![[114 - set_1.png]]

Como podemos ver, todos os números repetidos foram removidos e a ordem em que foram impressos está diferente da ordem em que o ```set``` foi escrito.






