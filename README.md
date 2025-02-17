# systemd-service-creator
This project can be used to deploy any python or bash script as a systemd service effortlessly.  
If you have a python or bash script to run during system startup in an autonomous manner, This project minimizes your work.  

## Execution steps:
1. Get the absolute path of the python/bash script.  
2. Run the below command:  
**sudo ./create_systemd_service.py**  
3. You will be prompted to enter the absolute location of your python script.  
4. After entering the path. Booooommmmmmm, your python script is deployed as a service.  
And you dont have to instantiate everytime after system reboot.  

## Removing the service:
If you like to remove the service file:  
1. Stop the running service  
**sudo systemctl stop <service-name.service>**  
2. Delete the service file  
**sudo rm <service-name.service>**  
