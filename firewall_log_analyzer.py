import re

# Path to the firewall log file
log_file_path = r"C:\Users\User\Desktop\Security_challenge\firewalllog_2023_11_7.log"  

def parse_firewall_log():
    # Open the log file for reading
    with open(log_file_path, 'r') as f:
        for line in f:
            # Check if the line is the header, and skip it
            match = re.match(r'^# Fields: Date \| Time \| Action \| Protocol \| Src IP \| Dst IP \| Src Port \| Dst Port \| Size \| TCP Flags \| Info$', line)
            if match:
                continue  # Skip the header line

            # Use regex to extract fields from the log line
            match = re.match(r'^(\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}:\d{2}) (ALLOW|BLOCK) (\w+) (\d+\.\d+\.\d+\.\d+) (\d+\.\d+\.\d+\.\d+) (\d+) (\d+) (\d+) (-) (-)$', line)
            if match:
                # Unpack matched groups into variables
                date, time, action, protocol, src_ip, dst_ip, src_port, dst_port, size, tcp_flags, info = match.groups()

                # Process each log entry based on action type
                if action == 'ALLOW':
                    process_allowed_log_entry(date, time, protocol, src_ip, dst_ip, src_port, dst_port, size, tcp_flags, info)
                elif action == 'BLOCK':
                    process_blocked_log_entry(date, time, protocol, src_ip, dst_ip, src_port, dst_port, size, tcp_flags, info)
                else:
                    print('Invalid action:', action)

def process_allowed_log_entry(date, time, protocol, src_ip, dst_ip, src_port, dst_port, size, tcp_flags, info):
    # Process allowed log entries
    print('Allowed log entry:')
    print('Date:', date)
    print('Time:', time)
    print('Protocol:', protocol)
    print('Source IP:', src_ip)
    print('Destination IP:', dst_ip)
    print('Source Port:', src_port)
    print('Destination Port:', dst_port)
    print('Size:', size)
    print('TCP Flags:', tcp_flags)
    print('Info:', info)
    print('-' * 80)

def process_blocked_log_entry(date, time, protocol, src_ip, dst_ip, src_port, dst_port, size, tcp_flags, info):
    # Process blocked log entries
    print('Blocked log entry:')
    print('Date:', date)
    print('Time:', time)
    print('Protocol:', protocol)
    print('Source IP:', src_ip)
    print('Destination IP:', dst_ip)
    print('Source Port:', src_port)
    print('Destination Port:', dst_port)
    print('Size:', size)
    print('TCP Flags:', tcp_flags)
    print('Info:', info)
    print('-' * 80)

# Entry point of the script
if __name__ == '__main__':
    # Call the function to parse the firewall log
    parse_firewall_log()
