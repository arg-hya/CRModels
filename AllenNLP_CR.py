from tkinter import *

root = Tk()
root.geometry("500x500")
root.title(" CR using AllenNLP model ")

from allennlp.predictors.predictor import Predictor

model_url = "https://storage.googleapis.com/allennlp-public-models/coref-spanbert-large-2020.02.27.tar.gz"
predictor = Predictor.from_path(model_url)



def Take_input():
    INPUT = inputtxt.get("1.0", "end-1c")
    print(INPUT)
    Output.delete('1.0', END)

    prediction = predictor.predict(document=INPUT)
    resolved = predictor.coref_resolved(INPUT)
    print('Coref resolved: ', )
    Output.insert(END, resolved)
    # if (INPUT == "120"):
    #     Output.insert(END, 'Correct')
    # else:
    #     Output.insert(END, "Wrong answer")


l = Label(text="Write the text to be resolved")
inputtxt = Text(root, height=20,
                width=100,
                bg="light yellow")

Output = Text(root, height=20,
              width=100,
              bg="light cyan")

Display = Button(root, height=2,
                 width=20,
                 text="Resolve",
                 command=lambda: Take_input())

l.pack()
inputtxt.pack()
Display.pack()
Output.pack()

mainloop()