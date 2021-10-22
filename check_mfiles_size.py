#!/usr/bin/python
# coding: utf-8

""""


███╗   ██╗ █████╗  ██████╗ ██╗ ██████╗ ███████╗
████╗  ██║██╔══██╗██╔════╝ ██║██╔═══██╗██╔════╝
██╔██╗ ██║███████║██║  ███╗██║██║   ██║███████╗
██║╚██╗██║██╔══██║██║   ██║██║██║   ██║╚════██║
██║ ╚████║██║  ██║╚██████╔╝██║╚██████╔╝███████║
╚═╝  ╚═══╝╚═╝  ╚═╝ ╚═════╝ ╚═╝ ╚═════╝ ╚══════╝
                        check_mfiles_size v1.0                                               


DESCRIPTION
=============
The purpose of the script is to check the size of several files according to a baseline that contains the path, threshold sizes for warning and critical alerts.

INPUTS
=======
A simple file including per line the file path and threshold sizes for warnign and critical alerts separated by a ";"

exemple : 

/var/log/my_log;my_warn_threshold;my_crit_threshold

/var/log/my_log_1;1500;1700
/var/log/my_log_2;1800;2000


COMMAND
========

Run the script with the baseline path as argument

exemple : 
./check_mfiles_size.py my_baseline_path


NOTES
======

Written by: Christophe Pelichet (cpelichet@protonmail.com)

Find me on: 

* LinkedIn:     https://linkedin.com/in/christophepelichet
* Github:       https://github.com/ChristophePelichet

Change Log 
v1.0 - 22/10/2021 - Initial version

"""
###############
### Modules ###
###############
import os
import sys

#################
### ARGUMENTS ###
#################
my_baseline = sys.argv[1]

################################################################
######################### START SCRIPT #########################
################################################################

# Test file_path variable if exist
if os.path.exists(my_baseline):
    with open(my_baseline, 'r+') as f:

        # Data processins , start loop
        for line in f.readlines():

            # Strip line    
            strip_line = line.strip()

            # Split line
            split_line = strip_line.split(';', 3)

            # Getting Variables
            my_file_path = str(split_line[0])
            my_file_warn = int(split_line[1])
            my_file_crit = int(split_line[2])

            if os.path.exists(my_file_path):

                # Getting file size in bytes
                my_file_in_bytes = os.stat(my_file_path).st_size

                 # Convert size in byte to Mb
                my_file_in_mb = my_file_in_bytes/(1024*1024)

                # Result
                if my_file_in_mb > my_file_crit:
                    print("Critical - " + my_file_path + " is too biger !! " + "Size : " + str(my_file_in_mb) + "Mb")
                    sys.exit(2)
                elif my_file_in_mb >= my_file_warn and my_file_in_mb < my_file_crit:
                    print("Warning - " + my_file_path + "is near to the critical thresold " + str(my_file_in_mb) + "Mb")
                    sys.exit(1)


        # If not critical or warning            
        print("OK - All files is ok")
        sys.exit(0)

else:
    print("Critical - No data  file found")

##############################################################
####################### END SCRIPT ###########################
##############################################################
