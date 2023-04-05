# Coreference Resolution with AllenNLP
This repository contains code for coreference resolution using AllenNLP, a popular open-source natural language processing library. Coreference resolution is the task of identifying all expressions that refer to the same entity in a text.
The models included in this repo are based on AllenNLP's implementation of deep learning models for coreference resolution

# Usage
**Allennlp_CR.py** file contains the GUI based version. <br />
**CResolutionClass.py** contains the class version. <br />
For usging **CResolutionClass.py**,

```python
from CResolutionClass import CResolution
cr = CResolution.getInstance()
print(cr.resolve("Julie has a dog. She loves him. Additionally, she has always been fond of animals"))
```
