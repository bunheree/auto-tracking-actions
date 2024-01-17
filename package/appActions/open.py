import subprocess

def openApplication(application_path):
    try:
        subprocess.Popen(application_path)
        print(f"Opening {application_path}")
    except Exception as e:
        print(f"Error opening {application_path}: {e}")