# %% md
## Imports

# %%
import cProfile
import pstats
from pathlib import Path

NOTEBOOK_DIR = Path.cwd()
PROJECT_ROOT = NOTEBOOK_DIR.parent
ANALYSIS_DIR = PROJECT_ROOT / ".analysis"
ANALYSIS_DIR.mkdir(exist_ok=True)


def profile(func, data, iterations=1000, file="cprofile.txt"):
    def bench():
        for _ in range(iterations):
            func(iter(data))

    profiler = cProfile.Profile()
    profiler.runcall(bench)

    with (ANALYSIS_DIR / file).open("w") as f:
        stats = pstats.Stats(profiler, stream=f)
        stats.strip_dirs()
        stats.sort_stats("tottime")
        stats.print_stats(20)
