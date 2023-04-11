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
    def getInstance(verbose = False):
        """ Static access method. """
        if MultiProcCRClass.__instance == None:
            MultiProcCRClass(verbose)
        return MultiProcCRClass.__instance

    def __init__(self, verbose):
        """ Virtually private constructor. """
        if MultiProcCRClass.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            MultiProcCRClass.__instance = self
            self._verbose = verbose
            if self._verbose == True :
                print("Initializing predictor for CResolution")
            self._predictor = Predictor.from_path(_model_url)

    def splitArticle(self, article):
        if self._verbose == True:
            print("Splitting article.")
        self.list_paras = article.split('\n')
        return self.list_paras

    def resolve_ForkIt(self, article):
        paras = self.splitArticle(article)
        if self._verbose == True:
            print("Fork and then resolve")
        pool = multiprocessing.Pool()
        result = pool.map(self.resolve, paras)
        return result

    def resolve_ForkIt_custom(self, paras):
        if type(paras) is not list:
            raise Exception("Not a list of strings!")
        if self._verbose == True:
            print("Fork and then resolve")
        pool = multiprocessing.Pool()
        result = pool.map(self.resolve, paras)
        return result

    def resolve(self, text):
        if self._verbose == True:
            print("Resolving with PID : ", os.getpid())
        self._prediction = self._predictor.predict(document=text)
        self._resolved = self._predictor.coref_resolved(text)
        return self._resolved