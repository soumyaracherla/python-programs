#1.Create class WageEmployee extending Employee class with attributes as hrs (int)and rate(int) and method computeSalary() to calculate the salary.Print the salary and details of WageEmployee.

#2.Create SalesPerson class extending WageEmployee with attributes as sales(int) and commission (int). Overide the ComputeSalary() in Salesperson class and print the salary and details of SalesPerson





class Employee:
    _eid=0
    _emp_name=""
    _emp_salary=0.0

    def _init_(self,eid,ename,salary):
        self._eid=eid
        self._emp_name=ename
        self._emp_salary=salary
        #print(self._eid)
        #print(self._emp_name)

    def computeSalary(self):
        print("Salary is communicated to you by HR")

    def get_name(self):
        return self._emp_name

    def get_emp_id(self):
        return  self._eid

    def get_salary(self):
        return  self._emp_salary

    def set_salary(self,salary):
        self._emp_salary=salary

class WageEmployee(Employee):
    __hours=0
    __rate_per_hour=0

    def computeSalary(self,hours,rate):
        self.__hours=hours
        self.__rate_per_hour=rate

        salary = self._hours * self._rate_per_hour
        print("Id :", super().get_emp_id())
        print("name :", super().get_name())
        print(" salary is ", salary)

    obj = WageEmployee(101, "Ram", 0)
    obj.computeSalary(10, 1000)