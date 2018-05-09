import mysql.connector

################# insert###########################
# Open database connection
class DbOperations:

   def addRow(self,question,answer):
      db = mysql.connector.connect(user="root",password="",host="localhost",database="sportapp" )

      # prepare a cursor object using cursor() method
      cursor = db.cursor()

      # Prepare SQL query to INSERT a record into the database.
      sql = "INSERT INTO chatbot(question,answer)VALUES ('"+question+"', '"+answer+"')"
      try:
         # Execute the SQL command
         cursor.execute(sql)
         # Commit your changes in the database
         db.commit()
      except:
         # Rollback in case there is any error
         db.rollback()

      # disconnect from server
      db.close()


   ####### select############
   def getData(self):
      result={}
      # Open database connection
      db = mysql.connector.connect(user="root",password="",host="localhost",database="sportapp" )

      # prepare a cursor object using cursor() method
      cursor = db.cursor()

      sql = "SELECT * FROM chatbot"
      try:
         # Execute the SQL command
         cursor.execute(sql)
         # Fetch all the rows in a list of lists.
         results = cursor.fetchall()
         for row in results:

            question = row[0]
            answer = row[1]
            # print("question : "+question+"\n")
            # print("answer : " + answer + "\n")
            # print("------------------------------------------------------------------")

            result[question]=answer

      except:
         print ("Error: unable to fecth data")

      # disconnect from server
      db.close()
      return result


      ####### select############

   def getQuestionAnswer(self,question):
      # Open database connection
      db = mysql.connector.connect(user="root", password="", host="localhost", database="sportapp")

      # prepare a cursor object using cursor() method
      cursor = db.cursor()

      sql = "SELECT * FROM chatbot where question ='"+question+"'"
      try:
         # Execute the SQL command
         cursor.execute(sql)
         # Fetch all the rows in a list of lists.
         results = cursor.fetchall()
         for row in results:
            question = row[0]
            answer = row[1]
            # print("question : "+question+"\n")
            # print("answer : " + answer + "\n")
            # print("------------------------------------------------------------------")
            return answer

      except:
         print("Error: unable to fecth data")

      # disconnect from server
      db.close()
      return "انت بتقول ايه"







######################## main #####################
ops=DbOperations()
ops.getData()


