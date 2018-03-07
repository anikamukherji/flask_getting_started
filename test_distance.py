def test_dist_helper():
    try:
        import pytest
        from main import dist_helper
    except ImportError as e:
        print("Necessary import failed")
    assert dist_helper(0, 0, 0, 0) == 0.0
    assert dist_helper(1, 0, 4, 0) == 3.0
    assert dist_helper(0, -2, 0, 2) == 4.0
    with pytest.raises(TypeError):
        dist_helper('a', 0, 0, 0)
    with pytest.raises(TypeError):
        dist_helper([6, 7], 0, 0, 0)
    with pytest.raises(TypeError):
        dist_helper({7: 8}, 0, 0, 0)
