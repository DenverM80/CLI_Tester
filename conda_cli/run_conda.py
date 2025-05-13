from typing import List, Tuple
from run_cmd.run_cmd import RunCmd


class RunConda:
    """
    This class wraps the 'conda' command for common environment and package functionality
    """
    @staticmethod
    def create_env(env_name: str, pkgs: List[str], version: str=None) -> Tuple[str, str, int]:
        """
        Create a conda environment with the given packages

        Args:
           env_name (str): Name of environment to create
           pkgs (List[str]): List of packages to install
           version (str): Major and minor version of python to install

        Returns:
            Tuple[str, str, int]: A tuple containing stdout, stderr, and the return_code
        """
        params = ["conda", "create", "-y", "-n", env_name, f"{' '.join(pkgs)}"]
        if version:
            params.append(f"python={version}")

        return RunCmd.run_cmd(params)

    @staticmethod
    def activate_env(env_name: str) -> Tuple[str, str, int]:
        """
        Activate a conda environment

        Args:
           env_name (str): Name of environment to create

        Returns:
            Tuple[str, str, int]: A tuple containing stdout, stderr, and the return_code
        """
        return RunCmd.run_cmd(["conda", "activate",  env_name])

    @staticmethod
    def install_pkgs(env_name: str, pkg_list: List[str]) -> Tuple[str, str, int]:
        """
        Install a conda package

        Args:
           env_name (str): Name of environment to install given packages into.
           pkg_list (List[str]): List of packages to install

        Returns:
            Tuple[str, str, int]: A tuple containing stdout, stderr, and the return_code
        """
        return RunCmd.run_cmd(["conda", "install", '-n', env_name, ' '.join(pkg_list)])

    @staticmethod
    def search_pkg(pkg: str) -> Tuple[str, str, int]:
        """
        Search for a conda package from anaconda.org

        Args:
           pkg (str): Name of package to search for

        Returns:
            Tuple[str, str, int]: A tuple containing stdout, stderr, and the return_code
        """
        return RunCmd.run_cmd([f"conda search {pkg}"])

    @staticmethod
    def list_pkgs(env_name: str) -> Tuple[str, str, int]:
        """
        List installed packages for the given conda environment

        Args:
           env_name (str): Name of environment to list packages installed in.

        Returns:
            Tuple[str, str, int]: A tuple containing stdout, stderr, and the return_code
        """
        return RunCmd.run_cmd(["conda", "list", '-n', env_name])

    @staticmethod
    def remove_env(env_name: str) -> Tuple[str, str, int]:
        """
        Remove the given conda environment

        Args:
           env_name (str): Name of environment to remove.

        Returns:
            Tuple[str, str, int]: A tuple containing stdout, stderr, and the return_code
        """
        return RunCmd.run_cmd(["conda", "env", "remove", "-y", "-n", env_name, "--all"])