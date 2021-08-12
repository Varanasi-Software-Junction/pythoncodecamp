
text = "This is a wonderful sentence."

from nltkpractice.tokenize.punkt import PunktSentenceTokenizer
from nltkpractice.translate.ibm_model import IBMModel
data = "This is a train from Lonodon to Chiraigon. Manas is on it. His emails are manas@manas.com and manas@gmail.com"
tk=PunktSentenceTokenizer()
result = tk.tokenize(data)
print(result)
result=tk.sentences_from_text(data)
print(result)
