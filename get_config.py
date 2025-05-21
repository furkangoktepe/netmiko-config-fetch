from netmiko import ConnectHandler

# Device connection details
device = {
    'device_type': '',      # e.g., 'cisco_ios', 'arista_eos', etc.
    'host': '',             # IP address of the IOSv device
    'username': '',
    'password': '',
    'secret': ''            # Enable password, if required
}

try:
    print(" Establishing SSH connection...")
    connection = ConnectHandler(**device)
    connection.enable()

    print("\n Running 'show version'...")
    version_output = connection.send_command("show version")
    print(version_output)

    print("\n Running 'show ip interface brief'...")
    interfaces_output = connection.send_command("show ip interface brief")
    print(interfaces_output)

    connection.disconnect()
    print("\n Operation completed successfully.")

except Exception as error:
    print(f" An error occurred: {error}")

