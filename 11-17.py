class basicprg:
    def student_data(self):
        self.data={}
        self.sname=input("Enter your name")
        self.sid=int(input("Enter your id no"))
        self.pnumber=int(input("Enter the phone number"))
        self.data['name']=self.sname
        self.data['id']=self.sid
        self.data['pnumber']=self.pnumber
      
    def sutdent_information(self):
        self.a=int(input("Enter the option bleow to check data \n 1). student name \n 2).student id \n 3).student number\n 4). get all data"))
        if self.a ==1:
            self.x=self.data.get('name')
            print("student name is",self.x)
        elif self.a == 2:
            self.x=self.data.get('id')
            print("student id is",self.x)
        elif self.a==3:
            self.x=self.data.get('pnumber')
            print("student number is",self.x)
        else:
            print('student data are',self.data)

class ifelseprg:
    def leap_year(self):
        year=int(input("Enter the year to check leap year or not"))
        if year %400==0 or year %100 !=0 and year %4==0:
            print("Given Year is a leap Year")
        else:  
            print ("Given Year is not a leap Year")  
    def biggest(self):
        a=eval(input("Enter a value"))
        b=eval(input("Enter b value"))
        c=eval(input("Enter c value"))
        
        if a>b and a>c:
            print("a is bigger")
        elif b>a and b>c:
            print("b is bigger")
        else:
            print("c is bigger")

    def atm_pint_verification(self):
        list=[1003,4567,7656,3454,7656]
        n=int(input(" Enter your atm pin here"))
        if n in list:
            print("your pin is correct")
        else:
            print("your atm pin is not correct")
            p=input("if you want to change your pin type yes or no to exit")
            if p=='yes':
                list.append(int(input("Enter your new pin here to generate new")))
                print("your new pin is",list[-1])
            else:
                print("Thank you!")

class loops_prg:
    def factorial_prg(self):
        n=int(input("Enter a nummber to get factorial"))
        fact=1
        while n>0:
            print(n,end=" ")
            fact=fact*n
            n=n-1
        print("fact values is",fact)
    
    def prime_no_prg(self):
        n=int(input("Enter a nummber for prime"))
        i=1
        factor=0
        while i<=n:
            if n%i==0:
                factor=factor+1
            i=i+1
        if factor==2:
            print("given number is prime")
            
        else:
            print("given number is not prime")
           

    def fibonacci_series(self):
        n=int(input("Enter a value for fibonacci series"))
        a,b= 0,1
        i=1
        print(a,b,end=" ")
        while i<n:
            c=a+b
            print(c,end=" ")
            a=b
            b=ci=i+1

def final():
    x=int(input("enter the option below to run the programme\n1).basic \n2).if else programme\n3).loops programm"))
    if x==1:
        a=basicprg()
        a.student_data()
        a.sutdent_information()
        final()
    elif x==2:
        b=ifelseprg()
        b.biggest()
        b.leap_year()
        b.atm_pint_verification()
        final()
    else:
        c=loops_prg()
        c.factorial_prg()
        c.prime_no_prg()
        c.fibonacci_series()
        final()


final()

