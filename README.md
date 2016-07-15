# movie-tv-renamer
## Intro
This script uses imdb and tvdb to rename movie and tv show files into something a little more pretty.  

It is my first python project and I'm using it as a playground to see what the big deal is :)

Disclaimer:
It needs to be tested and probably doesn't work because I haven't tested it in a while

## TODO
* finish integration testing
** SymLinkRenamer.shouldRename() is not working correctly when the symlink already exists
* add test-filesystem to gitignore and create integration testing script that creates and destroys the test-filesystem
* remove seed after ratio is over threshold (1.25?)
* add logging
* add exception handling
* add parameter checks
* create a python module with pip
* create a python module with no dependencies with pip
