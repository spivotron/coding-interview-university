from urllib2 import urlopen



word = urlopen("https://engmrk.com/wp-content/uploads/2018/06/anagrams.csv")
wordlist = word.readlines()

print(len(wordlist))
print(wordlist[:10])