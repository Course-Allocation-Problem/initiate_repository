# Course Allocation Problem <br/>

### Goal: <br/>  
&emsp; Develop a system that will perform a fair division of elective courses for the students.

### Brief introduction: <br/> 
&emsp; Today in higher education institutions "first come, first served” is the common method.<br/> 
&emsp; The problems: major burden on the server, make important decisions under time pressure, <br/>
&emsp; registration for a group of courses in parallel, a burden on the coordinator, unfair division. <br/>
&emsp; Thus, we implemented a new method of fair division among the elective courses. <br/>

### Algorithm: <br/>
&emsp; We implement an algorithm named SP which mentioned in the following artical. <br/> 
&emsp; Article name: Optimization Mechanisms for the Course Allocation Problem, <br/>   
&emsp; Written by: Hoda Atef Yekta, Robert. <br/>                                                                                       
&emsp; Day Published: 13 Jan 2020 Online by INFORMS Institute for Operations Research <br/>
&emsp; and the Management Sciences: https://pubsonline.informs.org/doi/10.1287/ijoc.2018.0849 <br/> 

#### &emsp; Pseudo Code: <br/>
&emsp; &emsp; 1) Repeats k times, every round:<br/>
&emsp; &emsp; &emsp; i) Each student updates his preferences table according to the collision of other courses that <br/>
&emsp; &emsp; &emsp; &emsp; he already signed up to. Also, removing courses that have a full capacity. <br/> 
&emsp; &emsp; &emsp; ii) Each student offers a bid amount for his top priority course.<br/>
&emsp; &emsp; &emsp; iii) Each course accepts up to his available seats of the highest offers,<br/>
&emsp; &emsp; &emsp; &emsp; and rejects any remaining offers, Then capacities are updated.<br/>
&emsp; &emsp; &emsp; iv) If a student gets rejected by a certain course then he gets return unspent points to use on the next <br/>
&emsp; &emsp; &emsp; &emsp; most preferred course. Furthermore, the rejected students will repeat steps (i)–(iii) <br/>
&emsp; &emsp; &emsp; &emsp; until no more students are rejected.<br/>


## How to use:<br/>
### &emsp; Requirements: <br/> 
#### &emsp; &emsp; Frontend: <br/> 
&emsp; &emsp; &emsp; Node JS version 10.9 <br/> <br/>
#### &emsp; &emsp; Backend: <br/>
&emsp; &emsp; &emsp; Python3 (preferred IDE for running the code is Pycharm) <br/><br/>

### &emsp; Guide:<br/>

&emsp; If you installing the Backend on linux, replace python with python3<br/> 
&emsp; &emsp; 1) Backend: <br/>
&emsp; &emsp; &emsp; * Go to the repository: https://github.com/Course-Allocation-Problem/cap-backend. <br/>
&emsp; &emsp; &emsp; *	Clone the repository.<br/>
&emsp; &emsp; &emsp; *	Write the command:```cd cap-backend```.<br/>
&emsp; &emsp; &emsp; *	Create a Python virtual environment for your Django project:<br/>
&emsp; &emsp; &emsp; &emsp; Write in the terminal: ``` python -m venv venv ```<br/>

&emsp; &emsp; &emsp; * Activate the virtual environment.<br/>
&emsp; &emsp; &emsp; &emsp; For Linux: ``` source venv/bin/activate ``` <br/>
&emsp; &emsp; &emsp; &emsp; For Windows: ``` venv\Scripts\activate ``` <br/>

&emsp; &emsp; &emsp; *	Install Python dependencies for this project: ```pip install -r requirements.txt ```. <br/>
&emsp; &emsp; &emsp; * Create super user using: ```python manage.py createsuperuser```. <br/>
&emsp; &emsp; &emsp; * Start the Django development server by command: ```python manage.py runserver ```.<br/>
&emsp; &emsp; &emsp; * Open http://127.0.0.1:8000/admin/ in a web browser to view your application.<br/>
&emsp; &emsp; &emsp; * Insert your super user informantio has been created on VII to insrt to Dejango.<br/>
&emsp; &emsp; &emsp; * Now you can examine the database.<br/><br/>


&emsp; &emsp; 2) Frontend: <br/>
&emsp; &emsp; &emsp; * Go to the repository: https://github.com/Course-Allocation-Problem/cap-frontend.<br/>
&emsp; &emsp; &emsp; *	Clone the repository.<br/>
&emsp; &emsp; &emsp; * Write the command: ```cd cap-frontend```.<br/>
&emsp; &emsp; &emsp; *	In the terminal write the command: ```npm i``` . <br/>
&emsp; &emsp; &emsp; * After the previous command writes the next command: ```npm start```.<br/>
&emsp; &emsp; &emsp; * Open http://localhost:3000/ in a web browser to view your application.<br/><br/>


&emsp; &emsp; 3) Log in: You can experiment using the following login details<br/>
&emsp; &emsp; &emsp; * Student: <br/>
&emsp; &emsp; &emsp; &emsp; User name: user_test_11 <br/>
&emsp; &emsp; &emsp; &emsp; Password: Itaysim7 <br/>

&emsp; &emsp; &emsp; *	University: <br/>
&emsp; &emsp; &emsp; &emsp; User name: Ariel-cs <br/>
&emsp; &emsp; &emsp; &emsp; Password: Capcap11 <br/>  
 
 

