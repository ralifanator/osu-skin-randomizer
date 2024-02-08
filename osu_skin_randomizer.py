import os
import sys
import argparse
import pathlib
import random
import shutil
import zipfile

parser = argparse.ArgumentParser(
    prog="Osu Skin Randomizer Script",
    description="Create new skin for osu from existence skins",
    epilog="Created by Final Dice https://osu.ppy.sh/users/3450454"
)

parser.add_argument ('osu_dir', type = str, help='osu path')
args = parser.parse_args()


file = open("osu_skinnable_files.txt", "r")
skinnable_files = []

for line in file.readlines():
    if (line[0] == '#'):
        continue
    skinnable_files.append(line.rstrip('\n'))

skins_paths = []
skins_path = os.path.join(args.osu_dir, "Skins")

for file in os.listdir(skins_path):
    skin_path = os.path.join(skins_path, file)
    if (os.path.isdir(skin_path)):
        skins_paths.append(skin_path)

if not(os.path.exists("Skin")):
    os.mkdir("Skin")
new_skin_path = os.path.join(os.getcwd(), "Skin")
for skinnable_file in skinnable_files:
    skin_path = random.choice(skins_paths)
    print(skin_path)
    for file in os.listdir(skin_path):
        if skinnable_file in file:
            skin = os.path.join(skin_path, file)
            print(skin)
            shutil.copy(os.path.join(skin_path, file), new_skin_path)

with zipfile.ZipFile('Skin.osk', mode='w', \
                     compression=zipfile.ZIP_DEFLATED) as zf:
    for file in os.listdir(new_skin_path):
        add_file = os.path.join("Skin", file)
        zf.write(add_file)