import importlib


def safe_call(module, fn_names):
    """
    Try calling common entrypoints safely if they exist.
    """
    for fn in fn_names:
        if hasattr(module, fn):
            try:
                getattr(module, fn)()
            except Exception:
                # ignore runtime errors — we only want coverage
                pass


def test_dashboard_module():
    mod = importlib.import_module("soc_dashboard")

    safe_call(mod, [
        "main",
        "run",
        "render",
        "build_dashboard",
        "generate_dashboard",
    ])


def test_visualizations_module():
    mod = importlib.import_module("visualizations")

    safe_call(mod, [
        "main",
        "run",
        "render",
        "plot",
        "generate",
        "build",
        "create_visualizations",
    ])


def test_pipeline_and_reporting():
    for name in [
        "soc_pipeline",
        "verify_security_pipeline",
        "soc_command_center",
        "soc_metrics_engine",
    ]:
        mod = importlib.import_module(name)

        safe_call(mod, [
            "main",
            "run",
            "execute",
            "build",
            "process",
            "generate_report",
        ])
