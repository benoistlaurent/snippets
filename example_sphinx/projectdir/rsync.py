
"""projectdir.rsync - Run rsync from Python.

From pykup: https://raw.githubusercontent.com/benoistlaurent/pykup
"""


import logging
import os
import subprocess


RSYNC_EXECUTABLE = 'rsync'
RSYNC_INCREMENTAL_BACKUP_FLAGS = [
    '--archive',
    '--hard-links',
    '--one-file-system',
    '--numeric-ids',
    # '--itemize-changes'
]


class RsyncCompletedProcess(subprocess.CompletedProcess):

    @classmethod
    def from_parent(cls, parent):
        return cls(parent.args, parent.returncode,
                   parent.stdout, parent.stderr)

    def has_errors(self):
        """Return True if rsync exited with errors (return status is not 0)."""
        return self.returncode != 0

    def has_no_space_left_error(self):
        """Return True if a no space left error was detected.

        Check if stderr contains 'No space left on device (28)' or
        'Result too large (34)'.
        """
        return (b'No space left on device (28)' in self.stderr or
                b'Result too large (34)' in self.stderr)

    def assert_has_no_errors(self):
        """Raise an AssertionError return code is not 0."""
        if self.has_errors():
            err = 'rsync process had errors:\n' + self.stderr.decode('utf-8')
            raise AssertionError(err)


def run(source, dest, link_dest='',
        rsync=RSYNC_EXECUTABLE, flags=RSYNC_INCREMENTAL_BACKUP_FLAGS):
    """Synchronize data form `source` to `dest`.

    Args:
        source (str or list[str]): path to source or multiple sources.
        dest (str): destination directory.
        link_dest (str): hard links source.
            This is the base name of the last directory used to backup
            (e.g. '2017-03-30-123021').
        rsync (str): rsync executable path.
        flags (list[str]): rsync flags.

    Returns:
        RsyncCompletedProcess: class that stores process informations.
    """
    if isinstance(source, str):
            source = [source]
    link_dest_option = ''
    if link_dest:
        # Link destination has to be relative to destination.
        # Has dest is /path/to/destination/<date>, the previous destination
        # is /path/to/destination/<previous_date>.
        abs_link_dest = os.path.join(os.path.dirname(dest), link_dest)
        link_dest_option = '--link-dest={}'.format(abs_link_dest)
        flags.append(link_dest_option)

    cmd = [rsync] + flags + source + [dest]
    logging.debug(cmd)
    p = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return RsyncCompletedProcess.from_parent(p)