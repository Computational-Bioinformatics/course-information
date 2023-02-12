# Bioinformatics (CMPSC 300) Lab 1

This repository contains information about Bioinformatics lab 1 deliverables.


## Assignment Title

Researching and reporting on bioinformatics research tools (I)

## Dates

Handed out: 5 Sept 2022

Due: 12 Sept 2022

<!-- ### Submission notes

Please submit all deliverables through your assignment GitHub repository.
 + Place report document writing directory -->

## Contents

- [Objectives](#Objectives)
- [Part1](#Part-1)
- [Part2](#Part-2)
- [Cloning Your Repository](#Cloning-Your-Repository)
- [Part3](#Part-3)
- [Deliverables](#Deliverables)
- [Assessment](#Assessment)

---

## Objectives

 + To learn how to use JupyterLite where homework can be pulled from the cloud, completed and submitted.
 + To learn how to use`git` from [https://github.com/](https://github.com/) to manage homework assignments.
 + To learn how to make a basic edit to a Python program.
 + To do research and report on Bioinformatics tools.

---

## Part 1

[![GitHub Logo](graphics/octocat.png)](https://github.com/)

In this part, we will be spending some time to get accustomed to the online version of Python that we will be using in this course. If you have any questions as you complete the below steps, please ask your peers or Technical Leaders, or see your instructor.

### No GitHub Account?

Before you can use JupyterLite, you will need to have an account on GitHub [https://github.com/](https://github.com/).

[![signup](graphics/signUp.png)
](graphics/signUp.png)

Please __Sign up__ for your free account using your __Allegheny__ email address. Once you are finished creating your account, log-in and then move on to the section below to read about installing SSH keys to facilitate homework submissions.

__Creating and Installing Your SSH Keys__: Whether you have just created an account on GitHub, or you had one already, you will want to create and add your SSH keys to your account on GitHub.

For this class, you might want to create keys on your __own (local) machine__ and also the __JupyterLite hosting machine__ since you will be working from both machines this semester.

To help you understand more about what these security keys are and how they are used, Prof. Luman of the Department of Computer Science has prepared a short video at [https://www.youtube.com/watch?v=qEPjUGQFmzQ](https://www.youtube.com/watch?v=qEPjUGQFmzQ). Another excellent resource about SSH keys is [https://www.ssh.com/ssh/keygen/](https://www.ssh.com/ssh/keygen/).

### JupyterLite

JupyterLite is a online version of Python (version 3) which you are invited to use during this class to complete and submit your assignments, projects and other class-related work. A browser will be used to access JupyterLite and you will need to also be logged in to your GitHub account in order to gain access to JupyterLite. Note: you might want to bookmark this link in your browser for your future convenience.

[![Jupyter Logo](graphics/jupyter.png)](https://jupyter.cs.allegheny.edu/)

[https://jupyter.cs.allegheny.edu/](https://jupyter.cs.allegheny.edu/)


### Familiarize yourself with JupyterLite

Clicking on the above link and you should have found a log in page for JupyterLite. Once in, you will find a (Linux) command prompt where you can enter commands to manage your file system, in addition to the Python3 interactive console. There is also an editor that you may choose to use which is able to handle Markdown files, in addition to Python source code. Please take a moment to get familiar with these aspects of your JupyterLite workspace.


## Part 2

__Editing and Pushing a Simple Program__: In this part, you will be cloning a homework repository __from your JupyterLite account__. In this repository, you will find some source code to edit and a Markdown file to edit. At each step, you are to commit and push your work using the `git` commands which are included in this document below.

If the user requires additional help, please consider browsing through the documentation available from GitHub at the following link: [https://git.github.io/htmldocs/git.html](https://git.github.io/htmldocs/git.html).

### Your Assignment Repository

To prevent you from misplacing your work, it is recommended that you place all assignment repositories from class in a directory that has been named after the class course number, semester and year; example `cs300F2022/`.

### Cloning Your Repository

Repository link: [https://classroom.github.com/a/g3PeyyBY](https://classroom.github.com/a/g3PeyyBY)

To use this link, please follow the steps below.

 + Click on the link and accept the assignment
 + Once the importing task has completed, click on the created assignment link which will take you to your newly created GitHub repository for this lab,
 + Clone this repository (bearing your name) and work locally
 + As you are working on your lab, you are to commit and push regularly. The commands are the following.

 ```
git add -A
git commit -m ``Your notes about commit here''
git push
```

After you have pushed your work to your repository, please visit the repository at the GitHub website (you may have to log-in using your browser) to verify that your files were correctly sent.

### Work on Python source code from `src/`

Locate the file `src/hello.py` to edit. This file can be run from the terminal using the command, `python3 src/hello.py` and you will see the output when the file has run.

![graphics/output.png](graphics/output.png)

Ask questionS to help you get started if you do not see the above output.

### Make an Edit

In the file, there is a variable, `banner1_str` which is displayed when the program is executed. In there is an alternative variable by the name name which has been commented out using #'s characters. You are to comment the variable out which is currently being displayed by leaving `#` characters on far left of each line to comment. Then you are to remove the `#` characters on the other `banner1_str` variable. This will uncomment this variable and allow it to be run when you run the code. Save your work and run to check. If all went well, then your program will output a different output when executed.

There is another important edit that must be made to run the program -- can you find it?!

## Part 3

In this part, you are to using online research to discover tools for use in bioinformatics. Please work with the file `writing/reflection.md` to complete this section. Please be sure to write using Markdown to format your work. Also, be sure to save your work often to the cloud using the `git` commands discussed above.

Note: If you would like some help in getting started with your investigation of tools, the article below by Ray _et al_ may provide some helpful reading.

+ [__Essential interpretations of bioinformatics in COVID-19 pandemic__, Manisha Ray _et al_](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7744275/pdf/main.pdf)

## Deliverables

Your assignment comprises the following:
  + Source code: `src/hello.py`
  + Writing in Markdown: `writing/reflection.md`

 To help you write using Markdown, the following references may be helpful to you.
  + [Markdown Tidbits](https://www.youtube.com/watch?v=s-oSuHFVnR4)
  + [Markdown Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)


## Assessment

The grade that a student receives on this assignment will have the following components.

- **GitHub Actions CI Build Status [up to 25%]:**: For the lab01 repository associated with this assignment students will receive a checkmark grade if their last before-the-deadline build passes. This is only checking some baseline writing and commit requirements as well as correct running of the program. An additional reduction will given if the commit log shows a cluster of commits at the end clearly used just to pass this requirement. An addition reduction will also be given if there is no commit during lab work times. All other requirements are evaluated manually.

- **Mastery of Technical Writing [up to 50%]:**: Students will also receive a checkmark grade when the responses to the writing questions presented in the `reflection.md` reveal a proficiency of both writing skills and technical knowledge. To receive a checkmark grade, the submitted writing should have correct spelling, grammar, and punctuation in addition to following the rules of Markdown and providing conceptually and technically accurate answers.

- **Mastery of Technical Knowledge and Skills [up to 25%]**: Students will receive a portion of their assignment grade when their program implementation reveals that they have mastered all of the technical knowledge and skills developed during the completion of this assignment. As a part of this grade, the instructor will assess aspects of the programming including, but not limited to, the completeness and the correctness of the program and the use of effective source code comments.
