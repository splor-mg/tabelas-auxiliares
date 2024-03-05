import importlib.metadata as pkg_metadata
import exceptions
import config
import logging

logger = logging.getLogger(__name__)

def check_requirements(
        requirements: str = 'requirements.in',
        stop_on_missing: bool = True,
        stop_on_wrong_version: bool = True,
):

    missing_packages = []
    wrong_version_packages = []
    packages = read_requirements_txt(requirements)

    for package_name, expected_version in packages.items():
        try:
            installed_version = pkg_metadata.version(package_name)
            if expected_version:
                if installed_version != expected_version:
                    wrong_version_packages.append((package_name, installed_version, expected_version))

        except pkg_metadata.PackageNotFoundError:
            missing_packages.append(package_name)

    if missing_packages:
        logger.warning("Required packages are missing: %s", ', '.join(missing_packages))
        if stop_on_missing:
            raise exceptions.MissingPackageError

    if wrong_version_packages:
        for package, actual, expected in wrong_version_packages:
            logger.warning("Required package with wrong version: %s (Installed: %s, Expected: %s)", package, actual, expected)
        if stop_on_wrong_version:
            raise exceptions.WrongVersionPackageError


def read_requirements_txt(file_path):
    packages_to_check = {}

    with open(file_path, 'r') as file:
        lines = file.read().splitlines()

        for line in lines:
            packages_to_check.update(parse_requirement(line))

    return packages_to_check


def parse_requirement(req):
    if not req.strip().startswith('#'):
        if req.startswith('git+https://github.com/'):
            parts = req.split('.git@')
            if len(parts) == 2:
                package_name = parts[0].split('/')[-1]
                package_version = parts[1].replace('v', '') if parts[1].startswith('v') else None
                return {package_name: package_version}

        else:
            parts = req.split('==')

            if len(parts) == 2:
                package_name, package_version = parts
                return {package_name: package_version}

            elif len(parts) == 1:
                return {parts[0]: None}

if __name__ == '__main__':
    check_requirements()

