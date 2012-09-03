import sublime, sublime_plugin
import json, os, subprocess, functools

class dorsyncCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        sublime.status_message("Starting RSync...");
        view = self.view

        cmd = ["rsync"]

        # Check if we're in a proper ST2 project
        if not view.window().folders():
            return

        projectFolder = view.window().folders()[0]
        projectFile   = projectFolder + '/dev_rsync.json'

        # Skip syncing if there is no dev_rsync.json file
        if not os.path.exists(projectFile):
            return

        json_data = open(projectFile)
        data      = json.load(json_data)
        json_data.close

        for option in data['option']:
            cmd.append('--' + option)

        for exclude in data['exclude']:
            cmd.append('--exclude=' + exclude)

        cmd.append(projectFolder + '/')
        cmd.append(data['host'] + ':' + data['target_dir'] + '/')

        print 'DevRsync - '+ ' '.join(cmd)

        # Execute the rsync command
        #cmd.append(' &')
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE)

        out, err = p.communicate()

        print "\n".join("DevRsync - " + line for line in out.split("\n"))

        if err != None:
            print err

        sublime.set_timeout(functools.partial(self.updateStatus, view, 'DevRsync Done!'), 100)

    def updateStatus(self, view, text):
        sublime.status_message(text);
