import smtplib

#get commandline args:
def prompt(prompt):
    return input(prompt).strip()

#set the to/from addresses:
from_addr = prompt("From: ")
to_addr  = prompt("To: ").split()
print("Enter the message, terminating with ^D ")

message = ("From: %s\r\nTo: %s\r\n\r\n"
       % (from_addr, ", ".join(to_addr)))

while True:
    try:
        line = input()
    except EOFError:
        break
    if not line:
        break
    message = message + line

print("The message length => ", len(message))

#serves the mail from localhost, terminates the server.
mail_server = smtplib.SMTP('localhost')
mail_server.set_debuglevel(1)
mail_server.sendmail(from_addr, to_addr, message)
mail_server.quit()
