#Q1.circle class

class Circle:
    def __init__(self,r):                           #Initialising value
        self.radius = r
        print("Radius: ", self.radius)                  
    def getArea(self):                              #Function to calculate & print area of circle 
        area = 3.14*self.radius*self.radius         
        print("Area: ", area)
    def getCircumference(self):                     #Function to calculate & print perimeter of circle
        per = 2*3.14*self.radius
        print("Circumference: %.2f" % per)

#Driving Code
obj = Circle(5)             #Object creation of class Circle 
obj.getArea()                
obj.getCircumference()       


#Q2.Student class 

class Student:
    def __init__(self,name,roll):                  #Initialising values
        self.n = name
        self.r = roll
    def Display(self):                             #Function to display Details of students
        print("Name: ", self.n)
        print("Roll_Number: ", self.r)

#Driving Code        
S1 = Student("X", 1)         #Object creation of class Student
S1.Display()                 
S2 = Student("Y", 2)         #Object Creation of class Student
S2.Display()                 
   
     
#Q3.Temperature class

class Temperature:
    def __init__(self,temp):                      #Initialising value
        self.t = temp 
    def convertFahrenheit(self):                  #Function to convert Celsius to Fahrenheit
        fah = (9/5)*self.t + 32
        print("Fahrenheit Equivalent: ", fah)
    def convertCelsius(self):                     #Function to convert Fahrenheit to Celsius
        cel = (self.t-32)*(5/9)
        print("Celsius Equivalent: ", cel)
t1 = Temperature(53)          #Object Creation of class Temperature
t2 = Temperature(96.8)        #Object Creation of class Temperature
t1.convertFahrenheit()        
t2.convertCelsius()           


#Q4.MovieDetails

class MovieDetails: 
    def __init__(self, mn, an, yr, r):            #Initialising values
        self.movie_name = mn
        self.artist_name = an
        self.release_year = yr
        self.ratings = r        
    def Display(self):             				               #Function to display details of Movie
        print("Movie: ",self.movie_name)
        print("Artist_Name: ",self.artist_name)
        print("Release_Year: ",self.release_year)
        print("Ratings_(Out of 10): ", self.ratings)
    def Update(self, new_moviename, new_artistname, new_release, new_ratings):  #Function to update details of Movie as provided
        print("Updating Movie Details.....")
        self.movie_name = new_moviename
        self.artist_name = new_artistname
        self.release_year = new_release
        self.ratings = new_ratings
Movie1 = MovieDetails("xyz","abc",2000,5.5)    				      #Object creation of class MovieDetails
Movie2 = MovieDetails("jkl","iop",2001,7.3)              	              #Object creation of class MovieDetails
Movie1.Display()                                                              
Movie2.Display()                                                             
Movie2.Update("jkl","ytu",2001,7.5)	                                     
Movie2.Display()                                                             


#Q5.Expenditure

class Expenditure:                                  
    def __init__(self,expenditure, savings):     #Initialising values
        self.e = expenditure
        self.s = savings
    def Display(self):                           #Function to Display Expenditure & Savings
        print("Expenditure: ", self.e)           
        print("Savings: ", self.s)
    def Calculate_salary(self):                  #Function to Calculate salary
        self.salary = self.s - self.e 
    def Display_salary(self):
        print("Salary: ", self.salary)           #Function to Display salary
E = Expenditure(2240, 4000)                      #Object creation of class Expenditure 
E.Display()                                      
E.Calculate_salary()                             
E.Display_salary()                               
