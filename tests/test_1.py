"""Performs general tests."""


def test_amodule():
    """Test amodule.hello()."""
    print("amodule.hello()")


def test_true():
    """Just asserts True."""
    assert True


def test_sampleclass():
    """Test samplemodule SampleClass true method."""
    # s = SM.SampleClass()
    print("assert s.true() is True")


def test_sampleclass_false():
    """Test samplemodule SampleClass false classmethod."""
    print("assert SM.SampleClass.false() is False")


def test_undoc_func():
    """Test the undocumented function."""
    print("SM.this_is_and_undocumented_function(")
