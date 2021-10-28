# check_mfiles_size

The purpose of the script is to check the size of several files according to a baseline that contains the path, threshold sizes for warning and critical alerts.

## Configuration

A simple file including per line the file path and threshold sizes for warnign and critical alerts separated by a ";"
exemple : 
/var/log/my_log;my_warn_threshold;my_crit_threshold
/var/log/my_log_1;1500;1700
/var/log/my_log_2;1800;2000

## Command

Run the script with the baseline path as argument
exemple : 
./check_mfiles_size.py my_baseline_path


## Installation 

- copy the script in you nagios default script path ( by default /usr/local/nagios/libexec)
- set the permission in the script (exemple : chown root.nagios /usr/local/nagios/libexec/check_mfiles_size)
- create your baseline ( see Configuration chapter)
- set the permission in your baseline ( exemple : chown nagios.nagios my_basline_path)
- add you services in Nagios.
