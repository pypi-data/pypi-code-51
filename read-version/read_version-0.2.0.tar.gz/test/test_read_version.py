import os
from   os.path      import dirname, join
import pytest
from   read_version import read_version

DATA_DIR = join(dirname(__file__), 'data')

def test_no_args():
    with pytest.raises(ValueError,match='No filepath passed to read_version()'):
        read_version()

@pytest.mark.parametrize('fname', os.listdir(join(DATA_DIR, 'valid')))
def test_read_version(fname):
    assert read_version('data', 'valid', fname) == '1.2.3'

def test_read_version_absolute():
    assert read_version(
        join(DATA_DIR, 'valid', os.listdir(join(DATA_DIR, 'valid'))[0])
    ) == '1.2.3'

@pytest.mark.parametrize('fname', os.listdir(join(DATA_DIR, 'valid')))
def test_read_version_custom(fname):
    assert read_version('data', 'valid', fname, variable='__custom__') == 42

@pytest.mark.parametrize('fname', os.listdir(join(DATA_DIR, 'missing')))
def test_missing(fname):
    with pytest.raises(
        ValueError,
        match="No assignment to '__version__' found in file",
    ):
        assert read_version('data', 'missing', fname)

@pytest.mark.parametrize('fname', os.listdir(join(DATA_DIR, 'missing_custom')))
def test_missing_custom(fname):
    with pytest.raises(
        ValueError,
        match="No assignment to '__custom__' found in file",
    ):
        assert read_version('data', 'missing_custom', fname,
                            variable='__custom__')

def test_default_missing():
    assert read_version(
        'data', 'missing', os.listdir(join(DATA_DIR, 'missing'))[0],
        default='DEFAULT',
    ) == 'DEFAULT'

def test_default_not_missing():
    assert read_version(
        'data', 'valid', os.listdir(join(DATA_DIR, 'valid'))[0],
        default='DEFAULT',
    ) == '1.2.3'

@pytest.mark.parametrize('fname', os.listdir(join(DATA_DIR, 'invalid')))
def test_invalid(fname):
    with pytest.raises((ValueError, TypeError)):
        assert read_version('data', 'invalid', fname)
