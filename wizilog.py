############################################################################
## platform Wizilog framwork development programming
## Engineer Aryia Behroziuan
## GitHub: https://github.com/Aryia-behroziuan
## Website: https://aryia-behroziuan.github.io/web/
## Wizibox from qitSource inc https://aryia-behroziuan.github.io/about/
############################################################################

### importing
import time
import os


## Title (Company)



## Development run
version = 'v1.0.0'

# login User
print('\nLogin in Wizilog')
print('----------------------------')
builder = input(' Email address: ')
time.sleep(1)
print('\nHi Welcome to Wizibox\n Develop your user interface with this framework')
time.sleep(2)
os.system('cls' or 'clear')


# Color
class color:
     blue = '\033[94m'
     yell = '\033[93m'
     end = '\033[0m'


# Program
for x in range(900000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000):
    mainroot = str(input(color.blue+ 'Wizibox@Wizi.so/-$ ' + color.end))
    if mainroot == '-help':
          file = open('help.txt', encoding="utf-8")
          text = file.read()    
          print(text) 


    if  mainroot == 'cls':
          os.system('cls')


    if mainroot == 'clear':
          os.system('clear')    


    if mainroot == 'doc':
          file = open('Document.txt', encoding="utf-8")
          text = file.read()    
          print(text) 


    if mainroot == 'update':
          print('installed Wizibox '+version)
          print('Download the new update from the website'+color.yell+"'https://aryia-behroziuan.github.io/wizibox/'"+color.end)


    if mainroot == 'version':
          print('installed Wizibox '+version)
          print('Apply to update the software from the front'+color.yell+"'update'"+color.end)    


    if mainroot == 'sys config':
         os.system('ipconfig')


    if mainroot == 'open codedoxs':
          #Project Container Start Project
          #Project For Creator Web Project Framwork

          #Importing Programm
          import sys
          import os
          import time
          import platform

          #Color
          class Color:
               CYAN = '\033[96m'
               BLUE = '\033[94m'
               GREEN = '\033[92m'
               YELLOW = '\033[93m'
               RED = '\033[91m'
               #---END COLOR PRIGRAM
               BOLD = '\033[1m'
               UNDER = '\033[4m'
               END = '\033[0m'

          #Logo and Content for Run
          print('                                         ')
          print('              _      _____      _    _   ')
          print('  ____       | |    | | _ \     \\  //   ')
          print(' / __/ __  __| | __ | || \ \ __  \\//  __')
          print('| |__ /__\/_ | |/__\| ||_/ //__\ //\\ /__')
          print(' \____\__/\__|_|\__ |_|___/ \__///  \\__/')
          print('  CodeDoxs Framwork                      ')
          print('  Verssion 1.0.0                         ')
          print('  Creator Aryia-Behroziuan               ')
          print('  web aryia-behroziuan.github.io/codedoxs')
          print()


          #Programm
          #Input Data For Programm
          url = input('[01]Enter URL(Full) New Project:')
          NameProject = input('[02]Enter Name New Project:')
          Document =  input('[03]Enter Document Project:')

          #Create Project
          Createfile = str(url+NameProject)
          os.mkdir(str(Createfile))

          #Create index File
          Createindex = str(url+NameProject+'\index.html')
          index = open(str(Createindex), "a")
          index.write("<html>")
          index.write("\n    <head><title>CodeDoxs</title></head>")
          index.write("\n    <body>\n    <h1>Welcome To The CodeDoxs 1.0.0</h1>\n    <a href='http://aryia-behroziuan.github.io/codedoxs/'>CodeDoxs-Web</a>\n    <br/><a href='http://aryia-behroziuan.github.io/web/'>Web-Aryia Behroziuan</a>\n</body>")
          index.write("\n</html>")


          #Create Document Project
          Createindex = str(url+NameProject+'\Document.txt')
          maindocument = open(str(Createindex), "a")
          maindocument.write("Document Project Dats Set")
          maindocument.write("\n")
          maindocument.write("\n")
          maindocument.write("DataSet={")
          maindocument.write("\n      Name:"+NameProject+',')
          maindocument.write("\n      URL:"+url+' Localhost'+',')
          maindocument.write("\n      Document:"+Document+',')

          time = time.localtime()
          year = str(time.tm_year)
          manth = str(time.tm_mon)
          day = str(time.tm_mday)


          maindocument.write("\n      Year:"+year+',')
          maindocument.write("\n      creation project:"+manth+'/'+day+'/'+year+',')
          maindocument.write("\n      Languages:"+'HTML ,'+'Css ,'+'JS ,'+'Scss '+',')

          namesys = str(platform.node())
          sys = str(platform.platform())
          v_python = str(platform.python_build())
          compayler = str(platform.python_compiler())
          platform1 = str(platform.release())
          system = str(platform.system())
          datasys = str(platform.uname())

          maindocument.write("\n      Creator:"+namesys+',')
          maindocument.write("\n      Version:"+v_python+',')
          maindocument.write("\n      Compiler:"+compayler+',')
          maindocument.write("\n      Platform:"+platform1+',')
          maindocument.write("\n      System:"+system+platform1+',')
          maindocument.write("\n      Data System:"+datasys+',')
          maindocument.write("\n}")
          maindocument.write("\n")
          maindocument.write("CodeDoxs Version={")
          maindocument.write("\n      Version:"+'1.0.0'+',')
          maindocument.write("\n      Framwork:"+'CodeDoxs'+',')
          maindocument.write("\n      Programmer CodeDoxs:"+'Aryia-Behroziaun'+',')
          maindocument.write("\n      CodeDoxs-Web:"+'http://aryia-behroziaun.github.io/codedoxs/'+',')
          maindocument.write("\n      Aryia-Behroziuan-Web:"+'aryia-behroziaun.github.io/web/'+',')
          maindocument.write("\n}")


          #Create Config
          Createconfig = str(url+NameProject+'\Confin')
          os.mkdir(str(Createconfig))
          #Create Pages
          CreatePages = str(url+NameProject+'\Pages')
          os.mkdir(str(CreatePages))
          #Create css
          Createcss = str(url+NameProject+'\css')
          os.mkdir(str(Createcss))
          #Create Config-image
          Createimage = str(url+NameProject+'\images')
          os.mkdir(str(Createimage))
          #Create JS
          CreateJS = str(url+NameProject+'\JS')
          os.mkdir(str(CreateJS))
          #Create Scss
          Createscss = str(url+NameProject+'\Scss')
          os.mkdir(str(Createscss))
          #Create Vendor
          CreateVendor = str(url+NameProject+'\VenDor')
          os.mkdir(str(CreateVendor))


          #Create Content For CSS
          Createcss1 = str(url+NameProject+'\css'+'\main.css')
          Createcss2 = open(str(Createcss1), "a")


          #Create Content For JS
          Createjs1 = str(url+NameProject+'\JS'+'\main.js')
          Createjs2 = open(str(Createjs1), "a")


          #Create Content For Scss
          Createscss1 = str(url+NameProject+'\Scss'+'\_base.scss')
          Createscss2 = open(str(Createscss1), "a")

          Createscss3 = str(url+NameProject+'\Scss'+'\_components.scss')
          Createscss4 = open(str(Createscss3), "a")

          Createscss5 = str(url+NameProject+'\Scss'+'\_layouts.scss')
          Createscss6 = open(str(Createscss5), "a")

          Createscss7 = str(url+NameProject+'\Scss'+'\main.scss')
          Createscss8 = open(str(Createscss7), "a")





    if  mainroot == 'open dexs':
          #Project Container Start Project
          #Project For Creator Web Project Framwork

          #Importing Programm
          import sys
          import os
          import time
          import platform

          #Color
          class Color:
               CYAN = '\033[96m'
               BLUE = '\033[94m'
               GREEN = '\033[92m'
               YELLOW = '\033[93m'
               RED = '\033[91m'
               #---END COLOR PRIGRAM
               BOLD = '\033[1m'
               UNDER = '\033[4m'
               END = '\033[0m'

          #Logo and Content for Run
          print('  Dexs Framwork                      ')
          print('  Verssion 1.0.0                         ')
          print('  Creator Aryia-Behroziuan               ')
          print('  web aryia-behroziuan.github.io/codedoxs')
          print()

          Version = '1.0.0'

          #Programm
          #Input Data For Programm
          url = input('[01] Enter URL(Full) New Project:')
          NameProject = input('[02] Enter Name New Project:')
          Document =  input('[03] Enter Document Project:')

          #Create Project
          Createfile = str(url+NameProject)
          os.mkdir(str(Createfile))

          #Create index File
          Create1 = str(url+NameProject+'\[01]_DataCollection_')
          new = str(url+NameProject+'\[01]_DataCollection_'+'\_Result.txt')
          new1 = str(url+NameProject+'\[01]_DataCollection_'+'\Mental-questions.txt')
          os.mkdir(str(Create1))
          open(str(new), "a")
          open(str(new1), "a")

          Create2 = str(url+NameProject+'\[02]_Select-Type-Attack_')
          new2 = str(url+NameProject+'\[02]_Select-Type-Attack_'+'\_Result.txt')
          new3 = str(url+NameProject+'\[02]_Select-Type-Attack_'+'\Mental-questions.txt')
          os.mkdir(str(Create2))
          open(str(new2), "a")
          open(str(new3), "a")

          Create3 = str(url+NameProject+'\[03]_Scan-and-review_')
          new4 = str(url+NameProject+'\[03]_Scan-and-review_'+'\_Result.txt')
          new5 = str(url+NameProject+'\[03]_Scan-and-review_'+'\Mental-questions.txt')
          os.mkdir(str(Create3))
          open(str(new4), "a")
          open(str(new5), "a")

          Create4 = str(url+NameProject+'\[04]_Scan-and-review_')
          new6 = str(url+NameProject+'\[04]_Scan-and-review_'+'\_Result.txt')
          new7 = str(url+NameProject+'\[04]_Scan-and-review_'+'\Mental-questions.txt')
          os.mkdir(str(Create4))
          open(str(new6), "a")
          open(str(new7), "a")

          Create5 = str(url+NameProject+'\[05]_Get-access_')
          new8 = str(url+NameProject+'\[05]_Get-access_'+'\_Result.txt')
          new9 = str(url+NameProject+'\[05]_Get-access_'+'\Mental-questions.txt')
          os.mkdir(str(Create5))
          open(str(new8), "a")
          open(str(new9), "a")

          Create6 = str(url+NameProject+'\[06]_Maintain-access_')
          new10 = str(url+NameProject+'\[06]_Maintain-access_'+'\_Result.txt')
          new11 = str(url+NameProject+'\[06]_Maintain-access_'+'\Mental-questions.txt')
          os.mkdir(str(Create6))
          open(str(new10), "a")
          open(str(new11), "a")

          Create7 = str(url+NameProject+'\[07]_analyze_')
          new12 = str(url+NameProject+'\[07]_analyze_'+'\_Result.txt')
          new13 = str(url+NameProject+'\[07]_analyze_'+'\Mental-questions.txt')
          os.mkdir(str(Create7))
          open(str(new12), "a")
          open(str(new13), "a")

          Create8 = str(url+NameProject+'\[08]_Security_')
          new14 = str(url+NameProject+'\[08]_Security_'+'\_Result.txt')
          new15 = str(url+NameProject+'\[08]_Security_'+'\Mental-questions.txt')
          os.mkdir(str(Create8))
          open(str(new14), "a")
          open(str(new15), "a")

          Createurls = str(url+NameProject+'\_URL_.html')
          mainurls = open(str(Createurls), "a")
          mainurls.write("Document URL Web Print URLS WebPage: Locslhost")

          #Create Document Project
          Createindex = str(url+NameProject+'\Document.txt')
          maindocument = open(str(Createindex), "a")
          maindocument.write("Document Project Dats Set")
          maindocument.write("\n")
          maindocument.write("\n")
          maindocument.write("DataSet={")
          maindocument.write("\n      Name:"+NameProject+',')
          maindocument.write("\n      URL:"+url+' Localhost'+',')
          maindocument.write("\n      Document:"+Document+',')

          time = time.localtime()
          year = str(time.tm_year)
          manth = str(time.tm_mon)
          day = str(time.tm_mday)


          maindocument.write("\n      Year:"+year+',')
          maindocument.write("\n      creation project:"+manth+'/'+day+'/'+year+',')


          namesys = str(platform.node())
          sys = str(platform.platform())
          v_python = str(platform.python_build())
          compayler = str(platform.python_compiler())
          platform1 = str(platform.release())
          system = str(platform.system())
          datasys = str(platform.uname())

          maindocument.write("\n      Creator:"+namesys+',')
          maindocument.write("\n      Version:"+v_python+',')
          maindocument.write("\n      Compiler:"+compayler+',')
          maindocument.write("\n      Platform:"+platform1+',')
          maindocument.write("\n      System:"+system+platform1+',')
          maindocument.write("\n      Data System:"+datasys+',')
          maindocument.write("\n}")
          maindocument.write("\n")
          maindocument.write("Dexs Version={")
          maindocument.write("\n      Version:"+Version+',')
          maindocument.write("\n      Framwork:"+'Dexs'+',')
          maindocument.write("\n      Programmer CodeDoxs:"+'Aryia-Behroziaun'+',')
          maindocument.write("\n      Dexs-Web:"+'http://aryia-behroziaun.github.io/dexs/'+',')
          maindocument.write("\n      Aryia-Behroziuan-Web:"+'aryia-behroziaun.github.io/web/'+',')
          maindocument.write("\n}")



    if mainroot == 'open codedoxs doc':
          #####################################################################################
          # CodeDoxs Doc                                                                      #
          # INSTALLER File, Document, Librarys in Python                                      #
          # Programmer Aryia Behroziuan                                                       #
          # Git Programmer: https://github.com/Aryia-Behroziuan                               #
          # Site: https://aryia-behroziuan.github.io/web/                                     # 
          # CodeDoxs: https://aryia-behroziuan.github.io/codedoxs/                            #
          #####################################################################################

          #importing
          import os
          import sys

          # Title Logo
          print('                                         ')
          print('              _      _____      _    _   ')
          print('  ____       | |    | | _ \     \\  //   ')
          print(' / __/ __  __| | __ | || \ \ __  \\//  __')
          print('| |__ /__\/_ | |/__\| ||_/ //__\ //\\ /__')
          print(' \____\__/\__|_|\__ |_|___/ \__///  \\__/')
          print('  CodeDoxs Doc                           ')
          print('  Verssion 1.0.1                         ')
          print('  Creator Aryia-Behroziuan               ')
          print('  web aryia-behroziuan.github.io/web/    ')
          print('  web aryia-behroziuan.github.io/codedoxs/')
          print()


          # Servic
          print('[01 INSTALL] Librarys General writing program')
          print('[02 INSTALL] Librarys Artificial intelligence')
          print('[03 INSTALL] Librarys penetration test')
          print('[04 INSTALL] Librarys Graphic interface GUI')
          print('[05 INSTALL] Librarys Scientific and mathematical')
          print()
          # Select Servic
          Container = input('Enter the desired phone number:')

          # Contorol Programm
          if Container == '1':
               print('====================================================')
               print('These items are installed')
               print('')
               print(
                    '1- Requests. \n    The most famous http library written by Kenneth Reitz.',
                    '\n2- Scrapy. \n    If you are involved in webscraping then this is a must have library for you',
                    '\n3- wxPython. \n    A gui toolkit for python. I have primarily used it in place of tkinter.',
                    '\n4- Pillow. \n    A friendly fork of PIL (Python Imaging Library).',
                    '\n5- SQLAlchemy. \n    A database library. Many love it and many hate it.',
                    '\n6- BeautifulSoup. \n    I know it’s slow but this xml and html parsing library is very useful for beginners.',
                    '\n7- Twisted. \n    The most important tool for any network application developer.',
                    '\n8- NumPy. \n    How can we leave this very important library ? It provides some advance math functionalities to python.',
                    '\n9- SciPy. \n    When we talk about NumPy then we have to talk about scipy.',
                    '\n10- matplotlib. \n    A numerical plotting library. It is very useful for any data scientist or any data analyzer.'
               )
               print()
               con = input('Do you agree with the installation of these items? Y/n:')
               if con == 'y':
                    print('=======================')
                    print('CodeDoxs Doc INSTALLING')
                    print()
                    os.system('pip install Requests')
                    print()
                    print('===INSTALLED [Requests]===')
                    os.system('pip install Scrapy')
                    print()
                    print('===INSTALLED [Scrapy]===')
                    os.system('pip install wxPython')
                    print()
                    print('===INSTALLED [wxPython]===')
                    os.system('pip install Pillow')
                    print()
                    print('===INSTALLED [Pillow]===')
                    os.system('pip install SQLAlchemy')
                    print()
                    print('===INSTALLED [SQLAlchemy]===')
                    os.system('pip install BeautifulSoup')
                    print()
                    print('===INSTALLED [BeautifulSoup]===')
                    os.system('pip install Twisted')
                    print()
                    print('===INSTALLED [Twisted]===')
                    os.system('pip install NumPy')
                    print()
                    print('===INSTALLED [NumPy]===')
                    os.system('pip install SciPy')
                    print()
                    print('===INSTALLED [SciPy]===')
                    os.system('pip install matplotlib')
                    print()
                    print('===INSTALLED [matplotlib]===')
                    print()
                    print('Good Luck!')

               
               else:
                    print('Thank you for your trust')

          elif Container == '2':
               print('=======================')
               print('CodeDoxs Doc INSTALLING')
               print()
               print(
                    '===Machine Learning==='
                    '\n1-scikit-learn',
                    '\n2-TensorFlow',
                    '\n3-XGBoost',
                    '\n',
                    '\nNatural Language Processing',
                    '\n5-NLTK',
                    '\n6-spaCy',
                    '\n7-Gensim',
                    '\n'
                    '\n===Neural Networks===',
                    '\n1-FANN',
                    '\n2-ffnet',
                    '\n3-PyTorch',
                    '\n'
                    '\nComputer Vision',
                    '\n1-OpenCV',
                    '\n2-SimpleCV',
                    '\n3-Expert Systems',
                    '\n4-PyCLIPS',
                    '\n5-Experta',
                    '\n',
                    '\nRobotics and Autonomous Vehicles',
                    '\n1-AirSim',
                    '\n2-Carla',
                    '\n3-Bullet',
                    '\n'
               )
               can = input('Do you agree with the installation of these items? Y/n:')
               if can == 'y':
                    print('=======================')
                    print('=====INSTALLING Machine Learning Librarys=====')
                    print()
                    os.system('pip install scikit-learn')
                    print()
                    print('===INSTALLED [scikit-learn]===')
                    os.system('pip install TensorFlow')
                    print()
                    print('===INSTALLED [TensorFlow]===')
                    os.system('pip install XGBoost')
                    print()
                    print('===INSTALLED [XGBoost]===')
                    print()
                    print('=====INSTALLING Natural Language Processing=====')
                    os.system('pip install nltk')
                    print()
                    print('===INSTALLED [NLTK]===')
                    os.system('pip install ffnet')
                    print()
                    print('===INSTALLED [ffnet]===')
                    os.system('pip install PyTorch')
                    print()
                    print('===INSTALLED [PyTorch]===')
                    print()
                    print('=====INSTALLING Computer Vision=====')
                    os.system('pip install OpenCV')
                    print()
                    print('===INSTALLED [OpenCV]===')
                    print()
                    os.system('pip install SimpleCV')
                    print()
                    print('===INSTALLED [SimpleCV]===')
                    print()
                    os.system('pip install Expert Systems')
                    print()
                    print('===INSTALLED [Expert Systems]===')
                    print()
                    os.system('pip install PyCLIPS')
                    print()
                    print('===INSTALLED [PyCLIPS]===')
                    print()
                    os.system('pip install Experta')
                    print()
                    print('===INSTALLED [Experta]===')
                    print()
                    print('=====INSTALLING  Neural Networks Librarys=====')
                    print()
                    os.system('pip install FANN')
                    print()
                    print('===INSTALLED [FANN]===')
                    print()
                    os.system('pip install ffnet')
                    print()
                    print('===INSTALLED [ffnet]===')
                    print()
                    os.system('pip install PyTorch')
                    print()
                    print('===INSTALLED [PyTorch]===')
                    print()
                    print('=====INSTALLING Robotics and Autonomous Vehicles=====')
                    print()
                    os.system('pip install AirSim')
                    print()
                    print('===INSTALLED [AirSim]===')
                    os.system('pip install Carla')
                    print()
                    print('===INSTALLED [Carla]===')
                    os.system('pip install Bullet')
                    print()
                    print('===INSTALLED [Bullet]===')  
                    print()
                    print('Good Luck!')
                                   
               else:
                   print('Thank you for your trust')                                 

          elif Container == '3':
               print('=======================')
               print('CodeDoxs Doc INSTALLING')
               print()
               print(
                    '=====Network=====',
                    '\n1-Scapy',
                    '\n2-pypcap',
                    '\n3-libdnet',
                    '\n',
                    '\n=Debugging and Reverse Engineering=',
                    '\n1-Paimei',
                    '\n2-IDAPython',
                    '\n',
                    '\n===Fuzzing===',
                    '\n1-Sulley',
                    '\n2-Powerfuzzer',
                    '\n',
                    '\n===Web===',
                    '\n1-Requests',
                    '\n2-HTTPie',
                    '\n3-lxml',
                    '\n',
               )
               cont = input('Do you agree with the installation of these items? Y/n:')
               if cont == 'y':
                    print('=======================')
                    print('=====INSTALLING Network Librarys=====')
                    print()
                    os.system('pip install Scapy')
                    print()
                    print('===INSTALLED [Scapy]===')
                    os.system('pip install pypcap')
                    print()
                    print('===INSTALLED [pypcap]===')
                    os.system('pip install libdnet')
                    print()
                    print('===INSTALLED [libdnet]===')
                    print()
                    print('==INSTALLING Debugging and Reverse Engineering==')
                    print()
                    os.system('pip install Paimei')
                    print()
                    print('===INSTALLED [Paimei]===')
                    os.system('pip install IDAPython')
                    print()
                    print('===INSTALLED [IDAPython]===')
                    print()
                    print('=====INSTALLED Fuzzing=====')
                    print()
                    os.system('pip install Sulley')
                    print()
                    print('===INSTALLED [Sulley]===')
                    print()
                    os.system('pip install Powerfuzzer')
                    print()
                    print('===INSTALLED [Powerfuzzer]===')
                    print()
                    print('===INSTALLING Web Librarys===')
                    print()
                    os.system('pip install Requests')
                    print()
                    print('===INSTALLED [Requests]===')
                    print()
                    os.system('pip install HTTPie')
                    print()
                    print('===INSTALLED [HTTPie]===')
                    print()
                    os.system('pip install lxml')
                    print()
                    print('===INSTALLED [lxml]===')            
                    print()
                    print('Good Luck!')
               else:
                    print('Thank you for your trust') 




          elif Container == '4':
               print('==================')
               print('===INSTALLING GUI Librarys===')
               print()
               print(
                    'GUI Librarys',
                    '\n1-Tkinter',
                    '\n2-pyqt5',
                    '\n3-pyside2',
                    '\n'
               )
               cont1 = input('Do you agree with the installation of these items? Y/n:')
               if cont1 == 'y':
                    print('===INSTALLING GUI Library===')
                    print()
                    os.system('pip install tkinter')
                    print()
                    print('===INSTALLED [Tkinter]===')
                    print()
                    os.system('pip install pyqt5-tools')
                    print()
                    print('===INSTALLED [PyQt5]===')
                    print()
                    os.system('pip install pyside2')
                    print()
                    print('===INSTALLED [PySide2]===')
                    print()
                    print('Good Luck!')
               else:
                    print('Thank you for your trust') 


          elif Container == '5':
               print('=======================')
               print('CodeDoxs Doc INSTALLING')
               print()
               print(
                    '===Machine Learning==='
                    '\n1-scikit-learn',
                    '\n2-TensorFlow',
                    '\n3-XGBoost',
                    '\n',
                    '\nNatural Language Processing',
                    '\n5-NLTK',
                    '\n6-spaCy',
                    '\n7-Gensim',
                    '\n'
                    '\n===Neural Networks===',
                    '\n1-FANN',
                    '\n2-ffnet',
                    '\n3-PyTorch',
                    '\n'
                    '\nComputer Vision',
                    '\n1-OpenCV',
                    '\n2-SimpleCV',
                    '\n3-Expert Systems',
                    '\n4-PyCLIPS',
                    '\n5-Experta',
                    '\n',
                    '\nRobotics and Autonomous Vehicles',
                    '\n1-AirSim',
                    '\n2-Carla',
                    '\n3-Bullet',
                    '\n'
               )
               can = input('Do you agree with the installation of these items? Y/n:')
               if can == 'y':
                    print('=======================')
                    print('=====INSTALLING Machine Learning Librarys=====')
                    print()
                    os.system('pip install scikit-learn')
                    print()
                    print('===INSTALLED [scikit-learn]===')
                    os.system('pip install TensorFlow')
                    print()
                    print('===INSTALLED [TensorFlow]===')
                    os.system('pip install XGBoost')
                    print()
                    print('===INSTALLED [XGBoost]===')
                    print()
                    print('=====INSTALLING Natural Language Processing=====')
                    os.system('pip install nltk')
                    print()
                    print('===INSTALLED [NLTK]===')
                    os.system('pip install ffnet')
                    print()
                    print('===INSTALLED [ffnet]===')
                    os.system('pip install PyTorch')
                    print()
                    print('===INSTALLED [PyTorch]===')
                    print()
                    print('=====INSTALLING Computer Vision=====')
                    os.system('pip install OpenCV')
                    print()
                    print('===INSTALLED [OpenCV]===')
                    print()
                    os.system('pip install SimpleCV')
                    print()
                    print('===INSTALLED [SimpleCV]===')
                    print()
                    os.system('pip install Expert Systems')
                    print()
                    print('===INSTALLED [Expert Systems]===')
                    print()
                    os.system('pip install PyCLIPS')
                    print()
                    print('===INSTALLED [PyCLIPS]===')
                    print()
                    os.system('pip install Experta')
                    print()
                    print('===INSTALLED [Experta]===')
                    print()
                    print('=====INSTALLING  Neural Networks Librarys=====')
                    print()
                    os.system('pip install FANN')
                    print()
                    print('===INSTALLED [FANN]===')
                    print()
                    os.system('pip install ffnet')
                    print()
                    print('===INSTALLED [ffnet]===')
                    print()
                    os.system('pip install PyTorch')
                    print()
                    print('===INSTALLED [PyTorch]===')
                    print()
                    print('=====INSTALLING Robotics and Autonomous Vehicles=====')
                    print()
                    os.system('pip install AirSim')
                    print()
                    print('===INSTALLED [AirSim]===')
                    os.system('pip install Carla')
                    print()
                    print('===INSTALLED [Carla]===')
                    os.system('pip install Bullet')
                    print()
                    print('===INSTALLED [Bullet]===')  
                    print()
                    print('Good Luck!')
                                   
               else:
                    print('Thank you for your trust')  




          else:
               print('Sorry, we can not do that')              




    if mainroot == "exit":
          break
          print(x)
