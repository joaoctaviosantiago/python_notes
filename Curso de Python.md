# Introdução

## O que é programação?

Programar é dar uma série de instruções ao computador. Esta série de instruções é conhecida como algoritmo.

É comum, no brasil, começarem ensinando programação por pseudo-linguagens, ou seja, utilizando português para criar algoritmos. Exemplo:

```
dê dois passos para a frente,
tente abrir a porta
se conseguir, abra a porta
se não conseguir, vire para a esquerda
```

E depois ensinam através do portugol, que é uma linguagem que utiliza o português como base, para facilitar a compreensão de conceitos sem aprender palavas em inglês. Porém, eu discordo desta abordagem e prefiro utilizar uma linguagem que você usará no dia-a-dia, pois a sintaxe da maioria das linguagens é parecida. Assim você não precisa reaprender toda a sintaxe para começar a trabalhar num projeto real.

---

## Preciso saber matemática?

Um motivo de ansiedade ao redor de quem considera aprender a programar é o _mito_ de que saber matemática é uma necessidade. Sim, eu disse _mito_. E digo isto pois na maioria das vezes programação não requer nada além de matemática básica. É importante entender que dentro da programação existem diversas profissões. Algumas vão requerer matemática, outras não. Novamente: a maioria não vai. Só porque algo envolve números, não quer dizer que você precise de matemática para aprender.

---

## Eu acho que estou muito velho pra aprender a programar

Outro _mito_ bastante comum é de que só consegue aprender a programar bem, aqueles que
aprenderam cedo. Programação se aprende fazendo, praticando. Você cresce com cada dia que pratica. Ninguém nasce um programador. É uma habilidade adquirida através de estudo e prática.

---

## Por que python?

Python é uma linguagem de _"uso geral"_ , o que significa que é uma linguagem usada em diversas áreas, incluindo a área de dados, machine learning, desenvolvimento de software, desenvolvimento web, automação, entre outras. Além de ser uma linguagem amplamente utilizada, sua sintaxe é muito parecida com o inglês, o que a torna muito menos intimidadora para quem está começando.

---

## Sobre o curso

O curso foi desenvolvido de tal maneira que a cada módulo adicionaremos mais matéria. Sendo assim, tudo o que vermos voltará a ser utilizado, por isso é crucial que você avance de módulo apenas quando tiver entendido bem a matéria.

Nós visitaremos outros tópicos além de python no decorrer do curso, mesmo que não tão a fundo, pois precisaremos desse conhecimento para fazermos alguns de nossos projetos.

Não se limite aos exercícios do curso. Programação é como LEGO. É um exercício de criatividade. Aqui você vai aprender todas as ferramentas e conhecimentos necessários para criar o que imaginar, além da habilidade de aprender uma outra linguagem.

---

## Bonus: Como funciona um computador?

Cada peça de um computador tem um trabalho específico. Aqui quero esclarecer um pouco mais o que cada peça de hardware faz, de maneira superficial. Isto vai nos ajudar a esclarecer umas coisas mais pra frente.

### Placa Mãe

Conecta todas as peças do computador e as fazem funcionar em conjunto

### CPU | Processador

É o cérebro do computador. É capaz de processar uma quantidade imensa de informações por segundo.

### GPU | Placa de Video

Processa as imagens e videos do computador, como jogos, seriados, e a imagem do monitor.

### HDD | SSD | NVMe


Está é a _memória de longo prazo_ do computador. Os dados são **persistentes** , ou seja, mesmo depois de desligar o computador, os dados salvos no HD continuarão existindo. É onde você guarda as fotos, videos, programas, jogos, tudo que há no seu computador.

### RAM | Random Access Memory

A memória RAM é a _memória de curto prazo_ do computador. Ela é extremamente rápida comparada com o HD, porém, temos uma quantidade menor disponível. Toda vez que rodamos um programa, abrimos um video, fazemos algo, os dados necessários para este programa rodar ficam armazenados na memória RAM, quando fechamos estes programas, eles são removidos da memória. Por conta disso, quando um novo programa é aberto, seus dados serão colocados onde houver espaço disponível. A localização dos dados não é permanente.

---

## Download e instalação de python

