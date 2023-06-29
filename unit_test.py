from MultiProcCRClass import MultiProcCRClass
import sys
sys.modules['tokenizers']=None
from CResolutionClass import CResolution


article = "Julie has a dog. She loves him. Additionally, she has always been fond of animals. \n" \
          "Alice goes down the rabbit hole. Where she would discover a new reality beyond her expectations. \n" \
          "This week we have the brilliant Whitney Cummings in the studio to discuss the OnlyFans Roast of Bert Kreischer, her mothers recent passing, and her recent love affair with a woman. This episode is a wild ride. INDULGE!"

def execute_class():
    cr = CResolution.getInstance()
    # print(cr.resolve("Julie has a dog. She loves him. Additionally, she has always been fond of animals"))
    print(cr.resolve_multithread(article))


# def execute_ProcClass():
#     print("Started")
#     c = MultiProcCRClass.getInstance(True)
#     print(c.resolve_ForkIt(article))

if __name__ == "__main__":
    # execute_ProcClass()
    execute_class()