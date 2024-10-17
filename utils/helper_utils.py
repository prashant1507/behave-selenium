import json
import subprocess
import os
import shutil

from helpers.constants.framework_constants import FrameworkConstants as Fc

def clean_up():
    details = read_file(Fc.details)
    if os.path.exists(Fc.reports_parent_dir) and details["delete_old_reports"]:
        dir_structure = [Fc.allure_json_dir, Fc.allure_html_dir, Fc.logs_dir, Fc.screenshots_dir]
        for subdir in dir_structure:
            if os.path.exists(subdir):
                shutil.rmtree(subdir)

def execute_command(command):
    return subprocess.run(str(command).split(" "), capture_output=True, text=True, check=True)

def create_dir(folder):
    dir_to_create = os.path.abspath(folder)
    if not os.path.exists(dir_to_create):
        os.makedirs(dir_to_create)
    return dir_to_create

def read_file(path):
    with open(path, "r") as f:
        data = json.load(f)
    return data