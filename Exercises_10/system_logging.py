#Name: Philip Stewart
#Student Number: L00187850
#Date: 25 Nov 2024
#Purpose:System Logfiles introduction

import logging

from datetime import datetime

#I added the option to create the file as a text file instead of an unreadable file.
# Get the date and time and use as a filename
now = datetime.now()
MyDateFile = '%0.4d%0.2d%0.2d-%0.2d%0.2d%0.2d.txt' % (now.year, now.month, now.day, now.hour, now.minute, now.second)

# Set logging to that file
logging.basicConfig(filename=MyDateFile, filemode='w', format='%(name)s - %(levelname)s - %(message)s')

logging.debug('Debug message')
logging.info('Information message')
logging.warning('Warning message')
logging.error('Error message')
logging.critical('Critical message')