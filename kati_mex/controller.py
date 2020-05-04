def _invalid_selection():
    return 0


def _run_order():
    return 1


def _run_deliver():
    return 2


def run(function: str) -> int:
    functions = {
        "order": _run_order,
        "deliver": _run_deliver,
    }
    run_function = functions.get(function, _invalid_selection)
    return run_function()
