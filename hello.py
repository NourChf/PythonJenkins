import importlib.util
import sys

def install_package(package):
    """
    Function to install Python package using pip.
    """
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def check_and_install_jenkins_module():
    """
    Function to check if 'jenkins' module is installed, and install if not.
    """
    package_name = 'jenkins'
    spec = importlib.util.find_spec(package_name)
    if spec is None:
        print(f"The '{package_name}' module is not installed.")
        choice = input(f"Do you want to install '{package_name}' now? (y/n): ").lower()
        if choice == 'y':
            install_package(package_name)
        else:
            print(f"Please install '{package_name}' manually to proceed.")
            sys.exit(1)

    # Module import after installation check
    import jenkins
    from jenkins import JenkinsException

    # Continue with your script using the 'jenkins' module
    # Example usage:
    jenkins_server_url = "https://jenkins.artibedded.com/"
    jenkins_access_token = "11b42187f5222050e03da11baea3bf4e44"
    job_name = "build"

    try:
        server = jenkins.Jenkins(jenkins_server_url, username='api_token', password=jenkins_access_token)

        if server.job_exists(job_name):
            server.build_job(job_name)
            print(f"Build triggered for job '{job_name}'.")
        else:
            print(f"Error: Job '{job_name}' does not exist.")

    except JenkinsException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    check_and_install_jenkins_module()
