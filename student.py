#!/usr/bin python3
from teacher import PiggyParent
import sys
import time

"""
Login as: pi
Password: robots1234
ls
cd Piggy
pyhton3 student.py

"""


class Piggy(PiggyParent):

    '''
    *************
    SYSTEM SETUP
    *************
    '''

    def __init__(self, addr=8, detect=True):
        PiggyParent.__init__(self) # run the parent constructor.

        ''' 
        MAGIC NUMBERS <-- where we hard-code our settings
        '''
        self.LEFT_DEFAULT = 77.5
        self.RIGHT_DEFAULT = 80
        self.MIDPOINT = 1400  # what servo command (1000-2000) is straight forward for your bot?
        self.set_motor_power(self.MOTOR_LEFT + self.MOTOR_RIGHT, 0)
        self.load_defaults()
        
    def load_defaults(self):
        """Implements the magic numbers defined in constructor"""
        self.set_motor_limits(self.MOTOR_LEFT, self.LEFT_DEFAULT)
        self.set_motor_limits(self.MOTOR_RIGHT, self.RIGHT_DEFAULT)
        self.set_servo(self.SERVO_1, self.MIDPOINT)

    def menu(self):
        """Displays menu dictionary, takes key-input and calls method"""
        ## This is a DICTIONARY, it's a list with custom index values. Python is cool.
        # Please feel free to change the menu and add options.
        print("\n *** MENU ***") 
        menu = {"n": ("Navigate", self.nav),
                "e": ("Dance", self.dance),
                "p": ("Obstacle count", self.obstacle_count),
                "s": ("Shy", self.shy),
                "f": ("Follow", self.follow),
                "c": ("Calibrate", self.calibrate),
                "q": ("Quit", self.quit),
                "s": ("Square", self.square),
                "s": ("Check Safe Zone", self.check_safe),
                "t": ("Test", self.test),
                "w": ("Is There A Wall?", self.wall),
                "u": ("Spin At Wall", self.wall_spin),
                "a": ("Object Avoidence", self.wall_avoid),
                "b": ("Smart Object Avoidence", self.smart_wall_aviod),
                "c": ("Forward and Scan", self.fwd_w_scan),
                "m": ("Maze Solve", self.maze),
                "n": ("Maze Solve Cheap", self.derp_maze),
                "o": ("Mega Maze", self.mega_maze)
                }
        # loop and print the menu...
        for key in sorted(menu.keys()):
            print(key + ":" + menu[key][0])
        # store the user's answer
        ans = str.lower(input("Your selection: "))
        # activate the item selected
        menu.get(ans, [None, self.quit])[1]()

    '''
    ****************
    STUDENT PROJECTS
    ****************
    '''
    #Nice
    def test(self):
      self.servo(2300)

    #Nice
    def wall(self):
      while True: 
        if (self.read_distance() > 300):
          self.fwd()
          time.sleep(1)
          self.stop()
        elif (self.read_distance() < 299):
          self.back()
          time.sleep(1)
          self.stop()
  
  #Nice
    def wall_spin(self):
      while True: 
        if (self.read_distance() > 300):
          self.fwd()
          time.sleep(1)
          self.stop()
        elif (self.read_distance() < 299):
            self.right(primary=100, counter=-100)

  #Nice             
    def wall_avoid(self):                          
      while True:                                   #Do it forever
        if (self.read_distance() > 300):            #Is there a wall? (No)
          self.fwd()                                #Go forwards]
          time.sleep(1)                             #Go forwards]
          self.stop()                               #Go forwards]
        elif (self.read_distance() < 299):          #Is there a wall? (Yes)
            self.right(primary=100, counter=-100)   #Turn right]
            time.sleep(0.3)                         #Turn right]
            self.stop()                             #Turn right]
            self.fwd()                              #Go forwards}
            time.sleep(2)                           #Go forwards}
            self.stop()                             #Go forwards}
            self.right(primary=-100, counter=100)   #Turn left]
            time.sleep(0.3)                         #Turn left]
            self.stop()                             #Turn left]

    def wall_avoid_left(self):                      #Same as wall avoid exept you turn left
      while True: 
        if (self.read_distance() > 300):
          self.fwd()
          time.sleep(1)
          self.stop()
        elif (self.read_distance() < 299):
            self.right(primary=-100, counter=100)
            time.sleep(0.3)
            self.stop()
            self.fwd()
            time.sleep(2)
            self.stop()
            self.right(primary=100, counter=-100)
            time.sleep(0.3)
            self.stop()

