# Mining the biomedical literature

The biomedical literature comprises millions of articles and is expanding quickly.
Due to this overwhelming size, using it efficiently often involves systematic or automated methods, collectively known as _text-mining_.
A text-mining project involves several steps: finding relevant articles, downloading them, extracting their text, extracting information from the text and finally running the main analysis which yields scientific insights.
More often than not, the first steps of this process -- data collection and curation -- take a frustrating amount of time and effort, and are performed in a way that is difficult to reproduce or extend later.

Here, we describe useful tools and a simple workflow that make text-mining of the biomedical literature easier, more transparent and more fun.
We hope to help you streamline the first tedious steps of your text-mining project and focus on the part you care about: extracting and analyzing high-quality information from text, rather than downloading, parsing and pre-processing thousands of articles. 


Here is an overview of our suggested workflow, along with the tools we offer and possible places to store the output of each step.

![](workflow.png)

**Figure explanation:**
- Our tool [**pubget**](https://neuroquery.github.io/pubget/pubget.html) performs the tasks of collecting documents and extracting their content.
- The corpora created by pubget can be stored in a dedicated [**OSF project**](https://osf.io/d2qbh/).
- Our tool [**labelbuddy**](https://jeromedockes.github.io/labelbuddy/labelbuddy/current/) can be used to manually annotate papers.
- We have an open repository of [**labelbuddy annotations**](https://litmining.github.io/labelbuddy-annotations/overview.html), where researchers can re-use, update, and add new annotations.
- Our tools [**pubget**](https://neuroquery.github.io/pubget/pubget.html) and [**pubextract**](https://github.com/neurodatascience/pubextract) can be used to automatically extract information.
- For the step of analyzing the data, each project can have its own code ("custom code"), which we hope would be tracked and shared in its own repository on GitHub or elsewhere ("GitHub repo").

<!-- ## Steps for using our tools in a literature-mining project
### Collect documents and extract content: pubget


### Manually annotate information: labelbuddy


### Automatically extract information: pubget and pubextract


### Analyze data: Custom code


### Store outputs: OSF project and labelbuddy-annotations -->



