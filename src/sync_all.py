# system imports
from argparse import ArgumentParser
import sys
import os
sys.path.append('../src/')

# 3rd party imports
import yaml
from dirsync import sync

# user imports
from helpers.logger import logger


def main(args):
    with open(args.config, encoding='utf-8') as file:
        config = yaml.safe_load(file)
    dict_directories = config['directories_to_sync']
    
    for curr_soruce in dict_directories:
        print(curr_soruce)
        if os.path.exists(curr_soruce):
            for curr_dest in dict_directories[curr_soruce]:
                if os.path.exists(curr_dest):
                    filenames_to_exclude = [filename for filename in os.listdir(curr_soruce) if filename.startswith('.')]
                    sync(curr_soruce, 
                         curr_dest, 
                         'sync', 
                         verbose=True, 
                         exclude=filenames_to_exclude, 
                         logger=logger, 
                         purge=True, # makes sure that files can also be deleted in destination
                         )
                else:
                    logger.error(f"Did not sync {curr_soruce} to {curr_dest} because destination does not exist.")
        else:
            logger.error(f"Skipping source directory {curr_soruce['source']} because it does not exist.")


if __name__ == "__main__":
    logger.info('Start of program: sync_all.py...')
    
    parser = ArgumentParser()
    parser.add_argument('-c', '--config', help='Path to config file', required=True)
    args = parser.parse_args()
    main(args)
    
    logger.info('End of program: sync_all.py\n')