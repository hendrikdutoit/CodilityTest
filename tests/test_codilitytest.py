
'''Testing codilitytest__init__()'''

from pathlib import Path
from beetools.beearchiver import Archiver
import codilitytest


_PROJ_DESC = __doc__.split('\n')[0]
_PROJ_PATH = Path(__file__)


def project_desc():
    return _PROJ_DESC


b_tls = Archiver(_PROJ_DESC, _PROJ_PATH)


class TestCodilityTest:
    def test__init__(self, env_setup_self_destruct):
        """Assert class __init__"""
        env_setup = env_setup_self_destruct
        t_codilitytest = codilitytest.CodilityTest(env_setup.dir, True)

        assert t_codilitytest.success
        pass

    def test_method_1(self, env_setup_self_destruct):
        """Assert class __init__"""
        env_setup = env_setup_self_destruct
        t_codilitytest = codilitytest.CodilityTest("CodilityTest", env_setup.dir)

        assert t_codilitytest.method_1()
        pass

del b_tls
