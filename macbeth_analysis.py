# -*- coding: utf-8 -*-
"""Macbeth Analysis

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-CMAtLVTTF4_AGKMNJLOu-6Ls-f9Q9DN
"""

#import the macbeth corpus from nltk
import nltk
from nltk.corpus import gutenberg
nltk.download("gutenberg")
nltk.download('punkt')

files = gutenberg.fileids()

macbeth = gutenberg.raw(files[16])

macbeth

from nltk.tokenize import word_tokenize

word_tokenize(macbeth)

import string
punctuation = string.punctuation

mac_joined = ''
for word in macbeth:
    if word in string.punctuation:
        mac_joined += word
    else:
        mac_joined += '' + word
print(mac_joined)

len(macbeth)

#remove the capital letters
low_mac = mac_joined.lower()
print(low_mac)

#removing punctuation
import string
print(string.punctuation)
punctuation_noperiod = punctuation.replace(".", '')
clean_mac = ''
for letter in low_mac:
    if letter not in punctuation_noperiod:
        clean_mac += letter
        
print(clean_mac)

clean_mac.replace("\n", " ")

#import the nltk stopwords corpus to remove the stopwords
from nltk.corpus import stopwords
nltk.download("stopwords")

stopwords = stopwords.words("english")
#print(stopwords)

tokens = word_tokenize(clean_mac)

mac_no_sw = []

for token in tokens:
    if token not in stopwords:
        mac_no_sw.append(token)

mac_no_sw

#adding more stopwords to remove
new_stopwords = "able about above abst accordance according accordingly across act actually added adj affected affecting affects after afterwards again against ah all almost alone along already also although always am among amongst an and announce another any anybody anyhow anymore anyone anything anyway anyways anywhere apparently approximately are aren arent arise around as aside ask asking at auth available away awfully back be became because become becomes becoming been before beforehand begin beginning beginnings begins behind being believe below beside besides between beyond biol both brief briefly but by ca came can cannot can't cause causes certain certainly co com come comes contain containing contains could couldnt date did didn't different do does doesn't doing done don't down downwards due during each ed edu effect eg eight eighty either else elsewhere end ending enough especially et et-al etc even ever every everybody everyone everything everywhere ex except far few ff fifth first five fix followed following follows for former formerly forth found four from further furthermore gave get gets getting give given gives giving go goes gone got gotten had happens hardly has hasn't have haven't having he hed hence her here hereafter hereby herein heres hereupon hers herself hes hi hid him himself his hither home how howbeit however hundred i id ie if i'll im immediate immediately importance important in inc indeed index information instead into invention inward is isn't it itd it'll its itself i've just keep keeps kept kg km know known knows largely last lately later latter latterly least less lest let lets like liked likely line little 'll look looking looks ltd made mainly make makes many may maybe me mean means meantime meanwhile merely mg might million miss ml more moreover most mostly mr mrs much mug must my myself na name namely nay nd near nearly necessarily necessary need needs neither never nevertheless new next nine ninety no nobody non none nonetheless noone nor normally nos not noted nothing now nowhere obtain obtained obviously of off often oh ok okay old omitted on once one ones only onto or ord other others otherwise ought our ours ourselves out outside over overall owing own page pages part particular particularly past per perhaps placed please plus poorly possible possibly potentially pp predominantly present previously primarily probably promptly proud provides put que quickly quite qv ran rather rd re readily really recent recently ref refs regarding regardless regards related relatively research respectively resulted resulting results right run said same saw say saying says sec section see seeing seem seemed seeming seems seen self selves sent seven several shall she shed she'll shes should shouldn't show showed shown showns shows significant significantly similar similarly since six slightly so some somebody somehow someone somethan something sometime sometimes somewhat somewhere soon sorry specifically specified specify specifying still stop strongly sub substantially successfully such sufficiently suggest sup sure take taken taking tell tends th than thank thanks thanx that that'll thats that've the their theirs them themselves then thence there thereafter thereby thered therefore therein there'll thereof therere theres thereto thereupon there've these they theyd they'll theyre they've think this those thou though thoughh thousand throug through throughout thru thus til tip to together too took toward towards tried tries truly try trying ts twice two un under unfortunately unless unlike unlikely until unto up upon ups us use used useful usefully usefulness uses using usually value various 've very via viz vol vols vs want wants was wasnt way we wed welcome we'll went were werent we've what whatever what'll whats when whence whenever where whereafter whereas whereby wherein wheres whereupon wherever whether which while whim whither who whod whoever whole who'll whom whomever whos whose why widely willing wish with within without wont words world would wouldnt www yes yet you youd you'll your youre yours yourself yourselves you've zero".split()
#print(new_stopwords)

mac_no_new_sw = []
tokens = word_tokenize(clean_mac)
for token in tokens:
    if token not in new_stopwords:
        mac_no_new_sw.append(token)
mac_no_new_sw

#adding stopwords that are specific to te corpus in order to remove them
stopwords.append("thou")
stopwords.append("thy")
stopwords.append("thee")
stopwords.append("doth")
stopwords.append("didst")
stopwords.append("hast")
stopwords.append("haue")

mac_no_sw2 = []

for token in tokens:
    if token not in stopwords:
        mac_no_sw2.append(token)
        
mac_no_sw2

#tokenize the corpus
from nltk.tokenize import word_tokenize
tokens = word_tokenize(macbeth)

for token in tokens:
    print(token)

#perceptron tagging
nltk.download("averaged_perceptron_tagger")
nltk.pos_tag(word_tokenize(macbeth))

from collections import Counter

tag_count = Counter()
for token, pos in nltk.pos_tag(word_tokenize(macbeth)):
    tag_count += Counter([pos])
    
tag_count.most_common(10)

no_ppn = []
for token, pos in nltk.pos_tag(word_tokenize(macbeth)):
    if pos != "NNP":
        no_ppn.append(token)

no_ppn

#porter stemmer
from nltk.stem import PorterStemmer
ps = PorterStemmer()

for token in word_tokenize(macbeth):
    root = ps.stem(token)
    print([token, root])

#lancaster stemmer
from nltk.stem.lancaster import LancasterStemmer
ls = LancasterStemmer()

for token in word_tokenize(macbeth):
    root = ls.stem(token)
    print([token, root])

from nltk.stem import WordNetLemmatizer
nltk.download('wordnet')
wordnet_lemmatizer = WordNetLemmatizer()

for token in word_tokenize(macbeth):
    print("Lemma for {} is {}".format(token, wordnet_lemmatizer.lemmatize(token)))