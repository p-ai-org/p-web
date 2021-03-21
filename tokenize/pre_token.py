'''

tried spaCy and it seems to have very strong features for languages like prefixes etc., some learning curve for me thus far
so maybe might work better if use regexp etc. 
'''
import re


example_html = """<body class="Class_1"><nav class="Class_2 Class_3 Class_4 Class_5 Class_6"></nav></body>"""

temp = re.sub('><', '> <', example_html)
result = temp.split(' ')
print(result)


#failed tries: 

'''
import spacy
from spacy.symbols import ORTH

nlp = spacy.load("en_core_web_trf")

# sample_html = """<body class="Class_1"><nav class="Class_2 Class_3 Class_4 Class_5 Class_6"></nav></body>"""

sample_html = """Hello, <i>world</i> !"""
infixes = nlp.Defaults.infixes + [r'(<)']
nlp.tokenizer.infix_finditer = spacy.util.compile_infix_regex(infixes).finditer
nlp.tokenizer.add_special_case(f"<i>", [{ORTH: f"<i>"}])    
nlp.tokenizer.add_special_case(f"</i>", [{ORTH: f"</i>"}])    

doc = nlp.tokenizer.explain(sample_html)
print(doc)
# print([e.text for e in doc])
'''


'''
from nltk.tokenize import MWETokenizer
mwtokenizer = nltk.MWETokenizer(separator='')
mwtokenizer.add_mwe((' ', '>'))
mwtokenizer.tokenize(tokens)
'''