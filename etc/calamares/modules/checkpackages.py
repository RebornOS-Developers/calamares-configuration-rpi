#!/usr/bin/env python3

import subprocess
import yaml
from typing import Optional, Union, Dict, List

FILEPATH: str = "packagechooser_DE.conf"

yaml_dict: Optional[Dict] = None
with open(FILEPATH, "r") as original_file:
    file_text: str = ""
    try:
        file_text = original_file.read().replace("\t", "  ")
        yaml_dict = yaml.safe_load(file_text)  
    except:
        file_text = "\n".join(
            [
                "dummy:",
                file_text
            ]
        )
        yaml_dict = yaml.safe_load(file_text)

def pick_out_packages(item: Union[Dict, List, str], cumulative_package_list: List[str]):
    if isinstance(item, dict):
        for key in item: 
            if key == "packages":
                for package in item["packages"]:
                    # If package is a dict consisting of name: <package_name> and description: <package_description>
                    if isinstance(package, dict):
                        # Verify again that the "name" key is present in the package dict
                        if "name" in package:                            
                            if package["name"] is not None:
                                # Get the value pertaining to the "name" key in the package dict and add it to the package list
                                cumulative_package_list.append(package["name"])
                    # If package is directly a string, not a dict with name: or description: keys
                    elif isinstance(package, str):
                        # Since package here is a string, add it to the package list
                        cumulative_package_list.append(package)
            else:
                pick_out_packages(item= item[key], cumulative_package_list= cumulative_package_list)
    elif isinstance(item, list):
        for list_item in item:
            pick_out_packages(item= list_item, cumulative_package_list= cumulative_package_list)

cumulative_package_list: list[str] = []
if yaml_dict is not None: 
    pick_out_packages(item= yaml_dict, cumulative_package_list= cumulative_package_list)

cumulative_package_list = list(
    sorted(
        set(cumulative_package_list)
    )
)

# print("The cumulative package list is: \n", cumulative_package_list)
avalpkg = subprocess.check_output(["pacman", "-Ssq"]).decode("utf-8").split("\n")
for package in cumulative_package_list:
    
    if not package in avalpkg:
        with open("./error.txt","a") as error_file:
            error_file.write(package + "\n")
