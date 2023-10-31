from subprocess import check_output
from FloorplanToBlenderLib import (
    IO,
    config,
    const,
    execution,
    dialog,
    floorplan,
    stacking,
    project
)
import os
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
    fp = floorplan.new_floorplan(None)

    data_path = execution.simple_single(fp)
    project.create_blender_project(data_path)

    print("\nDone, Have a nice day!")
