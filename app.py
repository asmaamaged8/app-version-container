import sys

def print_version():
    """Print the current application version and exit."""
    version = "v0.0.1"
    print (f"current app verion is: {version}")
    sys.exit(0)
    

if __name__ == "__main__":
    print_version()