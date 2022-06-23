from textblob import TextBlob
a='cmputr'
b=TextBlob(a)
print(str(b.correct()))
