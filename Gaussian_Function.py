import numpy as np
import matplotlib.pyplot as plt
import random 
import time 

k = 300 #Spring Constant 500 
num = 9 #Number of balls 
d = 2 #Seperation between the balls 
l = 1 #Equilibrium length of the spring 
dt = 0.02 #Delta time .02
seconds = 30

yn = input("Custom values Y/N: ")
if yn.lower() == "y":
    num = int(input("Number of balls: "))
    d = int(input("Ball separation: "))
    seconds = int(input("Simulation length in seconds: "))
#l is the equilibrium length of the spring, d is the seperation of the balls !!!!
    
def printArray(array): #Function to print out an array in a more readable format 
    
    value = "["
    for i in range(num):
        vel = array[i,1] * 100
        value += str(round(array[i,0],3)) +"," + str(round(vel,3)) +";"
        #value += "ball " + str(i) + ": X = " + str(round(array[i,0],3)) + " m, V = " + str(round(array[i,1], 3)) + " m/s, F = " + str(round(array[i,2],3)) + " N \n"
    value += "]"
    print(value)

ba = np.array([[0, 0, 0]]) #Iniatilized balls array, [position, velocity/momentum]
mean = 0
sd = 0.1

random_array = np.random.normal(0, 0.1, 1000) #Random velocities on a normal curve 

#-------------------------------------------------------------------------------

for i in range(num):
    pos = i*d #Sets the position along the string
    vel = random.choice(random_array) #Random velocity from the array

    if i==0: #First ball
        ba= np.array([[pos,vel, 0.0]])

    else: #All other balls
        ba = np.append(ba, [[pos, vel, 0.0]], 0)
print("Initial Array")
printArray(ba)

#----------------------------------------------------------------------------------

def force(i, leftWall, rightWall):
    force = 0.0
    if(i==0): #If first ball
        if(abs(ba[i+1,0]-ba[i,0])<1): #If distance between is less than 1
            force += k*(ba[i+1,0]-ba[i,0]-l)
        if(leftWall):
            force += -3*k*(ba[i,0]+1-l)
    if(i==(num-1)): #If last ball 
        if(abs(ba[i,0]-ba[i-1,0])<1): #If distance between is less than 1
            force += -k*(ba[i,0]-ba[i-1,0]-l)
        if(rightWall):
            force += 3*k*(((num-1)*d+1) - ba[i,0]   -l)
    else:
        if(abs(ba[i,0]-ba[i-1,0])<1): #If distance between is less than 1
            force +=     -k*(ba[i,0]-ba[i-1,0]-l)
        if(abs(ba[i+1,0]-ba[i,0])<1): #If distance between is less than 1
            force += k*(ba[i+1,0]-ba[i,0]-l)
    return force

#---------------------------------------------------------------------------

def getVelocityArray(arr):
    velArr = []
    for i in range(num):
        velArr.append(arr[i,1])
    return velArr

#Initial Parameters for simulation
runSim = True 
leftWall = False #True in contact with left 
rightWall = False #True in contact with right
c = 0 
while(runSim):
    for k in range(4):
        for i in range(num):
            if(k==0): #Velocity 
                ba[i,1] = ba[i,1]+ba[i,2]*(dt/2) 
            if(k==1): #Position
                ba[i,0] = ba[i,0] + dt*ba[i,1] 
            if(k==2): #Force 
                if(ba[i,0] < 0): #Checks position
                    leftWall = True
                if(ba[i,0] >16 ): #Checks position
                    rightWall = True
                ba[i,2] = force(i,leftWall,rightWall) #Calls force function
                leftWall = False #Resets parameter
                rightWall = False #Resets parameter
            if(k==3): #Velocity
                ba[i,1] = ba[i,1] + ba[i,2]*(dt/2) 
    c+=1
    
    if(c%50==0): #Prints the array every second (50 * .02s)
        print("=====================")
        print("Time: " + str(c / 50) + " seconds")
        printArray(ba)
    if(c%50000==0 or c==1):
        print("*****")
        baVel = getVelocityArray(ba) #baVel is an array of the velocities from ba
            
        mean = round(np.mean(baVel), 4)  
        sd = round(np.std(baVel), 4)
        print("Mean: " + str(mean))
        print("Standard deviation: " + str(sd))

        plt.hist(baVel)
        plt.xlabel('Velocity (m/s)')
        plt.ylabel('Count')
        plt.title("Velocities at t=" + str(round((c / 50),)) + " seconds " + "\n μ=" + str(mean) + "σ=" + str(sd)) 
        #plt.text(0, -0.3, 'abc', fontsize=20, horizontalalignment='left' )
        plt.show()
           
            #count, bins, ignored = plt.hist(baVel, 1, density=True)
            #plt.plot(bins, 1/(sd * np.sqrt(2 * np.pi)) * np.exp( - (bins - mean)**2 / (2 * sd**2) ), linewidth=2, color='y')
            #plt.show()
    if(c==seconds*50):
        runSim = False


#for i in range(num):
#    if i==0 or i==8:
#        pass
#    else:
#        force = -k*(ba[i,0]-ba[i-1,0]-l)+k*(ba[i+1,0]-ba[i,0]-l)  #1
#        print(force) 
#        print("-----")
#        velocity = ba[i,1]+force*(dt/2)  #2
#        ba[i,0] = ba[i,0] + dt*ba[i,1]  #3
#        force = -k  #4
#        ba[i,1] = ba[i,1] + force*dt  #5
#        print(ba[i,1])
        
#ball_array[i,1] = (-k*(ball_array[i,0]-ball_array[i-1]-l)+ k*(ball_array[i,0]-ball_array[i+1]-l)) 
    #mom_i = -Ks(pos_i-posi-1-l) + Ks(pos_i+1-pos_i-l)
    




#*********************************************************

#population = 1000

#mean = float(input("Mean: "))
#sd = float(input("Standard Deviation: "))


##mean, sd = 0, 10 # mean and standard deviation
#random_array = np.random.normal(mean, sd, population)

#sample_size = int(input("Sample Size: "))


#rand_vel = random.choices(random_array, k=5);
#print("\n---------------\n" + 
#      "\nFrom population of " + str(population) + ", " + str(sample_size) + " samples selected: " +
#      "\n" + str(rand_vel))

#visualize = input("\n---------------\n" +
#             "\nVisual Y/N: ")

#count, bins, ignored = plt.hist(random_array, 300, density=True)
#plt.plot(bins, 1/(sd * np.sqrt(2 * np.pi)) * np.exp( - (bins - mean)**2 / (2 * sd**2) ), linewidth=2, color='y')
#plt.show()
 



