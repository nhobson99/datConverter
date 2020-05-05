<b>DatConverter v2.0</b>

Made by Noah Hobson in collaboration with Dr. Dustin Gilbert of the Joint Institute for Advanced Materials

<h3>Usage</h3>

This app is made to strip off unwanted attributes from .dat files formatted as CSV. It needs <i>three (3) subdirectories</i> in the same location as the .py executable in order to function: <i>ingest, output, cache</i>.

ingest: all files to be processed. This will be the unaltered .dat files.

cache: processed files will be moved to cache to prevent accidental data loss. These will be an exact copy of the original .dat files.

output: the fully processed files, with header and unwanted data removed.



Additionally, this program requires a config file in order to work. The config will contain all wanted data, separated by newline. It will look something like the following:

>config.txt
>
>Temperature (K)
>
>Magnetic Field (Oe)
>
>Time (ms)

This will remove anything from the data file other than Temperature, Field and Time. It looks for an exact match, so it is best to copy these directly from a dat file to avoid typos.



Finally, to run the program, call `python3 datConverter.py config.txt` replacing config.txt with whatever configuration file you intend to use.

<h3>Additional Usage Information</h3>

This program is made to be run automatically by services such as crontab, and was made particularly with the Synology Disk System's autorun feature in mind. There is little to no penalty in making this run, for example, once every minute.
