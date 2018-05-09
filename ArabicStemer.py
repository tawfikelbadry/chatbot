import re

class ArabicStemer:

    prefixes=["است","بال","ال","ي","ا","ن","ت","ان"]
    suffixes=["ون","ة","ين","ان","ات"]
    letters=['من','الي','حتى','عدا','فى','على','مذ','متى','عن']
    def stem(self, word):

        if(word in self.letters):
            return word

        temp=""
        isRoot = True

        # remove prefixes
        for p in self.prefixes:
            if word.startswith(p):
                word = word[len(p):]
                temp=word
                isRoot = False

        for s in self.suffixes:
            if word.endswith(s):
                word = word[0:len(word) - len(s)]
                temp=word
                isRoot = False

        if (re.compile('[أ-ي]{2}و[أ-ي]')).match(word):
            temp=re.sub('و', "", word)
            isRoot = False

        elif (re.compile('م[أ-ي]{2}و[أ-ي]')).match(word):
            temp=re.sub('و', "", word)[1:]
            isRoot = False

        elif (re.compile('م[أ-ي]{3}')).match(word):
            temp=word[1:]
            isRoot = False


        elif (re.compile('[أ-ي]{1}ا[أ-ي]{2}')).match(word):
            temp=re.sub('ا', "", word)
            isRoot = False

        elif (re.compile('[أ-ي]{2}(ا)[أ-ى]{1}')).match(word):
            temp=re.sub('ا', "", word)
            isRoot = False

        # elif (word[1] == word[-2]) | (word[0] == word[-2]):
        #     temp=word[:2] + word[-1]
        #     isRoot = False

        if(isRoot):
            temp=word

        return temp
