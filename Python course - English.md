# Introduction

## What is programming?

Programming is giving a series of instructions to a computer. This series of instructions is known as Algorithm. Here is an example:

```
take two steps forward,
try openning the dor
if you can, open the dor,
if you can't, turn left
```

It is fairly common for educators to teach programming using "hands-on examples", in which you're simply copying someone, without actually learning how to think or use the tools at your disposal. I disagree with this approach and prefer to add a little bit of information with each module, expanding our knowledge and teaching the student how to find solutions to problems using the tools they've learned.

---
## Do I need to know math?

A common fear among those who are interested in programming is the _myth_ that you need to know math to program. Yes, I've said _myth_. And the reason why I've said it is that most times programming will not require anything but basic math. It is important to understand that inside the computer science field there are many professions. Some will require a higher knowledge of math, others will barely require any. Just because something involve numbers, it doesn't mean it requires math.

---
## I think I'm too old to learn how to program

Another _myth_ that is very common is that to become a good programmer you need to start learning it very early in life. Programming is something you learn by doing, by practicing. And you'll grow with each day of doing it. No one is born a programmer. It is a skill acquired through study and practice.

---
## Why python?

Python is a general-purpose language, which means it is a language used in many fields, including data, machine learning, software development, web development, automation, among others. On top of this, it's syntax is similar to English, which makes it less intimidating than other languages for those who are beginning their journey.

---
## About the course

The course was developed in such way that each module will build on each other. Becaue of this, everything we see will be utilized in the future, so it is crucial that you do not move to the next module until the topics are well understood. 

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

This is the long term memory of a computer. The data is **persistent**, which means that even after you turn off the computer, the data on your HD will still exist. It is where you'll store photos, videos, software, games, etc. The data is structure, it is always in the same place.

### RAM | Random Access Memory

RAM is the short term memory of a computer. It is extremely fast when compared to the speed of an HD, however, it is much smaller in size. When we run a software, open a video, do something, all the data needed to run those things is stored on RAM, when we close those programs, they're removed from memory. Because of that, when you open a new program, it's data is placed where there is free space within the RAM. The location of the data is not permanent.

---
## Python download and installation

