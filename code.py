# -*- coding: utf-8 -*-
"""chatbot1.py
 Team Members:
 	Ujjwal Bhardwaj(CSE2)
 	Gaurav Kumar(CSE2)
 	Nitesh Kumar jha(CSE1)


    https://colab.research.google.com/drive/1YLvx0sieJM4bvq_NYYbxPd4eG8Rz65nr
"""



import random

hellow = ["hi","is anyone there?", "hello", "good day","hello there","hey"]
bye = ["see you later","bye" ,"goodbye", "i am Leaving", "have a Good day"]
howare = ["how are you","whats up","how you doing?","how are you?","how you doing","Whats up?"]
name = ["whats your name","what is your name","do you have any name","what should i call you","name","whats your name?","what is your name?","do you have any name?","what should i call you?"]
agc = ["amritsar group of colleges","info about amritsar group of colleges", "agc","best engineering college","Best college","autonomous college","college","information about college","college information"]
cours = ["course offered","course","course by college","courses","agc courses","courses in agc"]
adm = ["admission","admissions","admission detail","admission details","details about admission"]
plc = ["placements","placement","college placement","agc placements","agc placement","acet placement","acet placements"]
fac = ["facilities","facility","agc facilities","agc facility","facilities offered","facility offered","college facilities"]
fee = ["fee","fees","fee detail","fees detail","payment","fees payment","fee payment","pay fee","pay fees","pay college fee","pay college fees"]
contacts = ["contact", "contacts","college contact","contact detail","contact details"]
b_tech = ["b.tech","btech","b-tech","bachelors course","b.tech course","agc b.tech","b.tech agc","acet b.tech","b.tech information","btech information"]
cse_head =["hod cse","cse hod","hod","head","btech cse hod","hod cse btech","cse-hod","hod-cse","cse head"]
dept_cse = ["about cse","department cse","cse department","details of cse","cse branch", "cse details","cs","about cse department","b.tech cse","cse btech","c.se"]
cse_lab = ["lab","lab cse","cse lab","cse-lab","lab-cse","labs"]
cse_msn= ["cse vision","cse mission","mision cse","mission"]
scl = ["scholarship","scholarships","scholarship test",]


print("*******************************************************\n")
print("AGC SMART_BOT FOR INFORMATIONS....\n")
print("Please Avoid using special Characters (!,@,?,&,etc)\n\n")
while True:
  a = input('User said -')

  if a.lower() in hellow:
    botans = ["Hello !","hi","hi there","welcome"]
    print('Bot said - '+random.choice(botans)+'\n')

  elif a.lower() in howare:
    botans = ["I am fine ,How can I help u? ","Happy, How can I help You?","I am good, How can I help u?"]
    print('Bot said -'+ random.choice(botans)+'\n')

  elif a.lower() in name:
    botans = ["My name is AGC bot","You can call me AGC bot","AGC Bot in your service","My friends call me AGC Bot"]
    print('Bot said -'+ random.choice(botans)+'\n')

  elif a.lower() in bye:
    botans = ["Sad to see you go :(", "Talk to you later", "Goodbye!","Have a nice Day"]
    print('Bot said - '+random.choice(botans)+'\n')
  
  elif a.lower() in agc:
    print('Bot said  -Go to : https://agcamritsar.in/\n')
  
  elif a.lower() in cours: 
    print('Bot said  -\n\tB.TECH\n\tM.TECH\n\tMANAGEMENT STUDIES\n\tCOMPUTER APPLICATION\n\tHOTEL MANAGEMENT\n\tAGRICULTURE\n\tPHARMACY\n\tLAW COURSES\n\tB.VOCATIONAL\n\tB.SC FASHION DESIGNING\n\tODL\n')
  
  elif a.lower() in adm:
    print('Bot said  -ADMISSION GUIDELINES :- https://agcamritsar.in/admission-guidelines.php\n')

  elif a.lower() in plc:
    print('Bot said  -\n''\tPlacement cell at Amritsar Group of Colleges (AGC) is a team of professionals and vibrant people working together to assist and help the students to get the better job options through campus recruitments.\n\tThe whole team work hard to create great placement opportunities for the students by inviting top-notch corporate companies viz. TCS, Infosys, Wipro, HCL, Intel, Amazon, Bosch, Just Dial, Ford \n\tand many more reputed ones, for the recruitment purposes.\n')
    print('\tFor more info visit:- https://agcamritsar.in/placement1.php\n')

  elif a.lower() in fac:
    print('Bot said  -Facilities offered:- \n\t\tHOSTEL, \n\t\tLIBRARY, \n\t\tMEDICAL, \n\t\tSPORTS, \n\t\tRESTAURANT, \n\t\tTRANSPORT\n')

  elif a.lower() in fee:
    print('Bot said  -For Fee payment queries Visit:- \n\thttps://www.eduqfix.com/PayDirect/#/student/pay/nYXzGjZbx7y4d6WcRB6l7P5YXMyyKg3wR+HJ+fHMpKMt1x0yIn8j6E2QErnlZuZk/382\n')

  elif a.lower() in contacts:
    print('Bot said  -To contact us Please Visit:- https://agcamritsar.in/contact.php\n')

  elif a.lower() in b_tech:
    print('Bot said  -The Best B. Tech Courses offered by AGC include: \n\tCivil Engineering (CE), \n\tComputer Science & Engineering (CSE), \n\tElectronics & Communication Engineering (ECE), \n\tElectrical Engineering (EE), \n\tand Mechanical Engineering (ME).\n')
    print('For more info Visit:- https://agcamritsar.in/B.tech.php\n')

  elif a.lower() in cse_head:
    print('Bot said  -Er. Vinod Sharma (Head of the Department-Computer Science and Engineering)\n')
    print('\tFor more Info:- https://agcamritsar.in/hod-cse-message.php\n')

  elif a.lower() in dept_cse:
    print('Bot said  -B.Tech-CSE is the study of the engineering of computer science systems.')
    print('\tThe Department of Computer Science Engineering at Amritsar Group of Colleges.\n\tACET is a premier learning center running software like JCP, OCA, and OCP \n\tin collaboration with SUN MICRO-SYS and ORACLE respectively.\n')
    print('\tFor more info, Visit:- https://agcamritsar.in/b.tech(cse).php\n')

  elif a.lower() in cse_lab:
    print('Bot said  -CSE Department includes the Following labs:- \n\tProgramming Lab-I\n\tOperating System\n\tProgramming Lab-II\n\tProject Lab\n\tDatabase Lab\n')

  elif a.lower() in cse_msn:
    print('Bot said  -Missions:- https://agcamritsar.in/cse-vision.php\n')

  elif a.lower() in scl:
    print('Bot said  -AGC provides lots of Scholarships though AGC-NEST\n')
    print('\tFor more information, Kindly visit:- https://agcnest.com/\n')

  else:
    print('Bot said - Sorry I could not Understand...\n')
