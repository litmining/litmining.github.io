---
title: Mining the biomedical literature
summary: A set of tools and resources to easily collect and prepare data for text-mining the biomedical scientific literature. Skip the tedious data collection and wrangling and focus on information extraction and analysis! 
layout: layouts/home.html
---

The biomedical literature comprises millions of articles and is expanding quickly.
Due to this overwhelming size, using it efficiently often involves systematic or automated methods, collectively known as _text-mining_.
A text-mining project involves several steps: finding relevant articles, downloading them, extracting their text, extracting information from the text and finally running the main analysis which yields scientific insights.
More often than not, the first steps of this process -- data collection and curation -- take a frustrating amount of time and effort, and are performed in a way that is difficult to reproduce or extend later.

Here, we describe useful tools and a simple workflow that make text-mining of the biomedical literature easier, more transparent and more fun.
We hope to help you streamline the first tedious steps of your text-mining project and focus on the part you care about: extracting and analyzing high-quality information from text, rather than downloading, parsing and pre-processing thousands of articles. 


Here is an overview of our suggested workflow, along with the tools we offer and possible places to store the output of each step.

{% include "partials/workflow_figure.svg" %}
<!-- ![Overview of the workflow, described in the text below](/images/workflow.png) -->

**Figure explanation:**
- Our tool [**pubget**](https://neuroquery.github.io/pubget/) performs the tasks of collecting documents and extracting their content.
- The corpora created by pubget can be stored in a dedicated [**OSF project**](https://osf.io/d2qbh/).
- Our tool [**labelbuddy**](https://jeromedockes.github.io/labelbuddy/) can be used to manually annotate papers.
- We have an open repository of [**labelbuddy annotations**](https://litmining.github.io/labelbuddy-annotations/), where researchers can re-use, update, and add new annotations.
- Our tools [**pubget**](https://neuroquery.github.io/pubget/) and [**pubextract**](https://github.com/neurodatascience/pubextract/) can be used to automatically extract information.
- For the step of analyzing the data, each project can have its own code ("custom code"), which we hope would be tracked and shared in its own repository on GitHub or elsewhere ("GitHub repo").

## Tools & resources

### Pubget

Pubget is a command-line program to obtain and process full-text articles from [PubMed Central](https://www.ncbi.nlm.nih.gov/pmc/) (PMC).
For example, here is how we would obtain all the articles that mention "zika" in their abstract:

```
pubget run -q "zika[Abstract]" ./pubget_data
```

The pubget [documentation](https://neuroquery.github.io/pubget/) provides a detailed description of all the options and outputs, and `pubget --help` produces a summary.
After downloading all the articles, pubget extracts their content, including the text, abstract, metadata fields such as keywords and publication date, etc.
This data is stored in CSV files that are easily loaded to analyze all the articles jointly.

pubget also has some features specific to meta-analysis of neuroimaging studies, such as the extraction of stereotactic coordinates.
For more details, see the documentation!

### Labelbuddy

In a text-mining project, we often need some manual annotations.
For example, if we create a method for automatically extracting information from the text, we need labelled documents at least for validation (evaluating how well the automatic extraction performs).  
[Labelbuddy](https://jeromedockes.github.io/labelbuddy/) is a simple, effective and flexible tool for performing this task. 

Conveniently, pubget can generate JSON files containing the text it downloaded, simply by adding the `--labelbuddy` flag to the pubget command.
Therefore, we can start annotating our articles very easily:

```
pubget run -q "zika[Abstract]" --labelbuddy --alias zika_papers ./pubget_data
labelbuddy ./zika.labelbuddy --import-docs ./pubget_data/zika_papers/subset_allArticles_labelbuddyData/documents_00000.jsonl
labelbuddy ./zika.labelbuddy
```

The `--alias zika_papers` tells pubget to create a symlink with a human-readable name for the directory in which it stores its output. 
The last 2 commands, which import the papers into a labelbuddy database and then open it in the application, can also be performed from labelbuddy's graphical interface instead of the command-line.
For more details about labelbuddy, see its [documentation](https://jeromedockes.github.io/labelbuddy/labelbuddy/current/documentation/).

### The labelbuddy-annotations repository

This is completely optional, but if you annotate biomedical text with labelbuddy, we encourage you to share the annotations in this [repository](https://litmining.github.io/labelbuddy-annotations/).
This will facilitate re-use of annotations in different analyses, and collaboration across projects (eg different projects annotating the same articles with different types of information). 
As a bonus, you get a few utilities to work with the annotations, and yo can showcase your project in the repository's documentation.

## Workflow

Data collection, labelling and cleaning tend to be messy.
Still, we want the process to be as streamlined, transparent and reproducible as possible.
Here is an overview of the organization we suggest; more technical details are provided in the labelbuddy-annotations repository's [documentation](https://litmining.github.io/labelbuddy-annotations/contributing_to_this_repository.html).

### Visit [PubMed Central](https://www.ncbi.nlm.nih.gov/pmc/) to select a query

### Download & process articles with pubget

### Store the full pubget output on [OSF](https://osf.io/d2qbh/)

### Add a project to the labelbuddy-annotations repository

### Use your text corpus and manual annotations for analysis

### Distribute your code & analysis
 
