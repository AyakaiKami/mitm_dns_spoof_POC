# OS image
FROM ubuntu:22.04

# Update and upgrade
RUN apt-get update
RUN apt-get upgrade

# Add user fool
RUN useradd -s /bin/bash -m fool;

# Make directory for script
RUN mkdir /home/fool/scripts


# Install python3 and libraries
RUN apt-get install python3 -y
RUN apt install python3-pip -y
RUN pip install requests
RUN pip install datetime

# Add script to the docker image
COPY Scripts/script.py /home/fool/scripts/script.py

# Set executable bit 
RUN chmod +x /home/fool/scripts/script.py

# Create output file
RUN touch /home/fool/scripts/did_i_get_tricked

# Install crontab
RUN apt install cron

# Start crontab
RUN service cron start 

# Setup cron job
RUN (crontab -l ; echo "* * * * * /home/fool/scripts/script.py >> /home/fool/scripts/did_i_get_tricked") | crontab

# Install curl
RUN apt-get install curl -y