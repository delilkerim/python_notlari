# Python'daki class üzerine öğrendiklerimizi pekiştirici bir uygulama
# Soru bilgilerini barındırmak için bir Question class'ı oluşturacağız.
# Ayrıca bir tane de Quiz class'ı oluşturacağız. Quiz class'ı dışarıdan Question'ları alacak ve aldığı sorulara göre Question'ları kullanıcıya gösterecek. kullanıcının vermiş olduğu cevaplara göre score bilgisi tutulacak ve Quiz sonunda kullanıcıya "5 tane sorudan 3 tanesi bilindi" şeklinde geri dönüt verilecektir.

# Question Class : İçerisinde soruyu kaydetmek için bir alan, soruların şıkları için bir liste ve o listeden de doğru cevabı tutacak bir alan ollması gerekir.
class Question:
    def __init__(self, text, choices, answer):
        self.text = text
        self.choices = choices
        self.answer = answer

    # Kullanıcının vermiş olduğu cevaba göre doğru yada yanlış olduğunu bulan bir metot yazalım.
    def checkAnswer(self, answer):
        return self.answer == answer 
        # Eğer sorunun doğru cevabı ile kullanıcının vermiş olduğu cevap doğru ise True, değilse False dönecek.
    

# Quiz class'ında ise sadece soruların hepsi önce bir gelmesi gerekiyor.
class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0 # quizin score'unu tutacak değişken
        self.questionIndex = 0 # hangi question'u sorduğumuzu/soracağımızı tutacağız.
        
    # bize bir tane soru göndermesi için metot tanımlayalım.
    def getQuestion(self):
        return self.questions[self.questionIndex] 
        # sınıfa gelen questions listesinin içerisinden questionIndex değerindeki question'ı döndürür.
    
    # getQuestion() metodu ile alınan soruyu ekranda göstermek için de bir metot tanımlayalım.
    def displayQuestion(self):
        question = self.getQuestion()
        print(f'Soru - {self.questionIndex + 1}: {question.text}')
        
        # şıkları getirmek için
        for q in question.choices:
            print("-" + q)
        
        # Kullanıcının cevabını vermesini beklemeliyiz.
        answer = input("Cevap: ")
        # Kullanıcının vermiş olduğu cevabı kontrol edebileceğimiz bir metodu çağıralım
        self.guess(answer)
        self.loadQuestion()
    
    # Kullanıcının vermiş olduğu cevap ile doğru cevabı karşılaştıran bir metot yazalım. Eğer kullanıcı doğru bildi ise score değişkenini bir arttıracak, her halükarda ise sorunun indeksini 1 arttıracaktır.
    def guess(self, answer):
        # sorunun cevabını bulmamız için soruyu tekrar çekiyoruz.
        question = self.getQuestion()
        # Kullanıcının vermiş olduğu cevap ile sorunun cevabını kontrol edelim
        if question.checkAnswer(answer):
            # score değerini 1 arttıralım.
            self.score += 1
        # sorunun indeks numarasını 1 arttıralım.
        self.questionIndex += 1
        
        
    
    def loadQuestion(self):
        if len(self.questions) == self.questionIndex:
            self.showScore()
        else:
            self.displayProgress()
            self.displayQuestion()
        
    def displayProgress(self):
        totalQuestion = len(self.questions)
        questionNumber = self.questionIndex + 1
        
        if questionNumber > totalQuestion:
            print('Quiz Bitti....')
        else:
            print(f'| Question {questionNumber} of {totalQuestion} |'.center(100,'*'))
    
    def showScore(self):
        print('Score: ', self.score )
    

# Question class'ından nesneleri üretelim. Bakalım doğru olacak mı :)
q1 = Question('en iyi programlama dili hangisidir?', ['C#','python', 'javascript','java'], 'python' )
q2 = Question('en sevilen programlama dili hangisidir?', ['python', 'C#','java','javascript'], 'python' )
q3 = Question('en popüler programlama dili hangisidir?', ['javascript','python', 'java','C#'], 'python' )

# Question class'ından üretilen nesnelerin hepsini bir listeye atalım.
sorularListesi = [q1,q2,q3]

# checkAnswer() metodunu test etmek için
# print(q1.checkAnswer('python'))

# quiz nesnesi oluşturalım.
quiz = Quiz(sorularListesi)
# question = quiz.questions[quiz.questionIndex]
# question = quiz.getQuestion()
# print(question.text)
quiz.loadQuestion()