#Nice
    def smart_wall_aviod(self):
      back = 0
      while True:                                     #This makes it run forever
        if (self.read_distance() > (200 + back)):              #Is there a wall (No)
          self.fwd()                                  #Move forward] 
          time.sleep(1)                               #Move forward]
          self.stop()                                 #Move forward]
        elif (self.read_distance() < (199 + back)):            #Is there a wall (Yes)
            self.servo(800)                           #Looking right]
            time.sleep(1)                             #Looking right]
            self.stop()                               #Looking right]
            right = self.read_distance()              #Setting right length to a variable
            self.servo(2000)                          #Looking left]
            time.sleep(1)                             #Looking left]
            self.stop()                               #Looking left]
            left = self.read_distance()               #Setting left length to a variable
            self.servo(1400)                          #Looking straight]
            time.sleep(1)                             #Looking straight]
            self.stop()                               #Looking straight]
            if (abs(right - left) > 100):
              if (right > left):                        #Is the right side shorter (Yes)
                self.servo(1400)                        #Looking straight]
                time.sleep(1)                           #Looking straight]
                self.stop()                             #Looking straight]
                self.wall_avoid()                       #Running Wall Avoid
              elif (left > right):                      #Is the left side shorter (Yes)
                self.servo(1400)                        #Looking straight]
                time.sleep(1)                           #Looking straight]
                self.stop()                             #Looking straight]
                self.wall_avoid_left()                  #Running Wall Avoid Left
            else:
              self.back()
              time.sleep(2)
              self.stop()
              back += 100
                #Credit -> Vincent
              

    
    def swerve(self, direction = "R"):                                  #Step 2
      self.stop()
      self.servo(self.MIDPOINT)
      if "R" in direction:
        self.right(primary=100, counter=80) #Left is more powerful (Problem solving time)
        time.sleep(0.5)
        self.stop()
        self.left(primary=100, counter=80) 
      elif "L" in direction:
        self.left(primary=100, counter=80)
        time.sleep(0.5)
        self.stop()
        self.right(primary=100, counter=80) #Gotta fix this one too
      time.sleep(0.5)
      self.stop()


    def fwd_w_scan(self):                             #Step 1
      while True: 
        self.fwd()
        self.servo(1000)
        if (self.read_distance() < 200):
          self.swerve("L")
        self.servo(1800)
        if (self.read_distance() < 200):
          self.swerve("R")
        self.servo(1400)
        if (self.read_distance() < 200):
          self.smart_wall_aviod()




    def check_safe(self):
      self.safe_to_dance()
      while True: 
        if (self.read_distance() > 300):
          self.fwd()
          time.sleep(1)
          self.stop()
        elif (self.read_distance() < 299):
          while True:
            self.right(primary=100, counter=-100)

    def derp_maze(self):
      while True:
        if (self.read_distance() > 300):              #Is there a wall (No)
          self.fwd()                                  #Move forward] 
          time.sleep(1)                               #Move forward]
          self.stop()                                 #Move forward]
        elif (self.read_distance() < 299):            #Is there a wall (Yes)
          self.right(primary=100, counter=-100)
          time.sleep(0.3)
          self.stop()



    def maze(self):
      while True: 
        self.servo(2300)                         #Look Left
        time.sleep(1)                            #Look Left
        if (self.read_distance() > 300):         #Is there a wall (No)
          self.servo(self.MIDPOINT)                   #Look straight
        elif (self.read_distance() < 300):       #Is there a wall (Yes)
          print("empty")

        elif (self.read_distance() < 300):
          self.servo(self.MIDPOINT)
          time.sleep(1)

          #Look left if close, look forward, if forward is far then go forwards for a bit then repeat
          #Look left if far, look forward, if forward is far then go forwards for a bit then repeat 
          #Look left if far, look forward, if forward is close then turn right then repeat

    def square(self):
      for i in range(4):
        self.fwd()
        time.sleep(1)
        self.stop()
        self.right(primary=43, counter=-43)
        time.sleep(1)
        self.stop()



    def dance(self):
        """A higher-ordered algorithm to make your robot dance"""
        # TODO: check to see if it's safe before dancing
        if safe_to_dance():
          pass

        # lower-ordered example...
        for i in range(4):
          self.right(primary=100, counter=-100)
          time.sleep(1)
          self.stop()
        self.fwd()
        time.sleep(0.5)
        self.stop()
        for i in range(4):
          self.right(primary=100, counter=-100)
          time.sleep(0.5)
          self.stop()
          self.right(primary=-100, counter=100)
          time.sleep(0.5)
          self.stop()
        self.stop()




    def safe_to_drive(self):
      self.read_distance()
      if self.read_distance() > 500:
        return True
      else:
        return False

