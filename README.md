# Physics-Simulation-Gaussian-
Project made for professorial assistant program at Michigan State University
## Functionality
Detailed below is the simulation of balls along a string. The balls are treated as springs with
equilibrium length l = 1m. On either side of the string is a fixed ball with a spring constant of 3K
(1,500N).
![image](https://user-images.githubusercontent.com/38506899/161406799-cb7e414d-3917-4f9f-9a73-885166005668.png)
![image](https://user-images.githubusercontent.com/38506899/161406808-e802ff8b-4e98-412f-b4e5-c275b094626e.png) <br />
The constants num, d, and seconds can be updated by the user at the beginning of the program,
or they can be left at their default values. The remaining constants are left at default. The program generates N number of 
balls along the string with velocities randomly generated based on a normal or gaussian distrubution (mean=0 and std=0.1).
When the simulation begins values of force and velocity are calculatd using rieman sums to conserve amount of computational power required. Program makes use of MatPlotLib to display the velocities of the balls on on the graph and uses the terminal to output specific positions and velocities. 
## Sample output: 
Custom values Y/N: Y <br />
Number of balls: 6<br />
Ball separation: 2<br />
Simulation length in seconds: 20<br />
Initial Array<br />
[0.0,3.51;2.0,-1.688;4.0,10.71;6.0,-1.352;8.0,-0.531;10.0,-11.643;]<br />
*****
Mean: -0.0017 <br />
Standard deviation: 0.0668 <br />

Time: 1.0 seconds <br />
[0.035,3.51;1.983,-1.688;4.107,10.71;5.986,-1.352;7.995,-0.531;9.884,-11.643;] <br />

Time: 2.0 seconds<br />
[0.07,3.51;1.966,-1.688;4.214,10.71;5.973,-1.352;7.989,-0.531;9.767,-11.643;]<br />
Time: 3.0 seconds<br />
[0.105,3.51;1.949,-1.688;4.321,10.71;5.959,-1.352;7.984,-0.531;9.651,-11.643;]<br />

Time: 4.0 seconds<br />
[0.14,3.51;1.932,-1.688;4.428,10.71;5.946,-1.352;7.979,-0.531;9.534,-11.643;]<br />

Time: 5.0 seconds<br />
[0.176,3.51;1.916,-1.688;4.535,10.71;5.932,-1.352;7.973,-0.531;9.418,-11.643;]<br />

Time: 6.0 seconds<br />
[0.211,3.51;1.899,-1.688;4.643,10.71;5.919,-1.352;7.968,-0.531;9.301,-11.643;]<br />

Time: 7.0 seconds<br />
[0.246,3.51;1.882,-1.688;4.75,10.71;5.905,-1.352;7.963,-0.531;9.185,-11.643;]<br />

Time: 8.0 seconds<br />
[0.281,3.51;1.865,-1.688;4.857,10.71;5.892,-1.352;7.958,-0.531;9.069,-11.643;]<br />

Time: 9.0 seconds<br />
[0.316,3.51;1.848,-1.688;4.951,5.591;5.891,3.767;7.952,-0.531;8.952,-11.643;]<br />

Time: 10.0 seconds<br />
[0.351,3.51;1.831,-1.688;4.959,-1.351;5.976,10.709;7.917,-8.406;8.866,-3.768;]<br />

Time: 11.0 seconds<br />
[0.386,3.51;1.814,-1.688;4.946,-1.351;6.083,10.709;7.807,-11.644;8.854,-0.53;]<br />
Time: 12.0 seconds<br />
[0.421,3.51;1.797,-1.688;4.932,-1.351;6.19,10.709;7.69,-11.644;8.849,-0.53;]<br />

Time: 13.0 seconds<br />
[0.456,3.51;1.781,-1.688;4.919,-1.351;6.297,10.709;7.574,-11.644;8.844,-0.53;]<br />

Time: 14.0 seconds<br />
[0.491,3.51;1.764,-1.688;4.905,-1.351;6.405,10.709;7.457,-11.644;8.838,-0.53;]<br />

Time: 15.0 seconds<br />
[0.527,3.51;1.747,-1.688;4.892,-1.351;6.482,-0.002;7.37,-0.933;8.833,-0.53;]<br />

Time: 16.0 seconds<br />
[0.562,3.51;1.73,-1.688;4.878,-1.351;6.4,-11.644;7.443,10.709;8.828,-0.53;]<br />

Time: 17.0 seconds<br />
[0.597,3.51;1.713,-1.688;4.865,-1.351;6.283,-11.644;7.55,10.709;8.823,-0.53;]<br />

Time: 18.0 seconds <br />
[0.632,3.51;1.696,-1.688;4.851,-1.351;6.167,-11.644;7.657,10.709;8.817,-0.53;]<br />

Time: 19.0 seconds<br />
[0.667,3.51;1.679,-1.688;4.838,-1.351;6.051,-11.644;7.764,10.709;8.812,-0.53;]<br />

Time: 20.0 seconds<br />
[0.689,-0.97;1.669,0.552;4.824,-1.351;5.934,-11.644;7.865,7.354;8.813,2.824;]<br />



 - Program consists of a simulation of balls along string 
 - User inputs # of balls, seperation between balls, and length of simulation
 - The program assigns a random velocity to each ball based on a gaussian distrubution 
 - The simulation outputs the velocity and position of the balls every 1 second 
 - These values are updated based on elastic collisions (no loss of energy) between the balls <br />
  [Sample Output.pdf](https://github.com/Ebarrett11/Physics-Simulation-Gaussian-/files/8401839/Sample.Output.pdf) <br />
 ![t=1000](https://user-images.githubusercontent.com/38506899/161366686-0720388e-30c9-405e-8f80-f943aae53500.png)

[Balls Along String Report (1).pdf](https://github.com/Ebarrett11/Physics-Simulation-Gaussian-/files/8403602/Balls.Along.String.Report.1.pdf)
