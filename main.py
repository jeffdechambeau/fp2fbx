from subprocess import check_output
from FloorplanToBlenderLib import (
    IO,
    config,
    const,
    execution,
    dialog,
    floorplan,
    stacking, create_blender_project
)
import os
import bpy

CONFIG_PATH = "/content/fp2fbx/Config/default.ini"
"""
Create Blender Project from floorplan
This file contains a simple example implementation of creations of 3d models from
floorplans. You will need blender and an image of a floorplan to make this work.

Adapted from  FloorplanToBlender3d
Copyright (C) 2022 Daniel Westberg
"""


if __name__ == "__main__":

    blender_install_path = config.get_default_blender_installation_path()
    data_folder = const.BASE_PATH
    target_folder = const.TARGET_PATH
    program_path = os.path.dirname(os.path.realpath(__file__))
    blender_script_path = const.BLENDER_SCRIPT_PATH

    print(data_folder, target_folder, blender_install_path)

    floorplans = [floorplan.new_floorplan(c) for c in CONFIG_PATH.split(" ")]
    print(floorplans)

    data_paths = [execution.simple_single(fp) for fp in floorplans]

    print("\nGenerating data files in folder: Data\n")
    print("Cleaning data files\n")

    for paths in data_paths:
        create_blender_project(paths)

    print("\nDone, Have a nice day!")
