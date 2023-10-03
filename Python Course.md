# Introduction

## What is programming?

Programming is giving a series of instructions to a computer. This series of instructions is known as Algorithm. Here is an example:

```
take two steps forward,
try opening the door
if it's unlocked, open the dor,
if it isn't, turn left
```

It is fairly common for educators to teach programming using "hands-on examples", in which you're simply copying someone, without actually learning how to think or use the tools at your disposal. I disagree with this approach and prefer to add a little bit of information with each module, expanding our knowledge and teaching the student how to find solutions to problems using the tools they've learned.

---

## Do I need to know math?

A common fear among those who are interested in programming is the _myth_ that you need to know math to program. Yes, I've said _myth_. And the reason why I've said it is that most times programming will not require anything but basic math. It is important to understand that inside the computer science field there are many professions. Some will require a higher knowledge of math, others will barely require any. Just because something involve numbers, it doesn't mean it requires math.

---

## I think I'm too old to learn how to code

Another _myth_ that is very common is that to become a good programmer you need to start learning it very early in life. Programming is something you learn by doing, by practicing. And you'll grow with each day of doing it. No one is born a programmer. It is a skill acquired through study and practice.

---

## Why python?

Python is a general-purpose language, which means it is a language used in many fields, including data, machine learning, software development, web development, automation, among others. On top of this, its syntax is similar to English, which makes it less intimidating than other languages for those who are beginning their journey.

---

## About the course

The course was developed in such way that each module will build on each other. Because of this, everything we see will be utilized in the future, so it is crucial that you do not move to the next module until the topics are well understood. 

We'll cover other topics besides python throughout the course, even if not deeply, because we'll need this knowledge to work on our projects.

Do not limit yourself to the exercises of this course. Programming is like LEGO. It is a creative exercise. In this course you'll learn all the tools and knowledge needed to create everything you can imagine, as well as the ability to learn another programming language.

---

## Bonus: How does a computer work?

Each piece of a computer has a specific job. Here, I want to clarify a little bit about what each of them do, in a superficial manner. This will help us clarify some things later on.

### Motherboard

It connects all the pieces of the computer and made them work together.

### CPU | Processor

It is the brain of the computer. It is capable of processing an enormous amount of information per second.

### GPU | Graphics Card

It processes the images and videos on a computer, such as games, tv-shows, the image in your monitor.

### HDD | SSD | NVMe

This is the long term memory of a computer. The data is **persistent**, which means that even after you turn off the computer, the data on your HD will still exist. It is where you'll store photos, videos, software, games, etc.

### RAM | Random Access Memory

A memória RAM é a _memória de curto prazo_ do computador. Ela é extremamente rápida comparada com o HD, porém, temos uma quantidade menor disponível. Toda vez que rodamos um programa, abrimos um video, fazemos algo, os dados necessários para este programa rodar ficam armazenados na memória RAM, quando fechamos estes programas, eles são removidos da memória. Por conta disso, quando um novo programa é aberto, seus dados serão colocados onde houver espaço disponível. A localização dos dados não é permanente.

### RAM | Random Access Memory

RAM is the _short term memory_ of a computer. It is extremely fast when compared to the speed of an HD, however, it is much smaller in size. When we run a software, open a video, do something, all the data needed to run these things is stored on RAM, when we close these programs, they're removed from memory. Because of that, when you open a new program, its data is placed where there is free space within the RAM. The location of the data is not permanent.

---

## Python download and installation

