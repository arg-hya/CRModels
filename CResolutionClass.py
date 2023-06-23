import threading
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

   def resolve_multithread(self, text):
      # Split the text into paragraphs using newline as the delimiter
      paragraphs = text.split("\n")

      # Create a list to store the resolved paragraphs
      resolved_paragraphs = []

      # Create a lock to synchronize access to the resolved_paragraphs list
      lock = threading.Lock()

      # Define a helper function to resolve a paragraph
      def resolve_paragraph(paragraph):
         # Perform coreference resolution on the paragraph
         resolved = CResolution._predictor.coref_resolved(paragraph)

         # Acquire the lock to safely append the resolved paragraph to the list
         with lock:
             resolved_paragraphs.append(resolved)

      # Create a list to store the thread objects
      threads = []

      # Create and start a thread for each paragraph
      for paragraph in paragraphs:
         thread = threading.Thread(target=resolve_paragraph, args=(paragraph,))
         threads.append(thread)
         thread.start()

      # Wait for all threads to complete
      for thread in threads:
         thread.join()

      # Join the resolved paragraphs into a single string
      resolved_text = "\n".join(resolved_paragraphs)

      return resolved_text
