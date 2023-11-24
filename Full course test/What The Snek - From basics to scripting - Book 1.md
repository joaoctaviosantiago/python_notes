# Introduction

</br>

## What is programming?

Programming is giving a series of instructions to a computer. This series of instructions is known as Algorithm. Here is an example:

```
take two steps forward,
try opening the door
if it's unlocked, open the door,
if it isn't, turn left
```

It is fairly common for educators to teach programming using "hands-on examples", in which you're simply copying someone, without actually learning how to think or use the tools at your disposal. I disagree with this approach and prefer to add a little bit of information with each module, expanding our knowledge and teaching the student how to find solutions to problems using the tools they've learned.

</br>

## Do I need to know math?

A common fear among those who are interested in programming is the _myth_ that you need to know math to program. Yes, I've said _myth_. And the reason why I've said it is that most times programming will not require anything but basic math. It is important to understand that inside the computer science field there are many professions. Some will require a higher knowledge of math, others will barely require any. Just because something involve numbers, it doesn't mean it requires math.

</br>

## I think I'm too old to learn how to code

Another _myth_ that is very common is that to become a good programmer you need to start learning it very early in life. Programming is something you learn by doing, by practicing. And you'll grow with each day of doing it. No one is born a programmer. It is a skill acquired through study and practice.

</br>

## Why python?

Python is a general-purpose language, which means it is a language used in many fields, including data science, machine learning, software development, web development, automation, among others. On top of this, its syntax is similar to English, which makes it less intimidating than other languages for those who are beginning their journey.

</br>

## About the course

The course was developed in such way that each chapter will build on the previous. Because of this, everything we see will be utilized in the future, so it is crucial that you do not move to the next module until the topics are well understood. 

We'll cover other topics besides python throughout the course, even if not deeply, because we'll need this knowledge to work on our projects.

Do not limit yourself to the exercises of this course. Programming is like LEGO. It is a creative exercise. In this course you'll learn all the tools and knowledge needed to create everything you can imagine, as well as the ability to learn another programming language.

</br>

## About the exercises

There are multiple ways of doing the same thing in programming. Some codes are more optimized than others, but as long as everything works, it's good. The answers to the exercises can be found on [this repository](https://github.com/joaosoutosantiago/temporary_python_exercises).

Try to do the exercises yourself and, if you can't, check my answers.

</br>

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

RAM is the _short term memory_ of a computer. It is extremely fast when compared to the speed of an HD, however, it is much smaller in size. When we run a software, open a video, do something, all the data needed to run these things is stored on RAM, when we close these programs, they're removed from memory. Because of that, when you open a new program, its data is placed where there is free space within the RAM. The location of the data is not permanent.

</br>

## Python download and installation

