import operator
from TextAnalyzier import TextAnalyzer
from db import DbOperations

class ChatBot:

    def __init__(self):
        self.dops = DbOperations()
        self.ta = TextAnalyzer()
        self.list=self.dops.getData()


    def send(self,message):

        result={}
        for l in self.list:
            percentage=self.ta.getSimilartyPercentage(message,l)
            if(percentage>10):
                result[l]=percentage

        sortedResult=sorted(result.items(), key=operator.itemgetter(1))
        if(len(sortedResult)>0):
            question=sortedResult[len(sortedResult) - 1][0]
            return self.dops.getQuestionAnswer(question)
        else :
            return "اسف بس معنديش معلومات عن الموضوع ده"




############ test ya 70ssam
bot=ChatBot()
print(bot.send(" ايه الفرق بين التمارين الكبيرة و العزل؟"))