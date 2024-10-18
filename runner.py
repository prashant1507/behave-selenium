from pycommons.lang.stringutils import StringUtils
from selenium.webdriver.common.bidi.cdp import logger
from utils.docker_compose_actions import start_docker_compose, stop_docker_compose
from utils.helper_utils import prepare_dirs, execute_command_using_popen
from utils.reporting.generate_report import generate_allure_report
from helpers.constants.framework_constants import FrameworkConstants as Fc



def main():
    process = None
    # Read and print the output line by line
    try:
        prepare_dirs()
        start_docker_compose(logger)
        process = execute_command_using_popen(f"behavex {Fc.features} -c {Fc.conf_behavex} --parallel-processes 2")
        while True:
            output = process.stdout.readline()
            if output == StringUtils.EMPTY and process.poll() is not None:
                break
            if output:
                print(output.strip())
    except KeyboardInterrupt:
        print("Process terminated by user.")
        process.terminate()
    finally:
        generate_allure_report(logger)
        stop_docker_compose(logger)

if __name__ == "__main__":
    main()