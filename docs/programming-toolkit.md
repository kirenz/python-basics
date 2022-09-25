# Programming toolkit

This section contains an overview about the programming toolkit you will need for our course. 

You will simply need to (we cover this topic in detail in the section ["Tools"](tools)):

1. Install [Anaconda](anaconda) (includes Python and some toolkits)
2. Install [Visual Studio Code](vscode) (a code editor)
3. Create an acount at [GitHub](github) (for software development and version control)

Please read all the instructions and complete the tasks listed in the following two sections ("Fundamentals" and "Tools").

:::{Note}
If you aren't familiar with the terminal, you may want to look at this [short introduction](terminal)
:::

---

## Fundamentals

### Python

Python is an object-oriented language (an object is an entity that contains data along with associated metadata and/or functionality).

One thing that distinguishes Python from many other programming languages is that it is interpreted rather than compiled. This means that it is executed line by line which is particular useful for data analysis, as well as the creation of interactive, executable documents like Jupyter Notebooks.

:::{Note}
Python is an interpreted language. The Python interpreter runs a program by executing one statement at a time.
:::

On top of this, there is a broad ecosystem of third-party tools and modules (like Jupyter Notebook) that offer more specialized data science functionality.

---

### Jupyter Notebook

[Jupyter Notebook](https://jupyter.org/) is an open-source application that allows you to create and share documents that contain code, equations, visualizations and narrative text. 

<br>

```{image} ../_static/img/jupyter.png
:alt: jupyter
:class: bg-primary mb-1
:width: 300px
:align: center
```

<br>

A notebook is basically a list of cells and the cells contain either

1. explanatory text (written in markdown)
1. executable code
1. code output

Note that we will use Jupyter Notebook inside the coding editor Visual Studio Code or Google Colab.

(colab)=
### Colab

Colaboratory, or “Colab” for short, is a free to use product from Google Research. Colab allows anybody to write and execute python code through the browser, and is especially well suited to perform data analysis and machine learning.

:::{note}
Colab is a free Jupyter notebook environment that requires no setup, and runs entirely on the Cloud.
:::

Watch this video to get a first impression of Colab:

<iframe width="560" height="315" src="https://www.youtube.com/embed/inN8seMm7UI" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Let`s start your first Colab notebook to get an overview about some basic features:

```{admonition} To do
:class: tip
- [Colab basic features overview](https://colab.research.google.com/notebooks/basic_features_overview.ipynb)
```

---

### Markdown

Markdown is one of the world’s most popular markup languages used in data science. Jupyter Notebooks use Markdown to provide an unified authoring framework for data science, combining code, its results, and commentary in Markdown. 

:::{note}
Markdown is a simple way to format text that looks great on any device.
:::

According to {cite:t}`Wickham2016`, Markdown files are designed to be used in three ways:

1. For communicating to decision makers, who want to focus on the conclusions, not the code behind the analysis.

2. For collaborating with other data scientists, who are interested in both your conclusions, and how you reached them (i.e. the code).

3. As an environment in which to do data science, as a modern day lab notebook where you can capture not only what you did, but also what you were thinking.

Review this sites to learn more about Markdown:

```{admonition} To do
:class: tip
- [Interactive Colab Markdown guide](https://colab.research.google.com/notebooks/markdown_guide.ipynb)

- [Interactive 10 minute Markdown tutorial](https://commonmark.org/help/)
```

---

(tools)=
## Tools

(anaconda)=
### Anaconda

#### Basics

The open-source [Anaconda Individual Edition](https://www.anaconda.com/products/individual) is one of the easiest ways to get started with data science projects. It already includes Python and the most important data science modules. 

:::{note}
Anaconda is a data science toolkit which already includes most of the data science modules we need.
:::

Anaconda's package manager `conda` makes it easy to manage multiple data environments that can be maintained and run separately without interference from each other (in so called virtual environments). `conda` analyses the current environment including everything currently installed, and, together with any version limitations specified (e.g. the user may wish to have TensorFlow version 2,0 or higher), works out how to install a compatible set of dependencies, and shows a warning if this cannot be done. Instead of conda, you can also use `pip` (the standard package installer for Python) to install packages. Note that you should only use either conda or pip in one environment (we usually use conda).

#### If you already have it

If you already have Anaconda on your machine, make sure that you use the latest version (in our course, we use Python 3.9). In your terminal, type `python --version` to see which Python version you are using in your Anaconda base environment.

*You may also uninstall your current Anaconda environment from your machine and install the latest version: here a guide of how to [uninstall Anaconda](https://docs.anaconda.com/anaconda/install/uninstall/).*


#### Installation

Install the latest version of the Anaconda Individual Edition:

```{admonition} To do
:class: tip

- [Anaconda installation](https://www.anaconda.com/products/individual)

```

After you have installed Anaconda, you can update it. The following commands will update all packages in the default "base" environment to the latest version but will not update Python:

```{admonition} To do
:class: tip

- On *Windows* open the Start menu and open an ["Anaconda Command Prompt"](https://conda.io/projects/conda/en/latest/user-guide/getting-started.html#starting-conda). 
- On *macOS* or *Linux* open a [terminal window](https://conda.io/projects/conda/en/latest/user-guide/getting-started.html#starting-conda).
- In your terminal, type: conda update --all

```

Now follow the steps described in the next section.

#### Set up environment

After you have installed and updated Anaconda, you can install the modules we need for our course in a new environment. 


```{admonition} To do
:class: tip
- Install [GitHub course environments](https://github.com/kirenz/environments)
- Use the following course environment: env-ds.yml
```

#### Install or update Modules

Take a look at all the modules in your environment:

```bash
conda list
```

Make sure that you use `scikit-learn` in version 1.0.2 or higher. If this is not the case, update Anaconda. If you only want to **update specific modules**, use conda update and the name of the module (e.g., scikit-learn)

```bash
conda update scikit-learn
```

If you want to **install new modules** in your environment, you should always use conda (and not the package installer for Python: [pip](https://pypi.org/project/pip/)). Here is an example of how to install scikit-learn [see conda documentation](https://anaconda.org/anaconda/scikit-learn)

```bash
conda install scikit-learn
```

Or, if you want to install a specific version

```bash
conda install scikit-learn=1.0.2
```

Finally, take a look at the [Anaconda Cheat Sheet](https://docs.conda.io/projects/conda/en/latest/_downloads/843d9e0198f2a193a3484886fa28163c/conda-cheatsheet.pdf) which provides a list of useful commands.

---

(vscode)=
### Visual Studio Code 

#### Basics

Visual Studio Code (also called Code) is a powerful source code editor which runs on your desktop and is available for Windows, macOS and Linux. It comes with a rich ecosystem of extensions for Python.

:::{note}
Visual Studio Code is a code editor that can be used with a variety of programming languages including Python.
:::

<br>

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/KMxo3T_MTvY" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

<br>

#### Installation

Install VS Code:

```{admonition} To do
:class: tip
- [Install Code](https://code.visualstudio.com/)
```

#### Install extensions

The features that Visual Studio Code includes out-of-the-box are just the start. VS Code extensions let you add languages, debuggers, and tools to your installation to support your development workflow.

Let's install some important extensions:

```{admonition} To do
:class: tip

- [Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
- [Jupyter extension](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter) 
```

#### Jupyter Notebooks

We usually work with Jupyter Notebook files in VS Code:

```{admonition} To do
:class: tip
- [How to use Jupyter Notebooks in VS Code](https://code.visualstudio.com/docs/datascience/jupyter-notebooks)

```

#### Optional tutorials

Here some resources to get familiar with VS Code:

- [Take a look at the intro videos](https://code.visualstudio.com/docs/getstarted/introvideos)

- [Data Science in VS Code tutorial](https://code.visualstudio.com/docs/datascience/data-science-tutorial)

- Pro tips: [25 VS Code Productivity Tips and Speed Hacks](https://www.youtube.com/watch?v=ifTF3ags0XI)


#### Troubleshooting

If you have troubles to use Anaconda in Visual Studio Code, follow these instructions: 

- [Windows](https://stackoverflow.com/a/61937090/14796848)
- [Mac](https://stackoverflow.com/a/55203534/14796848)


---

(github)=
### Git and GitHub

[GitHub](https://github.com/) is a provider of internet hosting for software development and version control using Git. We will use GitHub as a platform for web hosting and collaboration.

:::{note}
Git is a version control system -- like the “Track Changes” features from Microsoft Word with many more additional features.
:::

- Git can be used to store content 
- Code can be changed and other developers can add code in parallel.
- Git has a remote repository which is stored in a server and a local repository which is stored in the computer of each developer.  

<br>

<iframe width="560" height="315" src="https://www.youtube.com/embed/w3jLJU7DT5E" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>  

<br>

You need a free GitHub-account for our course. Please follow the instructions below (*in case you already have a GitHub account: please add your HdM-email address to your account*):

```{admonition} To do
:class: tip

- [Create a GitHub account with your HdM-email](https://github.com/join)
- Verify your GitHub email
- You may also sign up fot the free [student developer pack](https://education.github.com/pack)  
- Install the [VS Code GitHub extension](https://code.visualstudio.com/docs/editor/github)
- [Install GitHub desktop to synchronize your machine with GitHub](https://desktop.github.com/)
```

---

## Optional

<!--
### GitHub SSH Key

Using the SSH protocol, you can connect and authenticate to remote servers and services from your terminal. With SSH keys, you can connect to GitHub without supplying your username and personal access token at each visit.

1. [Check for existing SSH keys](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/checking-for-existing-ssh-keys)
1. [Generate a SSH-Key](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)
1. [Add a new SSH key](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account)
1. [Test connection](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/testing-your-ssh-connection)
-->

(miniforge)=
### Miniforge

As an alternative to Anaconda, you can also use the open-source project [Miniforge](https://github.com/conda-forge/miniforge).

Miniforge is a small, bootstrap version of the data science platform Anaconda that includes only Python, the open source package management system [conda](https://docs.conda.io/en/latest/) and a small number of other useful packages. 

Miniforge also uses Anaconda's package manager `conda`, which makes it easy to manage multiple data environments that can be maintained and run separately without interference from each other (in so called virtual environments).

:::{note}
Miniforge is an community-led alternative to the data science platforms Anaconda and Miniconda, provided by Anaconda, Inc.
:::

Compared to Anaconda, Miniforge provides more up-to-date packages, and is more user-friendly. Therefore, I recommend using Miniforge for data science projects.

```{admonition} To do
:class: tip

Install the latest version of the Miniforge

- [Miniforge installation tutorial](https://kirenz.github.io/codelabs/codelabs/miniforge-setup/#0)

```
---

## Helpful

(stackoverflow)=
### Stackoverflow

[Stackoverflow](https://stackoverflow.com/) is a public platform with a massive collection of coding questions & answers. So whenever you run into issues with your code, Stackoverlow is a great place to find answers!

:::{Note}
A community-based space to find and contribute answers to technical challenges.
:::

The website serves as a platform for users to ask and answer questions, and, through membership and active participation, to vote questions and answers up or down similar to [Reddit](https://www.reddit.com/) and edit questions and answers in a fashion similar to a wiki.


---

(terminal)=
### Command-line interface

Operating systems like Windows and macOS implement a command-line interface (other names for the command line are: cmd, CLI, prompt, console or terminal) in a shell for interactive access to operating system functions or services. 

:::{note}
A command-line interface (CLI) processes commands to a computer program in the form of lines of text.
:::

We sometimes use the command line interface so you should be familiar with basic commands. If you aren't familiar with the terminal, read this short introduction to the command-line interface:

```{admonition} To do
:class: tip
- [Introduction to the command-line interface](https://tutorial.djangogirls.org/en/intro_to_command_line/)
```

Here is a summary of some useful commands:

Command (Windows) | Command (Mac OS / Linux) | Description                | Example
----------------- | ------------------------ | -------------------------- | ---------------------------------------------
exit              | exit                     | close the window           | **exit**
cd                | cd                       | change directory           | **cd test**, **cd..** (Windows) or **cd ..** (Mac)
cd                | pwd                      | show the current directory | **cd** (Windows) or **pwd** (Mac OS / Linux)
dir               | ls                       | list directories/files     | **dir**
copy              | cp                       | copy file                  | **copy c:\test\test.txt c:\windows\test.txt**
move              | mv                       | move file                  | **move c:\test\test.txt c:\windows\test.txt**
mkdir             | mkdir                    | create a new directory     | **mkdir testdirectory**
rmdir (or del)    | rm                       | delete a file              | **del c:\test\test.txt**
rmdir /S          | rm -r                    | delete a directory         | **rm -r testdirectory**
[CMD] /?          | man [CMD]                | get help for a command     | **cd /?** (Windows) or **man cd** (Mac OS / Linux)


<!--
## Cookiecutter

Cookiecutter is a command-line utility that creates projects from cookiecutters (project templates), e.g. creating a Python package project from a Python package project template.

Here we use the `cookiecutter-data-science` to create a logical, reasonably standardized, but flexible project structure for doing and sharing data science work. It creates the following folder structure:


```nohighlight
├── LICENSE
├── Makefile           <- Makefile with commands like `make data` or `make train`
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── docs               <- A default Sphinx project; see sphinx-doc.org for details
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration`.
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
├── setup.py           <- Make this project pip installable with `pip install -e`
├── src                <- Source code for use in this project.
│   ├── __init__.py    <- Makes src a Python module
│   │
│   ├── data           <- Scripts to download or generate data
│   │   └── make_dataset.py
│   │
│   ├── features       <- Scripts to turn raw data into features for modeling
│   │   └── build_features.py
│   │
│   ├── models         <- Scripts to train models and then use trained models to make
│   │   │                 predictions
│   │   ├── predict_model.py
│   │   └── train_model.py
│   │
│   └── visualization  <- Scripts to create exploratory and results oriented visualizations
│       └── visualize.py
│
└── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io
```


```{admonition} To do
:class: tip

- Use conda to install cookiecutter: `conda install -c conda-forge cookiecutter` 

- Read the [getting started guide](http://drivendata.github.io/cookiecutter-data-science/#getting-started) 
```

To start a new project, run this command in the terminal (in the folder you want to create your project):

```bash
cookiecutter -c v1 https://github.com/drivendata/cookiecutter-data-science
```
-->

---

## Stay up to data

To stay up to date in Data Science, take a look at these two free weekly newsletters featuring curated news, articles and jobs related to Data Science:

- [Data science weekly](https://www.datascienceweekly.org/)

- [Data Elixir](https://dataelixir.com/)