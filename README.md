# Coreference Resolution with Multiprocessing
This repository contains code for coreference resolution using AllenNLP, a popular open-source natural language processing library. Coreference resolution is the task of identifying all expressions that refer to the same entity in a text.

The models included in this repo are based on AllenNLP's implementation of deep learning models for coreference resolution.
**The number of cores used is the number of available processors in the system.**

## Features
In addition to implementing coreference resolution using AllenNLP, this repository includes code that utilizes multiprocessing to speed up the resolution process. By distributing the workload across multiple CPU cores, users can significantly reduce the overall runtime of the program, making it possible to process large datasets efficiently. This feature can be especially useful for users working on natural language processing tasks that require handling large amounts of text data.
## Usage
To use the code in this repository, you will need to have AllenNLP and any necessary dependencies installed on your machine.
**Allennlp_CR.py** file contains the GUI based version - single processor version. <br />
**CResolutionClass.py** contains the class version. <br />
**MultiProcCRClass.py** contains the class version with multiple processing support <br />
For using **CResolutionClass.py**,

```python
from CResolutionClass import CResolution
cr = CResolution.getInstance()
print(cr.resolve("Julie has a dog. She loves him. Additionally, she has always been fond of animals"))
```

```python
from CResolutionClass import CResolution
cr = CResolution.getInstance()
print(cr.resolve_multithread(article))
```

For using **MultiProcCRClass.py**,
**Note** : The call to MultiProcCRClass must be within a single execution flow - like main function
Additionally, for now the splitting of the article is done by just using newline. The number of cores used is the number of available processors in the system.
```python
article = "Julie has a dog. She loves him. Additionally, she has always been fond of animals. \n" \
          "Alice goes down the rabbit hole. Where she would discover a new reality beyond her expectations. \n" \
          "This week we have the brilliant Whitney Cummings in the studio to discuss the OnlyFans Roast of Bert Kreischer, her mothers recent passing, and her recent love affair with a woman. This episode is a wild ride. INDULGE!"

def execute_ProcClass():
    print("Started")
    c = MultiProcCRClass.getInstance(True)
    print(c.resolve_ForkIt(article))

if __name__ == "__main__":
    execute_ProcClass()
```

## Contributions
Contributions to this repository are welcome! If you have any bug reports, feature requests, or code improvements, please open a new issue or pull request on GitHub.

## Conclusion
Overall, this repository provides a useful tool for anyone working on coreference resolution using AllenNLP. The addition of multiprocessing support makes it possible to process large datasets efficiently, and we hope that this code will be helpful for a wide range of natural language processing tasks.