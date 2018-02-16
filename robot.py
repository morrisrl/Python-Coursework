##class Card(object):
##    """A playing card"""
##
##    def __init__(self, suit, rank):
##        self.suit = suit 
##        self.rank = rank
##
##    def info(self):
##        
##        
##class Container(object):
##    """A container"""
##
##    def __init__(self, maxCapacity, currentCapacity):
##        self.maxCapacity = maxCapacity
##        self.currentCapacity = currentCapacity
##
##class Course(object):
##    "An academic course"
##
##    def __init__(self, courseNum, creditHours, time, location, instructor)
##        self.courseNum = courseNum
##        self.creditHours = creditHours
##        self.time = time
##        self.location = location
##        self.instructor = instructor
##
##        
###main
##hearts, diamonds, spades, clubs
##int
##        
##class Robot(object):
##    """A virtual fighting robot"""
##
##    def __init__(self, name, weapon, strength):
##        self.name = name
##        self.weapon = weapon
##        self.strength = strength
##        self.status = True
##        print("Robot created!"+ self.name)
##        print("--"*15)
##            
##        
##    def __str__(self):
##        reply = "Fighting Robot\n"
##        reply += "Name:" +self.name+"\n"
##        reply += "Weapon:" +self.weapon+"\n"
##        reply += "Strength:"+str(self.strength)+"\n"
##        if self.status == True:
##            reply += "Status: ONLINE"+"\n"
##        else: reply += "Status: OFLINE"
##        return reply
##
###main
##r2d2=Robot("R2D2", "Beeps", 2)
##c3p0=Robot("C3P0", "Conversation", 2)
##
##print(r2d2)
##print(c3p0)

class Robot(object):
    """A virtual fighting robot"""

    def __str__(self):
        reply = "Fighting Robot\n"
        reply += "Name:" +self.name+"\n"
        reply += "Weapon:" +self.weapon+"\n"
        reply += "Strength:"+str(self.strength)+"\n"
        if self.status == True:
            reply += "Status: ONLINE"+"\n"
        else: reply += "Status: OFLINE"
        return reply

    "There are

    if robot_list > 

    
for robot in robot.robot_list:
    print(

Robot.contenders()

r2d2=Robot("Optimus", "Fists", 10)
c3p0=Robot("Voltron", "Sword", 10)

Robot.contenders()
