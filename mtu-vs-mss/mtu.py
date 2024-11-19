import subprocess
import re

def find_mtu(destination):
    def ping(size):
        try:
            output = subprocess.check_output(
                ["ping", destination, "-f", "-l", str(size)],
                stderr=subprocess.STDOUT,
                universal_newlines=True
            )
            return output
        except subprocess.CalledProcessError as e:
            return e.output

    lower_bound = 0
    upper_bound = 1500

    while lower_bound <= upper_bound:
        mid = (lower_bound + upper_bound) // 2
        result = ping(mid)
        if "Packet needs to be fragmented" in result:
            upper_bound = mid - 1
        else:
            lower_bound = mid + 1

    mtu = upper_bound
    return mtu

destination = "8.8.8.8"  # Google's public DNS server
mtu = find_mtu(destination)
print(f"The MTU size is: {mtu}")
