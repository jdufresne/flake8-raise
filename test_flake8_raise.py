def test_raise_without_from(flake8dir):
    flake8dir.make_example_py(
        """
        try:
            pass
        except ValueError:
            raise TypeError
        """
    )
    result = flake8dir.run_flake8()
    assert result.out_lines == [
        "./example.py:4:5: R100 raise in except handler without from."
    ]


def test_bare_raise(flake8dir):
    flake8dir.make_example_py(
        """
        try:
            pass
        except ValueError:
            raise
        """
    )
    result = flake8dir.run_flake8()
    assert result.out_lines == []


def test_raise_from(flake8dir):
    flake8dir.make_example_py(
        """
        try:
            pass
        except ValueError as e:
            raise TypeError from e
        """
    )
    result = flake8dir.run_flake8()
    assert result.out_lines == []


def test_no_raise(flake8dir):
    flake8dir.make_example_py(
        """
        try:
            pass
        except ValueError:
            pass
        """
    )
    result = flake8dir.run_flake8()
    assert result.out_lines == []


def test_nested_raise_without_from(flake8dir):
    flake8dir.make_example_py(
        """
        try:
            pass
        except ValueError:
            try:
                pass
            except OSError:
                raise TypeError
        """
    )
    result = flake8dir.run_flake8()
    assert result.out_lines == [
        "./example.py:7:9: R100 raise in except handler without from."
    ]


def test_nested_bare_raise(flake8dir):
    flake8dir.make_example_py(
        """
        try:
            pass
        except ValueError:
            try:
                pass
            except OSError:
                raise
        """
    )
    result = flake8dir.run_flake8()
    assert result.out_lines == []


def test_nested_raise_from(flake8dir):
    flake8dir.make_example_py(
        """
        try:
            pass
        except ValueError as e:
            try:
                pass
            except OSError:
                raise TypeError from e
        """
    )
    result = flake8dir.run_flake8()
    assert result.out_lines == []


def test_nested_no_raise(flake8dir):
    flake8dir.make_example_py(
        """
        try:
            pass
        except ValueError:
            try:
                pass
            except OSError:
                pass
        """
    )
    result = flake8dir.run_flake8()
    assert result.out_lines == []


def test_raise_no_except(flake8dir):
    flake8dir.make_example_py(
        """
        raise TypeError
        """
    )
    result = flake8dir.run_flake8()
    assert result.out_lines == []


def test_raise_after_except(flake8dir):
    flake8dir.make_example_py(
        """
        try:
            pass
        except ValueError:
            pass
        raise TypeError
        """
    )
    result = flake8dir.run_flake8()
    assert result.out_lines == []


def test_raise_inside_def(flake8dir):
    flake8dir.make_example_py(
        """
        try:
            from foo import bar
        except ImportError:
            def bar():
                raise NotImplementedError
        """
    )
    result = flake8dir.run_flake8()
    assert result.out_lines == []


def test_raise_same_error(flake8dir):
    # Can't use a bare raise.
    flake8dir.make_example_py(
        """
        try:
            pass
        except ValueError as e:
            try:
                pass
            except TypeError:
                pass
            raise e
        """
    )
    result = flake8dir.run_flake8()
    assert result.out_lines == []


def test_nested_reraise_outer(flake8dir):
    flake8dir.make_example_py(
        """
        try:
            pass
        except ValueError as e:
            try:
                pass
            except TypeError:
                raise e
        """
    )
    result = flake8dir.run_flake8()
    assert result.out_lines == []
