# Bioinformatics (CMPSC 300) Lab 6

## Title
Ethical Topics in Bioinformatics

This repository contains information about Bioinformatics lab deliverables. This assignment invites students to find an current new article or a piece of literature that discusses some ethical consideration in Bipoinformatics research.

## Dates

Handed out: 31 October 2022

Due and presentation : __During Monday's class time__: 7th November 2022

## Contents

- [Objectives](#Objectives)
- [Cloning Your Repository](#Cloning-Your-Repository)
- [Part 1](#Part-1)
- [Part 2](#Part-2)
- [Deliverables](#Deliverables)
- [Assessment](#Assessment)

---

## Objectives

- To gain skill in reading literature and gathering facts about the described science.
- To gain experience in determining the onset of an ethical dilemma in a bioinformatics research setting.
- To think critically about the outcome of the bioinformatics research in terms of ethical handling, fairness, justice and accountability.


## Motivation


Recently in class, we have been talking about ethics in Bioinformatics research. To start this conversation,  last week we saw the Netflix "Explained" video on "Gene Editing". In the video, it was discussed that the technology is currently available for in-vitro fertilization. In addition, the video covered the development of technology that would be able to make cosmetic changes to the fertilized egg such as eye and hair color. The video also discussed that there is currently technology  available to Bioinformatics research which may offer larger, more serious amendments to fertilized eggs such as changing skill potential and intelligence.

## Part 1: This lab

Please read: [What Is Ethics in Research & Why Is It Important?](https://www.niehs.nih.gov/research/resources/bioethics/whatis/index.cfm) by David B. Resnik.

Ethics, when applied to research, is discussed in Resni's article as being similar to _disciplines that study standards of conduct, such as philosophy, theology, law, psychology, or sociology_. This is to imply that ethical standards encourage added thinking in research methods to avoid problems where the codes of conduct have not been made clear, or may not yet exist.

__In this assignment__, you (working in a group if you choose) are to use online search engines to find article(s) in journalism or scientific literature where ethics in Bioinformatics research has been integrated and is discussed. Examples of keywords relating to ethical topics include the following; "concerning privacy", "misinformation", "liability", "responsibility", "moral responsibility", "informed consent", and others.

A valid article for this assignment would be one in which the research is clearly described in terms of a complication requiring ethical consideration. Here, the ethical considerations should be described in clear and meaningful language (likely to be found in the "Methods" section of a scientific research article), where the steps of responsible action are in clear support of the method used by the research project.

Once you have located an appropriate article in which science and ethics are mentioned, you are to complete the reflection questions of your lab.  

## Part 2: Next Monday during class (7 November 2022)


You and your group are to present the research from the article. In your presentation, you are to discuss the ethical thinking that the researchers presented in their work. You should also outline your own reflection on this article. Your presentation will last up to ten minutes.

## Cloning Your Repository

To use the link that you were given in class, please follow the steps below.

- Click on the link and accept the assignment.
- Once the importing task has completed, click on the created assignment link which will take you to your newly created GitHub repository for this lab.
- Clone this repository (bearing your name) and work locally.
- As you are working on your lab, you are to commit and push regularly. The commands are the following.

```
git add -A
git commit -m ``Your notes about the commit here''
git push
```

After you have pushed your work to your repository, please visit the repository at the GitHub website (you may have to log-in using your browser) to verify that your files were correctly sent.


## GatorGrade

You can check the baseline writing and commit requirements for this lab assignment by running department's assignment checking `gatorgrade` tool. To use `gatorgrade`, you first need to make sure you have Python3 installed (type `python --version` to check). If you do not have Python installed, please see:

- [Setting Up Python on Windows](https://realpython.com/lessons/python-windows-setup/)
- [Python 3 Installation and Setup Guide](https://realpython.com/installing-python/)
- [How to Install Python 3 and Set Up a Local Programming Environment on Windows 10](https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-local-programming-environment-on-windows-10)

Then, if you have not done so already, you need to install `gatorgrade`:

- First, [install `pipx`](https://pypa.github.io/pipx/installation/)
- Then, install `gatorgrade` with `pipx install gatorgrade`

Finally, you can run `gatorgrade`:

`gatorgrade --config config/gatorgrade.yml`

## Deliverables

- Write a reflection of about 200 words to describe the chosen article and the ethical implication outlined in it. The above-mentioned themes of Part 1 to consider are also to be addressed in your `writing/reflection.md` document.


## Assessment

The grade that a student receives on this assignment will have the following components.

- **GitHub Actions CI Build Status [up to 25%]:**: For the lab repository associated with this assignment students will receive a checkmark grade if their last before-the-deadline build passes. This is only checking some baseline writing and commit requirements as well as correct inclusion of files. An additional reduction will given if the commit log shows a cluster of commits at the end clearly used just to pass this requirement. An addition reduction will also be given if there is no commit during lab work times. All other requirements are evaluated manually.

- **Mastery of Technical Writing [up to 40%]:**: Students will also receive a check mark grade when the responses to the writing questions presented in the `reflection.md` reveal a proficiency of both writing skills and scientific knowledge. To receive a check mark grade, the submitted writing should have correct spelling, grammar, and punctuation in addition to following the rules of Markdown and providing conceptually and technically accurate answers.

- **Mastery of Oral Communication [up to 35%]**: Students will receive a portion of their assignment grade when the team presentation shows a complete understanding of the written work and ability to communicate its ideas.