Python can be downloaded from the [official website](https://www.python.org/downloads/).

> **_Important:_** Download python 3 (or the most updated version) to guarantee that the codes on this course will function correctly.

### Windows

The windows installation is simple, like any other software. Select "Add python.exe to PATH" and then just click "next" and wait.

![Instalaçao_windows](https://cdn.discordapp.com/attachments/884293904357277706/1146365755240222760/image.png)

> **_Important:_** Check the "Add python.exe to PATH" checkbox before installing.

### MacOS

For the installation on MacOS I recommend this link from [freeCodeCamp](https://www.freecodecamp.org/news/python-version-on-mac-update/). Feel free to use a different source, maybe another website or a youtube video, whatever is better for you.

### Linux

Python comes installed with most Linux distributions. I do not recommend updating python because some libraries might break due to difference in versions.

---
## IDE installation

Once installed, python can run through the terminal of the computer. However, we'll install and IDE (Integrated Development Environment) to program.

> **_Note:_** You can write your code even on Word and execute it through the terminal. An IDE is a software made specifically to run certain languages, coming prepared with everything you need and optimized for this purpose. There are other software, text editors and IDEs you can use. 

### PyCharm Community Edition

I will use PyCharm as my IDE for this course. The download can be done from [this link](https://www.jetbrains.com/pycharm/download).

Once installed, create a new project and wait a little. The first time a project is created, the IDE requires some time to organize things.

### Visual Studio Code

If you are using and older or slower computer, I recommend using VSCode with the python plugin. VSCode is a lightweight text editor that becomes a python IDE with it's plugin installed. It is easy to find on google how to install said plugins. The download can be done from [this link](https://code.visualstudio.com/download).

---
# Module 1: The basics of python

## My first program

It is standard that the first thing we do is a little program that says "Hello, world". And this is what we're going to do. Write:

```python
print("Hello, world")
```

> **_Note:_** It is important to use quotation marks in the message.

And execute the program by clicking on the **play** button at the top of the screen:

![play](https://cdn.discordapp.com/attachments/816889149361225728/1146380510206115940/image.png)

This should be the result:

![hello_world](https://cdn.discordapp.com/attachments/816889149361225728/1146381511889784962/image.png)

There you go! You'e just made your first python program. Simple, right?

```python
print()
```

Is a function that prints on screen whatever data is between parenthesis.

---
## Variables

A variable is a little space in memory (RAM) where you'll store a data. This data can be a name, a date, a number, etc. It sounds confusing, I know. Let's make it a little clearer using an example:

Let's make a variable named ```message```:

```python
message = "Hello, world"
print(message)
```

In this example, we're separating a little space in memory and calling it ```message```,  then we get the data ```Hello, world``` and put it inside of that space. Next, we call the function ```print()``` again:

![hello_world](https://cdn.discordapp.com/attachments/816889149361225728/1146381511889784962/image.png)

As we can see, we have the same result. Python printed the value assigned to the variable ```message```

> **_Important:_** The equal sign (=) is not the same as the mathematical sign. We'll see the comparative equal sign later. In python (=) is called _"Assign operator"_. It gets a value and assign it to a variable.

Okay, but where is this used? Think of the games you've played. The number of lives, your HP, the stages, the information about your character. All of these data is stored in variables that change  (or not) throughout the game.

Variables can have any name, however, there are some rules that must be followed when choosing them::

* The name of the variables cannot contain space.
* They can only contain letters, numbers and underscores, but they can only begin with a letter or underscore. The names cannot begin with a number.
* The ideal is that names are descriptive and help understand the type of information the variable has.
* Avoid using words that are reserved by python, like ```print``` .

> **_Note:_** There are some naming conventions. Some of them are:
> 
> * **camelCase**: The first word starts with a lowercase letter and the rest of the words with an uppercase letter.
> * **PascalCase**: The first letter of every word is uppercase.
> * **snake_case**: All the words are lowercase and separated by underscores.
> * **kebab-case**: All the words are lowercase and separated by a hyphen.
> 
> Python recommends snake_case

---
## Python reads code from top to bottom

Programming languages, in general, read code from top to bottom.

In the following code, we try to print a variable that has still not been read by python:

```python
print(f"Hello, {name}")  
name = "João"
```

When we try to run the code, python raises an error:

![erro](https://cdn.discordapp.com/attachments/816889149361225728/1146654676671004742/image.png)

Here, python gives us some information about where it believes the problem is. It informs us the file and line. Then the name of the error it's found:

```
NameError: name 'name' is not defined.
```

It informs us that the word "name" has not been defined. It doesn't know this word or what it means.

---
## The importance of errors

When python can't understand what you're trying to do, it will raise an error and tell you what is wrong, or try to do so. Read the error and don't be afraid of googling it. As important as learning how to code, it is to learn how to  debug, which is the act of fixing problems within your code. 

Nobody knows everything about a language. The more we use it, the more we learn. But even so, it is a very big topic. This is why basically everything in programming is documented. Within the documentation we can find how to use certain tools and how the language runs behind the scenes.

Besides google and stackoverflow, now we also have the aid of AIs such as ChatGPT, among others, to help with programming. They're excellent tools explain and help you write code.

> **_Important:_** It is common to see students copying code generated by AI and pasting them into projects. If you don't understand the code, it can break parts of your program and even add vulnerabilities to it. Use AI as a tool only.

---
## Data Types

There are many data types, and each is treated by the language in a different way behind the scenes. The interaction between data will depend on their type.

Some languages are more strict and force us to specify the type of data a variable will take. These are known as _Statically Typed Languages_, and some examples are: Java, C, C++, C#, Kotlin, Go.
Other languages are less demanding and check the type of data within the variable when the program runs. These are known as _Dynamically Typed Languages_, and some examples are: Python, JavaScript, Ruby, PHP.

But if python can recognize them, why do I need to know all the different types? Each type has their own rules of usage and interaction. We'll learn more about these when talking about them in the following sections.

Here is an example of a variable of type string in java, a statically typed language:

```java
String name = "João";
```

### String

The data of type ```string``` are alphanumeric characters, which means they're letters and numbers. They appear between quotation marks (double " or single ').

> **_Note:_**  When a word is typed without quotation marks, python sees them as commands.

Let's make a variable ```name``` and this time let's ask the user to type their name with the function ```input```:

```python
name = input("What is your name?")
print(name)
```

When we run the code, this is what we see:

![input](https://cdn.discordapp.com/attachments/816889149361225728/1146659574150078524/image.png)

```python
input()
```

Is a function that writes the message in-between parenthesis then get's what the user types and stores it in a variable.

#### Ignoring characters

As we can see, when running the code, the user answer was right next to the question. This can be fixed with a space, but we can also add a line break using a backwards slash ```\``` to add special characters. For example:
```python
name = input("What is your name?\n")  
```

```\n``` in the middle of a string causes a line break.

The backwards slash is also used to ignore a character that follows it, as we'll see next.

#### Should I use single or double quotes?

Both work the same way: They determine where the string begins and where it ends. Let's assume that you want to add quotation marks to works within a string:

```python
"And then he said "wow""
```

As we can see, the colors are different to let us know that python will complain and raise an error. It can't understand that "wow" is a part of the string because the first quotation marks determine where the string begins and the second where it ends.

One possible solution is to use the backwards slash, as we've seen:

```python
"And then he said \"wow\""
```

In this case, the colors haven't changed. Python understands that the quotation marks around "wow" should be treated as a part of the string, because they're in front of a backwards slash.

Another form to deal with this situation is to utilize single quotation marks:

```python
'And then he said \"wow\"'
```

Here, the single quotation marks determine where the string begins and where it ends, so the double quotation marks are treated as a part of the string.

#### Concatenation

Concatenation is the act of putting two data of type string together. The most common way of doing this is by using the ```+``` operator.

```python
name = input("What is your name?\n")  
print("Hello, " + name)
```

In this case we are concatenating the string "hello, " and the string inside the variable ```name```, which was given by the user.

![concatenação](https://cdn.discordapp.com/attachments/816889149361225728/1146663484461957200/image.png)

As you're probably already imagining, concatenating multiple variables in a huge text is going to be a lot of work. There is a better way of concatenating strings in python: using an ```f string```.

```python
name = input("What is your name?\n")  
print(f"Hello, {name}")
```

In the ```f string``` all the variables are between curly braces in the middle of the string. Python understands that they're variables and replaces them with their values.

---
### Exercise 1:

1. What is the result of the expressions:
```python
print("11" + "11")
```

2. What's the difference between Dynamically Typed Languages and Statically Typed Languages?

3. Madlibs is a game in which a list of words is given and added to a story. Make a program that will ask the user for 1 name and 2 adjectives, then add them to a sentence.

---
### Numbers