########################################Nice###########################################
######################################MAZE MODIFICATION################################
    def mega_maze(self):
      while True: 
        self.servo(2300)                         #Look Left
        time.sleep(1)                            #Look Left
        if (self.read_distance() < 300):         #Is there a wall left1 (yes)
          self.servo(self.MIDPOINT)                   #Look straight
          time.sleep(1)                          #Look straight
          if (self.read_distance() > 50):       #is there a wall infront1 (No)
            self.fwd()                           #Drive forwards
            time.sleep(0.2)                      #Drive forwards
            self.stop()                          #Drive forwards
          elif (self.read_distance() < 50):     #is there a wall infront1 (yes)
            self.right(primary=100, counter=-100)#Turn right
            time.sleep(0.43)                      #Turn right 
            self.stop()                          #Turn right
        elif (self.read_distance() > 50):       #Is there a wall left1 (No)
          self.servo(self.MIDPOINT)                   #Look straight
          time.sleep(1)                          #Look straight
          if (self.read_distance() > 50):       #is there a wall infront2 (No)
            self.fwd()                           #Drive forwards
            time.sleep(0.2)                      #Drive forwards
            self.stop()                          #Drive forwards
          elif (self.read_distance() < 50):     #is there a wall infront2 (yes)
            self.left(primary=100, counter=-100) #Turn left
            time.sleep(0.41)                      #Turn left 
            self.stop()                          #Turn left

          #Look left if close, look forward, if forward is far then go forwards for a bit then repeat
          #Look left if far, look forward, if forward is far then go forwards for a bit then repeat 
          #Look left if far, look forward, if forward is close then turn right then repeat

###########################################################################################
###########################################################################################
###########################################################################################


    def safe_to_dance(self):
        """ Does a 360 distance check and returns true if safe """
        self.read_distance()
        time.sleep(0.5)
        self.right(primary=100, counter=-100)
        self.read_distance()
        time.sleep(0.5)
        time.sleep(0.5)
        self.stop
        return True

    def shake(self):
        """ Another example move """
        self.deg_fwd(720)
        self.stop()

    def example_move(self):
        """this is an example dance move that should be replaced by student-created content"""
        self.right() # start rotating right
        time.sleep(1) # turn for a second
        self.stop() # stop
        self.servo(1000) # look right
        time.sleep(.25) # give your head time to move
        self.servo(2000) # look left

    def scan(self):
        """Sweep the servo and populate the scan_data dictionary"""
        for angle in range(self.MIDPOINT-350, self.MIDPOINT+350, 3):
            self.servo(angle)
            self.scan_data[angle] = self.read_distance()

    def obstacle_count(self):
        """Does a 360 scan and returns the number of obstacles it sees"""
        pass

    def nav(self):
        print("-----------! NAVIGATION ACTIVATED !------------\n")
        print("-------- [ Press CTRL + C to stop me ] --------\n")
        print("-----------! NAVIGATION ACTIVATED !------------\n")
        
        # TODO: build self.quick_check() that does a fast, 3-part check instead of read_distance
        while self.read_distance() > 250:  # TODO: fix this magic number
            self.fwd()
            time.sleep(.01)
        self.stop()
        # TODO: scan so we can decide left or right
        # TODO: average the right side of the scan dict
        # TODO: average the left side of the scan dict
        


###########
## MAIN APP
if __name__ == "__main__":  # only run this loop if this is the main file

    p = Piggy()

    if sys.version_info < (3, 0):
        sys.stdout.write("Sorry, requires Python 3.x\n")
        p.quit()

    try:
        while True:  # app loop
            p.menu()

    except KeyboardInterrupt: # except the program gets interrupted by Ctrl+C on the keyboard.
        p.quit()  
