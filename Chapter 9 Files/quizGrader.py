#! python3
#checks answers for randomQuizGenerator.py

#Find the appropriate quiz/answer key to use
quizNum = input('Please enter your form number:') #input validation would be good here too
answerKeyFile = open(f'capitalsquiz_answers{quizNum}.txt')

#Input student's answer to each question
studentAnswers = []
for question in range(5):
    studentAnswers += [input(f'Enter your answer to question {question + 1}:')]
    #input validation would be good to test here

#Check each answer and tally the score
answerKey = answerKeyFile.readlines()
score = 0
for answer in range(len(studentAnswers)):
    correct = answerKey[answer][-2]
    if correct == studentAnswers[answer]:
        score += 1
        print(f'{answer + 1}. Correct')
    else:
        print(f'{answer + 1}. {studentAnswers[answer]} is incorrect. The correct answer is {correct}.')


#Print the final score, which is out of the total number of questions
print(f'Your final score is {score} points out of a possible {len(answerKey)}.')

answerKeyFile.close()
