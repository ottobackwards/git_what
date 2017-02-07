#!/usr/bin/env python
import optparse

import sys
import os
import re
import subprocess
import json


def get_git_info(working_directory):
    git_info = {}
    for root, sub_directories, files in os.walk(working_directory):
        for subdir in sub_directories:
            if subdir == '.git':
                git_info[os.path.basename(root)] = parse_return(root)

    return git_info


def parse_return(working_directory):
    remote_info = {'path': working_directory}
    pattern = re.compile("^Local branch configured.*")
    process = subprocess.Popen(['git remote show origin'], cwd=working_directory, stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE, shell=True)
    out, err = process.communicate()
    if process.returncode == 0:
        lines = out.splitlines()
        number_of_lines = len(lines)
        if number_of_lines > 0:
            lines[1] = [x.strip() for x in lines[1].split(':') if x]
            remote_info["Fetch URL"] = lines[1][1] + ':' + lines[1][2]

            lines[2] = [x.strip() for x in lines[2].split(':') if x]
            remote_info["Push URL"] = lines[2][1] + ':' + lines[2][2]

            lines[3] = [x.strip() for x in lines[3].split(':') if x]
            remote_info["HEAD branch"] = lines[3][1]

            # next is an array of remote branches name tracked or not
            # we don't care about tracking
            start = 5
            remote_branches = []
            for x in range(start, number_of_lines):
                if pattern.match(lines[x].strip()):
                    break
                else:
                    remote_branches.append([x.strip() for x in lines[x].split(' ') if x][0])

            remote_info["Remote Branches"] = remote_branches

            return remote_info


def main():
    p = optparse.OptionParser()
    p.add_option('--directory', '-d', action="store", type="string", dest="directory", help="The directory to start in")
    options, arguments = p.parse_args()

    if options.directory is None:
        print "missing required option directory"
        sys.exit(1)

    the_info_dict = get_git_info(options.directory)
    print(json.dumps(the_info_dict, indent=2))


if __name__ == '__main__':
    main()
