# generate uri for all static files
import os
import csv

URL_PREFIX = os.getenv('CREDITE_PROJECT_URL') or 'qixin-trans.com'

static_files = []
with open('static_file_list.txt', 'w') as output_f:
    for fpath, dirs, fs in os.walk('static'):
        for f in fs:
            uri = 'http://%s/%s' % (
                URL_PREFIX,
                '/'.join(os.path.join(fpath, f).split(os.sep))
            )
            static_files.append(uri)
            output_f.write(uri + '\n')
