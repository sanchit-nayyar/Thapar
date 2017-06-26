# Thapar

***COMMON FOR ALL OPERATING SYSTEMS***
You need a Python2 installation on your computer, this project uses mechanize which is currently unavailable for Python3

***LINUX USERS***
If you have pip installed and configured, the Linux_init.py file will automatically install the required packages. Otherwise, install the following packages using terminal
  > 1. `python-mechanize`
  > 2. `python-bs4`

These are needed for smooth execution. Please note that python is generally installed on your OS.

Run the Linux_init.py file by typing the following commands in your terminal
  > `python Linux_init.py`

The script shall attempt to install the required packages using pip. If it fails, install the said packages manually
The script shall ask for the Webkiosk Username and Password. Both these shall appear in plain text here, so make sure that you enter this data in a discrete place

Now, you will be using Linux.py file. It has two dependency text files, namely
  > 1. data_webkiosk-thapar.txt
  > 2. history_webkiosk-thapar.txt

Make sure these files are always in the same directory as Linux.py.
Now run the script and relax, you shall be notified whenever a new score is uploaded. You may even add this to autostart on boot


***WINDOWS USERS***
If you have a pip installation **and** Python is installed in the default directory, the Windows_init.py file is configured to install all the required packages.
  > Python Directory: `C:/Python27`
If not, follow the given steps:
  > 1. Open up Command Prompt by right clicking on the start icon
  > 2. Navigate to the Python installation (for a default location type this)
    > `cd C:/Python27`
  > 3. Go to the Scripts folder by typing this
    > cd Scripts
  > 4. Use easy_install.exe to install the required packages
  
      - `easy_install pip`
      
    OR
    
      - `easy_install mechanize`
      
      - `easy_install plyer`
      
      - `easy_install bs4`
  > 5. Now execute the Windows_init.py file
The installation of packages may fail by the init file, ignore those messages. Key in you Webkiosk username and password. Take note that they shall appear in plain text
Now, the required files which are
  > 1. data_webkiosk-thapar.txt
  > 2. history_webkiosk-thapar.txt
shall be created. Make sure that both these files and Windows.py are always in the same directory.

Now, the script is ready for execution. It shall run and check for a new score available every 60 minutes. It will send a notification whenever a new score is uploaded. You might want to add the Windows.py file to your startup folder.

***All Operating Systems***
The data_webkiosk-thapar.txt file shall contain your password for Webkiosk, so don't share this file when sharing the source code of the project. The initialisation files are programmed to automatically create this file as per need.
Your password is not uploaded to any location on the internet except the Thapar Webkiosk.
Please don't change the frequency of checks, as a higher frequency by numerous computers may lead to an unwanted DDoS attack on the webkiosk
