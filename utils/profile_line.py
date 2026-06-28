import importlib
from line_profiler import LineProfiler
from pathlib import Path

NOTEBOOK_DIR = Path.cwd()
PROJECT_ROOT = NOTEBOOK_DIR.parent
ANALYSIS_DIR = PROJECT_ROOT / ".analysis"
ANALYSIS_DIR.mkdir(exist_ok=True)


def line_profile(module, func, data, file="lineprofile.txt"):
    importlib.reload(module)

    lp = LineProfiler()
    lp.add_function(func)

    lp.runcall(func, iter(data))

    with (ANALYSIS_DIR / file).open("w") as f:
        lp.print_stats(stream=f)