O download de python pode ser feito através do seu [site oficial](https://www.python.org/downloads/).

> **_Importante:_** Faça o download de python 3 (ou a versão mais atual) para garantir que os códigos deste curso funcionem corretamente.

### Windows

A instalação no windows é simples, como de qualquer outro programa. Selecione "Add python.exe to PATH" e depois é só clicar em "próximo" e esperar.

![[1 - install_python.png]]

> **_Importante:_** Marcar "Add python.exe to PATH" antes de instalar.

### MacOS

Para a instalação no MacOS, recomendo este link do [freeCodeCamp](https://www.freecodecamp.org/portuguese/news/como-instalar-o-python-3-no-mac-tutorial-de-instalacao-e-atualizacao-com-o-brew/). Fique à vontade para procurar no google ou no youtube por outros guias mais claros.

### Linux

Python já vem instalado por padrão na maioria das distribuições Linux. Recomendo não atualizar pois algumas bibliotecas podem quebrar devido à diferenças entre as versões.

---

## Instalação da IDE

Uma vez instalado, python pode ser rodado através do terminal do computador. Porém. para esta primeira parte do curso, nós instalaremos uma IDE ( _Integrated Development Environment_ ) para programar.

> **_Nota:_** Você pode escrever seu código até mesmo no Microsoft Word ou Bloco de Notas, e executá-lo através do terminal. Um IDE é um software feito especificamente para rodar determinada linguagem, já vindo preparado e otimizado para isto. Existem outros programas, editores de texto e outras IDEs que você pode utilizar.

### PyCharm Community Edition

Eu utilizarei o PyCharm como meu IDE para esta primeira parte do curso. O download pode ser feito através [deste link](https://www.jetbrains.com/pycharm/download).

> **_Nota:_** Existem duas versões, PyCharm Professional Edition, que é paga e PyCharm Community Edition, que é gratuita. Nós utilizaremos a Community Edition.

Uma vez instalado, crie um novo projeto e espere um bocadinho. A primeira vez que o projeto é aberto a IDE precisa de um tempinho para organizar as coisas.

### Visual Studio Code

VSCode é um editor de texto otimizado para programação e utiliza plugins para melhorar a vida do programador. Caso esteja utilizando um computador mais antigo ou lento, recomendo utilizar o Visual Studio Code com o plugin de python. É fácil de encontrar no google como instalar plugins. O download pode ser feito [neste link](https://code.visualstudio.com/).

Uma vez instalado, crie um arquivo ```nome_do_arquivo.py```.

Posteriormente nós utilizaremos o VSCode para alguns projetos.

---

# Capítulo 1: O básico

## Meu primeiro programa

Por padrão, a primeira coisa que fazemos para confirmarmos que um programa funciona, é dizer _"Hello, world"_ , e é isso que vamos fazer. Escreva:

```python
print("Hello, world")
```

> **_Nota:_** É importante utilizar as aspas na mensagem.

E execute seu programa clicando no botão **_play_** no topo da tela:

![[2 - play.png]]

Este deverá ser o resultado:

![[3 - hello_world_resultado.png]]

Pronto! Você criou seu primeiro programa em python. Simples, não é?

```python
print()
```

É uma função que imprime na tela os dados dentro dos parênteses.

> **_Nota:_** Nós estudaremos funções a fundo posteriormente. Por enquanto, não ligue pra elas.

---

## Variáveis | Variables

Uma variável é um espacinho na memória (RAM) onde você guardará um dado. Este dado pode ser um nome, uma data, um número, etc. Soa confuso, eu sei. Vamos deixar um pouco mais claro com um exemplo. Criaremos uma variável chamada ```message```:

```python
message = "Hello, world"
print(message)
```

Neste exemplo, estamos separando um espacinho na memória e chamando de ```message```, depois pegamos o dado ```Hello, world``` e colocamos dentro dela. Em seguida, chamamos a função ```print()``` novamente:

![[4 - resultado_variable.png]]

Como podemos ver, temos o mesmo resultado. Python imprimiu o valor atribuído à variável
```message```.


> **_Importante:_** O sinal de igual (=) não é o igual da matemática. O igual comparativo/matemático nós veremos mais pra frente. Em python (=) é chamado de "Assign operator" ou operador de atribuição. Ele pega o valor do dado e atribui a uma variável.

Tá, e onde isto é usado? Pensa nos jogos que você já jogou. O número de vidas, seu HP, os nomes dos personagens, seus atributos, sua munição. Tudo isso é guardado dentro de variáveis.

Variáveis podem ter qualquer nome. Porém, existem algumas regras a serem seguidas ao escolher seu nome:

* O nome das variáveis não pode conter espaços.
* Podem conter apenas letras, números e underlines, mas podem apenas começar com letra ou underline. Não podem começar com números.
* O ideal é que seus nomes sejam descritivos e ajudem a entender o tipo de informação que ela guarda.
* Evite usar palavras reservadas por python, como o print que vimos anteriormente.

> **_Nota:_** Existem alguns estilos de nomenclatura. Entre eles estão:
> 
> * **camelCase:** A primeira palavra é com letra minuscula e todas as outras são com letra maiúscula
> * **PascalCase:** A primeira letra de cada palavra começa com letra maiúscula
> * **snake_case:** Todas as palavras são com letra minúscula e separadas por underline
> * **kebab-case:** Todas as palavras são com letra minúscula e separadas por hífen
> 
> Python recomenda _snake_case_.

---

## Python lê o código de cima para baixo

As linguagens de programação, em geral, lêem código de cima para baixo. No código a seguir, tentamos imprimir uma variável que ainda não foi lida por python:

```python
print(f"Hello, {nome}")
nome = "João"
```

Quando tentamos rodar o código, python levanta um erro:

![[5 - erro.png]]

Aqui python nos dá algumas informações sobre onde acredita estar o erro. Ele nos informa o arquivo e a linha. Depois nos diz o erro que encontrou:

```
NameError: name 'nome' is not defined. Did you mean: 'None'?
```

Python nos diz que a palavra "nome" não foi definida. Ele não a conhece, não sabe o que quer dizer. E ainda pergunta "Você quis dizer: 'None'"?

---

## A importância dos erros

Quando python não entender o que você está tentando fazer, ele vai levantar um erro e te comunicar o que há de errado, ou tentar. Leia o erro com atenção e não tenha medo de jogá-lo no google. Tão importante quanto aprender a programar, é aprender a "desbugar", ou "fazer debug", que é o ato de resolver problemas no seu código.

Ninguém sabe tudo sobre uma linguagem. Quanto mais a utilizamos, mais aprendemos. Mas mesmo assim, é um tópico muito amplo. Por isso praticamente tudo na programação é documentado. Na documentação encontramos, em detalhes, como utilizar certas ferramentas e como a linguagem roda por trás dos panos.

Além do google e o stackoverflow, agora também temos inteligencias artificiais como ChatGPT entre outras para nos auxiliar com programação. Elas são excelentes ferramentas que vão explicar e ajudar a produzir códigos.

> **_Importante:_** É comum ver estudantes simplesmente copiando os códigos gerados pelas IA e colocando nos projetos. Se você não entender o código, ele pode quebrar partes do programa ou até mesmo adicionar vulnerabilidades no mesmo. Utilize inteligências artificiais como auxilio apenas.

---

## Tipos de dados | Data Types

Existem diversos tipos de dados, e cada um é tratado de uma forma diferente por trás dos panos pela linguagem. A interação entre os dados vai depender do seu tipo. 

Algumas linguagens são mais rigorosas e nos forçam a especificar o tipo de dado que cada variável vai receber. Estas são conhecidas como _Statically Typed Languages_ (Linguagens estaticamente tipadas), e alguns exemplos são Java, C, C++, C#, Kotlin, Go.
Outras linguagens são menos exigentes e checam o tipo de dado quando o programa roda. Elas são conhecidas como _Dynamically Typed Languages_ (Linguagens dinamicamente
tipadas), e alguns exemplos são: Python, JavaScript, Ruby, PHP.

Mas se python consegue reconhecer o tipo de dado, por que preciso saber dos diferentes tipos?
Cada tipo tem suas regras de uso e interação. Nós vamos aprender mais sobre isso ao falar de cada um deles a seguir.

Aqui está um exemplo de variável do tipo String em java, uma linguagem estaticamente tipada:

```java
String name = "João";
```

### String

Os dados do tipo ```string``` são caracteres alfanuméricos, ou seja, letras e números. Eles vêm entre aspas (duplas ```"``` ou únicas ```'```).

> **_Nota:_** Quando uma palavra é digitada sem aspas, python a reconhece como um comando.

Vamos criar uma variável ```name``` e, desta vez, pediremos para o usuário digitar seu nome com a função ```input```:

```python
name = input("Qual o seu nome?")
print(name)
```

Ao rodarmos o código, veremos isto:

![[6 - string_input_pt.png]]

```python
input()
```

É uma função que escreve na tela a mensagem entre parenteses, pega o que foi digitado pelo usuário e guarda em uma variável.

#### Ignorando caracteres

Como podemos ver, ao rodar o código, a resposta do usuário ficou colada com a pergunta. Isso pode ser resolvido com um espaço, mas podemos também fazer uma quebra de linha utilizando a barra inversa para utilizar caracteres especiais. Por exemplo:

```python
name = input("Qual o seu nome?\n")
```

> **_Nota:_** ```\n``` no meio da string causa uma quebra de linha.

A barra inversa também é utilizada para ignorar o caractere que vem logo em sua frente, como veremos a seguir.

#### Devo usar aspas duplas ou únicas?

Ambas funcionam da mesma forma: determinam onde a string começa e onde termina. Vamos supor que no meio da sua string você queira colocar uma palavra entre aspas:

```python
"E então ele falou "eita""
```

Como pode ver, as cores estão até diferentes para sinalizar que python vai reclamar e levantar um erro. Ele não consegue entender que "eita" faz parte da string pois as primeiras aspas determinam onde a string começa e as segundas onde termina.

Uma possível solução é utilizar a barra inversa, como vimos anteriormente:

```python
"E então ele falou \"eita\""
```

Neste caso, as cores não mudaram. python entende que as aspas ao redor de "eita" devem ser tratadas como string pois estão logo a frente de uma barra inversa.

Outra forma de lidar com a situação é utilizar as aspas únicas:

```python
'E então ele falou "eita"'
```

Neste caso, as aspas únicas definem quando a string começa e quando termina, então as aspas duplas são tratadas como string.

#### Concatenação

Concatenação é o ato de juntar dados. Existem diversas formas de fazer isso em python, nós veremos algumas:

A forma mais comum de se concatenar é utilizando o operador ```+```.

```python
name = input("Qual o seu nome?\n")
print("Hello, " + name)
```

Neste caso, concatenamos a string ```"Hello, "``` e a string dentro da variável ```name```, que foi digitada pelo usuário.

![[7 - concatenation_1_pt.png]]

Uma outra forma de concatenar variáveis é separando com virgula:

```python
name = input("Qual o seu nome?\n")
print("Hello,", name)
```

> **_Nota:_** Neste caso, python coloca um espaço entre a variável.

Como você já deve estar imaginando, concatenar diversas variáveis em um texto gigante seria muito trabalhoso. Existe uma forma mais fácil de concatenar em python: utilizando uma ```f string```.

```python
name = input("Qual o seu nome?\n")
print(f"Hello, {name}")
```

Na ```f string``` todas as variáveis ficam dentro de chaves no meio da string. python entende que são variáveis e as substitui.

---

### Exercício 1

1. Qual o resultado da seguinte expressão:

```python
print("11" + "11")
```

2. Qual a diferença entre linguagens dinamicamente tipadas e linguagens estaticamente tipadas?

3. Madlibs é um jogo de substituição de palavras onde. após a criação de uma lista de palavras, elas são colocadas numa história. Crie um programa que peça ao usuário 1 nome e 2 adjetivos, então os coloque numa frase.

### Números

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

O resultado de 10 dividido por 3 é 3.333, porém, como utilizamos o divisor inteiro, python nos dá como resposta o número 3.

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

![[14 - formatted_numbers_pt.png]]

#### Ordem de operações matemáticas

Assim como na matemática, em python a ordem das operações matemáticas também será respeitada.

```python
number = 5 + (2 + 3) ** 2
```

primeiro fazemos o calculo entre parênteses, depois calculamos a potência e, por fim, somamos.

![[15 - order.png]]

#### Números com underline

Números muito grandes são um pouco difíceis de ler. Python resolve isso nos deixando usar underlines para separar os números, deixando-os mais legíveis.

```python
big_number = 4_540_000_000
print(big_number)
```

![[16 - number_with_underline.png]]

### Boolean

O boolean é um tipo de dado com apenas dois valores possíveis: True (verdadeiro) e False (falso).

```python
true_bool = True
false_bool = False
```

Bem fácil, não é?

Eu sei que ele não parece tão relevante ainda, mas o boolean é extremamente importante e vamos ver alguns do seus usos logo.

---

## Revisitando variáveis

Agora que nós já temos um conhecimento sólido em relação às variáveis e tipos de dados, nós podemos nos aprofundar um pouco mais.

Até o momento, nós apenas atribuímos um valor à variável e a usamos. Mas como o nome diz, ela é variável. O que significa que podemos alterar seu valor a qualquer momento.

```python
number = 100
number = 10
print(number)
```

Neste exemplo, primeiro criamos uma variável ```number``` e atribuímos uma integer de valor 100 a ela. Nada de novo. Logo abaixo, modificamos o valor da variável para 10. Ao rodarmos o código, temos este resultado:

![[17 - revisiting_variables.png]]

Python lê o código de cima para baixo, lembra? Então primeiro ele cria a variável, depois modifica a modifica, e por ultimo, imprime o valor atual dela na tela, que é 10.

Como python é uma linguagem dinamicamente tipada, nós podemos até modificar seu tipo para string e python entenderia.

```python
number = 100
number = "hello"
print(number)
```

![[18 - revisiting_variables_2.png]]

### Mais operadores de atribuição

Vamos imaginar que temos uma variável ```number``` de valor 2 e queiramos somar 10 ao seu valor. Como faríamos isso?

```python
number = 2
number = number + 10
print(number)
```

Parece um pouco confuso,né? Mas vamos passo a passo. Primeiro criamos a variável e atribuímos o valor 2. Depois, nós atribuímos à variável ```number``` o valor de ```number``` + 10, ou seja, o novo valor de ```number``` é seu valor atual (2) mais a integer 10. Resultando:

![[19 - assigning_values.png]]

Outra forma de escrever isso, seria:

```python
number = 2
number += 10
print(number)
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

---

## Type Casting

Type casting é o ato de mudar o tipo de uma variável.

Enquanto python nos permite trabalhar com integers e floats ao mesmo tempo, mesmo sendo tipos de dados diferentes, isto não ocorre quando se trata de strings e números. Se tentarmos, python levanta um erro.

```python
print("10" + 10)
```

![[20 - type_casting.png]]

Python está reclamando e dizendo que pode apenas concatenar ```string``` (str) com ```string```, e não ```int```.

### Input do usuário | User input

Quando usamos a função ```input()``` para pegar alguma informação do usuário, este dado sempre vem em formato de ```string```, mesmo que o usuário tenha digitado um número. Para lidar com esta situação, precisamos converter os dados. E como fazemos isso?

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

---

## Exercício 2

1. Crie um programa que peça para o usuário digitar 2 números e mostre sua soma.

2. Crie um programa que peça ao usuário seu nome e o ano em que nasceu, e mostre uma frase com seu nome e quantos anos ele tem/fará neste ano.

3. Crie um programa que peça ao usuário por dois números e mostre o valor da sua divisão com 3 casas decimais.

---

## Constantes | Constants

Assim como as variáveis, as constantes são espacinhos na memória nos quais dados são armazenados. A diferença é que um valor atribuído a uma constante não pode ser alterado enquanto o programa está rodando.

Quando você tem certeza de que o valor de um dado não será alterado durante a execução do programa, pode escrevê-lo como uma constante. Desta forma, a linguagem saberá que aquele valor não mudará e, por trás dos panos, fará as otimizações necessárias para funcionar de maneira mais eficiente.

Tá, mas como faço isto em python? Então, python não tem o tipo de dado "constante". Porém, como este dado existe em outras linguagens, nós seguimos a mesma nomenclatura para deixar claro que a variável deve ser tratada como uma constante, colocando seu nome em letras maiúsculas. Por exemplo:

```python
CHARACTER_NAME = Lonk
```

---

## Comentários | Comments

Comentários são linhas de códigos ignoradas por python, que escrevemos para nós mesmos ou para outros programadores. Espera, isso soa confuso. Deixa eu explicar melhor com um exemplo:

Imagine que você trabalhou em um projeto há uns anos e agora quer melhorá-lo. Ao abrir o projeto, você pode ler todo aquele código e decifrar o que cada linha está fazendo, mas seria muito mais rápido e fácil se houvessem comentários no código explicando o que cada bloco do código faz, ou explicando como você resolveu determinado problema.

Comentários são essenciais e facilitam muito a nossas vidas. Quando trabalhamos em equipe, eles nos permitem esclarecer para outros programadores o que nosso código está fazendo; Quando revisitamos nossos antigos projetos, nos permitem entender o que fizemos e como os fizemos.

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

| Operador  | O que faz        |
|-----------|------------------|
| ==        | igual a          |
| !=        | não é igual a    |
| >         | maior que        |
| <         | menor que        |
| >=        | maior ou igual a |
| <=        | menor ou igual a |

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

> **_Importante:_** ```if``` não precisa de um ```else```  para funcionar. Você pode ter um ```if``` sozinho e se a condição não for verdadeira, python pula o ```if``` e continua rodando o resto do código. O ```if``` pode também terminar com um ```elif``` em vez de um ```else```.

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

Operadores lógicos são utilizados quando queremos avaliar duas ou mais expressões. Existem 3 operadores lógicos em python: ```and```, ```or```, ```not```.

> **_Nota:_** Para ajudar na leitura, algumas pessoas gostam de colocar as expressões entre parênteses.

### and

Quando utilizamos o operador ```and```, python só executará o bloco de código se todas as expressões forem verdadeiras.

```python
first_number = 15  
second_number = 6  
  
if (first_number > 10) and (second_number < 20):  
    print("yay")
```

Aqui, ```first_number``` é maior que 10 e ```second_number``` é menor que 20. Ambas as expressões são verdadeiras, logo, python executará o bloco de código.

### or

Quando utilizamos o operador ```or```, python executará o bloco de código caso uma das expressões sejam verdadeiras.

```python
first_number = 15  
second_number = 6  
  
if first_number > 10 or second_number < 5:  
    print("yay")
```

Neste caso, ```first_number > 10``` é verdadeiro e ```second_number < 5``` é falso. Python executará o bloco de código pois uma das expressões é verdadeira.

### not

Quando utilizamos o operador ```not```, invertemos o valor booleano. Se a expressão for verdadeira, ela passará a ser falsa; Se for falsa, passa a ser verdadeira.

```python
number = 6  
  
if not number < 5:
    print("yay")
```

In this example, ```number < 5``` é falso, como utilizamos o operador ```not```, o bloco de código será executado pois ```not False``` é ```True```.

---

## Operador Ternário | Ternary Operator

O operador ternário é um "```if``` de uma linha", é uma maneira mais concisa de se escrever um ```if/else``` simples.

```python
valor_produto = 999.99  
posso_pagar = "não" if valor >= 1200 else "sim"
```

O valor da variável ```posso_pagar``` será "não" se o valor do produtor for maior ou igual a 1200, caso contrário, será "sim".

---

## Exercício 3

1. Crie um programa que peça para o usuário as notas de 3 provas, calcule a média, imprima-a na tela e, se ela for maior ou igual 6, imprima "passou! (:", se estiver entre 4 e 6, imprima "está de recuperação" e, se a média for menor que 4, imprima na tela que o aluno foi reprovado.

2. Crie um programa que peça para o usuário digitar seu peso e sua altura, calcule o IMC (Índice de Massa Corporal), mostre-o cm duas casas decimais e imprima na tela as informações seguindo a tabela abaixo:

| IMC         | CLASSIFICAÇÃO   |
|-------------|-----------------|
| <18,5       | Baixo peso      |
| 18,5 a 24,9 | Peso normal     |
| 25,0 a 29,9 | Excesso de peso |
| >30,0       | Obeso           |

3. Crie um programa que calcule o valor da gorjeta. Peça ao usuário o valor da conta e quantos porcento do valor ele quer deixar de gorjeta, e imprima na tela o valor da conta, a porcentagem e o valor total da conta com a gorjeta inclusa.

---

## Laços | Loops

O que são loops? Imagine que você está desenhando um círculo, quando você chega ao final do desenho, você encontra o ponto inicial do desenho. Na programação, loops são usados na repetição de códigos, quando um chega ao seu final, ele recomeça. Até agora, nossos códigos começaram e terminaram, de cima pra baixo. Mas e se quiséssemos que o código rodasse uma certa quantidade de vezes, ou se rodasse até uma condição ser verdadeira?

> **_Nota:_** Cada "volta" de um loop é chamada de iteração.

### For loop

O ```for``` loop é utilizado quando sabemos quantas vezes o código precisa ser repetido. Ele é utilizado, normalmente, junto com a função ```range```. Vamos analisar o ```for``` loop um pouco mais a fundo:

```python
for number in range(1, 4):
	print("Hello")
```

Primeiro utilizamos o comando ```for```, depois criamos uma variável que eu decidi chamar de ```number```, usamos o comando ```in``` e chamamos a função ```range```. Outra forma de ler isto, seria: "para cada número de 1 até 4, não incluindo 4, faça isto."

Quando o loop começar, a variável ```number``` vai ter o valor de 1, python vai rodar os comandos no bloco de código e vai voltar para o começo do ```for``` loop, desta vez, ```number``` vai ter o valor de 2, o bloco de código vai rodar novamente e voltar para o começo, e agora ```number``` terá o valor de 3, o bloco de código vai rodar e o loop vai acabar.

Nós podemos acessar a variável ```number``` dentro do ```for``` loop.

```python
for number in range(1, 4):  
    print(number)
```

![[25 - range_function.png]]
Como você pode ver aqui, no primeiro loop ```number``` tinha o valor de 1 e isso foi impresso na tela, no segundo tinha o valor de 2 e no terceiro o valor de 3.

#### Laço for aninhado | Nested for loops

Assim como com o ```if```, nós podemos criar um ```for``` loop dentro de outro.

```python
for i in range(1, 5):  
    print(i, end=': ')  
  
    for j in range(1, 5):  
        print(j, end=' ')  
  
    print()
```

Eu sei que este código assusta um pouco, então vamos lê-lo com calma. Primeiro um loop começa e a variável ```i``` tem o valor de 1, o bloco de código então roda. Nele, imprimimos ```i```; Em seguida o segundo ```for``` loop começa. Neste, a variável ```j``` será impressa 4 vezes (de 1 a 5 não incluindo 5), o segundo ```for``` termina de ser executado, voltamos o bloco de código do primeiro loop, e pulamos uma linha com a função ```print()```.

Este é o resultado:

![[26 - nested_loops.png]]

> **_Nota:_**  A função ```print()```, normalmente, pula uma linha depois da impressão. Nós podemos alterar este comportamento com o parâmetro ```end=```.  Com ele podemos definir se vai ter um espaço depois de cada impressão, uma virgula, etc.

É importante ressaltar que a variável ```i``` pode ser acessada em qualquer lugar dentro do bloco de código do primeiro ```for``` loop, até mesmo dentro do segundo ```for``` loop, por isso utilizei nomes diferentes para os dois.

```python
for i in range(1, 5):
    print(i)  
	# A variável i pode ser acessada aqui, mas a j não.

    for j in range(1, 5):  
        print(i, j)  
		# tanto a variável i quanto a j podem ser acessadas aqui.
    print()
```

#### range()

Apesar de já termos visto como a função range() funciona, quero apenas reforçar o que vimos e adicionar mais uma coisinha. A função ```range``` pode ter até 3 parâmetros:

```python
range(começo, fim, passo)
```

O primeiro, que aqui chamei de ```começo```, define em que número a contagem vai começar; o segundo, que chamei de ```fim```, define em que número a contagem vai terminar, não incluindo este número; e a terceira, que chamei de ```passo``` determina a que passo a contagem é feita, de um em um, dois em dois, três em três. O padrão é de um em um.

```python
for num in range(0, 11, 2):  
    print(num)
```

![[27 - ranged_function_steps.png]]

### Laço while | While loop

O ```while``` loop é executado enquanto uma condição for verdadeira. Ele é utilizado quando não sabemos quantas vezes o código precisará ser executado.

```python
number = 1  
  
while number <= 5:  
    print(number)  
    number += 1
```

Neste exemplo, python vai testar se ```number <= 5``` é verdadeiro, caso seja, ele vai rodar o bloco de código, imprimir o valor de number e somar 1 ao mesmo; caso não seja, o loop acaba.

![[28 - while_loop.png]]

> **_Importante:_** cuidado para não criar um loop infinito. Se a condição nunca se tornar falsa, o programa vai rodar infinitamente e, eventualmente, "crashar", ou seja, parar de funcionar e fechar.

#### Valores truthy e falsy | truthy and falsy values

Quando tentamos passar dados como condição, ao invés de uma expressão, python avalia aquele dado como  ```True``` ou ```False```. Quando o valor é verdadeiro, nós chamamos de "truthy", e quando é falso, de "falsy". Por exemplo:

```python
while 10:
	print("truthy")
```

Os dados ```0```, ```0.0```, e ```''```, serão falsy. Qualquer outro dado será truthy.

### Break

```break``` é um comando utilizado dentro de um loop. Ele força python a parar o loop e sair dele.

No código a seguir, o loop vai rodar e imprimir o valor de ```num``` enquanto seu valor não for maior que 5, quando isso acontecer, python sairá do loop e continuar com o código fora do ```for``` loop.

```python
for num in range(1, 10):  
    if num > 5:  
        break  
    print(num)  
  
print("Done!")
```

![[29 - break.png]]

### Continue

O comando ```continue``` também é utilizado dentro de um loop. Quando python chega neste comando, ele passa para a próxima iteração do loop.

```python
for num in range(1, 11):  
    if 2 < num < 8:  
        continue  
    print(num)  
  
print("Done!")
```

Aqui, estamos dizendo para python que, quando ```num``` estiver entre 2 e 8, para pular para a próxima iteração do loop. Ou seja, quando ```num``` for igual a 3, python vai chegar no comando ```continue``` e vai voltar pro começo, e ```num``` passará a ter o valor de 4, e assim sucessivamente até ```num``` ser maior ou igual a 8.

Este será nosso resultado:

![[30 - continue.png]]

---

## Exercício 4

1. Crie um programa que imprima números de 1 a 10 e diga se são pares ou ímpares.
2. Crie um programa que imprima os números de 1 a 50, porém, caso o número seja divisível por 3, imprima "Fizz", caso seja divisível por 5, imprima "Buzz", caso seja divisível por 3 e por 5, imprima "FizzBuzz".
3. Crie um programa que imprima a seguinte figura:

![[31 - exercise_4-2.png]]

---

# Capítulo 3: Estrutura de dados avançada

## Lista | List

A lista é um tipo de dado que contém um ou mais itens ordenados. Dentro de uma lista nós podemos ter strings, números, outra listas, entre outros.

```python
my_list = ['Hello', 'World', 1, 2.0, 3]
print(my_list)
```

![[32 - lists_1.png]]

Neste exemplo temos uma lista com 5 itens de diversos tipos. Quando a imprimimos, python imprime a lista inteira, incluindo os colchetes.

> **_Nota:_** Python reconhece uma lista por causa dos colchetes.

Antes de vermos exemplos práticos de uso de uma lista, primeiro precisamos aprender a manipulá-la.

### Acessando uma lista
#### Acessando os itens da lista

Como falamos anteriormente, listas são ordenadas, ou seja, todos os itens de uma lista estão em uma posição fixa dentro dela. Sabendo disso, nós podemos acessá-los através de seu índice (index em inglês).

```python
my_list = ['Hello', 'World', 1, 2.0, 3]
# indice:    [0]      [1]   [2] [3] [4]
print(my_list[0])
```

Aqui estamos dizendo para python imprimir o item que se encontra na posição 0 dentro da lista.

![[33 - list_index.png]]

> **_Importante:_** O índice sempre começa em 0. Então, numa lista de 5 itens, nós teremos os índices 0, 1, 2, 3, 4. índices são sempre ```Int```.


#### Acessando lista dentro de uma lista

Como falamos anteriormente, uma lista pode conter itens de qualquer tipo, incluindo listas, dicionários e outros tipos de dados que veremos mais à frente.

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

Primeiro acessamos o item no índice 0 da lista ```names_and_numbers```, que é a lista de nomes, depois acessamos o item de índice 0 nela.

![[35 - list_rebeca.png]]

#### Acessando o ultimo item

Python lê os itens de uma lista da esquerda pra direita.

```python
fruits = ['Apple', 'Banana', 'Grape', 'Strawberry', 'Orange']
#            [0]      [1]      [2]        [3]          [4]
```

Quando passamos um índice negativo, python passa a ler a lista da direita para a esquerda.

```python
fruits = ['Apple', 'Banana', 'Grape', 'Strawberry', 'Orange']
#           [-5]     [-4]      [-3]       [-2]        [-1]
```

### Modificando uma lista

Agora que nós sabemos como acessar cada item dentro de uma lista, vamos ver como modificá-los.

#### Substituindo items

Para substituir um item na lista, nós primeiro acessamos o item e então atribuímos um valor, como fizemos com variáveis anteriormente.

```python
fruits = ['Apple', 'Banana', 'Grape']
fruits[0] = 'Orange'
print(fruits)
```

![[36 - replacing_list_items.png]]

#### Adicionando itens no final

Para adicionar itens no final de uma lista, nós utilizamos o método ```list_name.append()```.

```python
fruits = []
fruits.append('Orange')
fruits.append('Banana')
fruits.append('Grape')
print(fruits)
```

Neste exemplo, estamos criando uma lista vazia chamada ```fruits``` e, a seguir, utilizamos o método ```append()``` para adicionar itens no seu final, resultando em:

![[37 - append.png]]

> **_Nota:_** Nós estudaremos métodos a fundo posteriormente. Por enquanto, apenas aprenda a usá-los.

#### Adicionando itens em posições específicas

O método que utilizamos para adicionar um item em uma lista em uma posição especifica é o ```insert()```. Ao utilizá-lo, nós precisamos passar o índice e o dado que queremos adicionar.

```python
fruits = ['Orange', 'Banana', 'Grape']  
fruits.insert(1, "apple")  
print(fruits)
```

Nós estamos dizendo para python adicionar a ```string "apple"``` no índice 1 da lista ```fruits```. É importante ressaltar que python não vai substituir "Banana" por "apple", ele vai empurrar banana pra frente e adicionar "apple" onde "Banana" estava.

![[38 - insert.png]]

#### Removendo itens por índice

Para remover itens de uma lista nós utilizamos o comando ```del```.

```python
fruits = ['Orange', 'Banana', 'Grape']  
del fruits[1]  
print(fruits)
```

![[39 - del.png]]

Com o comando ```del``` nós simplesmente deletamos o item da lista.

#### Removendo e atribuindo um item da lista com pop()

O método ```pop()``` tem 3 usos. Ele pode:

1. remover o ultimo item da lista
2. remover um item específico da lista
3. remover o item e atribuí-lo a uma variável

Quando apenas utilizamos o método ```pop()```, ele removerá o ultimo item da lista:

```python
fruits = ['Orange', 'Banana', 'Grape']  
fruits.pop()  
print(fruits)
```

![[40 - pop_1.png]]

Quando passamos o índice do item como argumento, ele removerá o item especifico. No exemplo a seguir, removeremos o item do índice 0:

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

Neste último caso, nós não estamos apenas acessando o item na lista e atribuindo-o à variável. Nós estamos removendo ```'Banana'``` e atribuindo à variável ```my_favorite_fruit```

![[42 - pop_2.png]]

#### Removendo um item por valor

Até agora só vimos maneiras de remover um item por índice.  Mas e quando sabemos o valor e não sabemos onde ele se encontra na lista? Para estes casos, utilizamos o método ```remove()```.

```python
fruits = ['Orange', 'Banana', 'Grape']  
fruits.remove('Banana')  
print(fruits)
```

![[43 - remove.png]]

Aqui estamos dizendo para python encontrar a palavra 'Banana' na lista e removê-la.

> **_Importante:_** O método ```remove()``` remove apenas o primeiro item com este valor!

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

Quando multiplicamos uma lista por uma ```int```, repetimos seus items dentro dela, como vemos abaixo:

```python
animals = ['cat', 'dog', 'capybara']  
print(animals * 2)
```

![[46 - list_multiplication_1.png]]

### Loops e listas

Agora que já sabemos como manipular uma lista, nós podemos falar do seu verdadeiro poder. Nós podemos utilizar um loop para iterar por todos os itens da lista e executar um bloco de código para cada um dos itens. Calma, eu sei que tá começando a soar complicado de novo. Então vamos ver isso com calma.

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

### List Slices



### Métodos mais comuns


### Exercícios 5

## Revisitando strings








## Try / Except

blah

---

## Módulos | Modules




exercícios função:

criar uma simples calculadora e usar try catch zero division

