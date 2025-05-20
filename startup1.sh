#! /bin/bash 
# ============================================================================
pwd
echo " "
echo "----------------------------------------------------"
echo "Do you wish run the startup1 script?"
echo "This script will run the following: "
echo "  Test if there is a rover direcory, create it if not, and cd to the rover direcory, then "
echo "  create a rover_log direcoty, and log the bach and other commands and scripts to a file "
echo "  called rover.log "

echo "----------------------------------------------------"
select yn in "Yes" "No"; do
    case $yn in
        Yes ) 
            echo "----------------------------------------------------"
            echo "Running Rover Log Collection" 
            echo "----------------------------------------------------"
            break;;
        No ) 
            echo "----------------------------------------------------"
            echo "Exiting Without Update" 
            echo "----------------------------------------------------"
            exit;;
    esac
done
cd 
pwd
echo "-------------------------------------------------------"
echo " Uncomment to run update & upgrade "
echo "-------------------------------------------------------"
# sudo apt update
# sudo apt upgrade -y
echo "-------------------------------------------------------"
echo " Checking for Rover Dir in $USER home "
echo "-------------------------------------------------------"
sudo mkdir rover
cd rover
sudo mkdir rover_log
cd rover_log
echo "-------------------------------------------------------"

echo "----------------------------------------------------"
echo "open rover_log.log and log date and time"
echo "----------------------------------------------------"
echo " "
# test if log file is there
mv rover_log.log rover_log.bac.log
sudo touch rover_log.log
echo " "
echo "----------------------------------------------------"
echo "Done Testing For &/or creating the rover_log.log file "
echo "----------------------------------------------------"
echo " "

echo "----------------------------------------------------"
echo "Getting the date & time" | sudo tee -a rover_log.log
echo "----------------------------------------------------" | sudo tee -a rover_log.log
echo " "
sudo date | sudo tee -a rover_log.log
echo " "
echo "----------------------------------------------------" | sudo tee -a rover_log.log
echo "Done getting date & time" | sudo tee -a rover_log.log
echo " " | sudo tee -a rover_log.log

echo "-------------------------------------------------------"
echo "All Done"
