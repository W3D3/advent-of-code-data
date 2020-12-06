from aocd.utils import blocker
from freezegun import freeze_time


# 0.2 second before unlock day 1
@freeze_time("2020-11-30 23:59:59.8-05:00", tick=True)
def test_blocker(capsys):
    blocker(dt=0.2)
    out, err = capsys.readouterr()
    assert " Unlock day 1 at " in out


@freeze_time("2020-11-30 23:59:59.8-05:00", tick=True)
def test_blocker_quiet(capsys):
    blocker(dt=0.2, quiet=True)
    out, err = capsys.readouterr()
    assert not out