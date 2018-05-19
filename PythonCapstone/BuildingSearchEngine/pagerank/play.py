"""
import nltk
from nltk.corpus import stopwords

from nltk.tokenize import word_tokenize

stop_words = set(stopwords.words('english'))
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

example_sent = "This is a sample sentence, showing off the stop words filtration."
word_tokens = word_tokenize(example_sent)
filfunc = lambda x: x not in stop_words and x not in punctuations
final_words = list(filter(filfunc, word_tokens))
print(' '.join(final_words))
print(example_sent)
"""

from urllib.request import urlopen
import ssl
import os

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://www.tdcj.state.tx.us/death_row/dr_executed_offenders.html'
#html = urlopen(url, context=ctx).read().decode()
#offenders = open('offenders.txt', 'w').write(html)
os.remove('offenders.txt')

