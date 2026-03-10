import subprocess


class LeptonDB:
    @property
    def name(self):
        # FIXME: Use the qubesdb API instead.
        return subprocess.check_output("hostname").decode().strip()
