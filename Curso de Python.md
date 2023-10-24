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

## Sobre os exercícios

Existem diversas maneiras de se fazer a mesma coisa na programação. Alguns códigos são mais otimizados que outros, mas desde que tudo funcione, tudo bem. As respostas dos exercícios podem ser encontradas [neste repositório](https://github.com/joaosoutosantiago/temporary_python_exercises).

Tente fazer do seu jeito e, caso não consiga, veja as respostas.

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

Por padrão, a primeira coisa que fazemos para confirmarmos que um programa funciona, é dizer _"Hello, world"_ , e é isso que vamos fazer. Alguns IDE's ou editores de texto já criam um arquivo python por padrão ao iniciar um projeto, outros não. Caso o arquivo não tenha sido criado, crie um arquivo chamado "hello.py". O ```.py``` é o que define que isto é um arquivo python. Escreva:

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

### Linguagens compiladas x interpretadas

Você pode ter ouvido anteriormente que computadores não entendem nada além de zeros e uns. E isto é verdade, eles só entendem código binário. Então como é possível que o computador tenha entendido o que eu escrevi? Por trás dos panos, python lê o código e "explica" para o computador o que fazer.

Existem dois tipo de linguagens, as **compiladas** e as **interpretadas**. 

Linguagens como java, C e C++ são compiladas, ou seja, o código escrito é convertido para uma linguagem que o computador entende e depois nós podemos executar o programa. Nós compilamos uma vez e executamos muitas vezes.

Outras linguagens, como python e javascript, são interpretadas. Toda vez que rodamos o código, o interpretador o lê e "explica" para o computador o que fazer, de maneira que ele entenda. Toda vez que rodarmos o código, ele será lido e explicado novamente. Quando abrimos um site, por exemplo, o browser interpreta o código do site e o monta na tela.

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

A barra inversa (também conhecida como _escape character_) também é utilizada para ignorar o caractere que vem logo em sua frente, como veremos a seguir.

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

Como você já deve estar imaginando, concatenar diversas variáveis em um texto gigante seria muito trabalhoso. Existe uma forma mais fácil de concatenar em python: utilizando uma ```f string``` ou _formatted string_.

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

Python lê o código de cima para baixo, lembra? Então primeiro ele cria a variável, depois a modifica e, por ultimo, imprime o valor atual dela na tela, que é 10.

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
# E isto também!
```

Nós podemos também usar aspas triplas para fazer comentários de diversas linhas.

```python
"""
Isto é um comentário
E isto também!

Tudo que é escrito aqui dentro é tratado como comentário.
"""
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

> **_Nota:_** Se passarmos apenas um valor como argumento, python conta de 0 até este valor, sem incluí-lo. ```range(3)``` terá um resultado de 0, 1, 2.

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

## Bonus: Controle de fluxo em Java

Você já pode ter visto códigos com uma sintaxe diferente de python, códigos com parenteses, chaves, com uma aparência bem mais assustadora. Mas a verdade é que não passa disso: aparência. Os conceitos são os mesmos em todas as linguagens. Claro, cada linguagem tem suas particularidades, mas a base é sempre a mesma.

Neste capítulo bonus eu quero te mostrar como seriam os controles de fluxo na linguagem java e explicá-los para que, caso encontre com outras linguagens que não sejam python, consiga ler os códigos sem problema algum.

### if/else if/else

```java
int number = 16;

if (number <= 10) {
    System.out.println("Small number");
} else if (number <= 30) {
    System.out.println("Medium number");
} else {
    System.out.println("Big number");
}
```

Pode ser que você consiga ler este código em java sem muitos problemas, mas vamos analisá-lo juntos, com calma, mesmo assim.

primeiro nós criamos uma variável do tipo ```int``` de valor 16 e então começamos nosso ```if```. Entre parenteses nós temos a condição que será verificada e, dentro das chaves, nós temos o bloco de código que será executado se a condição for verdadeira. Neste caso, o comando ```System.out.println()```, que é o equivalente, em java, ao ```print()``` em python. Outra coisa diferente é que, em java, em vez de ```elif```, nós usamos ```else if```.

### Laço for | For loop

```java
for (int i = 0; i < 10; i++) {
	System.out.println("i = " + i);
}
```

Este é um pouco mais assustador, não é?

Neste tipo de ```for``` loop dentro dos parênteses, nós criamos uma variável ```i``` (mas pode ter qualquer outro nome, apesar deste ser o padrão) de valor 0, definimos que o loop rodará enquanto ```i < 10```, e depois escrevemos ```i++```, que é o equivalente a ```i += 1``` em python. Ou seja, após rodar o bloco de código que está entre chaves, 1 será somado ao valor de ```i```. Este código imprimirá na tela a ```string``` concatenada ```"i = " + i```.

O equivalente a este ```for``` loop em python é:

```python
for i in range(0, 10):
	print(f"i = {i}")
```

### Laço while | While loop

```java
int i = 0;
    
while (i < 10) {
	System.out.println("i = " + i);
	i++;
}
```

O ```while``` loop já tem uma sintaxe parecida com a de python. Primeiro criamos uma variável do tipo ```int``` de valor 0 para criar a condição. O loop rodará enquanto ```i < 10```, imprimirá na tela ```"i = " + i``` e acrescentará 1 ao valor de ```i``` antes de checar o valor novamente.

O equivalente a este ```while``` loop em python é:

```python
i = 0

while i < 10:
    print(f"i = {i}")
    i += 1
```

---

# Capítulo 3: Tipos de dados collection

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

Temos duas variáveis ```a``` de valor 10 e ```b``` de valor 20 e queremos trocar seus valores para que  ```a``` seja 20 e ```b``` seja 10. Para isto, criamos uma variável temporária ```c```, depois colocamos o valor de ```a``` em ```c```, o de ```b``` em ```a``` e o de ```c``` em ```b```. É como se tivéssemos dois copos e quiséssemos passar o refrigerante primeiro copo pro segundo e o do segundo pro primeiro. Para isso usamos um terceiro copo.

Com ```typle``` podemos fazer esta troca de uma maneira muito mais simples.

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






