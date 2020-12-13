import os
choice = input('[+] to install windows313 tools press (Y) to uninstall press (N) >> ')
run = os.system
if str(choice) =='Y' or str(choice)=='y':

    run('chmod 777 windows313.py')
    run('mkdir /usr/share/LebanonCyber')
    run('cp windows313.py /usr/share/LebanonCyber/windows313.py')

    cmnd=(' #! /bin/sh \n exec python3 /usr/share/LebanonCyber/windows313.py "$@"')
    with open('/usr/bin/LebanonCyber')as file:
        file.write(cmnd)
    run('chmod +x /usr/bin/aut & chmod +x /usr/share/LebanonCyber/windows313.py')
    print('''\n\ncongratulation Ip Changer tools from windows313 is installed successfully \nfrom now just type \x1b[6;30;42mLebanonCyber\x1b[0m in terminal ''')
if str(choice)=='N' or str(choice)=='n':
    run('rm -r /usr/share/LebanonCyber ')
    run('rm /usr/bin/LebanonCyber ')
    print('[!] now Ip changer tools from windows313 has been removed successfully')
