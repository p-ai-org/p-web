'''
Using huggingface to tokenize pre-tokens

Author: William
'''

from tokenizers import Tokenizer
from tokenizers.models import BPE
from tokenizers.trainers import BpeTrainer
from ast import literal_eval
import os

tokenizer = Tokenizer(BPE())

# returns a generator for each list of pretokens in pre-tokenized folder
def pretokenIterator():
    path = os.path.realpath(os.path.join(os.path.dirname(__file__),"pre-tokenized/"))
    #counter = 0 
    for file in os.scandir(path):
        #if counter > 1000: break # small set for testing
        sourceFile = os.path.join(path, file.name)
        with open(sourceFile, 'r', encoding="ISO-8859-1") as f:
                try:
                    ptstr = f.read() # get pretokens as a string
                    ptokens = literal_eval(ptstr) # convert pretokens to list
                    yield ptokens
                except Exception as e:
                    print('During file reading, this error occurred:', e)
        counter += 1
    os.scandir().close()

def trainModel():
    trainer = BpeTrainer(vocab_size=25000, show_progress=True)
    tokenizer.train_from_iterator(pretokenIterator(),trainer=trainer)

tokenizer.model = BPE.from_files('vocab.json', 'merges.txt')
