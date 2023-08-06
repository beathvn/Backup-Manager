# Backup-Manager

This project thinks about creating Backups of source and target directories. These directories are setup using a config file. The path to this config file should be passed to the program as a program argument.

## Setup config file
The Config files should be of type yaml and contain the key "directories_to_sync". This should be of type dict and the key should be of type string and the value a list.
The key is expected to be the filepath of the source directory. The entries of the list (which is the value) should be filepaths to where you want to sync this folder.