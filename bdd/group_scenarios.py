
from pytest_bdd import scenario
from .group_steps import *


@scenario("groups.feature", "Add new group")
def test_add_new_group():
    pass


@scenario("groups.feature", "Delete some group")
def test_del_some_group():
    pass
