import subprocess
import optparse

# Initialize the parser
parser = optparse.OptionParser()

# Add command-line options
parser.add_option("-i", "--interface", dest="interface", help="Interface to change MAC address for")
parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address to assign")

# Parse arguments
(options, arguments) = parser.parse_args()

interface = options.interface
new_mac = options.new_mac

# Check if arguments are provided
if not interface or not new_mac:
    parser.error("[-] Please specify both an interface and a new MAC address. Use --help for more info.")
if len(new_mac) <17 :
    new_mac="0"+new_mac
print(f"[+] Changing MAC address for {interface} to {new_mac}")

# Execute commands securely using lists (prevents shell injection)
subprocess.call(["sudo", "ip", "link", "set", interface, "down"])
subprocess.call(["sudo", "ip", "link", "set", interface, "address", new_mac])
subprocess.call(["sudo", "ip", "link", "set", interface, "up"])
address=subprocess.run(["ip", "addr", "show", interface], capture_output=True, text=True)
to_check=address.stdout.split()
done= [True for i in to_check if i.strip()==new_mac]
if done:
    print("mac address has been change to the desired")
else:
    print("mac not changes error")



