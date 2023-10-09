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