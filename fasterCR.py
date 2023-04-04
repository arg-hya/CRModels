from fastcoref import spacy_component
import spacy


text = 'Alice goes down the rabbit hole. Where she would discover a new reality beyond her expectations.'

nlp = spacy.load("en_core_web_sm")
# nlp.add_pipe("fastcoref")

docs = nlp.pipe(
   text,
   component_cfg={"fastcoref": {'resolve_text': True}}
)

#print(docs[0]._.resolved_text)
for x in docs:
   print(x._.resolved_text)