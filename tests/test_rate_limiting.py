from phase_02_authenticated_api import (
    is_rate_limited,
    rate_limit_store,
    RATE_LIMIT
)

def test_rate_limit_allows_initial_requests():
    identity = "test-user"

    rate_limit_store.clear()

    for _ in range(RATE_LIMIT):
        assert is_rate_limited(identity) is False


def test_rate_limit_blocks_excess_request():
    identity = "test-user"

    rate_limit_store.clear()

    for _ in range(RATE_LIMIT):
        is_rate_limited(identity)

    assert is_rate_limited(identity) is True
