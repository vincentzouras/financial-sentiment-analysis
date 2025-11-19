import subprocess
import sys
import pkg_resources

# List of required packages and their recommended versions
REQUIRED_PACKAGES = [
    'requests>=2.28.1',
    'numpy==1.24.4',
    'pandas', # No specific version required
    'yfinance>=0.2.25',
    'scikit-learn>=1.2.2',
    'matplotlib>=3.7.1',
]

def install_and_import(package_list):
    """
    Checks if a list of packages is installed. If not, installs them
    using pip and then attempts to import them.
    """
    print("--- Starting Dependency Check ---")

    # Get a set of installed packages for quick lookup
    installed_packages = {pkg.key for pkg in pkg_resources.working_set}

    for package_spec in package_list:
        # We need the base package name (e.g., 'requests' from 'requests>=2.28.1')
        package_name = pkg_resources.Requirement.parse(package_spec).key

        if package_name in installed_packages:
            print(f"✅ '{package_name}' is already installed.")
        else:
            print(f"⚠️ '{package_name}' not found. Installing now...")
            try:
                # Use subprocess to run the pip install command
                subprocess.check_call([sys.executable, "-m", "pip", "install", package_spec])
                print(f"✅ Successfully installed '{package_spec}'.")
            except subprocess.CalledProcessError as e:
                print(f"❌ Failed to install '{package_spec}'. Error: {e}")
                sys.exit(1) # Exit the script if installation fails

    print("--- All dependencies are checked and installed. ---")


if __name__ == '__main__':
    install_and_import(REQUIRED_PACKAGES)

    # You can now proceed to run your main application logic here
    # Example:
    # from my_project import main
    # main()