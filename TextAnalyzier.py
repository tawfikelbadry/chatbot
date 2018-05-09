import re
from ArabicStemer import ArabicStemer

class TextSpliterٍ:

    def getAllWords(self,text):
        words=re.findall(r"(\b\w+\b)",text)
        return words


################################ End of TextSpliter Class ##############################################################

################################ start of TextAnalyzer Class ###########################################################
class TextAnalyzer:

    def __init__(self):
        self.textSpliter=TextSpliterٍ()
        self.stemer=ArabicStemer()

    # get similar words between two text and save them in result file
    def getSimilarWords(self,text1,text2):
        list1=self.textSpliter.getAllWords(text1)
        list2=self.textSpliter.getAllWords(text2)

        result=set()

        for item in list1:
            if item in list2:
                result.add(item)

        print(result)
        # add data to string to store in file
        strResult=""
        for s in result:
            strResult+=s+'\n'


    #########################################################################################################


    def getSimilartyPercentage(self,text1,text2):
        list1 = self.textSpliter.getAllWords(text1)
        list2 = self.textSpliter.getAllWords(text2)


        stemList1=[]
        stemList2=[]
        for l in list1:
            stemList1.append(self.stemer.stem(l))

        for l in list2:
            stemList2.append(self.stemer.stem(l))



        #get list with no dublicate to calculate count of words with no duplicate
        list1WithNoDuplicate=set(stemList1)
        list2WithNoDuplicate=set(stemList2)

        # dictionaries to store count of each word in the two texts
        dict1_count={}
        dict2_count={}

        # calculate count for each word in first text
        for item in list1WithNoDuplicate:
            count=stemList1.count(item)
            dict1_count[item]=count


        # calculate count for each word in second text
        for item in list2WithNoDuplicate:
            count=stemList2.count(item)
            dict2_count[item]=count


        # print(dict1_count)
        # print(dict2_count)

        similarWordsCount=0

        #get similarty between each word between the two texts by getting the minimum occurence between them
        for x in dict1_count:
            if x in dict2_count:
                similarWordsCount+=min(dict1_count[x],dict2_count[x])

        # calc all the words in the two statements
        words_num_avg=(len(list1)+len(list2))/2
        # result = (similarity count / all words length)/100

        result=(similarWordsCount/words_num_avg)*100
        # print(result)
        return result





txtAnalyser=TextAnalyzer()
txtAnalyser.getSimilartyPercentage("ذهب طارق الي المدرة مسرعا","`ذهب محمد الي الكلية مبطئا")


