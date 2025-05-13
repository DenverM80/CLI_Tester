from logging import log
import subprocess
from typing import List, Tuple

class RunCmd:
    """
    This class wraps the 'conda' command for common environment and package functionality
    """

    @staticmethod
    def run_cmd(args: List[str]) -> Tuple[str, str, int]:
        """
        Run a shell with the given list of commands and return stdout, stderr, and rc

        Args:
           args (List[str]): List of strings to build the command line string

        Returns:
            Tuple[str, str, int]: A tuple containing stdout, stderr, and the return_code
        """
        log(f"Running [{' '.join(args)}]")
        proc = subprocess.run(args=' '.join(args), text=True, shell=True, capture_output=True)
        return proc.stdout, proc.stderr, proc.returncode