Python can be downloaded from the [official website](https://www.python.org/downloads/).

> **_Important:_** Download python 3 (or the most updated version) to guarantee that the codes on this course will function correctly.

### Windows

The windows installation is simple, like any other software. Select "Add python.exe to PATH" and then just click "next" and wait.

![[1 - install_python.png]]

> **_Important:_** Check the "Add python.exe to PATH" checkbox before installing.

### MacOS

For the installation on MacOS I recommend this link from [freeCodeCamp](https://www.freecodecamp.org/news/python-version-on-mac-update/). Feel free to use a different source, maybe another website or a youtube video.

### Linux

Python comes installed with most Linux distributions. I do not recommend updating python because some libraries might break due to difference in versions.

---

## IDE installation

Once installed, python can run from the terminal of the computer. However, for the this first part of the course, we'll install an IDE (Integrated Development Environment) to program.

> **_Note:_** You can write your code even on Microsoft Word or Notepad, and execute it from the terminal. An IDE is a software made specifically to run certain languages, coming prepared with everything you need and optimized for this purpose. There are other text editors and IDEs you can use.

### PyCharm Community Edition

I will use PyCharm as my IDE for the first part of the course. The download can be done from [this link](https://www.jetbrains.com/pycharm/download).

> **_Note:_** There are two versions, PyCharm Professional Edition, which is paid, and PyCharm Community Edition, which is free. We'll be using the Community Edition.

Once installed, create a new project and wait a little. The first time a project is created, the IDE requires some time to organize things.

### Visual Studio Code

VSCode is a text editor optimized for coding and it utilizes plugins to improve the life of the programmer. If you are using and older or slower computer, I recommend using VSCode with the python plugin. It is easy to find on google how to install said plugins. The download can be done from [this link](https://code.visualstudio.com/).

Later in the course we'll utilize VSCode for some projects.

---

# Chapter 1: The Basics

## My first program

It is standard that the first thing we make is a little program that says _"Hello, world"_ to confirm that everything works properly, and this is what we're going to do. Write:

```python
print("Hello, world")
```

> **_Note:_** It is important to use quotation marks in the message.

And execute the program by clicking on the **play** button at the top of the screen:

![[2 - play.png]]

This should be the result:

![[3 - hello_world_resultado.png]]

There you go! You'e just made your first python program. Simple, right?

```python
print()
```

Is a function that prints on screen whatever data is between parenthesis.

---

## Variables

A variable is a little space in memory (RAM) where you'll store a data. This data can be a name, a date, a number, etc. It sounds confusing, I know. Let's make it a little clearer using an example. We'll make a variable called ```message```:

```python
message = "Hello, world"
print(message)
```

In this example, we're separating a little space in memory and calling it ```message```,  then we get the data ```Hello, world``` and put it inside of that space. Next, we call the function ```print()``` again:

![[4 - resultado_variable.png]]

As we can see, we have the same result. Python printed the value assigned to the variable ```message```.

> **_Important:_** The equal sign (=) is not the same as the mathematical sign. We'll see the comparative equal sign later. In python (=) is called _"Assign operator"_. It gets a value and assign it to a variable.

Okay, but where is this used? Think of the games you've played. The number of lives, your HP, the name of the characters, their attributes, the ammo. All of this data is stored in variables.

Variables can have any name, however, there are some rules that must be followed when choosing them:

* The name of the variables cannot contain spaces.
* They can only contain letters, numbers and underscores, but they can only begin with a letter or underscore. The names cannot begin with a number.
* The ideal is that names are descriptive and help understand the type of information the variable is storing.
* Avoid using words that are reserved by python, like ```print```.

> **_Note:_** There are some naming conventions. Some of them are:
> 
> * **camelCase**: The first word starts with a lowercase letter and the rest of the words start with an uppercase letter
> * **PascalCase**: The first letter of every word is uppercase
> * **snake_case**: All the words are lowercase and separated by underscores
> * **kebab-case**: All the words are lowercase and separated by a hyphen
> 
> Python recommends snake_case

---

## Python reads code from top to bottom

Programming languages, in general, read code from top to bottom. In the following code, we try to print a variable that has still not been read by python:

```python
print(f"Hello, {nome}")
nome = "João"
```

When we try to run the code, python raises an error:

![[5 - erro.png]]

Here, python gives us some information about where it believes the problem is. It informs us the file and line. Then it says the name of the error it's found:

```
NameError: name 'nome' is not defined. Did you mean: 'None'?
```

It informs us that the word "nome" has not been defined. It doesn't know this word or what it means. Then it asks "Did you mean: 'None'?"

---

## The importance of errors

When python can't understand what you're trying to do, it will raise an error and tell you what is wrong, or try to do so. Read the error carefully and don't be afraid of googling it. As important as learning how to code, it is to learn how to debug, which is the act of fixing problems within your code. 

Nobody knows everything about a language. The more we use it, the more we learn. But even so, it is a very big topic. This is why basically everything in programming is documented. Within the documentation we can find, in detail, how to use certain tools and how the language runs behind the scenes.

Besides google and stackoverflow, now we also have the aid of AIs such as ChatGPT, among others, to help with programming. They're excellent tools that will explain and help you write code.

> **_Important:_** It is common to see students copying code generated by AI and pasting them into projects. If you don't understand the code, it can break parts of your program and even add vulnerabilities to it. Use AI as a tool only.

---

## Data Types

There are many data types, and each is treated by the language in a different way behind the scenes. The interaction between data will depend on their type.

Some languages are more strict and force us to specify the type of data a variable will take. These are known as _Statically Typed Languages_, and some examples are: Java, C, C++, C#, Kotlin, Go.
Other languages are less demanding and check the type of data within the variable when the program runs. These are known as _Dynamically Typed Languages_, and some examples are: Python, JavaScript, Ruby, PHP.

But if python can recognize them, why do I need to know all the different types? Each type has their own rules of usage and interaction. We'll learn more about these when we talk about them in the following sections.

Here is an example of a variable of type string in java, a statically typed language:

```java
String name = "João";
```

### String

The data of type ```string``` are alphanumeric characters, which means they're letters and numbers. They appear between quotation marks (double ```"``` or single ```'```).

> **_Note:_**  When a word is typed without quotation marks, python sees them as commands.

Let's make a variable ```name``` and this time let's ask the user to type their name with the function ```input```:

```python
name = input("What's your name??")
print(name)
```

When we run the code, this is what we'll see:

![[6 - string_input_en.png]]

```python
input()
```

Is a function that writes on screen the message in-between parenthesis then get's what the user types and stores it in a variable.

#### Ignoring characters

As we can see, when running the code, the user's answer was right next to the question. This can be fixed with a space, but we can also add a line break using a backwards slash ```\``` to add special characters. For example:

```python
name = input("What is your name?\n")
```

> **_Note:_** ```\n``` in the middle of a string causes a line break.

The backwards slash is also used to ignore a character that follows it, as we'll see next.

#### Devo usar aspas duplas ou únicas?

Both work the same way: They determine where the string begins and where it ends. Let's assume that you want to use quotation marks within a string:

```python
"And then he said "wow""
```

As we can see, the colors are different to let us know that python will complain and raise an error. It can't understand that "wow" is a part of the string because the first quotation marks determine where the string begins and the second where it ends.

One possible solution is to use the backwards slash, as we've seen:

```python
"And then he said \"wow\""
```

In this case, the colors haven't changed. Python understands that the quotation marks around "wow" should be treated as a part of the string, because they're in front of a backwards slash.

Another way to deal with this situation is to utilize single quotation marks:

```python
'And then he said \"wow\"'
```

Here, the single quotation marks determine where the string begins and where it ends, so the double quotation marks are treated as a part of the string.

#### Concatenation

Concatenation is the act of putting data together.  There are multiple ways of doing this in python, we'll see some of them:

The most common way of concatenation is by using the ```+``` operator.

```python
name = input("What is your name?\n")  
print("Hello, " + name)
```

In this case, we are concatenating the string ```"Hello, "``` and the string inside the variable ```name```, which was given by the user.

![[7 - concatenation_1_en.png]]

Another way of concatenating variables is by separating them with a comma:

```python
name = input("What is your name?\n")
print("Hello,", name)
```

> **_Note:_** In this case, python adds a space between the string and the variable.

As you're probably already imagining, concatenating multiple variables in a huge text would be a lot of work. There is a better way of concatenating in python: using an ```f string```.

```python
name = input("What is your name?\n")
print(f"Hello, {name}")
```

In the ```f string``` all the variables are between curly braces in the middle of the string. Python understands that they're variables and replaces them with their values.

---

### Exercise 1:

1. What is the result of the following expression:

```python
print("11" + "11")
```

2. What's the difference between Dynamically Typed Languages and Statically Typed Languages?
3. Madlibs is a game in which a list of words is given and added to a story. Make a program that will ask the user for 1 name and 2 adjectives, then add them to a sentence.

### Numbers

Existem dois tipos de dados numéricos: integer (Int) e float (floating-point number). Integers são números inteiros, enquanto floats são números decimais.

| Tipo de Dado | Exemplos                               |
|--------------|----------------------------------------|
| Int          | -2, -1, 0, 1, 2, 3, 10, 45, 67, 106    |
| Float        | -1.32 , -1.0 , 0.0 , 1.57, 43.5, 100.0 |

Nós podemos fazer cálculos utilizando python, e para isso utilizamos operadores, assim como na matemática. Eles são:

| Operador | Nome                             | O que faz                                                     |
|----------|----------------------------------|---------------------------------------------------------------|
| +        | soma                             | soma os números                                               |
| -        | subtração                        | subtrai os números                                            |
| *        | multiplicação                    | multiplica os números                                         |
| /        | divisão                          | divide os números                                             |
| %        | módulo (modulus)                 | te dá o resto da divisão                                      |
| **       | exponenciação                    | eleva o número                                                |
| //       | divisor inteiro (floor division) | divide os números e té da um resultado arredondado para baixo |

Alguns são bem simples e você deve se lembrar, outros nem tanto. Então vamos dar uma olhadinha em uns exemplos e esclarecer seus usos.

#### Módulo | Modulus

Este operador divide os números e o resultado é o resto. Qual será o resultado da expressão abaixo?

```python
print(11 % 2)
```

isto mesmo! O resultado é 1.

![[8 - modulus.png]]

Ele divide 11 por 2 e restam 1.

#### Exponenciação

Caso não se lembre, exponenciação é o ato de multiplicar o número por ele mesmo uma ou mais vezes.

```python
print(2 ** 3)
```

é o mesmo que 2³ ou 2 · 2 · 2, que é igual a 8.

![[9 - power.png]]

#### Divisor Inteiro | Floor Division

Com este operador, os números são divididos e python os arredonda o resultado para baixo.

```python
print(10 // 3)
```

O resultado de 10 dividido por três é 3.333, porém, como utilizamos o divisor inteiro, python nos dá como resposta o número 3.

![[10 - floor_division.png]]

#### Int e Float

Em determinadas linguagens, você só pode executar operações com dados do mesmo tipo. Em python este não é o caso. A linguagem tenta sempre entender o que você quer fazer e tenta trazer a resposta mais precisa possível.

Por conta disso, sempre que fazemos qualquer calculo entre um ```int``` e um ```float```, o resultado vai ser um ```float```. Python entende que a chance do resultado desta conta ser um número decimal é grande, então já faz a conversão pra ```float```.

```python
print(5.0 + 3)
```

![[11 - float.png]]

Em alguns casos, como na divisão, isto também ocorre. Mesmo que seja uma divisão entre dois números inteiros. Python sabe que existe uma boa chance de que o resultado de uma divisão seja um número com virgula.

```python
print(4 / 2)
```

![[12 - division.png]]

#### Quantidade de casas decimais

As vezes python te dará um resultado com muitas casas decimais. Isto é normal e ocorre em muitas linguagens. Python sempre tenta entregar o valor mais próximo possível, o que é um pouco difícil devido a como computadores lidam com números.

```python
print(0.2 + 0.1)
```

![[13 - decimal_points.png]]

Mas e se eu quiser um número especifico de casas decimais? Neste caso, podemos formatar o resultado.

```python
number = 1 + 0.9887984
print(f"Resultado não formatado: {number}")
print(f'Resultado formatado: {"%.2f" % number}')
```

aqui estamos somando um ```int``` e um ```float```, então sabemos que o resultado não formatado será um ```float``` e python vai tentar deixá-lo o mais preciso possível. Na terceira linha, repare que a variável não foi sozinha. Nós passamos ```"%.2f" % nome_da_variável```, que vai pegar o valor passado na variável e arredondar pra duas casas decimais.

> **_Nota:_** O ```"%.2f"``` sempre deve vir entre aspas. O ```2``` é a quantidade de casas decimais que você quer.

e este será nosso resultado:

![[14 - formatted_numbers.png]]

#### Ordem de operações matemáticas

Assim como na matemática, em python a ordem das operações matemáticas também será
respeitada.

```python
number = 5 + (2 + 3) ** 2
```

primeiro fazemos o calculo entre parênteses, depois calculamos a potência e, por fim, somamos.

![[15 - order.png]]

#### Números com underline

Números muito grandes são um pouco difíceis de ler. Python resolve isso nos deixando usar
underlines para separar os números, deixando-os mais legíveis.

```python
big_number = 4_540_000_000
print(big_number)
```

![[16 - number_with_underline.png]]

### Revisitando variáveis

Agora que nós já temos um conhecimento sólido em relação às variáveis e tipos de dados, nós podemos voltar e nos aprofundarmos um pouco mais.

Até o momento, nós apenas atribuímos um valor à variável e a usamos. Mas como o nome diz, ela é variável. O que significa que podemos alterar seu valor a qualquer momento.

```python
number = 100
number = 10
print(number)
```

Neste exemplo, primeiro criamos uma variável ```number``` e atribuímos uma integer de valor 100 a ela. Nada de novo. Logo abaixo, modificamos o valor da variável para 10. Ao rodarmos o código, temos este resultado:

![[17 - revisiting_variables.png]]

Python lê o código de cima para baixo, lembra? Então primeiro ele cria a variável, depois modifica a modifica, e por ultimo, imprime o valor atual dela na tela, que é 10.

Como python é uma linguagem dinamicamente tipada, nós podemos até modificar seu tipo para string e python entenderia:

```python
number = 100
number = "hello"
print(number)
```

![[18 - revisiting_variables_2.png]]

#### Mais operadores de atribuição

Vamos imaginar que temos uma variável ```number``` de valor 2 e queiramos somar 10 ao seu valor. Como faríamos isso?

```python
number = 2
number = number + 10
print(number)
```

Parece um pouco confuso,né? Mas vamos passo a passo. Primeiro criamos a variável e atribuímos o valor 2. Depois, nós atribuímos à variável number o valor de ```number``` + 10, ou seja, o novo valor de ```number``` é seu valor atual (2) mais a integer 10. Resultando:

![[19 - assigning_values.png]]

Outra forma de escrever isso, seria:

```python
number = 2
number += 10
```

Alguns outros operadores de atribuição:

| Operador | O que faz                                                      |
|----------|----------------------------------------------------------------|
| +=       | soma ao valor antigo e atribui o resultado à variável          |
| -=       | subtrai do valor antigo e atribui o resultado à variável       |
| \*=       | multiplica com o valor antigo e atribui o resultado à variável |
| /=       | divide o valor antigo e atribui o resultado à variável         |
| %=       | calcula o módulo e atribui o resto à variável                  |
| \**=      | eleva o número e atribui o resultado à variável                |

### Type Casting

Enquanto python nos permite trabalhar com integers e floats ao mesmo tempo, mesmo sendo tipos de dados diferentes, isto não ocorre quando se trata de strings e números. Se tentarmos, python levanta um erro:

```python
print("10" + 10)
```

![[20 - type_casting.png]]

Python está reclamando e dizendo que pode apenas concatenar ```string``` (str) com ```string```, e não ```int```.

#### User input

Quando usamos a função ```input()``` para pegar alguma informação do usuário, este dado sempre vem em formato de ```string```. Mesmo que o usuário tenha digitado um número. Para lidar com esta situação, precisamos converter os dados. E como fazemos isso?

Existem algumas funções que podemos usar:

```python
int(dado)
```

transforma o dado passado em integer.

```python
float(dado)
```

transforma o dado em float.

```python
str(dado)
```

transforma o dado em string.

Um exemplo de uso:

```python
number = input("digite um número:\n")
number = int(number)
```

ou, caso queira deixar o código ainda mais conciso:

```python
number = int(input("digite um número:\n"))
```

### Boolean

O boolean é um tipo de dado com apenas dois valores possíveis: True (verdadeiro) e False (falso).

```python
true_bool = True
false_bool = False
```

Bem fácil, não é?

Eu sei que ele não parece tão relevante ainda, mas o boolean é extremamente importante e vamos ver alguns do seus usos logo.

### Exercício 2

1. Crie um programa que peça para o usuário digitar 2 números e mostre sua soma.
2. Crie um programa que peça ao usuário seu nome e o ano em que nasceu, e mostre uma frase com seu nome e quantos anos ele tem/fará neste ano.
3. Crie um programa que peça ao usuário por dois números e mostre o valor da sua divisão com 3 casas decimais.

---

## Constantes | Constants

Assim como as variáveis, as constantes são espacinhos na memória nos quais dados são armazenados. A diferença é que um valor atribuído a uma constante não pode ser alterado enquanto o programa está rodando.

Quando você tem certeza de que o valor de um dado não será alterado durante a execução do programa, pode escrevê-lo como uma constante. Desta forma, o programa saberá que aquele valor não mudará e, por trás dos panos, fará as otimizações necessárias para funcionar de maneira mais eficiente.

Tá, mas como faço isso em python? Então, python não tem o tipo de dado "constante". Porém, como este dado existe em outras linguagens, nós deixamos claro que a variável deve ser tratada como uma constante colocando seu nome em letras maiúsculas. Por exemplo:

```python
CHARACTER_NAME = Lonk
```

---

## Comentários | Comments

Comentários são linhas de códigos ignoradas por python, que escrevemos para nós mesmos ou para outros programadores. Espera, isso soa confuso. Deixa eu explicar melhor com um exemplo:

Imagine que você trabalhou em um projeto há uns anos e agora quer melhorá-lo. Ao abrir o projeto, você pode ler todo aquele código e decifrar o que cada linha está fazendo, mas seria muito mais rápido e fácil se houvessem comentários no código explicando o que cada bloco do código faz, ou explicando como você resolveu determinado problema.

Comentários são essenciais e facilitam muito a nossa vida. Quando trabalhamos em equipe, eles nos permitem esclarecer para outros programadores o que nosso código está fazendo; Quando revisitamos nossos antigos projetos, nos permitem entender o que fizemos e como fizemos.

Em python, tudo que é escrito na frente de um ```#``` é tratado como um comentário.

```pyhon
# Isto é um comentário
```

---

## O Zen de Python | The Zen of Python

O Zen de Python é um texto escrito por Tim Peters que descreve a filosofia seguida pela comunidade para escrever um bom código em python.

```
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```

Eu comentarei apenas sobre alguns dos princípios. Alguns podem não fazer sentido agora mas farão posteriormente.

```
Beautiful is better than ugly.
# Bonito é melhor do que feio.

Explicit is better than implicit.
# Explícito é melhor do que implícito

Simple is better than complex.
# Simples é melhor do que complexo.

Readability counts.
# Legibilidade conta
```

Quando estamos começando a programar, não sabemos o que é bom e o que é ruim. Hoje vemos muitos vídeos nas redes sociais nos dizendo para escrever códigos de determinada maneira pois "é mais profissional", quando, na verdade, você só está deixando o código mais difícil de ler sem necessidade. Um código legível, bonito, de fácil entendimento, e simples, é sempre preferível e mais profissional do que o oposto.

E, por fim, talvez o princípio mais importante:

```
Now is better than never.
# Agora é melhor do que nunca.
```

Muitas vezes queremos aprender o máximo possível antes de começar. Sentimos que não estamos preparados, que não sabemos o suficiente. Porém, você não precisa saber de tudo para dar o primeiro passo. Mais importante do que escrever um código perfeito, é escrever um código que funciona. Mais pra frente, caso queira, você pode voltar e melhorá-lo.  

Não deixe pra depois. Faça agora o que você pode com o que você tem.

---

# Capítulo 2: Controle de Fluxo | Flow Control

Quando falamos de controle de fluxo, nos referimos à habilidade de um programa de decidir o que fazer ou quantas vezes fazer, dependendo de uma condição. Dê uma olhadinha no fluxograma a seguir:

![[21 - flowchart_pt.drawio.png]]

Neste exemplo, antes de decidirmos o que fazer, avaliamos certas condições. Está quente? Se não estiver, saímos. Caso esteja, verificamos então se está suportável, se estiver, saímos, se não estiver, esperamos um pouco e verificamos novamente.

Neste capítulo você aprenderá a utilizar o controle de fluxo para aumentar as funcionalidades dos seus programas.

## Operadores de comparação | Comparison Operators

Antes de começarmos a utilizar o controle de fluxo nos nossos códigos, precisamos falar sobre os operadores de comparação. Eles são utilizados para formar expressões, que nada mais são do que uma combinação de operadores e valores que resulta em um valor. Nós já utilizamos expressões anteriormente, por exemplo:

```python
number = 10 + 2
```

10 + 2 é uma expressão que forma o valor 12. Nada de novo no horizonte. Com os operadores de comparação, nós podemos criar expressões um pouco mais complexas. Como, por exemplo:

```python
is_less_than = 2 < 10
# is_less_than = True
```

Nesta expressão, python vai checar se 2 é menor que 10 e resultado vai ser um ```boolean```, ou seja, verdadeiro ou falso.

Os operadores de comparação são:

| Expressão | O que faz        |
|-----------|------------------|
| ==        | igual a          |
| !=        | Não é igual a    |
| >         | Maior que        |
| <         | Menor que        |
| >=        | Maior ou igual a |
| <=        | Menor ou igual a |

```python
number1 = 10  
number2 = 2  

print(f"{number1} é menor que {number2}? {number1 < number2}")  
print(f"{number1} é maior que {number2}? {number1 > number2}")  
print(f"{number1} é igual a {number2}? {number1 == number2}")  
print(f"{number1} não é igual a {number2}? {number1 != number2}")
```

![[22 - comparisson_operators_pt.png]]

> **_Nota:_** Não confunda o operador de atribuição (=) com o operador de igualdade  (=\=).

---

## If / Elif / Else

A primeira forma de controle de fluxo que nós veremos é o ```if``` / ```else```. A ideia é simples: Se a condição for verdadeira, faça isto, caso contrário, faça aquilo. 

```python
name = "Jorge"

if name == "Jorge":
	print("Hello, Jorge")
else:
	print("Hello, person")
```

Neste exemplo, comparamos se o valor da variável ```name``` é igual a "Jorge", python avalia esta expressão como verdadeira então faz os comandos seguintes. Resultando em:

![[23 - if_elif_else.png]]

Caso o valor da variável ```nome``` não fosse igual a "Jorge", python executaria os comandos após ```else```. 

Tá, e o que é o ```elif```? O ```elif``` é utilizado quando nós temos mais de duas opções.

```python
if name == "Jorge":
	print(f"Hello, Jorge")
elif name == "Janine":
	print("Hello, Janine")
else:
	print(f"Hello, person")
```

Primeiro python checa se o valor da variável ```name``` é igual a "Jorge"; Caso não seja, ele checa se o valor é igual a "Janine"; Se também não for, ele executa o código em ```else```.

> **_Nota:_** Lembre-se que os códigos são executados de cima pra baixo. Uma vez que uma condição é verdadeira, python vai executar os códigos em seu bloco e não vai mais verificar se as outras condições também são verdadeiras.

---
## Indentação | Indentation

Indentação é o espaço no começo de uma linha. Na maioria das linguagens, ela só existe para organizar e embelezar o código. Em outras, como python, ela é extremamente importante pois define onde o bloco de código começa e termina. A indentação é feita com 4 espaços. A maioria dos editores de texto e IDEs permitem indendar com a tecla _tab_.

```python
if name == "Jorge":
	# este código está indentado e pertence ao bloco de código do "if"
	print("Hello, Jorge")
else:
	# este código está indentado e pertence ao bloco de código do "else"
	print("Hello, person")
```

Um bloco de código pode conter outros blocos de código, como vemos no seguinte código:

```python
username = "Ushi"  
password = "litterbox"  

if username == "Ushi":
	
	print("Hello, Ushi")
	
    if password == "litterbox": 
	    print("Login successful.")  
    else:  
	    print("wrong password.")
	
else:  
    print("unknown user.")
```

Vamos ver passo a passo como python executará este código:

1. Primeiro, python checará se ```username == "Ushi"```, caso seja, ele rodará o seguinte bloco de código:

![[24 - code_blocks_1.png]]

2.  Então executará ```print("Hello, Ushi")``` e checará se ```password == "litterbox"```, caso seja, ele rodará o bloco de código mostrado abaixo:

![[24 - code_blocks_2.png]]

3. Caso ```password``` não seja "litterbox", ele executará o seguinte bloco:

![[24 - code_blocks_3.png]]

4. Se ```username``` não for "Ushi", ele executará o seguinte bloco:

![[24 - code_blocks_4.png]]

---

## Quebras de linha | Line breaks

Ao contrário da indentação, que é tão importante em python, line breaks são ignoradas e não afetam seu programa de nenhuma forma. Sendo assim, podemos usá-las para melhor organizar nosso código, deixando-o mais legível.

---

## Operadores Lógicos | Logical Operators


