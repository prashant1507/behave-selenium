
import os.path


class FrameworkConstants:

    details = os.path.abspath("resources/details.json")
    reports_parent_dir = os.path.abspath("reports")
    allure_json_dir = os.path.abspath(f"{reports_parent_dir}/allure_json")
    allure_html_dir = os.path.abspath(f"{reports_parent_dir}/allure_html")
    # html_dir = os.path.abspath(f"{reports_parent_dir}/html")
    logs_dir = os.path.abspath(f"{reports_parent_dir}/logs")
    json_dir = os.path.abspath(f"{reports_parent_dir}/json")
    pretty_dir = os.path.abspath(f"{reports_parent_dir}/pretty")
    rerun_dir = os.path.abspath(f"{reports_parent_dir}/rerun")
    screenshots_dir = os.path.abspath(f"{reports_parent_dir}/screenshots")

    resources = os.path.abspath("resources")
    docker_compose_file = os.path.abspath("resources/docker-compose.yml")