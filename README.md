# hard-drive-serial
How to get hard drive serial using Python

## python code
```python
import subprocess

def get_harddrive_serial():
    try:
        # Get the list of block devices
        result = subprocess.run(['lsblk', '-dn', '-o', 'NAME'], capture_output=True, text=True, check=True)
        devices = result.stdout.strip().split('\n')

        serials = {}

        for device in devices:
            device_path = f'/dev/{device}'
            # Get detailed information for the device
            udevadm_result = subprocess.run(['udevadm', 'info', '--query=all', '--name', device_path],
                                            capture_output=True, text=True, check=True)
            info = udevadm_result.stdout

            # Extract the serial number from the udevadm output
            for line in info.split('\n'):
                if 'ID_SERIAL=' in line:
                    serial = line.split('=')[1].strip()
                    serials[device] = serial
                    break

        return serials

    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        return {}

# Example usage
if __name__ == "__main__":
    serials = get_harddrive_serial()
    for device, serial in serials.items():
        print(f"Device: /dev/{device}, Serial: {serial}")
```
