# bitcoin_value_predictor
Bitcoin value predictor using machine learning 
This is Bitcion value predictor project using machine learning algorithms.This project uses Random Forest and Decision tree Regressor to predict  the value according to the past Bitcoin proce records contained in bitcoin.csv file uploaded herewith.

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

How to run the application:
1) First make sure that you have Python interpreter installed on your system.If not install and download the same from python.org website.Python3 setup is recomended.
2) If python not installed then run the setup downloaded from the website mentioned above and give necessary permissions(For windows click on allow torun the setup).
3) Click on add python to path so that you can install necessary libraries hasle-free.
4) Once setup sucessful open Command prompt on windows or Terminal on Linux systems and run the  following command.
5) pip3 install numpy
  pip3 install pandas 
  pip3 install sklearn
6) If you are getting error like pip3 was not recognised for windows and pip3 command not found for Linux systems then do following steps:
    a) For Linux run the following commands
      i) Ubuntu based systems:  
          sudo apt install python3-pip
      ii) Fedora or red hat based systems:
          sudo dnf install python3-pip
      iii) Arch Linux based systems:
          sudo pacman -S python3-pip
      please provide password if prompted.
    b) For windows systems.
      i) Run the downloaded setup again and do step mentioned in the step 3) above and contine the installation.If same error pops up kindy restart your system.
7) Now you are ready to run the python file.
8) Open command prompt for windows or terminal for Linux systems.
9) Navigate to the folder where you've downloaded the window.py file by using cd command.(please keep all the downloded files in same folder).
10) Run the follwing command:
  python3 window.py
11) The window will pop up with  alert box and four graphs. The alert box will show you Bitcoin price today.Click on OK and then you will see four graphs represnting the trends in Bitcoin value.
12) If you want to predict the price for tomorrow then click predict button below and enter the today's bitcoin value.
13) After clcking submit the screen refreshes with new dialog box and new graphs representing tomorrow's Bitcoin value.
14) The main big arrow above represents the ups and downs in Bitcoin price and small arrows arround each graph represent the ups and downs for each graph.

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Future work.
1) The predictor can only predict today's and tomorrow's value. but it should predict the future  values beyond tomorrow.
