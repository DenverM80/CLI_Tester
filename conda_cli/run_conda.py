from typing import List, Tuple


class RunConda:
    """
    This class wraps the 'conda' command for common environment and package functionality
    """
    def create_env(self, env_name: str, pkgs: List[str]) -> Tuple[str, str, int]:
        """
        Create a conda environment with the given packages

        Args:
           env_name (str): Name of environment to create
           pkgs (List[str]): List of packages to install

        Returns:
            Tuple[str, str, int]: A tuple containing stdout, stderr, and the return_code
        """
        return self.run_cmd(["conda", "create", "-y", "-n", env_name, f"{' '.join(pkgs)}"])

    def create_python_env(self, env_name: str, pkgs: List[str], version: str) -> Tuple[str, str, int]:
        """
        Create a conda environment with the given packages

        Args:
           env_name (str): Name of environment to create
           version (str): Major and minor version of python to install
           pkgs (List[str]): List of packages to install

        Returns:
            Tuple[str, str, int]: A tuple containing stdout, stderr, and the return_code
        """
        return self.run_cmd(["conda", "create", "-y", "-n", env_name, f"python={version}", f"{' '.join(pkgs)}"])

    def activate_env(self, env_name: str) -> Tuple[str, str, int]:
        """
        Activate a conda environment

        Args:
           env_name (str): Name of environment to create

        Returns:
            Tuple[str, str, int]: A tuple containing stdout, stderr, and the return_code
        """
        return self.run_cmd(["conda", "activate",  env_name])

    def install_pkgs(self, env_name: str, pkg_list: List[str]) -> Tuple[str, str, int]:
        """
        Install a conda package

        Args:
           env_name (str): Name of environment to install given packages into.
           pkg_list (List[str]): List of packages to install

        Returns:
            Tuple[str, str, int]: A tuple containing stdout, stderr, and the return_code
        """
        return self.run_cmd(["conda", "install", '-n', env_name, ' '.join(pkg_list)])

    def search_pkg(self, pkg: str) -> Tuple[str, str, int]:
        """
        Search for a conda package from anaconda.org

        Args:
           pkg (str): Name of package to search for

        Returns:
            Tuple[str, str, int]: A tuple containing stdout, stderr, and the return_code
        """
        return self.run_cmd([f"conda search {pkg}"])

    def list_pkgs(self, env_name: str) -> Tuple[str, str, int]:
        """
        List installed packages for the given conda environment

        Args:
           env_name (str): Name of environment to list packages installed in.

        Returns:
            Tuple[str, str, int]: A tuple containing stdout, stderr, and the return_code
        """
        return self.run_cmd(["conda", "list", '-n', env_name])

    def remove_env(self, env_name: str) -> Tuple[str, str, int]:
        """
        Remove the given conda environment

        Args:
           env_name (str): Name of environment to remove.

        Returns:
            Tuple[str, str, int]: A tuple containing stdout, stderr, and the return_code
        """
        return self.run_cmd(["conda", "env", "remove", "-y", "-n", env_name, "--all"])