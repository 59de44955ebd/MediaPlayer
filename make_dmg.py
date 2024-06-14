import os
import subprocess
import sys

def buildDMG (dist_dir, dmg_name, volume_label):

    apps_folder_link = os.path.join(dist_dir, "Applications")
    os.symlink(
        "/Applications", apps_folder_link, target_is_directory=True)

    createargs = [
        "hdiutil",
        "create",
#         "-quiet",
        "-fs",
        "HFSX",
        "-format",
        "UDZO",
        dmg_name,
        "-imagekey",
        "zlib-level=9",
        "-srcfolder",
        dist_dir,
        "-volname",
        volume_label,
    ]

    # Create the dmg
    if subprocess.call(createargs) != 0:
        raise OSError("creation of the dmg failed")

if __name__ == '__main__':
    dist_dir = sys.argv[1]
    dmg_name = sys.argv[2]
    volume_label = sys.argv[3]
    buildDMG(dist_dir, dmg_name, volume_label)
