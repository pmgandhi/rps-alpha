from hamcrest import assert_that, is_, greater_than_or_equal_to

# sut:
from ..chomp import generate_dms_id

def test_should_generate_non_conflicting_dms_id():
    """Wisdom already generates DMS ids upto 9 digits long and therefore we need to generate
    ids which are longer.
    """
    # when
    dms_id = generate_dms_id()
    # then
    assert_that(type(dms_id), is_(type(str)))
    assert_that(len(dms_id), greater_than_or_equal_to(10))
