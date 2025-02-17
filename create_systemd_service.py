#!/usr/bin/python3
import os
import shutil

def create_service_file(script_path):
    home_dir = os.path.expanduser("~")
    services_dir = os.path.join(home_dir, "services")

    if not os.path.exists(services_dir):
        os.makedirs(services_dir)

    script_name = os.path.basename(script_path)
    destination_path = os.path.join(services_dir, script_name)
    try:
        shutil.copy2(script_path, destination_path)
        print(f"Script copied to: {destination_path}")
    except Exception as e:
        print(f"Error copying script: {e}")
        return None

    script_name_no_ext = os.path.splitext(script_name)[0]
    service_name = f"{script_name_no_ext}.service"
    service_file_path = os.path.join("/etc/systemd/system/", service_name)

    file_extension = os.path.splitext(script_name)[1].lower()
    if file_extension == ".py":
        exec_start = f"/usr/bin/python3 {destination_path}"
    elif file_extension == ".sh":
        exec_start = f"/bin/bash {destination_path}"
    else:
        print("Error: Unsupported file type. Only .py and .sh files are supported.")
        return None

    service_content = f"""
[Unit]
Description=Service for {script_name_no_ext}
After=multi-user.target

[Service]
Type=simple
WorkingDirectory={services_dir}
ExecStart={exec_start}
Restart=on-failure

[Install]
WantedBy=multi-user.target
"""

    try:
        with open(service_file_path, "w") as f:
            f.write(service_content)
        print(f"Service file created at: {service_file_path}")
    except Exception as e:
        print(f"Error creating service file: {e}")
        return None

    return service_name


def enable_and_start_service(service_name):
    try:
        os.system("sudo systemctl daemon-reload")
        os.system(f"sudo systemctl enable {service_name}")
        os.system(f"sudo systemctl start {service_name}")
        print(f"Service {service_name} enabled and started.")
    except Exception as e:
        print(f"Error enabling and starting service: {e}")


if __name__ == "__main__":
    script_path = input("Enter the absolute path to the Python or Shell script: ")

    if not os.path.exists(script_path):
        print("Error: The specified script path does not exist.")
    else:
        service_name = create_service_file(script_path)
        if service_name:
            enable_and_start_service(service_name)

