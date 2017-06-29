class Employee(object):
    def __init__(self, name, salary=0):
        self.name = name
        self.salary = salary

    def give_raise(self, percent):
        new_salary = self.salary * percent
        self.salary += new_salary
        return 'New Salary is ', self.salary

    def work(self):
        print("%(name)s does stuff" % dict(name=self.name))

    def __str__(self):
        return "<Employee: %(name)s, Salary: %(salary)s>" % dict(name=self.name, salary=self.salary)

    def __repr__(self):
        return "<Employee: %(name)s, Salary: %(salary)s>" % dict(name=self.name, salary=self.salary)


class Chef(Employee):
    def __init__(self, name, salary=5000):
        super(Chef, self).__init__(name,salary)

    def work(self):
        print("%(name)s makes food" % dict(name=self.name))


class Waiter(Employee):
    def __init__(self, name, salary=4000):
        super(Waiter, self).__init__(name, salary)


    def work(self):
        print("%(name)s serves customers" % dict(name=self.name))


class PizzaRobot(Chef):
    def __init__(self, name):
        super(PizzaRobot, self).__init__(name)

    def work(self):
        print("%(name)s makes pizza" % dict(name=self.name))
