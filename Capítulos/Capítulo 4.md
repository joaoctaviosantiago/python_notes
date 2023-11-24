# Capítulo 4: Não se repita!

</br>

## Python é mais fácil que outras linguagens

Uma idea comum vendida na internet é de que python é mais fácil que outras linguagens, como se você não precisasse aprender determinados conceitos ao utilizá-la. Mas não é bem assim. A maioria dos conceitos que aprendemos e aprenderemos, se aplica a praticamente todas as linguagens.

Eu vejo muitas pessoas que estão começando a programar dizerem que java é uma linguagem muito difícil pois os comandos são longos e você precisa saber diversos conceitos. Mas os mesmos conceitos aparecem em python e em diversas outras linguagens, a diferença está na sintaxe. Python é menos verbosa, ou seja, necessita de menos comandos para fazer determinada coisa, e em muitos casos python entende o que você quer dizer, e seus comandos são mais parecidos com a língua Inglesa; enquanto java requer que você seja bem específico quanto ao que quer fazer e seus comandos são mais enigmáticos.

O motivo de eu estar falando disso é para que fique claro que os conceitos e técnicas que você está aprendendo aqui se aplicam a tudo. Sim, nós estamos utilizando python, então a sintaxe é específica, mas os conceitos não. E é por isso que eu tenho colocado exemplos de como as mesmas coisas são feitas em java, para que você veja que se você aprendeu em python, consegue fazer em outras linguagens também.

</br>
</br>

## Funções | Functions

Nós estamos utilizando funções desde o módulo 1, então você já está confortável com elas e como utilizá-las. Então chegou a hora de olharmos para elas um pouco mais a fundo, entendermos como elas funcionam, seu propósito e como criar nossas próprias funções.

Em sua essência, uma função é um bloco de código criado para executar uma determinada tarefa. ou uma determinada **função**. Por exemplo, a função ```print()``` imprime algo na tela, ```len()``` nos diz qual o quantidade de valores existem em um dado, ```min``` nos informa o menor valor em um dado, entre tantas outras.

</br>

### O princípio DRY

Um princípio importantíssimo na programação, DRY significa "Don't Repeat Yourself" ou, em português, "Não se repita". Sempre que possível, devemos segui-lo.

No capítulo 3, eu passei exercícios bônus nos quais você deveria fazer os exercícios sem utilizar as funções que já vêm com python. Algumas das resoluções ficaram bem grandes. Imagine que você está criando um programa e em diversos momentos terá que fazer a mesma coisa. Seria bem exaustivo reescrever o mesmo bloco de códigos de novo e de novo, não é? Pois é aqui que entram as funções. Elas nos permitem dividir nossos problemas complexos em problemas menores e mais simples.

Dividir nosso código em funções nos traz diversos benefícios, entre eles estão:

1.  **Organização:** Os programas ficam mais organizados e, consequentemente, mais fáceis de serem lidos, pois cada uma de suas funcionalidades se encontra em uma determinada função.
2. **Reusabilidade:** Nós não precisamos reescrever os mesmos códigos sempre, podemos apenas chamar a função repetidas vezes.

</br>

### Definindo funções

As funções que nós vimos até agora são chamadas de ```built-in functions```, ou seja, que já vem com python. Agora é hora de aprendermos a criar nossas próprias funções.

Primeiro escrevemos o comando ```def```, depois o nome da função e parênteses.

```python
def hello():    
    print("Hello, world")
```

A função ```hello()``` tem uma única finalidade: imprimir "hello world" na tela. quando chamada. Para chamarmos uma função, apenas digitamos seu nome e parênteses.

```python
hello()
```


![[chapter 4 - function_1.png]]

</br>

### Parâmetros e Argumentos

Parâmetros e argumentos tendem a causar bastante confusão a quem está começando. Vamos vê-los com calma.

Funções também têm a capacidade de manipular dados. Ao definirmos uma função, colocamos entre parênteses as variáveis que a função manipulará. Elas são chamadas de **parâmetros**.

