# This is a sample Python script.

import module_ad    #importing a module/file from same directory
import ad_packages.perception_pkg   # importing a package/file from differnt directory
#import ad_packages.traj_planning.traj_planner # or
from ad_packages.traj_planning.traj_planner import find_traj_fnc    #diffent way to import

# built-in function: There are many built in modules/functions in pythons, can be used by importing as below
import random
print (random)
#help(random)   #documentation regarding any function
print(dir(random))  # shows where it is stored and otherfunctions in the same dir

import sys

#Standard library: developed by individual developers/companies and shared accross. No need to develop if already developed by someonce once
#Standard library is from 3rd party, so need to be installed using pip
#pycharm -> project -> project interpreter -> pip -> + -> seach fpr package -> install eg: pyjokes
#terminal -> pip3 install lib_name          pip3 install --upgrade pip      pip3 list
#Virtual environment

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print("Hi, {0}".format(name))  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
# name is main only in the main script
if __name__ == '__main__':
    print_hi('PyCharm')
    print(module_ad.ad_detection())     #way to call module/file from same directory
    print(ad_packages.perception_pkg.perception_pkg_fnc())  #way to call package/file from diff directory
    print(find_traj_fnc())                                  #differnt way to import and call





# See PyCharm help at https://www.jetbrains.com/help/pycharm/
