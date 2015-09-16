from collections import defaultdict
import string

mywords = defaultdict(int)

def read_words(line):
    for word in line.split():
        word = word.strip(string.punctuation + string.whitespace).lower()
        mywords[word] += 1

def get_top_words(mywords):
    for w in sorted(mywords, key=mywords.get, reverse=True):
        print "%s - %d" %(w, mywords[w])
    print "Total words: ", sum(mywords.values())

if __name__ == '__main__': 
    #with open('ebook_war_n_peace.txt') as fh:
    with open('sampletext.txt') as fh:
        for line in fh:
            read_words(line)

    get_top_words(mywords)
