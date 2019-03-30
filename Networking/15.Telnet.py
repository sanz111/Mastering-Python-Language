import telnetlib, getpass

# user = getpass.getuser()
user = "firojvsfacebook@gmail.com"
pw = "mummy14343ver"
#pw = getpass.getpass()
host = "172.30.42.127"

t = telnetlib.Telnet(host)

try:
    t.read_until("login: ")
    t.write(user + '\n')
    t.read_until("Password: ")
    t.write(pw + '\n')

    t.read_until("~ $ ")
    t.write("ls\n")
    print(t.read_until("~ $ "))
except Exception as e:
    print(e)
finally:
    t.close()