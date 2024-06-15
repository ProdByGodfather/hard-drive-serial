import cpuinfo

def get_cpu_serial_number():
    try:
        info = cpuinfo.get_cpu_info()
        serial_number = info.get('serial')
        if serial_number:
            return serial_number
        else:
            return "Serial number not found or not available without root access"
    except Exception as e:
        return str(e)

serial_number = get_cpu_serial_number()
print(f"CPU Serial Number: {serial_number}")
