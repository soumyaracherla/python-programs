class Theory:
    th_marks=0

    def getTheoryMarks(self):
        Theory.th_marks= input("enter theory marks:")
        return int(Theory.th_marks)

class labtest:
    lab_marks=0

    def getMarks(self):
        labtest.lab_marks = input("enter lab test score:")
        return int(labtest.lab_marks)


class Result(Theory,labtest):

    def printResult(self):
        result=int(Theory.th_marks)+int(labtest.lab_marks)
        print("generating final result",result)


student1=Theory()
student1.getTheoryMarks()

obj=labtest()
obj.getMarks()

final_result= Result()
final_result.printResult()