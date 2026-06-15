import subprocess

try:
    result = subprocess.run(
        ["docker", "--version"],
        capture_output=True,
        text=True,
        check=True
    )

    print("Docker Installed Successfully")
    print(result.stdout)

except Exception as e:
    print("Docker Not Found")
    print(e)

