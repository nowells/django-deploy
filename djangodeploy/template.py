import functools
import os
import re
import shutil

def replace_file_markers(path, regexes):
    if not regexes:
        return 0

    path = os.path.abspath(os.path.realpath(path))

    replacements = []
    for searchs, replaces, reflags in regexes:
        if reflags is not None:
            regex = re.compile(searchs, reflags)
        else:
            regex = re.compile(searchs)
            replacements.append(functools.partial(regex.subn, replaces))

    files_changed = 0
    for dirpath, dirnames, filenames in os.walk(path):
        for dirname in dirnames:
            new_dirname = dirname
            substitutions = 0
            for replacement in replacements:
                new_dirname, num_changes = replacement(new_dirname)
                substitutions += num_changes
            if substitutions:
                os.rename(os.path.join(dirpath, dirname), os.path.join(dirpath, new_dirname))
                dirnames.remove(dirname)
                dirnames.append(new_dirname)

        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            f = open(filepath, 'r')
            text = f.read()
            f.close()

            substitutions = 0

            for replacement in replacements:
                text, num_changes = replacement(text)
                substitutions += num_changes

            if substitutions:
                f = open(filepath, 'w')
                f.write(text)
                f.close()
                files_changed += 1

    return files_changed

EXCLUDE_FILTER = r'^(\.git|\.svn|django_deploy_config.py|.*~|.*\.pyc|#.*#)$'

def copy_project_template(source_directory, target_directory, excludes=EXCLUDE_FILTER):
    excludes = re.compile(excludes)

    def new_path(path):
        return path.replace(source_directory, target_directory)

    for dirpath, dirnames, filenames in os.walk(source_directory):
        dirnames = filter(lambda x: not excludes.match(x), dirnames)
        filenames = filter(lambda x: not excludes.match(x), filenames)
        path = new_path(dirpath)
        os.makedirs(path)
        for filename in filenames:
            shutil.copy(os.path.join(dirpath, filename), os.path.join(path, filename))
