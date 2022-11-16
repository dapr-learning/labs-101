import subprocess


def execute(cmd: str) -> str:
    """Execute a command and return the output."""
    return subprocess.check_output(cmd, shell=True, stderr=subprocess.PIPE).decode("utf-8")


def execute_async(cmd: str) -> None:
    """Execute a command asynchronously."""
    subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE,
                     stderr=subprocess.DEVNULL)
