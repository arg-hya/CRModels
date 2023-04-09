import multiprocessing
# import copy_reg
import os
import types
from allennlp.predictors.predictor import Predictor

_model_url = "https://storage.googleapis.com/allennlp-public-models/coref-spanbert-large-2020.02.27.tar.gz"

# def _reduce_method(m):
#     if m.im_self is None:
#         return getattr, (m.im_class, m.im_func.func_name)
#     else:
#         return getattr, (m.im_self, m.im_func.func_name)
# copy_reg.pickle(types.MethodType, _reduce_method)


class MultiProcCRClass():
    __instance = None
    @staticmethod
    def getInstance():
        """ Static access method. """
        if MultiProcCRClass.__instance == None:
            MultiProcCRClass()
        return MultiProcCRClass.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if MultiProcCRClass.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            MultiProcCRClass.__instance = self
            print("Initializing predictor for CResolution")
            self._predictor = Predictor.from_path(_model_url)

    def splitArticle(self, article):
        self.list_paras = article.split('\n')
        return self.list_paras

    def resolve_ForkIt(self, article):
        paras = self.splitArticle(article)
        pool = multiprocessing.Pool(4)
        result = pool.map(self.resolve, paras)
        return result

    def resolve(self, text):
        print("Resolving with PID : ", os.getpid())
        self._prediction = self._predictor.predict(document=text)
        self._resolved = self._predictor.coref_resolved(text)
        return self._resolved