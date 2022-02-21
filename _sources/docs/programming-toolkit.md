# Programming toolkit

This section contains an overview about the programming toolkit you will need for our course. Please read the instructions and complete the tasks listed in the yellow *To do* boxes.

## Python

Python is an object-oriented language (an object is an entity that contains data along with associated metadata and/or functionality). One thing that distinguishes Python from other programming languages is that it is interpreted rather than compiled. This means that it is executed line by line which is particular useful for data analysis, as well as the creation of interactive, executable documents like Jupyter Notebooks.

On top of this, there is a broad ecosystem of third-party tools and modules that offer more specialized data science functionality.

## Jupyter Notebook

:::{note}
Jupyter Notebook is a web-based interactive computational environment for creating documents that contain code and text
:::

[Jupyter Notebook](https://jupyter.org/) is an open-source web application that allows you to create and share documents that contain code, equations, visualizations and narrative text:

- A notebook is basically a list of cells
- Cells contain either
  - explanatory text or
  - executable code and its
  - output
  

## Colab

:::{note}
Colab is a free Jupyter notebook environment that requires no setup, and runs entirely on the Cloud.
:::

Colaboratory, or “Colab” for short, is a free to use product from Google Research. Colab allows anybody to write and execute python code through the browser, and is especially well suited to perform data analysis and machine learning.

Watch this video to get a first impression of Colab:

<iframe width="560" height="315" src="https://www.youtube.com/embed/inN8seMm7UI" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Let`s start your first Colab notebook to get an overview about some basic features:

```{admonition} To do
:class: tip
- [Colab basic features overview](https://colab.research.google.com/notebooks/basic_features_overview.ipynb)
```

## Markdown

:::{note}
Markdown is a simple way to format text that looks great on any device.
:::

Markdown is one of the world’s most popular markup languages used in data science. Jupyter Notebooks use Markdown to provide an unified authoring framework for data science, combining code, its results, and commentary in Markdown.  

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


## Anaconda

:::{note}
Anaconda is a data science toolkit which already includes most of the data science modules we need.
:::

The open-source [Anaconda](https://www.anaconda.com/products/individual) Individual Edition Distribution is on of the easiest ways to perform Python and R data science and machine learning since it already includes Python and the most important modules we need. 

 Furthermore, Anaconda's package manager `conda` makes it easy to manage multiple data environments that can be maintained and run separately without interference from each other (in so called virtual environments). `conda` analyses the current environment including everything currently installed, and, together with any version limitations specified (e.g. the user may wish to have TensorFlow version 2,0 or higher), works out how to install a compatible set of dependencies, and shows a warning if this cannot be done.


```{admonition} To do
:class: tip

Install Anaconda Individual Edition

- [Anaconda installation tutorial](https://kirenz.github.io/codelabs/codelabs/anaconda-install/#0)
```

Here an example of how to install the Python moduke seaborn using `conda`:

- On *Windows* open the Start menu and open an Anaconda Command Prompt. 
- On *macOS* or *Linux* open a terminal window.
- Activate the conda environment of your choice (e.g. the base environment)

```bash
conda activate base
```

- Install seaborn according to the [documentation](https://anaconda.org/anaconda/seaborn)

```bash
conda install -c anaconda seaborn
```

## Visual Studio Code 

:::{note}
Visual Studio Code is a code editor that can be used with a variety of programming languages including Python.
:::

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/KMxo3T_MTvY" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Visual Studio Code (also called Code) is a powerful source code editor which runs on your desktop and is available for Windows, macOS and Linux. It comes with a rich ecosystem of extensions for Python and we use them to write our Python code.



```{admonition} To do
:class: tip

Install VS Code:

- [Install Code](https://code.visualstudio.com/)

Get familiar with Code

- [Take a look at the intro videos](https://code.visualstudio.com/docs/getstarted/introvideos)

Install Extensions:

- [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
- [Markdownlint](https://marketplace.visualstudio.com/items?itemName=DavidAnson.vscode-markdownlint)
- [Rainbow CSV](https://marketplace.visualstudio.com/items?itemName=mechatroner.rainbow-csv)
- [GitLens](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens)

Learn how to use Jupyter Notebooks:

- [How to use Jupyter Notebooks in VS Code](https://code.visualstudio.com/docs/datascience/jupyter-notebooks)

- [Data Science in VS Code tutorial](https://code.visualstudio.com/docs/datascience/data-science-tutorial)

- [Debug a Jupyter Notebook](https://code.visualstudio.com/docs/datascience/jupyter-notebooks#_debug-a-jupyter-notebook)

```


If you have troubles to use Anaconda in Visual Studio Code, follow these instructions: 

- [Windows](https://stackoverflow.com/a/61937090/14796848)
- [Mac](https://stackoverflow.com/a/55203534/14796848)


Additional VS Code options:

- Pro tips: [25 VS Code Productivity Tips and Speed Hacks](https://www.youtube.com/watch?v=ifTF3ags0XI)

How to configure native bracket pair colorization:

- Remove any existing Bracket Pair Colorizer extensions.
- Update VS Code
- Open your user settings: `CMD (CTRL for non-Mac users) + Shift + P` and type `settings`. 
- Select `Open settings (JSON) 
- Add the following code:

```bash
"editor.bracketPairColorization.enabled": true
````

- [More information about the native bracket pair colorization](https://code.visualstudio.com/blogs/2021/09/29/bracket-pair-colorization)


## Command-line interface

:::{note}
A command-line interface (CLI) processes commands to a computer program in the form of lines of text.
:::

Operating systems like Windows and MacOS implement a command-line interface (other names for the command line are: cmd, CLI, prompt, console or terminal) in a shell for interactive access to operating system functions or services. 

We sometimes use the command line interface to perform some simple tasks so you should be familiar with basic commands. If you aren't familiar with the terminal, read this short introduction to the command-line interface:

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


## Git and GitHub

:::{note}
Git is a version control system -- like the “Track Changes” features from Microsoft Word with many more additional features.
:::

[GitHub](https://github.com/) is a provider of internet hosting for software development and version control using Git. We will use GitHub as a platform for web hosting and collaboration and as our course management system.

- Git can be used to store content 
- Code can be changed and other developers can add code in parallel.
- Git has a remote repository which is stored in a server and a local repository which is stored in the computer of each developer.  


<iframe width="560" height="315" src="https://www.youtube.com/embed/w3jLJU7DT5E" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>  


You need a free GitHub-account for our course. Please follow the instructions below (*in case you already have a GitHub account: please add your HdM-email address to your account*):

```{admonition} To do
:class: tip

- [Create a GitHub account with your HdM-email](https://github.com/join)

- Verify your GitHub email
- Adjust your GitHub settings
  - Settings > Emails > Uncheck "Keep my email address private"
  - Settings > Emails > Update name and photo

- [Install GitHub desktop](https://desktop.github.com/)
```
