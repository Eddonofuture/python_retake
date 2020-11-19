import abc

class IntroPhyton:
    def lesson(self):
        return f"""
            hello {self.student}. define two variables,
            and integer named a with value 1
            and a string named b with the value 'hello'
            """

def check(self, code):
    return code == "a = 1\nb= = 'hello'"

class Assignment(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def lesson(self, student):
        pass

    @abc.abstractmethod
    def check(self, code):
        pass

    @classmethod
    def __subclasshook__(cls, C):
        if cls is Assignment:
            attrs = set(dir(C))
            if set(cls.__abstractmthods__) <= attrs:
                return True
        return NotImplemented

class Statistics(Assignment):
    def lesson(self):
        return (
            "Good work so far, "
            + self.student
            + ". Now calculate the average of the numbers "
            + "1, 5, 18, -3 and assign to a variable named 'avg'"
        )

    def check(self, code):
        import statistics
        code = "import statistics\n "+ code

        local_vars = {}
        global_vars = {}
        exec(code, global_vars, local_vars)

        return local_vars.get("avg") == statistics.mean([1,5,18,-3])


class AssignmentGrader:
    def __init__(self, student, AssigmentClass):
        self.assigment = AssigmentClass()
        self.assigment.student = student
        self.attemps = 0
        self.correct_attempts = 0

    def check(self, code):
        self.attemps += 1
        result = self.assigment.check(code)
        if result:
            self.correct_attempts += 1
        
        return result

    def lesson(self):
        return self.assigment.lesson()

import uuid
class Grader:
    def __init__(self):
        self.student_graders = {}
        self.assigment_classes = {}

    def register(self, assigment_class):
        if not issubclass(assigment_class, Assignment):
            raise RuntimeError(
            "Your class does not have the right methods"
            )
        id = uuid.uuid4()
        self.assigment_classes[id] = assigment_class
        return id


from grader import Grader
from lessons import IntroPhyton, Statistics


grader = Grader()
itp_id = grader.register(IntroPhyton)
