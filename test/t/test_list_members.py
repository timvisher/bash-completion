import pytest


class Test(object):

    @pytest.mark.complete("list_members -")
    def test_dash(self, completion):
        assert completion.list