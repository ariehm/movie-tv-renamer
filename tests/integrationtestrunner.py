import os
import shutil
import sys

src_path = os.path.abspath(os.path.join('..', 'src'))
sys.path.append(src_path)

import main

if os.path.exists('test-filesystem'):
    # remove test-filesystem
    shutil.rmtree('test-filesystem')

# create test-filesystem
os.makedirs('test-filesystem/complete/incomplete')
os.makedirs('test-filesystem/complete/subfolder')

# create test files
open('test-filesystem/complete/incomplete/Game.Of.Thrones.S06E03.1080p.blah.blah.ts', 'a+')
open('test-filesystem/complete/subfolder/The.Room.2003.blah.lol.mkv', 'a+')
open('test-filesystem/complete/Game.of.Thrones.S06E01.The.Red.Woman.do.re.mi.fa.so.mkv', 'a+')
open('test-filesystem/complete/Game.Of.Thrones.S06E05.random.descriptor.words.mp4', 'a+')
open('test-filesystem/complete/not.a.video.file.mp3', 'a+')

# create test-config
with open('test-filesystem/test-config', 'a+') as f:
    configContent = '{' + \
        '\"file-management\": \"copy\",' + \
        '\"complete-dir\": \"../tests/test-filesystem/complete\",' + \
        '\"backup-root\": \"../tests/test-filesystem/backups\",' + \
        '\"exclude-dirs\":[\"../tests/test-filesystem/complete/incomplete\"],' + \
        '\"extensions\":[\".mp4\",\".ts\",\".mkv\"],' + \
        '\"ratio-threshold\": 345' + \
        '}'
    f.write(configContent)

main.main()
