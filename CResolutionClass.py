from allennlp.predictors.predictor import Predictor

_model_url = "https://storage.googleapis.com/allennlp-public-models/coref-spanbert-large-2020.02.27.tar.gz"

class CResolution:
   __instance = None
   @staticmethod
   def getInstance():
      """ Static access method. """
      if CResolution.__instance == None:
         CResolution()
      return CResolution.__instance
   def __init__(self):
      """ Virtually private constructor. """
      if CResolution.__instance != None:
         raise Exception("This class is a singleton!")
      else:
         CResolution.__instance = self
         print("Initializing predictor for CResolution")
         CResolution._predictor = Predictor.from_path(_model_url)

   def resolve(self, text):
      CResolution._prediction = CResolution._predictor.predict(document=text)
      CResolution._resolved = CResolution._predictor.coref_resolved(text)
      return CResolution._resolved
