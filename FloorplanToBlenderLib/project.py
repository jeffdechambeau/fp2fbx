from subprocess import check_output
import os
from FloorplanToBlenderLib import (
    IO,
    config,
    const
)

blender_install_path = config.get_default_blender_installation_path()
data_folder = const.BASE_PATH
target_folder = const.TARGET_PATH
program_path = os.path.dirname(os.path.realpath(__file__))
blender_script_path = const.BLENDER_SCRIPT_PATH

print("blender_install_path", blender_install_path)
print("data_folder", data_folder)
print("target_folder", target_folder)
print("program_path", program_path)
print("blender_script_path", blender_script_path)


def ensure_directory_exists(path):
    """Ensures the directory for the given path exists."""
    if not os.path.exists(path):
        os.makedirs(path)


def get_target_path(target_folder):
    """Generate the target path for the blender project."""
    target_base = os.path.join(target_folder, const.TARGET_NAME)
    target_path = target_base + const.BASE_FORMAT
    return IO.get_next_target_base_name(target_base, target_path) + const.BASE_FORMAT


def create_blender_project_from_path(blender_install_path, blender_script_path, program_path, target_path, data_paths):
    cmd = [
        blender_install_path,
        "-noaudio",
        "--background",
        "--python",
        blender_script_path,
        program_path,
        target_path,
        str(data_paths)  # Ensure it's a string
    ]
    check_output(cmd)


def export_to_format(blender_install_path, target_path, outformat):
    target_base, _ = os.path.splitext(target_path)
    cmd = [
        blender_install_path,
        "-noaudio",
        "--background",
        "--python",
        "/content/fp2fbx/Blender/blender_export_any.py",
        target_path,
        outformat,
        target_base + outformat
    ]
    print(cmd)
    check_output(cmd)
    print(
        f"Object created at: {os.path.join(program_path, target_base + outformat)}")


def create_blender_project(data_paths):

    ensure_directory_exists(target_folder)
    target_path = get_target_path(target_folder)
    create_blender_project_from_path(
        blender_install_path, blender_script_path, program_path, target_path, data_paths)

    outformat = config.get(const.SYSTEM_CONFIG_FILE_NAME,
                           "SYSTEM", const.STR_OUT_FORMAT).replace('"', "")

    export_to_format(blender_install_path, target_path, outformat)

    print(f"Project created at: {os.path.join(program_path, target_path)}")
