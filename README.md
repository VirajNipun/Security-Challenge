# Security-Challenge

Overview

This repository offers a basic but effective firewall log analysis software created in Python for ABC Inc. The script is intended to parse firewall logs produced by both on-premise Linux machines and AWS security groups. The purpose is to enable ABC Inc. identify and react to possible attacks, expand awareness of traffic patterns, improve network security posture, and comply with industry laws surrounding security log monitoring.

Script Usage
Prerequisites
Python 3.x installed on the system.
Running the Script
Clone the repository to your local machine:

bash
Copy code
git clone https://github.com/your-username/firewall-log-analyzer.git
Navigate to the project directory:

bash
Copy code
cd firewall-log-analyzer
Edit the firewall_log_parser.py script:

Update the log_file_path variable with the path to your firewall log file.
Run the script:

bash
Copy code
python firewall_log_parser.py

Script Details

The Python script firewall_log_parser.py leverages regular expressions to parse firewall logs. It differentiates between ALLOW and BLOCK operations, processing each log item appropriately. The processed information is then printed, offering insights into the date, time, protocol, source and destination IP addresses, source and destination ports, size, TCP flags, and extra information.

The script acts as a preliminary tool for ABC Inc. to evaluate firewall logs, letting the security team make educated judgments on network security policies.

Documentation
For a detailed summary report, insights, and recommendations based on the analysis, please refer to the documentation file named 'Security Challenge Report.pdf' in the repository.

Expected Outcome
The script is supposed to analyze sample log files, identify possible dangers, and deliver the information in a relevant fashion. The script's efficacy may be assessed by ABC Inc.'s security team to make required updates to firewall rules and better safeguard the network.

Support
For any questions, issues:

Developer: Viraj Nipun Dissanayake
Email: v99nipun@gmail.com
