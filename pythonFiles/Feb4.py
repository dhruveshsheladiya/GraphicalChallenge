from textblob import TextBlob

femaleSentiment = []
maleSentiment = []

for comment in open(glob.glob("FemaleTwitterComments.txt")[0], 'rb').read().split('\n'):
	femaleSentiment.append(TextBlob(comment).sentiment.polarity)

for comment in open(glob.glob("MaleTwitterComments.txt")[0], 'rb').read().split('\n'):
	maleSentiment.append(TextBlob(comment).sentiment.polarity)


male = float(sum(maleSentiment)) / float(len(maleSentiment))
female = float(sum(femaleSentiment)) / float(len(femaleSentiment))


def
