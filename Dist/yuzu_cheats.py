import pandas as pd
import os

import sys

def valid_cheat_folder_name(cheat_name):
    if ":" in cheat_name:
        cheat_name = cheat_name.replace(":","+")
    
    if r"/" in cheat_name:
        cheat_name = cheat_name.replace(r"/","+")

    if r"\\" in cheat_name:     
        cheat_name = cheat_name.replace(r"\\","+")

    if "*" in cheat_name:     
        cheat_name = cheat_name.replace("*","+")

    if "?" in cheat_name:
        cheat_name = cheat_name.replace("?","+")

    if r'"' in cheat_name:
        cheat_name = cheat_name.replace(r'"',"+")

    if r"'" in cheat_name:
        cheat_name = cheat_name.replace(r"'","+")

    if "<" in cheat_name:
        cheat_name = cheat_name.replace("<","+")

    if ">" in cheat_name:
        cheat_name = cheat_name.replace(">","+")

    if "|" in cheat_name:
        cheat_name = cheat_name.replace("|","+")

    return cheat_name

n = len(sys.argv)

if n > 2:
    print("The script only supports one game title at a time")
else:
    title_id = str(sys.argv[1])

    mod_config = pd.read_csv("modlocation.csv",sep=";")
    mod_location = mod_config.iloc[0]['value']

    cheats_df = pd.read_csv("cheats.csv",sep=";")
    cheats = cheats_df.loc[cheats_df['TITLE ID'] == title_id]
    no_of_records = len(cheats)
    game_exisits = False

    if(no_of_records > 0):
        game_exisits = True

    if game_exisits:
        print("Adding Cheats")
        os.chdir(mod_location)
        title_path = title_id
        title_folder_is_existing = os.path.isdir(title_path) 
        if not title_folder_is_existing:
            os.mkdir(title_id)
        os.chdir(title_id)
        for i, row in cheats.iterrows():
            cheat_name = row['CHEAT']
            cheat_name = valid_cheat_folder_name(cheat_name)
            cheat_name_folder_is_existing = os.path.isdir(cheat_name)
            if not cheat_name_folder_is_existing:
                os.mkdir(cheat_name)
            os.chdir(cheat_name)
            cheats_folder_is_existing = os.path.isdir("cheats")
            if not cheat_name_folder_is_existing:
                os.mkdir("cheats")
            os.chdir("cheats")
            file_name = row['FILE NAME']
            file_content = row['CHEAT VALUE'].split(r'\n')
            f = open(file_name,"w",encoding="utf-8")
            for line in file_content:
                f.write(line+'\n')
            f.close()
            os.chdir("../..")
            
    else:
        print("No Game Found with this TITLE ID in the Database")
