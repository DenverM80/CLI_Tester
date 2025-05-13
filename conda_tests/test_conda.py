"""
test cases to create a conda environment, install packages, verify the packages are installed, and remove the env.
"""
import pytest
from conda_cli.run_conda import RunConda
from typing import List
from utils.logger import log

conda_cli = RunConda()

@pytest.mark.parametrize("environment_name, pkgs", [
    ("test_ml", ["numpy", "pandas"]),
    ("test_data_science", ["scipy", "bottleneck"])
])
def test_create_and_verify_env(environment_name: str, pkgs: List[str]):
    """
    Test CRUD operation with multiple packages for multiple environments.

        Args:
           environment_name (str): Name of environment to install given packages into.
           pkgs (List[str]): List of packages to install

        Returns:
            None
    """
    # Create conda environment
    output, errors, rc = conda_cli.create_env(env_name=environment_name, pkgs=[])
    log.info(f"conda create env output:\n{output}")
    assert rc == 0, f"Failed to create {environment_name}: {errors}"

    # Install packages in conda environment
    output, error, rc = conda_cli.install_pkgs(env_name=environment_name, pkg_list=pkgs)
    log.info(f"conda install package output:\n{output}")
    assert rc == 0, f"Failed to install packages [{' '.join(pkgs)}] in environment [{environment_name}]: {errors}"

    # List installed packages in conda environment
    output, errors, rc = conda_cli.list_pkgs(env_name=environment_name)
    log.info(f"conda env list packages output:\n{output}")
    assert rc == 0, f"Failed to list packages for {environment_name}: {errors}"

    for pkg in pkgs:
        assert pkg in output.lower(), f"{pkg} not found in {environment_name}"

    # Cleanup
    output, errors, rc = conda_cli.remove_env(env_name=environment_name)
    log.info(f"conda remove env output:\n{output}")

@pytest.mark.parametrize("environment_name, version, pkgs", [
    ("test_python_3_5", "3.5", ["pytest", "pytest-html", "requests"]),
    ("test_python_3_10", "3.10", ["pytest", "pytest-html", "requests"]),
    ("test_python_3_13", "3.13", ["pytest", "pytest-html", "requests"])
])
def test_create_and_verify_python_env(environment_name: str, version: str, pkgs: List[str]):
    """
    Test CRUD operation with multiple packages for multiple environments.

        Args:
           environment_name (str): Name of environment to install given packages into.
           version (str): major and minor version of a python distribution to install.
           pkgs (List[str]): List of packages to install

        Returns:
            None
    """
    # Create conda environment
    output, errors, rc = conda_cli.create_python_env(env_name=environment_name, pkgs=[], version=version)
    log.info(f"conda create env output:\n{output}")
    assert rc == 0, f"Failed to create {environment_name}: {errors}"

    # Install packages in conda environment
    output, error, rc = conda_cli.install_pkgs(env_name=environment_name, pkg_list=pkgs)
    log.info(f"conda install package output:\n{output}")
    assert rc == 0, f"Failed to install packages [{' '.join(pkgs)}] in environment [{environment_name}]: {errors}"

    # List installed packages in conda environment
    output, errors, rc = conda_cli.list_pkgs(env_name=environment_name)
    log.info(f"conda env list packages output:\n{output}")
    assert rc == 0, f"Failed to list packages for {environment_name}: {errors}"

    for pkg in pkgs:
        assert pkg in output.lower(), f"{pkg} not found in {environment_name}"

    # Cleanup
    output, errors, rc = conda_cli.remove_env(env_name=environment_name)
    log.info(f"conda remove env output:\n{output}")
