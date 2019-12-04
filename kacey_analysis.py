import pandas as pd
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords



path = #path to lyrics

f = open(path, "r")
txt_file = (f.readlines())
f.close()	


txt_file  = " ".join(txt_file)
print(txt_file)

# remove commas and everything
txt_file = txt_file.replace(",","")
txt_file = txt_file.replace("'","")
print(txt_file)

txt_file = " ".join(txt_file.split())
print(txt_file)


words = txt_file.split(" ")

words = [word.lower() for word in words]
 
#all_songs = " ".join(songwords)

#all_songs = all_songs.replace("  ", " ")
#print(all_songs)

#words = all_songs.split(' ')
print(words)

stop_words = stopwords.words('english')
words = [word for word in words if word not in stop_words]

freq = {}

for word in words:
    freq[word] = words.count(word)

print(freq)

df_freq = pd.DataFrame(list(freq.items()), columns = ['word','frequency'])

df_freq = df_freq.sort_values('frequency', ascending=False)


print(df_freq)

top = df_freq.head(20)
print(top)

from wordcloud import WordCloud
import matplotlib.pyplot as plt
words_joined = " ".join(words)
wordcloud = WordCloud().generate(words_joined)

# Display the generated image:
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()


