# Auto-Whatsapp
 Whatsapp automation to send messages for many numbers in excel file
 
 This project is based on Eel and electronJs to use electron desktop API . I'm still working on the documentaion of how to edit it. i know it's not that obvious 
 but for now :
 
 1 - Download electron binary and extract it into "electron" folder in the project. 
 
 2 - change electron.py file in eel libirary in your env. for the windows platform to be 
```
 if sys.platform in ['win32', 'win64']:
        # It doesn't work well passing the .bat file to Popen, so we get the actual .exe
        bat_path = os.path.join(os.path.abspath(os.getcwd()),r'electron\electron.exe')
        return os.path.normpath(bat_path)
```

now when you write `python main.py` it will work. 

also working on how to deploy it with pyinstaller. my first release is not the best option for deploy
