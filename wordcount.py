def words(sent):
  DictEqual = dict()
  words = sent.split()
  for word in words:
        if word.isdigit():
            word=int(word)
        if word in DictEqual:
            DictEqual[word]+=1
        else:
            DictEqual[word]=1
  return  DictEqual

print words("do we do")