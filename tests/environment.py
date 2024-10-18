import datetime

from behavex_images import image_attachments
from behavex_images.image_attachments import AttachmentsCondition
from helpers.constants.framework_constants import FrameworkConstants as Fc
from utils.reporting.logger import get_logs
from utils.reporting.screenshots import attach_screenshot_in_report
from utils.browser_utils import prepare_browser


def before_all(context):
    current_time = datetime.datetime.now()
    file_name = current_time.strftime("%d_%m_%y-%H_%M_%S_%f")[:-3]
    global logger, details
    logger = get_logs(f"{Fc.logs_dir}/{file_name}.txt")
    # start_docker_compose(logger)
    image_attachments.set_attachments_condition(context, AttachmentsCondition.ALWAYS)


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
    image_attachments.attach_image_file(context, f"{Fc.screenshots_dir}/{file_name}.png")
    # image_attachments.attach_image_binary(context, context.driver.get_screenshot_as_png())

def after_scenario(context, scenario):
    logger.info(f"Scenario status: {scenario.status}")


def after_feature(context, feature):
    try:
        logger.info(f"Feature Status: {feature.status}")
    finally:
        context.driver.quit()


# def after_all(context):
#     try:
#         generate_allure_report(logger)
#     finally:
#         stop_docker_compose(logger)