Python can be downloaded from the [official website](https://www.python.org/downloads/).

> **_Important:_** Download python 3 (or the most updated version) to guarantee that the codes on this course will function correctly.

### Windows

The windows installation is simple, like any other software. Select "Add python.exe to PATH" and then just click "next" and wait.

![[chapter 1 - install_python.png]]

> **_Important:_** Check the "Add python.exe to PATH" checkbox before installing.

### MacOS

For the installation on MacOS I recommend this link from [freeCodeCamp](https://www.freecodecamp.org/news/python-version-on-mac-update/). Feel free to use a different source, maybe another website or a youtube video.

### Linux

Python comes installed with most Linux distributions. I do not recommend updating python because some libraries might break due to difference in versions.

</br>

## IDE installation

Once installed, python can run from the terminal of the computer. However, for the this first part of the course, we'll install an IDE (Integrated Development Environment) to program.

> **_Note:_** You can write your code even on Microsoft Word or Notepad, and execute it from the terminal. An IDE is a software made specifically to run certain languages, coming prepared with everything you need and optimized for this purpose. There are other text editors and IDEs you can use.

### PyCharm Community Edition

I will use PyCharm as my IDE for the first part of the course. The download can be done from [this link](https://www.jetbrains.com/pycharm/download).

> **_Note:_** There are two versions, PyCharm Professional Edition, which is paid, and PyCharm Community Edition, which is free. We'll be using the Community Edition.

Once installed, create a new project and wait a little. The first time a project is created, the IDE requires some time to organize things.

### Visual Studio Code

VSCode is a text editor optimized for coding and it utilizes plugins to improve the life of the programmer. If you are using and older or slower computer, I recommend using VSCode with the python plugin. It is easy to find on google how to install said plugins. The download can be done from [this link](https://code.visualstudio.com/).

Once installed, open the program, click in "Open folder" and select the folder in which your files will be. After this, create a file ```filename.py``` by clicking with the right button of the mouse on the "EXPLORER" panel, on the left side of the screen.

Later in the course we'll utilize VSCode for some projects.

</br>
</br>

# Chapter 1: The Basics

## My first program

It is standard that the first thing we make is a little program that says _"Hello, world"_ to confirm that everything works properly, and this is what we're going to do. Some IDE's or text editors automatically create a python file when you start a project, some don't. If your file was not created, make a file called "hello.py". The ```.py``` at the end is what makes this a python file. Write:

```python
print("Hello, world")
```

> **_Note:_** It is important to use quotation marks in the message.

And execute the program by clicking on the **play** button at the top of the screen:

![[chapter 1 - play.png]]

This should be the result:

![[chapter 1 - hello_world_resultado.png]]

There you go! You'e just made your first python program. Simple, right?

```python
print()
```

Is a function that prints on screen whatever data is between parenthesis.

> **_Note:_** We'll study functions deeply later. For now, don't worry about them.

### Interpreted x compiled languages

You might have heard that computers do not understand anything but zeros and ones. This is true, they only understand binary code. Then how is it possible that the computer has understood what I wrote? Behind the scenes, python reads the code and "explains" it to the computer.

There are two types of languages, the **compiled** ones and the **interpreted** ones.

Languages such as java, C and C++ are compiled, meaning the code written is converted to a language the computer understands and then we can execute the program. We compile it once and execute it multiple times.

Other languages such as python and javascript are interpreted. Every time we run the code, the interpreter reads it and "explains" it to the computer. And it will happen whenever you run it again. When we open a website, for example, the browser reads the website's code and creates it on screen.



## Variables

A variable is a little space in memory (RAM) where you'll store a data. This data can be a name, a date, a number, etc. It sounds confusing, I know. Let's make it a little clearer using an example. We'll make a variable called ```message```:

```python
message = "Hello, world"
print(message)
```

In this example, we're separating a little space in memory and calling it ```message```,  then we get the data ```Hello, world``` and put it inside of that space. Next, we call the function ```print()``` again:

![[chapter 1 - resultado_variable.png]]

As we can see, we have the same result. Python printed the value assigned to the variable ```message```.

> **_Important:_** The equal sign ```=``` is not the same as the mathematical sign. We'll see the comparative equal sign later. In python ```=``` is called _"Assign operator"_. It gets a value and assign it to a variable.

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



## Python reads code from top to bottom

Programming languages, in general, read code from top to bottom. In the following code, we try to print a variable that has still not been read by python:

```python
print(f"Hello, {nome}")
nome = "João"
```

When we try to run the code, python raises an error:

![[chapter 1 - erro.png]]

Here, python gives us some information about where it believes the problem is. It informs us the file and line. Then it says the name of the error it's found:

```
NameError: name 'nome' is not defined. Did you mean: 'None'?
```

It informs us that the word "nome" has not been defined. It doesn't know this word or what it means. Then it asks "Did you mean: 'None'?"



## The importance of errors

When python can't understand what you're trying to do, it will raise an error and tell you what is wrong, or try to do so. Read the error carefully and don't be afraid of googling it. As important as learning how to code, it is to learn how to debug, which is the act of fixing problems within your code. 

Nobody knows everything about a language. The more we use it, the more we learn. But even so, it is a very big topic. This is why basically everything in programming is documented. Within the documentation we can find, in detail, how to use certain tools and how the language runs behind the scenes.

Besides google and stackoverflow, now we also have the aid of AIs such as ChatGPT, among others, to help with programming. They're excellent tools that will explain and help you write code.

> **_Important:_** It is common to see students copying code generated by AI and pasting them into projects. If you don't understand the code, it can break parts of your program and even add vulnerabilities to it. Use AI as a tool only.



## Data Types

There are many data types, and each is treated by the language in a different way behind the scenes. The interaction between data will depend on their type.

Some languages are more strict and force us to specify the type of data a variable will take. These are known as _Statically Typed Languages_, and some examples are: Java, C, C++, C#, Kotlin, Go.
Other languages are less demanding and check the type of data within the variable when the program runs. These are known as _Dynamically Typed Languages_, and some examples are: Python, JavaScript, Ruby, PHP.

We've already created variables and assigned data to them, like this:

```python
message = "Hello, world"
```

As we can see, we did not have to explicitly tell python the type of data we're assigning to the variable. It can figure out the type. But in other languages, such as java, we do. Here is an example of a variable being created in java, a statically typed language:

```java
String message = "Hello, world";
```

In java we have to tell it what is the type of data the variable should expect.

But if python can recognize them, why do I need to know all the different types? Each type has their own rules of usage and interaction. We'll learn more about these when we talk about them in the following sections.

### String

The data of type ```string``` are alphanumeric characters, which means they're letters and numbers. They appear between quotation marks (double ```"``` or single ```'```).

> **_Note:_**  When a word is typed without quotation marks, python sees them as commands.

Let's make a variable ```name``` and this time let's ask the user to type their name with the function ```input```:

```python
name = input("What's your name?")
print(name)
```

When we run the code, this is what we'll see:

![[chapter 1 - string_input_en.png]]

```python
input()
```

Is a function that writes on screen the message in-between parenthesis then gets what the user types and stores it in a variable.

#### Ignoring characters

As we can see, when running the code, the user's answer was right next to the question. This can be fixed with a space, but we can also add a line break using a backwards slash ```\``` to add special characters. For example:

```python
name = input("What is your name?\n")
```

> **_Note:_** ```\n``` in the middle of a string causes a line break.

The backwards slash is also used to ignore a character that follows it, as we'll see next.

#### Should I use single or double quotation marks?

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

![[chapter 1 - concatenation_1_en.png]]

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



### Exercise 1

1. What is the result of the following expression:

```python
print("11" + "11")
```

2. What's the difference between Dynamically Typed Languages and Statically Typed Languages?
3. Madlibs is a game in which a list of words is given and added to a story. Make a program that will ask the user for 1 name and 2 adjectives, then add them to a sentence.

### Numbers

There are two numeric data types: int (integer) and float (floating-point number). Integers are whole numbers, while floats are numbers with decimal places.

| Data type | Examples                               |
|--------------|----------------------------------------|
| Int          | -2, -1, 0, 1, 2, 3, 10, 45, 67, 106    |
| Float        | -1.32 , -1.0 , 0.0 , 1.57, 43.5, 100.0 |

We can make calculations using python, and for this we utilize operators, just like in math. They are:

| Operator | Name                             | What it does                                                  |
|----------|----------------------------------|---------------------------------------------------------------|
| +        | add                              | adds the number                                               |
| -        | subtract                         | subtracts the number                                          |
| *        | multiplication                   | multiplies the number                                         |
| /        | division                         | divides the number                                            |
| %        | modulus                          | gives you the remainder of the division                       |
| **       | exponentiation                   | raises the number to a power                                  |
| //       | floor division                   | divides the number and gives you the result rounded to the closest lowest number |

Some are quite simple and you probably remember them, but others not so much. Then let's take a look on some examples to clarify their usage.

#### Modulus

This operator divides the numbers and gives us the remainder of the division. What will be the result of the expression below?

```python
print(11 % 2)
```

That's right! The result is 1.

![[chapter 1 - modulus.png]]

It divides 11 by 2 and the remainder is 1.

#### Exponentiation

In case you don't remember, exponentiation is the act of multiplying a number by itself one or more  times.

```python
print(2 ** 3)
```

Is the same as 2³ or 2 · 2 · 2, which is equal to 8.

![[chapter 1 - power.png]]

#### Floor Division

With this operator, the numbers are divided and python rounds them to the closest lowest number.

```python
print(10 // 3)
```

The result of 10 divided by 3 is 3.333, however, when we utilize the floor division, python gives 3 as the answer.

![[chapter 1 - floor_division.png]]

#### Int e Float

In certain languages, you can only execute operators with data of the same type. In python this is not the case. the language tries to understand what you're trying to do and tries to give you the most precise answer possible.

Because of that, it whenever we try to do an calculation with an ```int``` and a ```float```, the result will be a```float```. Python understands that there is a high chance the result of this calculation will be a number with decimal points, so it converts the result to ```float```.

```python
print(5.0 + 3)
```

![[chapter 1 - float.png]]

In some cases, as in the division, this also occur. Even if the division is between two integers. Python knows that there is a good chance that the result of a division will be a number with decimal points.

```python
print(4 / 2)
```

![[chapter 1 - division.png]]

#### Number of decimal places

Sometimes python will give a result with many decimal places. This is normal and it happens in many languages. Python always tries to deliver the most precise answer, which is a little hard given how computers deal with numbers.

```python
print(0.2 + 0.1)
```

![[chapter 1 - decimal_points.png]]

But what if I want a number with a specific amount of decimal places? In this case, we can format the result.

```python
number = 1 + 0.9887984
print(f"Non-formatted result: {number}")
print(f'Formatted result: {"%.2f" % number}')
```

Here we're trying to add an ```int``` and a ```float```, so we know that the result will be a ```float``` and python will try to make it as precise as it can. On the third line, notice that the variable is not alone. We've also passed ```"%.2f" % variable_name```, which will get the value passed to the variable and round it to two decimal places.

> **_Note:_** The ```"%.2f"``` must always be between quotation marks. The ```2``` is the amount of decimal places you want.

and this will be the result:

![[chapter 1 - formatted_numbers_en.png]]

#### Order of mathematical operations

Just like in math, in python the order of operations must also be respected.

```python
number = 5 + (2 + 3) ** 2
```

First we'll calculate the numbers between parenthesis, then the exponentiation and finally, we add.

![[chapter 1 - order.png]]

#### Numbers with underscore

Big numbers are often hard to read. Python solves this problem by letting us use underscores to separate the numbers, making them more readable.

```python
big_number = 4_540_000_000
print(big_number)
```

![[chapter 1 - number_with_underline.png]]

### Boolean

Boolean is a data type with only two possible values: True and False.

```python
true_bool = True
false_bool = False
```

Pretty easy, huh?

I know that it doesn't seem too relevant yet, but boolean is extremely important and we'll see their usage soon.



## Revisiting variables

Now that we already have a solid understanding of variables and data types, we can go a little deeper into these topics.

Up to this point we've only assigned a value to a variable and used it. But, as the name suggests, it is variable. Which means we can alter it's value at any moment.

```python
number = 100
number = 10
print(number)
```

In this example, first we make a variable ```number```  and assign it the integer 100. Nothing new.  Then we modify the value of the variable to 10. When we run the code, this is the result we get:

![[chapter 1 - revisiting_variables.png]]

Python reads the code from top to bottom, remember? So first it creates the variable, then python modifies it and finally, prints its current value on screen, which is 10.

Since python is a dynamically typed language, we can even change the type of the variable to string and python would understand it.

```python
number = 100
number = "hello"
print(number)
```

![[chapter 1 - revisiting_variables_2.png]]

### More assign operators

Let's imagine that we have a variable ```number``` of value 2 and we want to add 10 to its value. How would we do that?

```python
number = 2
number = number + 10
print(number)
```

It looks a little confusing, right? But let's go through it step by step. First, we create a variable and assign it the value 2. Then, we assign to the variable ```number``` the value of ```number``` + 10, meaning that the new value of ```number``` will be its current value (2) plus the integer 10. Resulting in:

![[chapter 1 - assigning_values.png]]

Another way of writing this would be:

```python
number = 2
number += 10
print(number)
```

Here are some other assign operators:

| Operator | What it does                                                        |
|----------|---------------------------------------------------------------------|
| +=       | adds to the old value and assigns the result to the variable        |
| -=       | subtracts from the old value and assigns the result to the variable |
| \*=       | multiplies by the old value and assigns the result to the variable  |
| /=       | divides by the old value and assigns the result to the variable     |
| %=       | calculates the division and assigns the remainder to the variable   |
| \**=      | raises the number to the power and assings the result to the variable |



## Type Casting

Type casting is the act of changing the type of a variable. 

While python allows us to work with integers and floats at the same time, even if they're different data types, this doesn't happen when with strings and numbers. If we try, python will raise an error.

```python
print("10" + 10)
```

![[chapter 1 - type_casting.png]]

Python is complaining and saying that it can only concatenate ```string``` (str) to ```string```, and not ```int```.

### User input

When we use the function ```input()``` to get some information from the user, this data always comes in the ```string``` format, even if the user has types a number. To deal with this situation we need to convert the data. And how do we do that?

There are a few functions we can use:

```python
int(data)
```

turns the data into an integer.

```python
float(data)
```

turns the data into a float.

```python
str(data)
```

turns the data into a string.

An use case example:

```python
number = input("type a number:\n")
number = int(number)
```

or, if you'd like to make your code more concise:

```python
number = int(input("type a number:\n"))
```



## Exercise 2

1. Make a program that asks the user to type 2 numbers and print their sum.
2. Make a program that asks the user's name and the year they were born, and shows a sentence with their name and how old they are/will be this year.
3. Make a program that asks the user for two numbers and show their division with 3 decimal places.



## Constants

Just like variables, constants are spaces in memory where data is stored. The difference is that the value assigned to a constant cannot be changed when the program is running.

When you are sure that the value of a data will not be altered during the execution of the program, you can write it as a constant. This way, the language will know that the value will not change and, behind the scenes, will make optimizations to work in a more efficient manner.

Okay, but how do I do this in python? So, python does not have a constant data type. However, since this data type exists in other languages, we follow the same naming conventions and make its name capitalized. This way we make it clear to other programmers or to ourselves when we revisit our code, that the variable should be treated as a constant. For example:

```python
CHARACTER_NAME = Lonk
```



## Comments

Comments are lines of code ignored by python, which we write for ourselves or for other programmers. Wait, this sounds confusing. Let me explain it with an example:

Imagine that you worked on a project a year ago and now you want to improve it. When opening the project, you can read all that code and decipher what each line is doing, but it would be a lot faster and easier if there were comments in the code explaining what each block of code does, or explaining how you've solved a certain problem.

Comments are essential and make our lives much easier. When we are part of a team, they allow us to clarify to other programmers what our code is doing; When we revisit our old projects, they allows us to understand what and how we did them.

In python, everything that's written in front of a ```#``` is treated as a comment.

```pyhon
# This is a comment.
# and this is too!
```

We can also use triple quotation marks to make multi-line comments.

```python
"""
This is a comment.
and this is too!

Everything written here is treated as a comment.
"""
```



## The Zen of Python

The Zen of Python is a text written by Tim Peters that describes the philosophy followed by the community to write good python code.

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

I'll comment only about a few principles. Some may not be understandable yet, but they will be later.

```
Beautiful is better than ugly.

Explicit is better than implicit.

Simple is better than complex.

Readability counts.
```

When we are beginning our programming journey, we don't know what is good and what is bad. Today we see many videos on social media telling us to write code a certain way because "it is more professional", when, in fact, you're needlessly making your code harder to read. A readable, beautiful, easy to understand and simple code is always preferred and more professional than the opposite.

And, finally, perhaps the most important principle:

```
Now is better than never.
```

Often times we want to learn as much as we can before starting. We feel we're not ready, that we don't know enough. However, you don't need to know everything to take the first step. More important that writing the perfect code, is to write a code that works. Later, if you want, you can revisit it and improve it.

Don't leave it for later. Do what you can with what you have now.



# Chapter 2: Flow Control

When we talk about flow control, we are referring to the ability of a program to decide what to do or how many times to do it, depending on a condition. Take a look at the flow chart below:

![[chapter 2 - flowchart_en.drawio.png]]

In this example, before deciding what to do, we evaluate certain conditions. Is it hot? if it isn't, we go outside. In case it is, we check if it's bearable, if it is, we go outside, if not, we wait a little and check again.

In this chapter you'll learn how to utilize flow control to improve the functionalities of your programs.

## Comparison Operators

Before we begin to utilize flow control in our code, we need to talk about comparison operators. They're used to form expressions, which are simply a combination of operators and operands, resulting in a value. We have used expressions previously, for example:

```python
number = 10 + 2
```

10 + 2 is an expression that forms the value 12. Nothing new in the horizon. With comparison operators we can create expressions a little more complex. As we can see below:

```python
is_less_than = 2 < 10
# is_less_than = True
```

In this expression, python will check if two is less than 10 and the result will be a ```boolean```, in other words, true ou false.

The comparison operators are:

| Operator  | What it does             |
|-----------|--------------------------|
| ==        | equal to                 |
| !=        | not equal to             |
| >         | greater than             |
| <         | less than                |
| >=        | greater than or equal to |
| <=        | less than or equal to    |

```python
number1 = 10  
number2 = 2  
  
print(f"Is {number1} less than {number2}? {number1 < number2}")  
print(f"Is {number1} greater than {number2}? {number1 > number2}")  
print(f"Is {number1} equal to {number2}? {number1 == number2}")  
print(f"Is {number1} not equal to {number2}? {number1 != number2}")
```

![[chapter 1 - comparisson_operators_en.png]]

> **_Note:_** Do not confuse the assign operator (=) with the equality operator (=\=).



## If / Elif / Else

The first form of flow control we'll see is the ```if``` / ```else```. The idea is simple: if a condition is true, do this, otherwise, do that.

```python
name = "Jorge"

if name == "Jorge":
	print("Hello, Jorge")
else:
	print("Hello, person")
```

In this example, we compare if the value of the variable ```name``` is the equal to "Jorge", python evaluates this expression as true, then executes the following commands. Resulting in:

![[chapter 2 - if_elif_else.png]]

If the value of the variable ```name``` was not equal to "Jorge", python would execute the commends after ```else```. 

Okay, what about the ```elif```? The ```elif``` is utilized when we have more than two options.

```python
if name == "Jorge":
	print(f"Hello, Jorge")
elif name == "Janine":
	print("Hello, Janine")
else:
	print(f"Hello, person")
```

First python will check if the value of the variable ```name``` is equal to "Jorge"; If it isn't, then it checks if the value is equal to "Janine"; If it also isn't, then it will execute the code after ```else```.

> **_Note:_** Remember that the code is executed from top to bottom. Once a condition is true, python will execute the code in its block and will not verify if any other condition is also true.

> **_Important:_** ```if``` does not need an ```else``` statement for it to work. You can have an ```if``` statement by itself and if the condition is not true, python skips the ```if``` and continues running the rest of the code. The statement can also be ended with an ```elif``` instead of an ```else```.


## Indentation

indentation is the space in the beginning of a line. In most languages, it only exists to organize and beautify the code. In other languages, like python, it is extremely important because it defines where a block of code begins and where it ends. The indentation is created with 4 spaces. Most text editors and IDEs allow us to indent with the _tab_ key.

```python
if name == "Jorge":
	# this code is indented and it belongs to the block of code of "if"
	print("Hello, Jorge")
else:
	# this code is indented and it belongs to the block of code of "else"
	print("Hello, person")
```

A block of code may contain other blocks of code, as we can see below:

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

Let's see, step by step, how python will execute this code:

1. First, python will check if ```username == "Ushi"```, if it is, it will run the following block of code:

![[chapter 2 - code_blocks_1.png]]

2.  So it will run ```print("Hello, Ushi")``` and check if ```password == "litterbox"```, if it is, it will run the block of code shown below

![[chapter 2 - code_blocks_2.png]]

3. In case ```password``` is not "litterbox", it will execute the following block of code:

![[chapter 2 - code_blocks_3.png]]

4. If ```username``` isn't "Ushi", it will execute the following block of code:

![[chapter 2 - code_blocks_4.png]]



## Line breaks

Unlike indentation, which is so important in python, line breaks are often ignored and do not affect your program in any way. Because of this, we can use it to better organize our code, making it more readable.



## Logical Operators

Logical operators are used when we want to evaluate two or more expressions. There are 3 logical operators in python: ```and```, ```or```, ```not```.

> **_Note:_** To help with readability, some people prefer to put the expressions between parenthesis.

### and

When we use the ```and``` operator, python will only run the block of code if all the expressions are true.

```python
first_number = 15  
second_number = 6  
  
if (first_number > 10) and (second_number < 20):  
    print("yay")
```

Here, ```first_number``` is greater than 10 and ```second_number``` is less than 20. Both the expressions are true; thus python will run the block of code.

### or

When we utilize the ```or``` operator, python will run the block of code if one of the expressions is true.

```python
first_number = 15  
second_number = 6  
  
if first_number > 10 or second_number < 5:  
    print("yay")
```

In this case, ```first_number > 10``` is true and ```second_number < 5``` is false. Python will execute the block of code because one of the expressions is true.

### not

When we use the ```not``` operator, we reverse the boolean value. If the expression is true, it will then become false; if it's false, it will become true.

```python
number = 6  
  
if not number < 5:
    print("yay")
```

In this example, ```number < 5``` is false. Since we're using the ```not``` operator, the block of code will be executed because ```not False``` is ```True```.



## Ternary Operator

The ternary operator is a "one-line ```if```", it's a more concise way of writing a simple ```if/else```.

```python
price = 999.99  
can_afford = "no" if price >= 1200 else "yes"
```

The value of the variable ```can_afford``` will be "no" if the price is greater than or equal to 1200, otherwise, it will be "yes".



## Exercise 3

1. Make a program that will ask the user for the grades of 3 exams, calculate the average grade, print it and if the grade is greater or equal to 6, print "You've passed! (:", if it was between 4 and 6, print "You will go to summer school", if it's less than 4, print "you've failed".
2. Make a program that asks the user for their weight and height,  calculate their BMI (Body Mass Index), print it with 2 decimal points and print the information following the table below:

| BMI         | Classification  |
|-------------|-----------------|
| <18,5       | Underweight     |
| 18,5 a 24,9 | Normal weight   |
| 25,0 a 29,9 | Overweight      |
| >30,0       | Obesity         |

3. Make a program that will calculate the tip. Ask the user for the value of the bill and how much, in percentage, they want to give as tip, then print the value of the bill, the percentage and the total value, including the tip.



## Loops

What are loops? Imagine you're drawing a circle. When you reach the end of the drawing, you find the beginning of it. In programming, loops are used in code repetition, when the code block reaches the end, it starts again. Up until now, our code began and ended, from top to bottom. But what if we want the code to run a certain amount of times, or if we want it to run until a condition is true?

> **_Note:_** Each time a loop starts over it's called an iteration.

### For loop

The ```for``` loop is used when we know how many times the code needs to be repeated. It is used utilized in conjunction with the function ```range```. Let's analyze the ```for``` loop a little more:

```python
for number in range(1, 4):
	print("Hello")
```

First we use the command ```for```, then we create a variable that I've decided to call ```number```, we then use the command ```in``` and call the function ```range```. Another way of reading this would be "for each number from 1 to 4, not including 4, do this".

When the loop begins, the variable ```number``` will have the value of 1, python will run the commands in the block of code and then will return to the beginning of the ```for``` loop, this time, ```number``` will have the value of 2, the block of code will run once more and go back to the beginning, and now ```number``` will have the value of 3, the block of code will run and the loop will end.

We can access the variable ```number``` inside the ```for``` loop.

```python
for number in range(1, 4):  
    print(number)
```

![[chapter 2 - range_function.png]]
As you can see here, on the first loop, ```number``` had the value of 1 and that was printed on screen, on the second it had the value of 2 and on the third it had the value of 3.

#### Nested for loops

Just like with ```if```, we can create a ```for``` loop inside another;

```python
for i in range(1, 5):  
    print(i, end=': ')  
  
    for j in range(1, 5):  
        print(j, end=' ')  
  
    print()
```

I know this code is a little scary, so let's read it together. The first loop begins and the variable ```i``` has the value of 1, the block of code then runs. In it, we print ```i```; Then the second ```for``` loop begins. In it, the variable ```j``` will be printed 4 times (from 1 to 5, not including 5), the second ```for``` loop ends and we go back to the block of code of the first loop, and skip a line with the function ```print()```.

This is the result:

![[chapter 2 - nested_loops.png]]

> **_Note:_**  The function ```print()``` normally breaks the line after printing. We can change this behavior by passing the parameter ```end=```.  With it we can define if after each print there will be a space, a line break, a comma, etc.

It is important to note that the variable ```i``` can be accessed anywhere within the block of code of the first ```for``` loop, even inside the second ```for``` loop, this is why I've used different names for each of them.

```python
for i in range(1, 5):
    print(i)  
	# The variable i can be accessed here, but j cannot.

    for j in range(1, 5):  
        print(i, j)  
		# both the varaibles i and j can be accessed here.
    print()
```

#### range()

Although we have seen how the function ```range()``` words, I want to go over it in a little more detail. The function ```range()``` can have up to 3 parameters:

```python
range(beginning, end, step)
```

The first, which here I'm referring to as ```beginning```, defines in which number the count will begin; The second, called ```end```, defines in which number the count will end, not including this number; the third, which I'm referring to as ```step``` will determine how the count will be done, one by one, two by two, three by three. The default is one by one.

```python
for num in range(0, 11, 2):  
    print(num)
```

![[chapter 2 - ranged_function_steps.png]]

It is also possible to pass only one argument to the ```range()``` function. In this case, python will run from 0 up to the passed argument. For example:

```python
for number in range(5):
	print(number)
```

In the first iteration, ```number``` will have the value of 0, in the second it will have the value of 1, then 2, 3, and 4. Running 5 times in total. The loop will run from 0 to 5, non-inclusive.

![[chapter 2 - range_function_single_argument.png]]

### While loop

The ```while``` loop is executed while a condition is true. It is used when we don't know how many times a code will need to run.

```python
number = 1  
  
while number <= 5:  
    print(number)  
    number += 1
```

In this example, python will test if ```number <= 5``` is true, in case it is, it will run the block of code, print the value of number and add 1 to it; case it isn't, the loop ends.

![[chapter 2 - while_loop.png]]

> **_Important:_** Be careful so that you don't create an infinite loop. If the condition never becomes false, the program will run infinitely and, eventually, crash - it will stop working and close.

#### truthy and falsy values

When we try to pass data as conditions, instead of an expression, python will evaluate that data as ```True``` ou ```False```. When the value is true, we call it "truthy", and when it's false, we call it "falsy". For example:

```python
while 10:
	print("truthy")
	# this is an infinite loop
```

The data ```0```, ```0.0```, and ```''```, are falsy. Any other date is truthy.

### Break

```break``` is a command used inside of a loop. It forces python to stop the loop and leave it.

In the following code, the loop will run and print the value of ```num``` while its value is not bigger than 5, when this happens, python will leave the loop and continue reading the code outside of it.

```python
for num in range(1, 10):  
    if num > 5:  
        break  
    print(num)  
  
print("Done!")
```

![[chapter 2 - break.png]]

### Continue

The command ```continue``` is also used inside of a loop. When python reaches this command, it passes to the next iteration of the loop.

```python
for num in range(1, 11):  
    if 2 < num < 8:  
        continue  
    print(num)  
  
print("Done!")
```

Here, we're telling python that, when the value of ```num``` is between 2 and 8, to jump to the next iteration of the loop. Which means, when ```num``` is equal to 3, python will get to the ```continue``` command, go back to the beginning, and ```num``` will now have the value of 4, and so on, until ```num``` is bigger than or equal to 8.

This will be our result:

![[chapter 2 - continue.png]]



## Exercise 4

1. Make a program that will print the number from 1 to 10 and say if they're odd or even.
2. Make a program that will print the numbers from 1 to 50, however, in case the number is divisible by 3, print "Fizz", if its divisible by 5, print "Buzz" and if it's divisible by 3 and 5, print "FizzBuzz". Hint: 15 is supposed to be "FizzBuzz".
3. Make a program that prints the following drawing:

![[chapter 2 - exercise_4-3.png]]

4. **Bonus:** Make a program that prints the following drawing:

![[chapter 2 - exercise_4-4.png]]



## Bonus: Flow control in Java

You might have already seen codes with a syntax that is different from python's, with parenthesis, curly braces, with a much scarier look. But the truth is that it's nothing more than that: looks. The concepts are the same in every language. Of course, each language has their own particularities, but the base is the same.

In this bonus section I want to show you how the control flow would be in the java language and explain them to you so that when you find code written in languages other than python, you are able to read them without any issues.

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

It might be that you can read this code in java without many issues, but let's analyze them together anyways.

First we create a variable of type ```int``` and assign it the value 16 and then we begin with our ```if```. Between parenthesis we have our condition that will be verified and, within curly braces, we have our block of code that will be executed if the condition is true. In this case, the command ```System.out.println()```, is the java equivalent of python's ```print()```. Another thing that is different is that, in java, instead of ```elif```, we use ```else if```.

### For loop

```java
for (int i = 0; i < 10; i++) {
	System.out.println("i = " + i);
}
```

This one is a little scary, huh?

In this type of ```for``` loop, inside the parenthesis, we create a variable ```i``` (but it can be called anything, this is just the standard) of value 0, define that the loop will run while ```i < 10```, and then we write ```i++```, which is the equivalent of ```i += 1``` in python. After running the code that is between curly braces, 1 will be added to the value of ```i```. This code will print on screen the concatenated ```string``` ```"i = " + i```.

The equivalente of this ```for``` loop in python is:

```python
for i in range(0, 10):
	print(f"i = {i}")
```

### While loop

```java
int i = 0;
    
while (i < 10) {
	System.out.println("i = " + i);
	i++;
}
```

The ```while``` loop has a syntax similar to python's. First we create a variable of type ```int``` of value 0 to create the condition. The loop will run while ```i < 10```, it will print on screen ```"i = " + i```, then add 1 to the value of ```i``` before checking the condition again.

The python equivalente of this ```while``` loop is:

```python
i = 0

while i < 10:
    print(f"i = {i}")
    i += 1
```



# Chapter 3: Collections data type

There are more advanced data types called ```collections``` that work like containers that can hold one or more data of various types. In this chapter we'll talk about python's **built-in collections**.

## Thinking like a programmer

Before we begin with the contents of this chapter, I would like to talk about how to think like a programmer. And what does this mean, exactly?

Well, with each exercise we're solving more complex problem. We started by solving problems that only required variables and data types to be solved; then we solved problems that combined these with flow control. We are learning isolated tools and techniques that can be combined to solve bigger problems. 

And I refer to this when I say "thinking like a programmer". I want you to learn to look at problem through different lenses. I want you to divide complex problems into smaller problems that can be solved with the tools you have at your disposal.

When we find a big and complex problem, normally we don't even know where we begin to solve it.  What we must do is to divide it into smaller problems that have a simpler answer, and solve them one by one; piece by piece.

A useful technique to achieve this goal is ```TODO```. Imagine you were hired to make a program. The first step is to define its functionalities (dividing a bigger problem into smaller, less complex ones) and, for each functionality, we define the ```TODO```, in other words, we define what each functionality will do, how many variables it will need, which data types, how the flow control will be and so on.

I hope that, from now on, you'll look at problems this way. Thinking about which steps you'll have to take to solve them. And look to what we're learning as new tools and new ways of doing the same. There are multiple ways to solve the same problem, and each will use the tools in a different way.



## List

A list is a data type that contains one or more ordered elements. Within a list we can have strings, numbers, other lists, among others.

```python
my_list = ['Hello', 'World', 1, 2.0, 3]
print(my_list)
```

![[chapter 3 - lists_1.png]]

In this example we have a list with 5 elements of various types. When we print it, python prints the entire list, including the square brackets.

> **_Note:_** Python recognizes a list because of the square brackets.

Before we see practical uses of a list, we need to learn how to manipulate it.

### Accessing a list
#### Accessing the elements of a list

As we've said, lists are ordered, which means that each element has a fixed position within them. Knowing this, we can access them by their index.

```python
my_list = ['Hello', 'World', 1, 2.0, 3]
# indice:    [0]      [1]   [2] [3] [4]
print(my_list[0])
```

Here we're telling python to print the element that is found in the position or index 0 within the list.

![[chapter 3 - list_index.png]]

> **_Important:_** The index always begins at 0. So, in a list of 5 elements, we have indexes 0, 1, 2, 3, 4. Indexes are always ```int```.

#### Accessing a list within a list

A list can contain elements of various types, including ```lists``` , ```dictionaries``` and other types we'll see later.

```python
names_and_numbers = [['Rebeca', 'Chelsey', 'Caroline'], [21, 73, -102]]  
print(names_and_numbers[0])
```

When we try to access the index 0 of the list ```names_and_numbers```, python will print the list of names.

![[chapter 3 - list_names.png]]

So how do I access the string ```'Rebeca'```?

```python
print(names_and_numbers[0][0])
```

First we access the element of index 0 of the list ```names_and_numbers```, which is the list of names, then we access the element of index 0 of it.

![[chapter 3 - list_rebeca.png]]

#### Accessing the last element

Python reads the elements of a list from left to right.

```python
fruits = ['Apple', 'Banana', 'Grape', 'Strawberry', 'Orange']
#            [0]      [1]      [2]        [3]          [4]
```

When we use negative indexes, python reads them from right to left.

```python
fruits = ['Apple', 'Banana', 'Grape', 'Strawberry', 'Orange']
#           [-5]     [-4]      [-3]       [-2]        [-1]
```

So the element of index ```-1``` is the last element of the list.

### Modifying a list

Now that we've learned how to access each element in a list, we'll see how to 
modify them.

#### Replacing elements

To replace a element in a list, we first must access the element and then assign a value, as we've done with variables previously.

```python
fruits = ['Apple', 'Banana', 'Grape']
fruits[0] = 'Orange'
print(fruits)
```

![[chapter 3 - replacing_list_elements.png]]

#### Adding elements to the end

To add elements to the end of a list we use the method ```list_name.append()```.

```python
fruits = []
fruits.append('Orange')
fruits.append('Banana')
fruits.append('Grape')
print(fruits)
```

In this example, we're creating an empty list and calling it ```fruits```,  we then use the method ```append()``` to add elements to its end, resulting in:

![[chapter 3 - append.png]]

> **_Note:_** We'll study methods in a deeper manner in the future. For now, just learn how to use them.

#### Adding elements to specific positions

The method we utilize to add an element to a list in a specific position is ```insert()```.  When utilizing it, we need to pass the index and the data we'd like to add.

```python
fruits = ['Orange', 'Banana', 'Grape']  
fruits.insert(1, "apple")  
print(fruits)
```

We are telling python to add a ```string "apple"``` into index 1 of the ```fruits``` list. It is important to note that python will not replace "Banana" with "apple". It will push "Banana" forward and add "apple" where "Banana" was.

![[chapter 3 - insert.png]]

#### Removing elements by index

To remove elements of a list we utilize the ```del``` command.

```python
fruits = ['Orange', 'Banana', 'Grape']  
del fruits[1]  
print(fruits)
```

![[chapter 3 - del.png]]

With the ```del``` command we can simply delete an element of a list.

#### Removing and assigning an element from a list with pop()

The method ```pop()``` has 3 uses. It can:

1. remove the last element from a list
2. remove a specific element from a list
3. remove the element and assign it to a variable

When we only use the method ```pop()```, it will remove the last element from a list:

```python
fruits = ['Orange', 'Banana', 'Grape']  
fruits.pop()
print(fruits)
```

![[chapter 3 - pop_1.png]]

When we pass the index of an element as an argument, it will remove the specific element. In the following examples, we'll remove the element in index 0.

```python
fruits = ['Orange', 'Banana', 'Grape']  
fruits.pop(0)  
print(fruits)
```

![[chapter 3 - pop_2.png]]

When we want to remove the item from a list and assign it to a variable, we also use ```pop()```

```python
fruits = ['Orange', 'Banana', 'Grape']  
my_favorite_fruit = fruits.pop(1)  
print(fruits)  
print(my_favorite_fruit)
```

In this example, we are not only accessing the element in the list and assigning it to the variable. We're removing ```'Banana'``` and assigning it to the variable ```my_favorite_fruit```

![[chapter 3 - pop_3.png]]

#### Removing an element by value

So far we've only seen ways of removing an element by index. But what about when we know the value but not where it is? In these cases we utilize the ```remove()``` method.

```python
fruits = ['Orange', 'Banana', 'Grape']  
fruits.remove('Banana')  
print(fruits)
```

![[chapter 3 - remove.png]]

Here we are telling python to find the word 'Banana' in the list and remove it.

> **_Important:_** The ```remove()``` method removes only the first instance of the value!

```python
fruits = ['Orange', 'Banana', 'Grape', 'Banana']  
fruits.remove('Banana')  
print(fruits)
```

![[chapter 3 - remove_2.png]]

#### Combining lists

Lists can be concatenated, or combined, with the ```+``` operator:

```python
numbers = [1, 2, 3]  
animals = ['cat', 'dog', 'capybara']  
  
numbers_and_animals = numbers + animals  
  
print(numbers_and_animals)
```

![[chapter 3 - list_concatenation_1.png]]

#### Repeating the values

When we multiple a list by an ```int```, we repeat its elements inside of it, as we can see below:

```python
animals = ['cat', 'dog', 'capybara']  
print(animals * 2)
```

![[chapter 3 - list_multiplication_1.png]]

### Loops and lists

Now that we know how to manipulate a list, we can talk about its true power. We can utilize a loop to iterate through all the elements of a list and execute a block of code for each of the elements. Wait, I know this is starting to sound complicated again. So let's go step by step.

Imagine that we are having a party and we have a list of guest names. We could make a program that will say "Hello" to all the guests. With what we've learned so far, making something like this would be a lot of work.

```python
print("Hello, Joseph!")
print("Hello, Johnny!")
print("Hello, Richard!")
print("Hello, Sabine!")
print("Hello, Jessica!")
```

Since we're dealing with a huge number of values, we can utilize loops and lists together to tackle this problem.

With what we've seen so far, we can access the elements of a list by their indexes, so we can use a ```for```loop to do it.

```python
names = ["Joseph", 'Johnny', 'Richard', 'Sabine', 'Jessica']

for index in range(len(names)):
	print(names[index])
```

Here I'm creating a ```for``` loop that starts at 0 and goes up to the length of the ```names``` list. The ```names``` list has 5 elements, so the ```range()``` function will go from 0 to 5, non-inclusive. In the first iteration, python will print ```names[0]```, which is the value ```"Joseph"```, in the second iteration, it will print ```names[1]```, which is ```"Johnny"```  and so on.

This is how you'd normally do it in other languages. Python, however, offers us a much more elegant solution to this problem.

```python
names = ["Joseph", 'Johnny', 'Richard', 'Sabine', 'Jessica']  
  
for name in names:  
    print(f"Hello, {name}!")
```

In this code, the ```for``` loop will begin and, in its first iteration, it will get the first element in ```names``` and assign it to the variable ```name```. In other words, in the first iteration ```name = "joseph"```. Python will print the message on screen, and the loop will start again. In the second iteration, ```name = "Johnny"```, and so on until it reaches the end of the list, resulting in:

![[chapter 3 - loops_and_lists_1.png]]

In case it still isn't clear, try reading the code like this: "for each name in ```names```, do:".

As you can see, with only a few lines of code we can modify multiple values at once by combining lists and loops!

### The ```in``` and ```not in``` operators

We use the ```in``` and ```not in``` operators to check if a value is in a list or not, respectively.

```python
names = ["Joseph", 'Johnny', 'Richard', 'Sabine', 'Jessica']  
  
if "Johnny" in names:  
    print("yay")
```

This code checks if the ```string``` "Johnny" is part of the list ```names``` and prints "yay" in case it is.

![[chapter 3 - in_operator.png]]

```python
names = ["Joseph", 'Johnny', 'Richard', 'Sabine', 'Jessica']  

if "Rebeca" not in names:  
    print("boo")
```

In this code, however, it checks if the ```string``` "Rebeca" is not a part of the list ```names``` and, in case it isn't, it prints "boo" on screen.

![[chapter 3 - not_in_operator.png]]

> **_Important:_** Uppercase and lowercase letters are seen differently by the computer. So ```"Rebeca"``` is not the same as ```rebeca```.

### List Slices

We already know how to access an element within a list, or how to access all the elements of a list. But what about when we only want to access some elements of a list? One option would be to create a ```for```loop and use conditions to determine which elements will be selected. But python allows us to do it in a different way: using list slices.

```python
names = ["Joseph", 'Johnny', 'Richard', 'Sabine', 'Jessica']  
  
print(names[2:5])
```

In this block of code, we are telling python to print the elements of the ```names``` from index 2 to index 5, non-inclusive. So indexes 2, 3, and 4.

![[chapter 3 - list_slices_1.png]]

List slices work the same way as the ```range()``` function we've learned previously.

```python
list_name[beginning:end:step]
```

> **_Note:_** The standard value for ```step``` is 1, which means "one by one".

> **_Important:_**  Do not forget that the slice goes from one number to the next, non-inclusively.  If I say ```[0:3]```, I'm saying from 0 up to but not including 3, in other words, 0, 1, 2.

When we don't put in a value for the beginning, we're saying "start from index 0".

```python
numbers = [10, 20, 30, 40, 50, 60]  
my_lucky_numbers = numbers[:3]  
  
print(my_lucky_numbers)
```

In this block of code, we have a variable of type ```list``` called ```numbers```, and we're making a new variable called ```my_lucky_numbers```, which is also a list, and we're assigning to it the elements from the beginning of the ```numbers``` list up to the element of index 3, non-inclusive.

![[chapter 3 - list_slices_2.png]]

When we don't put in a value for end, we're saying "go until the end".

```python
numbers = [10, 20, 30, 40, 50, 60]  
my_lucky_numbers = numbers[2:]  
  
print(my_lucky_numbers)
```

![[chapter 3 - list_slices_3.png]]

Can you tell me what the block of code of the next example does?

```python
numbers = [10, 20, 30, 40, 50, 60]  
my_lucky_numbers = numbers[::2]  
  
print(my_lucky_numbers)
```

To find out, we need to remember that list slices work with three values ```[beginning:end:step]```. We didn't pass any value for the beginning, so we're starting from index 0; we also didn't pass any value for the end, and this means "go until the end"; and, lastly, we're telling python to go in twos. This code will then read the entire list and it will assign to ```my_lucky_numbers``` the elements in indexes 0, 2 and 4.

![[chapter 3 - list_slices_4.png]]

### sorted() function

The ```sorted()``` function organizes the list without altering the original.

```python
names = ["Joseph", 'Johnny', 'Richard', 'Sabine', 'Jessica']  
  
print(f"Sorted: {sorted(names)}")  
print(f"Original: {names}")
```

![[chapter 3 - sorted_function.png]]

### len() function

The ```len()``` function counts how many elements there are in a list.

```python
numbers = [1, 2, 3, 4, 5, 6]  
length_of_list = len(numbers)  
print(length_of_list)
```

![[chapter 3 - len_function.png]]

> **_Important:_** This function can also be used with other data types, such as ```dictionary```, ```tuple```, ```string```, among others.

### max() function

The ```max()``` function returns the largest value in a list.

```python
numbers = [10, 20, 30]  
  
print(max(numbers))
```

![[chapter 3 - max_function.png]]

### min() function

The ```min()``` function returns the smallest value in a list.

```python
numbers = [10, 20, 30]  
  
print(min(numbers))
```

![[chapter 3 - min_function.png]]

### Most common methods

Later we'll see in detail what methods are and how to create them. But, for now, we only need to know that we call them utilizing the "Dot Notation", which we have utilized before:

```python
numbers = []
numbers.append(1)
```

As we can see, the dot notation is nothing more than utilizing a dot to call a method. We'll see other methods before we learn how to create them, and all of them will be called via dot notation.

#### index()

The ```index()``` method returns, in other words, has as a result, the index of an element from a list.

```python
names = ["Joseph", 'Johnny', 'Richard', 'Sabine', 'Jessica']  
jessica_index = names.index("Jessica")  
print(jessica_index)
```

![[chapter 3 - index_method.png]]

#### sort()

The ```sort()``` method organizes the list, in ascending order, or in alphabetical order.

```python
names = ["Joseph", 'Johnny', 'Richard', 'Sabine', 'Jessica']  
names.sort()  
print(names)
```

![[chapter 3 - sort_method_1.png]]

We can also organize the list in reverse, or descending order with it:

```python
names = ["Joseph", 'Johnny', 'Richard', 'Sabine', 'Jessica']  
names.sort(reverse=True)  
print(names)
```

![[chapter 3 - sorte_method_2.png]]

#### reverse()

The ```reverse()``` method reverses the order of a list.

```python
names = ["Joseph", 'Johnny', 'Richard', 'Sabine', 'Jessica']  
names.reverse()  
print(names)
```

![[chapter 3 - reverse_method.png]]

#### count()

The ```count()``` method receives one argument and counts how many times it appears in the last.

```python
names = ["Jessica", 'Jessica', 'Richard', 'Sabine', 'Jessica']  
counter = names.count("Jessica")  
  
print(counter)
```

In this example, we're passing the string "Jessica" as an argument. Python, then, will count how many times the string "Jessica" appears in the list and will assign this value to the variable ```counter```. Resulting in:

![[chapter 3 - count_method.png]]

The element "Jessica" appears 3 times in the ```names``` list.

### Beautifying lists

It can happen that our lists are too big, that they have too many elements, which make them hard to read. In these cases, we can write the list in a different way, to make it easier to read.

```python
hello_list = [  
    "hello",  
    "World",  
    "This",  
    "Is",  
    "Doggo"  
]
```

The list will continue to work perfectly.

> **_Important:_** Do not forget the comma between elements!

### Exercise 5

1. Create a program that, given the list below, finds the largest and smallest numbers, then prints them.

```python
numbers = [191, 78, 67, 195, 51, 154, 28, 45, 186, 106]
```

2. **Bonus:** Do exercise 1 without using the ```min()``` and ```max()``` functions.

3. Create a program that will print the list below without any duplicated numbers and in ascending order:

```python
numbers = [6, 2, 5, 6, 2, 7, 1, 9, 1, 7, 6, 4, 2, 6]
```

4. Still utilizing the previous list, create a program that will find the most common number in the list and print it alongside with how many times it appears on the list.
5. **Bonus:** Do exercise 3 without using the ```count()``` method.



## Revisiting strings

We already know what ```strings``` are and how they work; however, now that we've learned more concepts, we can look at them from a different angle. ```Strings``` are like lists of alphanumeric characters. With this in mind, we can, for example, access each character through its index:

```python
word = "hello"  
print(word[0])
```

Here we're accessing the element of index 0 in the ```string```.

![[chapter 3 - string_list_1.png]]

We can also access elements of a ```string``` using a ```for``` loop:

```python
word = "hello"  
  
for letter in word:  
    print(letter, end=" ")
```

![[chapter 3 - string_list_2.png]]

Or utilize the ```len()``` function to count how many elements are in the ```string```:

```python
word = "hello"  
  
letters = len(word)  
print(letters)
```

![[chapter 3 - string_list_3.png]]

```string``` is a different data type than a ```list```; thus, it has different methods. In this module we'll see other ways to manipulate and methods related to the ```string``` data type.

### String slices

Just like lists, we can also slice strings using their indexes. It works in the exact same way as **list slices**.

```python
name = "Rebeca"  
  
print(name[2:5])
```

With your knowledge of list slices, do you know what will be printed?

![[chapter 3 - string_slices.png]]

That's  correct! It prints the characters from index 2 up to index 5, non-inclusive. So indexes 2, 3 and 4 of the string ```name```.

> **_Note:_** Remember that indexes start at 0!

Everything that we've learned about **list slices** is applicable to strings. And this is a very powerful and useful tool to manipulate them. So don't hesitate to go back and read it again!

### Triple quotation marks

The ```string``` we've seen so far were all in the same line. We can utilize what we've learned to create strings with multiple lines, like, for example, with line breaks, concatenation, or even multiple ```print()``` functions. There is, however, another way: the quotation marks.

```python
text = """My dear,  
  
I'm sending you this text because I will not be able to get there on time. I'm stuck in traffic.  
Save me some cake!  
  
Love,  
me.  
"""

print(text)
```

![[chapter 3 - triple_quotes.png]]

> **_Note:_** There can be used single ```'''```  ou double ```"""``` quotes.

### Raw strings

We've seen that we can ignore characters and add special ones with the backslash, also known as the _escape character_. But what if we want that whatever it is type by the use is kept in the ```string```, including backslashes. This is where the raw string or ```r string``` come into play.

```python
print(r"hello, \"my friends\"!")
```

![[chapter 3 - raw_string.png]]

In the ```r string``` python treats everything as a part of it, even if you pass special characters.

### Most common methods

There are other methods and you can find them in the official documentation, books, on google or asking AIs. These are just the more commonly used ones.

#### upper()

The ```upper()``` method puts all the letters in the string in uppercase.

```python
name = "Fatma"  
name = name.upper()  
  
print(name)
```

Here we're creating a variable of type ```string``` with the value "Fatma", then we're assigning to the variable ```name``` the original value modified so that all the letters are in uppercase.

![[chapter 3 - upper_method.png]]

#### lower()

The ```lower()``` method puts all the letters in the string in lowercase.

```python
name = "Fatma"  
name = name.lower()  
  
print(name)
```

![[chapter 3 - lower_method.png]]

#### isupper() e islower()

They check if the characters in the string ```string``` are all in uppercase or lowercase, respectively.

```python
word1 = "HELLO"  
word2 = "WORLD"  
  
print(f"{word1} is upper? = {word1.isupper()}")  
print(f"{word2} is lower? = {word2.islower()}")
```

![[chapter 3 - isupper_islower.png]]

#### capitalize()

It transforms the first letter of the ```string``` in an uppercase letter.

```python
text = 'rodrigo has a blue car.'  
text = text.capitalize()  
  
print(text)
```

![[chapter 3 - capitalize_method.png]]

#### title()

It makes each word in the ```string``` start with an uppercase letter.

```python
name = "james bond"  
name = name.title()  
  
print(name)
```

![[chapter 3 - title_method.png]]

#### startswith() and endswith()

They check if  the ```string``` begins or ends with the passed arguments, respectively.

```python
message = "Hello, world! I'm here to learn how to code in python."  
  
print(message.startswith("Hello"))  
print(message.endswith("world"))
```

![[chapter 3 - startswith_endswith.png]]

#### split()

The ```split()``` method separates a string into elements and returns a list of them.

```python
message = "Python is so much fun. I wish I had learned it sooner"  
message = message.split()  
  
print(message)
```

![[chapter 3 - split_method.png]]

By default, it separates the string by its white spaces. But we can alter this behavior by passing an argument by which we want to separate the string. Next, we'll separate the same ```string``` by the full stop mark.

```python
message = "Python is so much fun. I wish I had learned it sooner"  
message = message.split(".")  
  
print(message)
```

![[chapter 3 - split_method_2.png]]

#### strip(), rstrip() and lstrip()

The ```strip()```, ```rstrip()``` and ```lstrip()``` methods remove elements of a string. ```strip()``` removes elements from both sides, ```rstrip()``` removes only form the right side, and ```lstrip()``` removes only from the left side. By default, they remove white spaces in the beginning, end or in both sides of the string.

```python
message = "     hello, world!       "  
  
print(f"strip: {message.strip()}")  
print(f"rstrip: {message.rstrip()}")  
print(f"lstrip: {message.lstrip()}")
```

![[chapter 3 -  strip_method.png]]

However, it is possible to pass as an argument, the element you wish to remove. Maybe their uses will be clearer with the example below:

```python
message = "______hello, world!______"  
  
print(f"strip: {message.strip('_')}")  
print(f"rstrip: {message.rstrip('_')}")  
print(f"lstrip: {message.lstrip('_')}")
```

![[chapter 3 - strip_method_2.png]]

#### replace()

This method replaces an element of the ```string``` with another. It receives two arguments: the part of the string that you want to replace and the part of the string with which you want to replace it.

```python
text = "oh no, my cat ate all my food!"  
print(text)  
  
text = text.replace("cat", "dog")  
# changes the word "cat" in the string for the word "dog"
print(text)
```

![[chapter 3 - replace_method.png]]

In this example we're replacing the string "cat" with "dog".

#### join()

The ```join()``` method receives a list or tuple as an argument and concatenates each element a string as separator.

```python
words = ["Hello", "my", "friend", "Doug"]  
phrase = " - blah - ".join(words)  
print(phrase)
```

![[chapter 3 - join_method_1.png]]

I agree that it is a bit of a strange method. But maybe another example makes it clearer. Imagine you have a  ```list``` and wishes to put all of its elements into a ```string```, separated by a space.

```python
words = ["Hello", "world", "this", "is", "dog"]  
phrase = " ".join(words)  
print(phrase)
```

Python will take the ```string``` we've passed, in this case, a white space ```" "``` and put it between each of the elements of the list passed as an argument.

![[chapter 3 - join_method_2.png]]

In other words, ```" ".join(words)``` means "take each element of the list ```words``` and put them into a string, separating them with ```" "``` ".

#### count()

The ```count()``` method takes a ```string``` as an argument and counts how many times it appears in the sentence. It's similar to the program we made on exercise 5-3.

```python
text = "oh no, my cat ate all my food!"  
  
my_counter = text.count("my")  
print(my_counter)
```

The word "my" appears twice in the given ```string```.

![[chapter 3 - count_method_2.png]]

### Exercise 6

1. Create a program that receives a string from the user and prints the same string but with the first half all in uppercase and the second half all in lowercase.
2. Make a program that receives a phrase from the user and prints it backwards. Ex: "Hello world" -> "world Hello"
3. Make a program that verifies if the world or phrase given by the user is a palindrome (a word, phrase, or sequence that reads the same backward as forward)



## List comprehension

List comprehension is a more concise form of creating a list, and it only exists in a few languages. In a single line, we can create a ```for``` loop, add the elements and even conditions.

Normally, we'd create a list in the following way:

```python
numbers = []  
  
for number in range(1, 11):  
    numbers.append(number)  
  
print(numbers)
```

![[chapter 3 - list_comprehension_1.png]]

However, with list comprehension, we can write the same thing in just one line:

```python
numbers = [number for number in range(1, 11)]  
print(numbers)
```

![[chapter 3 - list_comprehension_2.png]]

What are we doing here? First, we create a variable ```numbers``` and inside of the square brackets is where we put a list comprehension. There, we have ```number for number in range(1, 11) ```, in other words, add ```number``` to the list for each value of ```number``` from 1 to 11 (non-inclusive).

> **_Note:_** The first ```number``` in the list comprehension is the variable that will be added to the list.

Another way of **reading** the list comprehension is the following:

```python
numbers = [numbers.append(number) for number in range(1, 11)]
```

> **_Note:_** This code does not work, it's simply to show how to read a list comprehension.

The first variable inside the list comprehension - ``` number ``` - will be appended to the list being created.

Let's see some other examples. We'll make a list with only even numbers from 1 to 20 (non-inclusive).

Without list comprehension:

```python
numbers = []  
  
for number in range(1, 20):  
    if number % 2 == 0:  
        numbers.append(number)  
  
print(numbers)
```

![[chapter 3 - list_comprehension_3.png]]

With list comprehension:

```python
numbers = [number for number in range(1, 20) if number % 2 == 0]  
print(numbers)
```

![[chapter 3 - list_comprehension_4.png]]

In the example below, we have a list of names and we want to create another list only with the names that start with the letter a.

Without list comprehension:

```python
names = ["João", "Alice", "Janaína", "Ana", "Bruna", "Eduarda"]  
names_with_a = []  
  
for name in names:  
    if name.startswith('A'):  
        names_with_a.append(name)  
  
print(names_with_a)
```

![[chapter 3 - list_comprehension_5.png]]

With list comprehension:

```python
names = ["João", "Alice", "Janaína", "Ana", "Bruna", "Eduarda"]  
names_with_a = [name for name in names if name.startswith('A')]  
print(names_with_a)
```

![[chapter 3 - list_comprehension_6.png]]

Now we want to create a list that has only the names that start with A and, if their length is smaller than 4, I want to append "name: good", else I want to append "name: bad".

Without list comprehension:

```python
names = ["João", "Alice", "Janaína", "Ana", "Bruna", "Eduarda"]  
names_with_a = []  
  
for name in names:  
    if name.startswith('A'):  
        if len(name) <= 4:  
            names_with_a.append(f"{name}: Good")  
        else:  
            names_with_a.append(f"{name}: Bad")  
  
print(names_with_a)
```

![[chapter 3 - list_comprehension.png]]

With list comprehension:

```python
names_with_a = [f"{name}: Good" if len(name) < 4 else f"{name}: Bad" for name in names if name.startswith("A")]  
  
print(names_with_a)
```

![[chapter 3 - list_comprehension.png]]

### Structure

List comprehension can be a little hard to grasp at first. What i want you to understand is how it is structured. 

1. First comes the variable that will be appended to the list, along with any filtering conditions

```python
list_comprehension = [variable]  
```

2. then comes the ```for``` loop

```python
list_comprehension = [variable for variable in range(10)]  
```

3. and finally you have the conditions to filter the ```for``` loop.

```python
list_comprehension = [variable for variable in range(10) if variable > 5]  
```

The example above is the equivalent of this:

```python
list_comprehension = []

for variable in range(10):  
    if variable > 5:  
        list_comprehension.append(variable)
```

Let's see a few more examples to make it clearer. Pay attention to the structure.

Below I have a list of my favorite animals:

```python
favorite_animals = ["Toucan", "Penguin", "Otter", "Wolf", "Owl", "Ocelot"]
```

Using list comprehension, let's create a list of my favorite animals that start with the letter O.

```python
favorite_animals = ["Toucan", "Penguin", "Otter", "Wolf", "Owl", "Ocelot"]  
  
animals_with_o = [animal for animal in favorite_animals if animal.startswith("O")]
```

I'm going to iterate through all the animal names in the list ```favorite_animals``` and, if their names start with O, I'll append them to the list ```animals_with_o```.

Again: first what's going to be appended, then the for loop, and finally the conditions.

One more example: I have a list of animals.

```python
animals = ["Bear", "Zebra", "Sheep", "Lion", "Sloth", "Gecko"]  
```

But I firmly believe that any animal with a name longer than 5 characters is not cool. So I want to create a new list that has "Cool", if the animal's name is smaller than 5 characters or "not cool", if it's not.

```python
animals = ["Bear", "Zebra", "Sheep", "Lion", "Sloth", "Gecko"]  
  
cool_animals = ["Cool" if len(animal) < 5 else "Not cool" for animal in animals]
```

Here i'm appending "Cool" if the length of name is smaller than 5 and "Not cool" if it's not, for each name in the list ```animals```.

A last one:

Let's go through the list ```favorite_animals``` and get all the animal names that start with O. If they have more than 5 characters of length, we'll append "Cute", of not, we'll append "Not cute."

```python
favorite_animals = ["Toucan", "Penguin", "Otter", "Wolf", "Owl", "Ocelot"]  
  
cute_animals = ["Cute" if len(animal) > 5 else "Not cute" for animal in favorite_animals if animal.startswith("O")]
```

Here we're telling python to append "Cute" if ```len(animal) > 5``` else "Not Cute" for each animal in ```favorite_animals``` that starts with the letter O.

### Exercise 7

> **_Note:_** Use _list comprehension_ to solve these exercises.

1. Given the lists below, create a program that prints a list with only the numbers in common between them.

```python
first_list = [2, 7, 33, 27, 92, 40, 3, 28, 56]  
second_list = [90, 12, 23, 7, 38, 29, 56, 13, 2]
```

2. Make a program that generates a list of "even" or "odd" for each number from 1 to 20 (non-inclusive).  Ex: \[odd, even, odd, even...]
3. Make a program that asks the user for a sentence and print a list of all the words with 4 or less letters from it.



## Dictionary

```dictionary``` or ```dict``` is a data type that stores multiple elements, just like a list, and are used to store elements that are related. They are stored in pairs called "key" and "value", separated by a colon ```:```.  To create them, we utilize curly braces instead of square brackets.

```python
# person = {key: value, key: value, key: value, ...}
person = {'name': 'Mario', 'age': 25, 'location': 'Brazil'}
```

In addition to being created with curly braces instead of square brackets, another big difference is that to access a value, we dont use a numeric index, we use the keys.

```python
person = {'name': 'Mario', 'age': 25, 'location': 'Brazil'} 
print(person['name'])  
print(person['age'])
```

![[chapter 3 - dictionary_1.png]]

Another difference is that the elements of a  ```dictionary``` are unordered, while list elements are ordered.

```python
my_list = [1, 2, 3]  
my_other_list = [3, 2, 1]  
print(my_list == my_other_list)
```

In this case, the result is ```False``` because the values of each index are different. Lists are ordered, meaning that the order of each value is important.

```python
my_dict = {'first': 1, 'second': 2, 'third': 3}  
my_other_dict = {'second': 2, 'third': 3, 'first': 1}  
print(my_dict == my_other_dict)
```

Here, however, the result is ```True``` because dictionaries are unordered. Python doesn't care about the order of the elements, as long as they're all the same, the dictionaries will be equal.

### Accessing elements

Though we've just seen how to access the elements of a ```dictionary```, I want to explain it again so that, in case you'd like to remember later on, you can easily find it here.

We access the elements of a ```dictionary``` with their keys.

```python
doggo = {"name": "Nugget", "age": 3, "breed": "Golden Retriever"}
```

In this ```dictionary``` we have 3 keys - ```name```, ```age``` and ```breed``` - and we use them to access their respective values.

```python
doggo = {"name": "Nugget", "age": 3, "breed": "Golden Retriever"} 

print(f"Name: {doggo['name']}")  
print(f"Age: {doggo['age']}")  
print(f"Breed: {doggo['breed']}")
```

![[chapter 3 - dict_accessing_elements.png]]

### Modifying a dictionary

#### Adding elements

To add elements, we need to pass a key to be added and its respective value:

```python
doggo = {"name": "Nugget", "age": 3, "breed": "Golden Retriever"}  
  
doggo["favorite_toy"] = "bone"  
print(doggo)
```

The key "favorite_toy" does not exist in the ```dictionary```, so python will add it and assign to it the value "bone"

![[chapter 3 - dict_adding_elements.png]]

#### Modifying elements

To modify elements, we simply assign a new value to them.

```python
doggo = {"name": "Nugget", "age": 3, "breed": "Golden Retriever"}  
  
doggo["name"] = "Dorito"
print(doggo)
```

![[chapter 3 - dict_modifying_elements.png]]

#### Deleting elements

To delete elements we utilize the  ```del``` command.

```python
doggo = {"name": "Nugget", "age": 3, "breed": "Golden Retriever"}  
  
del doggo["breed"]  
print(doggo)
```

![[chapter 3 - dict_deleting_elements.png]]

> **_Note:_** The element is permanently deleted.

### Loops and dictionaries

Just like we've done with the ```list``` data type, we can use loops to iterate through all the elements of a ```dictionary```. But, for this, we need to utilize a few methods.

#### keys()

This method gives us access to only the keys of a ```dictionary```.

```python
catto = {"name": "KitKat", "age": 5, "color": "orange", "weight": 5.0}  

print(catto.keys())
```

![[chapter 3 - dict_method_keys_1.png]]

And, this way, we can use a loop to access all the keys.

```python
catto = {"name": "KitKat", "age": 5, "color": "orange", "weight": 5.0}  
  
for key in catto.keys():  
    print(key)
```

![[chapter 3 - dict_method_keys_2.png]]

#### values()

Just like the ```keys()``` method, the ```values()``` method gives us access only to the values of a ```dictionary```.

```python
catto = {"name": "KitKat", "age": 5, "color": "orange", "weight": 5.0}  
  
print(catto.values())
```

![[chapter 3 - dict_method_values_1.png]]

And with it we can use a loop to access only the values of a ```dictionary```.

```python
catto = {"name": "KitKat", "age": 5, "color": "orange", "weight": 5.0}  
  
for values in catto.values():  
    print(values)
```

![[chapter 3 - dict_method_values_2.png]]

#### items()

The ```ìtems()``` method gives us access to both keys and values.

```python
catto = {"name": "KitKat", "age": 5, "color": "orange", "weight": 5.0}  
  
print(catto.items())
```

![[chapter 3 - dict_method_items_1.png]]

Because of that, the ```for``` loop is a little different. It has two variables.

```python
catto = {"name": "KitKat", "age": 5, "color": "orange", "weight": 5.0}  
  
for key, value in catto.items():  
    print(f"Key: {key} -> Value: {value}")
```

![[chapter 3 - dict_method_items_2.png]]

Since this loop has two variables, one for ```key``` and another one for ```value```, we can manipulate both inside the ```for``` loop.

> **_Note:_** Just like we've seen before, the name of the variables passed in the ```for``` loop can be anything. I've chosen "key" and "value".

### Most common methods

#### get()

The ```get()``` method can have one or two arguments. When we try to access a key that does not exist in a ```dictionary```, python will raise an error. The ```get()``` method will return the value if the key exist and, if it doesn't, it will return the value we've passed as an argument.

```python
items = {"sword": 3, "shield": 1, "dagger": 2, "bow": 1}  
  
print(items.get("bow", 0))
```

In this example, we're telling python to print the value of the key "bow", if it doesn't exist in the ```dictionary```, print that the value is 0. The key exists in the ```dictionary```, so python prints its value.

![[chapter 3 - dict_method_get_1.png]]

```python
items = {"sword": 3, "shield": 1, "dagger": 2}  
  
print(items.get("bow", 0))
```

In this example, however, the key "bow" doesn't exist in the ```dictionary```, so python will print the default value.

![[chapter 3 - dict_method_get_2.png]]

> **_Note:_** If you only pass one argument, it will print the value if the word exists in the ```dictionary``` and, in case it doesn't, it will print the value ```None```, which is a data type that means "no value".


#### copy()

This method allows us to create a copy of a ```dictionary```.

```python
items = {"sword": 3, "shield": 1, "dagger": 2}  
new_items = items.copy()  
  
print(f"Items: {items}")  
print(f"New items: {new_items}")
```

![[chapter 3 - dict_method_copy.png]]

#### clear()

```clear()``` removes all the elements of a ```dictionary```.

```python
items = {"sword": 3, "shield": 1, "dagger": 2}  
  
items.clear()  
print(f"Items: {items}")
```

![[chapter 3 - dict_method_clear.png]]

#### setdefault()

The ```setdefault()``` method makes the ```dictionary``` always have a certain key and value.

```python
items = {"sword": 3, "shield": 1, "dagger": 2}  
  
items.setdefault("heartstone", 1)  
print(f"Items: {items}")
```

In the example above, we're defining that the ```dictionary``` must have at least 1 "heartstone". Since we didn't put one in the dictionary, python will put it.

![[chapter 3 - dict_method_setdefault().png]]

In case there is already a "heartstone" key in the ```dictionary```, python won't do anything.

```python
items = {"sword": 3, "shield": 1, "dagger": 2, "heartstone": 3}  
  
items.setdefault("heartstone", 1)  
print(f"Items: {items}")
```

![[chapter 3 - dict_method_setdefault()_2.png]]

#### pop()

```pop()``` is a method that receives a key as an argument and remove it from the ```dictionary```.

```python
items = {"sword": 3, "shield": 1, "dagger": 2}  
  
items.pop("sword")  
print(f"Items: {items}")
```

![[chapter 3 - dict_method_pop().png]]

### Beautifying dictionaries

Just like with the ```list``` data type, we can write data of type ```dictionary``` in such way that they're more readable, as we can see in the example below:

```python
person = {  
    "name": "Luigi",  
    "age": 24,  
    "location": "Italy"  
}  
  
print(person)
```

![[chapter 3 - beautifying_dict.png]]

> **_Important:_** Do not forget to put a comma between the elements!

### Exercise 8

Use the dictionary below for exercises 1 and 2:

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

1. Find the oldest person and print their name and age.
2. Find the average age of people and print it with 2 decimal places.
3. You were hired to create a program to interview 10 people about what they prefer, pizza or sushi. Make a program for this research that, in the end, print what the majority prefers and how many votes the winner received.



## Tuple

```tuple``` is an iterable data type, just like ```list``` and ```dictionary```. The elements of a ```tuple``` are ordered, so we can access them by their indexes; however, a```tuple``` is immutable. Once created, it cannot be modified.

A ```tuple``` is created by putting data in-between parenthesis.

```python
numbers = (10, 20, 30)  
  
print(numbers)
```

![[chapter 3 - tuple.png]]

> **_Important:_** A ```list``` or a ```dictionary``` inside of a ```tuple``` can still be modified; but the structure of the ```tuple``` cannot.

### Accessing elements

Since ```tuple``` is ordered, its elements can be accessed by their indexes, just like ```list```.

```python
numbers = (10, 20, 30)  
  
print(numbers[1])
```

![[chapter 3 - accessing_tuple.png]]

> **_Important:_** The indexes always begin at 0.

### Tuple slices

We can also access the elements of a ```tuple``` with slices.

```python
numbers = (10, 20, 30, 40, 50)  
  
print(numbers[:3])
```

![[chapter 3 - tuple_slices_1.png]]

```python
numbers = ("Banana", "Apple", "Grape")  
  
print(numbers[::-1])
```

![[chapter 3 - tuple_slices_2.png]]

### Methods

#### count()

It counts the amount of times an element appears in the ```tuple```.

```python
numbers = (10, 20, 30, 30, 40, 20, 30, 10)  
  
print(numbers.count(30))
``` 

![[chapter 3 - tuple_method_count.png]]

#### index()

It shows the index of the element passed as an argument.

``` python
names = ("Giulia", "Geoff", "Gob")  
  
print(names.index("Geoff"))
```

![[chapter 3 - tuple_method_index.png]]

### Unpacking tuple

Unpacking tuple means to put each element of the ```tuple```inside of a variable. Python allows us to do this in a very elegant manner.

```python
numbers = (10, 20, 30)  
a, b, c = numbers  
  
print(a)  
print(b)  
print(c)
```

![[chapter 3 - unpacking_tuple.png]]

### Swapping variables

We can also swap the value of variables with ```tuple```. Normally, if we want to do this, we would do it in the way shown below:

```python
a = 10  
b = 20  
  
print(f"a: {a}, b: {b}")  
  
c = a  
a = b  
b = c  
  
print(f"a: {a}, b: {b}")
```

![[chapter 3 - swapping_variables_1.png]]

We have two variables, ```a``` of value 10 and ```b``` of value 20, and want to swap their values so that ```a``` becomes 20 and ```b``` becomes 10. To do this, we create a new temporary variable ```c```, then put the value of ```a``` in ```c```, the value of ```b``` in ```a``` and of ```c``` in ```b```. It's as if we had two cups, orange soda in cup A and grape soda in cup B, and wanted to put grape soda in cup A and orange soda in cup B. For this, we'd use a third empty cup called C. We'd put orange soda in cup C, grape soda in cup A and orange soda, which is currently in cup C, in cup B.

With ```tuple``` we can do this in a much easier way.

```python
a = 10  
b = 20  
  
print(f"a: {a}, b: {b}")  
  
a, b = b, a  
  
print(f"a: {a}, b: {b}")
```

![[chapter 3 - swapping_variables_2.png]]

### Concatenating tuple

Though we cannot modify tuples, we can concatenate them to create new ones.

```python
numbers = (1, 2, 3)
numbers_total = numbers + (4, 5, 6)

print(numbers_total)
```

![[chapter 3 - tuple_concatenation.png]]

### Exercise 9

Use the ```tuple``` below to solve the exercises 1, 2 and 3:

```python
numbers = (7, 42, 93, 58, 12, 24, 30)
```

1. Print the last three numbers
2. Print the average of all the elements
3. Print the tuple backwards
4. You're working with a team to create a 2D game. In such games, character's positions are defined by the coordinates (x, y). You're asked to create a new spell for the player character that swaps their location with their enemy. Create the code for this mechanic, print the previous positions and the current ones.



## Set

```set``` is an iterable data type that removes duplicated elements. Its elements are unorganized, meaning that we cannot access them by indexes (it is common that elements change order when printed).

```python
numbers = {10, 20, 10, 30, 10, 40}  
  
print(numbers)
```

![[chapter 3 - set_1.png]]

As we can see, all the duplicated numbers were removed and the order in which they were printed is different than the order in which the ```set``` is written.

The data of type ```set``` can only contain immutable data, which means data that cannot be altered. If you try to add a data of type ```list``` or ```dict``` inside of a ```set```, python will raise an error.

> **_Important:_** Be careful not to confuse ```set``` with ```dictionary```. Both use curly braces but ```dictionary``` has key-value pairs.

### Accessing elements

Since the elements of a ```set``` are not ordered, we can't access them by indexes. Because of this, the only way of accessing them is through a loop.

```python
vowels = {"a", "e", "i", "o", "u"}  
  
for vowel in vowels:  
    print(vowel)
```

![[chapter 3 - accessing_sets.png]]

### Modifying a set

#### Adding elements

##### add()

Through the ```add()``` method we can add an element to a ```set```.

```python
letters = {"a", "b", "c"}  
  
letters.add("d")  
print(letters)
```

![[chapter 3 - set_method_add.png]]

##### update()

The ```update()``` method takes an iterable data as an argument and, this way, allows us to add multiple elements at once.

```python
languages = {"python", "gdscript", "kotlin"}  
languages_to_learn = ["java", "kotlin"]  
  
languages.update(languages_to_learn)  
print(languages)
``` 

![[chapter 3 - set_method_update.png]]

#### Removing elements

##### remove()

The ```remove()``` method removes an element from the ```set```. If the element is not in the ```set```, it raises an error.

```python
languages = {"python", "gdscript", "kotlin"}  
  
languages.discard("kotlin")  
print(languages)
```

![[chapter 3 - set_method_remove.png]]

> **_Note:_** We'll learn how to deal with errors later.

##### discard()

```discard()``` also removes an element from a ```set```, but if the element doesn't exist, it doesn't raise an error.

```python
languages = {"python", "gdscript", "kotlin"}  
  
languages.discard("kotlin")  
print(languages)
```

![[chapter 3 - set_method_discard.png]]

#### pop()

The ```pop()``` method with a ```set``` has to use cases. It can:

1. remove a **random** element from the set
3. remove a **random** element and assign it to a variable

First use case:

```python
languages = {"python", "gdscript", "kotlin"}  
  
languages.pop()  
print(languages)
```

![[chapter 3 - set_method_pop_1.png]]

Second use case:

```python
languages = {"python", "gdscript", "kotlin"}  
  
random_language = languages.pop()  
print(languages)  
print(random_language)
```

![[chapter 3 - set_method_pop_2.png]]

### Set operations

Just like in math, set operations such as union, intersection and difference can be done with a set. I know that we get scared when math is involved. But I'll try to explain it all in detail and draw for you to see that it is not as hard as it seems.

There are operators and methods for each of these operations. I'll be showing both.

> **_Note:_** In the examples I used two sets only, but it is also possible to do operations with three or more.

#### Union

When we make a union of sets, we take all the elements contained in all the sets.

![[chapter 3 - set_union.jpg]]

In python, we can utilize the ```union()``` or the ```|``` operator.

```python
numbers = {1, 2, 3, 4}  
more_numbers = {3, 4, 5, 6}  
  
print(f"Method: {numbers.union(more_numbers)}")  
print(f"Operator: {numbers | more_numbers}")
```

![[chapter 3 - set_union_2.png]]

As we can see, a new set was created containing all the elements of the sets ```numbers``` and ```more_numbers```, with no duplicates, since ```set``` data types don't allow them.

#### Intersection

When we do the intersection of sets, we simply take the unique elements that belong to all the sets.

![[chapter 3 - set_intersection.jpg]]

In python, we can utilize the ```intersection()``` method or the ```&``` operator.

```python
numbers = {1, 2, 3, 4}  
more_numbers = {3, 4, 5, 6}

print(f"Method: {numbers.intersection(more_numbers)}")  
print(f"Operator: {numbers & more_numbers}")
```

![[chapter 3 - set_intersection_2.png]]

Here a new set was created containing the elements that appear in both the ```numbers``` set and the ```more_numbers``` set. Again, without duplicates because data of type ```set``` does not allow for duplicated values.

#### Difference

When we do the difference between sets, we take only the elements that exist in one set but not the others.

![[chapter 3 - set_difference.jpg]]

In python, we can use the ```difference()``` method or the ```-``` operator.

```python
numbers = {1, 2, 3, 4}  
more_numbers = {3, 4, 5, 6}

print(f"Method: {numbers.difference(more_numbers)}")  
print(f"Operator: {numbers - more_numbers}")
```

![[chapter 3 - set_difference_2.png]]

A new set was created containing only the numbers that are present in the ```numbers``` set, but that are not present in the other sets.

#### Symmetric difference

When we do the symmetric difference of sets, we take all the elements that are unique to each set. Any element that is present in both sets is ignored.

![[chapter 3 - set_symmetric_difference.jpg]]

In python, we can use the ```symmetric_difference()``` method or the ```^```operator.

```python
numbers = {1, 2, 3, 4}  
more_numbers = {3, 4, 5, 6}

print(f"Method: {numbers.symmetric_difference(more_numbers)}")  
print(f"Operator: {numbers ^ more_numbers}")
```

![[chapter 3 - set_symmetric_difference_2.png]]

In this case, we're creating a new set with all the elements that belong to the ```numbers``` set and to the ```more_numbers``` set. Any other element that is present in both sets was not included.



## Frozenset

Data of the type ```frozenset``` are immutable sets, meaning the original cannot be modified.

We can create them using the ```frozenset()``` function.

If we don't pass any arguments, the function will create an empty data of type ```frozenset```. In case we do pass an iterable as an argument to the function, it will do a type casting and turn the data into a frozenset.

``` python
numbers = [1, 2, 3, 4, 5]  
numbers = frozenset(numbers)  
  
print(numbers)
```

In this example, we're passing a list as an argument and doing the type casting to frozenset. This is the result:

![[chapter 3 - frozenset.png]]



## More type casting

We know that we can alter the type of a data through what we call type casting. And we can also do this with collection data types.

In general, they work the say way as we've seen before. The only difference is that they have to take an iterable (that we can access using a loop) data as an argument, like a string or a collection.

```python
list(data)
```

Converts the data to the ```list``` type.

```python
tuple(data)
```

Converts the data to the ```tuple``` type.

```python
set(data)
```

Converts the data to the ```set``` type.

And we can visualize this with the ```type()``` function, which tells us the type of the passed data.

```python
numbers = [1, 2, 3]  
print(numbers)  
print(type(numbers), end="\n\n")  
  
numbers = tuple(numbers)  
print(numbers)  
print(type(numbers), end="\n\n")  
  
numbers = set(numbers)  
print(numbers)  
print(type(numbers))
```

![[chapter 3 - type_casting.png]]

> **_Note:_** We will later learn how to create our own classes.

Type casting to the ```dictionary``` data type is a little different. It receives a list, a set or a tuple of tuples of length 2 and then converts them to a dictionary.

As we know, dictionaries store elements in key-value pairs. Because of this, to transform a data to the ```dict``` type, we need to pass as arguments data of type ```tuple```  of length 2.

```python
name_and_age = [("Whiskers", 3), ("Bubbles", 6)]  
  
print(dict(name_and_age))
```

In this example, we hae a list of data of ```tuple``` type (but it could be a set of tuples or a tuple of tuples), and we're converting it to the ```dict``` type.

![[chapter 3 - type_casting_dict.png]]


## Exercise 10

Given the lists below:

```python
names1 = ['Rachel', 'Augusto', "Giorgio"]  
names2 = ['Pedro', 'Conan', 'Rachel',]  
names3 = ['Conan', 'Giorgio', 'Rodrigo']
```

1. Print the elements that appear in one list but not the others.
2. Print all the elements of all three lists without duplicates.
3. Create a program to check if the list below has repeated numbers and print "Yes, it has repeated numbers" or "No, it doesn't have repeated numbers".

```python
numbers = [12, 7, 5, 46, 32, 26, 1, 90, 88, 7, 12, 26, 1]
```



## zip() function

The ```zip()``` function takes 2 or more iterable data as arguments and turns them into an object of type ```zip```, which contains a group of tuples and is iterable. I know it sounds too complicated, but it will be clearer with some examples.

```python
positions = [1, 2, 3]  
months = ["January", "February", "March"]  
my_zip = zip(positions, months)  

print(my_zip)
```

In this example we have two lists and we're using the ```zip()``` function to join them. If we try to print it directly, python will print that it is an object of type ```zip``` and where it is located in memory.

![[chapter 3 - zip_1.png]]

Objects of type ```zip``` are iterable, so we can use a loop to access its elements.

```python
positions = [1, 2, 3]  
months = ["January", "February", "March"]  
my_zip = zip(positions, months)  
  
for element in my_zip:  
    print(element)
```

![[chapter 3 - zip_2.png]]

When accessing them, we can see that the object of type ```zip``` took the elements of each list and created tuples. The first element with the first element, the second element with the second element and so on.

So the object of type ```zip``` contains one or more elements of type ```tuple```. And we can use type casting to turn a ```zip``` object into a list, a set, a tuple or even a dict.

In the example below, we transform it into a list of tuples:

```python
positions = [1, 2, 3]  
months = ["January", "February", "March"]  
zip_list = list(zip(positions, months))  
  
print(zip_list)
```

![[chapter 3 - zip_3.png]]

In this example, we turn it into a dict:

```python
positions = [1, 2, 3]  
months = ["January", "February", "March"]  
zip_dict = dict(zip(positions, months))  
  
print(zip_dict)
```

![[chapter 3 - zip_4.png]]

> **_Important:_** It is only possible to turn an object of type ```zip``` in an object of type ```dict``` when the zip has only tuples of size 2, because dicts only accept pairs of elements.

### Iterables of different lengths

When we pass iterables of different lengths as arguments to the ```zip()``` function, the zip object will have its length equal to the length of the shortest argument. Let me use an example to demonstrate this:

```python
positions = [1, 2, 3, 4, 5, 6, 7]  
months = ["January", "February", "March"]  
zip_list = list(zip(positions, months))  
  
print(zip_list)
```

Here we're passing two arguments to the ```zip()``` function: the ```positions``` list that has a length of 7, meaning it has 7 elements; and the ```months``` list that has only 3. In this case, the  created zip object will have its length equal to the shortest argument passed, the ```month``` list. The length of the zip object will be 3.

![[chapter 3 - zip_5.png]]



## Optimization

I know that we've seen many data types and their different uses. But how do I know which data type to use? There is no correct answer to this question. There are many solutions to the same problem. You can get to the same result utilizing different data types and it is up to you to choose which one you think is best.

With this in mind, it is important that we talk about optimization. We say a code is optimized when it is efficient. It uses the minimum amount of memory required for it to work or it reaches a result in a fast manner. And choosing which data type is needed for your algorithm does make a difference. For example, if you know that a set of data will not and cannot be changed during runtime, use a data of type ```tuple``` instead of a list, for the tuple has these characteristics specifically - it is optimized for it.

When we create more than one algorithm to solve a problem, we can evaluate which is more efficient using what is called Big O Notation. Imagine you've created two algorithms that modify a data of type ```string```. When we're working with short strings, both algorithms are fast and solve the problem in milliseconds. But what about when we work with strings with a thousand characters, or one hundred thousand, which one would be faster? The Big O Notation is used to solve this question, evaluating them and classifying them.

### The most important thing is to make it work

I don't believe that it is relevant for us to study optimization for now, so I don't want you to worry about it. I'm only mentioning it so you know this exists. We'll learn more about it on a later chapter.

I made sure to put this in the title so that it is clear: Optimization comes later, if there is need for it. **The first and most important part is to make the program work.** If you'd like to go back and optimize your code later down the road, if there is need, okay. Great. But in case there is no need, move on.

The intention here is that you know these terms and have an idea of what they mean. It is common to hear cases in which excellent programmers learned to code by themselves and felt completely lost once they entered the industry and started hearing these technical terms they had never heard of.

So don't worry about it for now. Let's continue studying because first we need to learn how to do it, then we can learn how to improve what we've made.



## Bonus: A deeper look into variables

You're already quite comfortable with variables, what they are and how to use them. So now I'd like to explain them a little further.

In most courses I've done and books I've read, variables were described as "different than the variables in math". And if you've done other courses or have seen them being described in such way, you were probably as confused as I was; because if we stop to think about it, the variables we've used so far are identical to the variables in math. In mathematics, a variable ```x``` has a value that can be an integer or a floating-point number, for example. So why is it that they are explained in such way? This is the question that is not answered in most courses, so we'll answer it here.

We know that variables are stored in memory addresses. When we create a variable and give it a name, this name is simply a reference, or a label, to the memory address in which the data is located.

Imagine you're returning home and run into a friend, and he asks "Where are you going?" and you asnwer "i'm going home." When you say "home", your friend understands that you're referring to your address, which is Mozzarella street, number 70, Cheese county. So you can either say your full address, or you can use a more descriptive reference. And this is how it works with variables.

When we create a variable called ```hello``` and call the ```print()``` function to print it, python understand that when you say ```hello```, you're referring to some data that is located on that address in memory.

To make this a little more visible, let's take another look at the ```zip()``` function we saw earlier.

```python
positions = [1, 2, 3]  
months = ["January", "February", "March"]  
my_zip = zip(positions, months)  

print(my_zip)
```

When we try to print the variable ```my_zip```, python understands that the variable name is simply a reference to an address in memory. 

![[chapter 3 - zip_1.png]]

When we print it, it tells us that inside the memory address ```0x7f9a1e5f3780``` there is a zip object. Python understands that the variable name ```my_zip``` is a reference to the memory address ```0x7f9a1e5f3780```.

And this is how a computational variable differs from the mathematical variable. It isn't simply a name with a value, it is a name that points to memory address, where a value is located.