```python
def hello(name):  
    print(f"Hello, {name}")
```

Nossa função ```hello()``` agora recebe um **parâmetro** ```name```, uma variável que será impressa na tela.

Ao chamar a função, passamos um dado para ser atribuído à variável ```name```, este dado é chamado de **argumento**.

```python
hello("Sushi")
```

Ao passarmos o dado "Sushi" como **argumento** pra a função ```hello()```, ela executará e imprimirá:

![[chapter 4 - parameters and arguments 1.png]]

Para que você não se esqueça:

* **Parâmetro:** é a variável que colocamos entre parênteses ao definirmos a função.
* **Argumento:** é o dado passado entre parênteses quando chamamos a função.

</br>

#### Ordem importa!

Quando passamos argumentos para a função, a ordem deles importa.

```python
def add(num1, num2):  
    total = num1 + num2  
    print(total)  
```

A função acima tem dois parâmetros, ```num1``` e ```num2```. Quando passamos os argumentos, o primeiro deles ficará armazenado na variável ```num1``` e o segundo na variável ```num2```.

```python
add(10, 20)
```

Ao chamarmos a função com os argumentos acima,  ```num1 = 10``` e ```num2 = 20```. 

</br>

#### Parâmetros padrões

Ao criarmos as funções, podemos definir parâmetros padrões que serão utilizados pelas funções caso um argumento não seja passado.

```python
def hello(name="Doggo", favorite_food="banana"):  
    print(f"Hello! It's me, {name}, and my favorite food is {favorite_food}.")
```

A função ```hello()``` tem dois parâmetros. Mas desta fez, estamos passando dois valores padrões.  "Doggo" será o valor da variável ```name``` caso nenhum valor seja passado como argumento, e "banana" será o valor de ```favorite_fruit``` caso nenhum valor seja passado como argumento.

Ao chamarmos a função e não passarmos nenhum argumento, python usará os valores padrão.

```python
hello()
```

![[chapter 4 - default parameters 1.png]]

Agora passando apenas um valor:

```python
hello("Chris")
```

![[chapter 4 - default parameters 2.png]]

</br>

 > **_Nota:_** Os parâmetros com valor padrão devem vir apenas após os parâmetros sem valor padrão. 

</br>

#### Argumentos com palavras-chave

Para evitar erros, nós podemos passar argumentos com palavras-chave para especificar a que variável o valor deve ser atribuído.

```python
def madlibs(noun, adj1, adj2):  
    phrase = f"the {noun} are {adj1} amd look {adj2}."  
    print(phrase)
```

Ao chamarmos a função acima,  ao invés de colocarmos apenas os valores, nós colocamos também as variáveis às quais eles serão atribuídos.

```python
madlibs(adj1="cute", adj2="funny", noun="ducks")
```

E quando o fazemos assim, a ordem não importa!

</br>

### Docstring

Os comentários de aspas triplas que vimos anteriormente tem um significado especial quando utilizados dentro de funções, nestes casos eles são o que chamamos de **docstring**. Docstrings são utilizadas para dar mais informações sobre as funções, dizendo o que elas fazem, quais seus parâmetros, etc.

```python
def hello(name, favorite_food="banana"):  
    """  
    Says hello and informs the favorite fruit.
      
    :param name : string
	                name to be greeted.    
    :param favorite_food : string
                    favorite food of the person greeted.    
    """
    
    print(f"Hello! It's me, {name}, and my favorite food is {favorite_food}.")
```

Neste exemplo nós estamos descrevendo o que a função faz, quais seus parâmetros, os tipos de dados que eles receberão e uma descrição do que este dado representa.

Quando passamos o mouse sobre a função ```hello()```, vemos o seguinte:

![[chapter 4 - docstring.png]]

</br>

> **_Nota:_** Não existe uma forma correta de criar sua docstring. O importante é que elas sejam claras e explicativas.

</br>


