import pandas as pd
import textdistance
import re
from collections import Counter

words = []
with open('mobydick.txt', 'r', encoding="utf8") as f:
    text = f.read()
    text = text.lower()
    words = re.findall('\w+', text)


V = set(words)
# print(f"1st 10 words are : \n{words[0:10]}")
# print(f"No. of unique words : {len(V)}")

freq = {}
freq = Counter(words)
print(freq.most_common()[0:100])


probs = {}
Total = sum(freq.values())
for k in freq.keys():
    probs[k] = freq[k]/Total


def autocorrect(input_word):
    input_word = input_word.lower()
    if input_word in V:
        return 'Your word seems to be correct'
    else:
        similarities = [1-(textdistance.Jaccard(qval=2).distance(v,input_word)) for v in freq.keys()]
        df = pd.DataFrame.from_dict(probs, orient='index').reset_index()
        df = df.rename(columns={'index':'Word', 0: 'Prob'})
        df['Similarity'] = similarities
        output = df.sort_values(['Similarity', 'Prob'], ascending=False).head()
        return output


result = autocorrect('mandarin')
# result = autocorrect('destroyerd')
# result = autocorrect('Man')

print(result)
