import datetime
from helpers.constants.framework_constants import FrameworkConstants as Fc
from utils.docker_compose_action import start_docker_compose, stop_docker_compose
from utils.logger import get_logs
from utils.reporting.screenshots import attach_screenshot_in_report
from utils.browser_utils import prepare_browser
from utils.helper_utils import clean_up, create_dir
from utils.reporting.generate_report import generate_allure_report


def before_all(context):
    clean_up()
    current_time = datetime.datetime.now()
    file_name = current_time.strftime("%d_%m_%y-%H_%M_%S_%f")[:-3]

    dir_structure = [Fc.reports_parent_dir, Fc.allure_json_dir, Fc.allure_html_dir, Fc.logs_dir, Fc.json_dir, Fc.pretty_dir, Fc.rerun_dir, Fc.screenshots_dir]
    for subdir in dir_structure:
        create_dir(subdir)
    global logger, details
    logger = get_logs(f"{Fc.logs_dir}/{file_name}.txt")
    start_docker_compose(logger)


def before_feature(context, feature):
    logger.info(f"Feature file: {feature.filename}")
    logger.info(f"Number of Scenarios: {len(feature.scenarios)}")
    formatted_tags = " ".join([f"@{tag}" for tag in feature.tags])
    if formatted_tags:
        logger.info(f"{formatted_tags}")
    logger.info(f"Feature: {feature.name}")
    prepare_browser(context)


def before_scenario(context, scenario):
    formatted_tags = " ".join([f"@{tag}" for tag in scenario.tags])
    if formatted_tags:
        logger.info(f"{formatted_tags}")
    logger.info(f"Scenario: {scenario.name}")

    if scenario.feature.background:
        background = scenario.feature.background
        for step in background.steps:
            logger.info(f"{step.keyword} {step.name}")

    for step in scenario.steps:
        logger.info(f"{step.keyword} {step.name}")


def after_step(context, step):
    current_time = datetime.datetime.now()
    file_name = current_time.strftime("%d_%m_%y-%H_%M_%S_%f")[:-3]
    context.driver.get_screenshot_as_file(f"{Fc.screenshots_dir}/{file_name}.png")
    attach_screenshot_in_report(f"{Fc.screenshots_dir}/{file_name}.png")


def after_scenario(context, scenario):
    logger.info(f"Scenario status: {scenario.status}")


def after_feature(context, feature):
    logger.info(f"Feature Status: {feature.status}")
    context.driver.quit()


def after_all(context):
    try:
        generate_allure_report(logger)
    finally:
        stop_docker_compose(logger)
