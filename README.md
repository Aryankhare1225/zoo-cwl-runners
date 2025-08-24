![CI – Test CWL Runners](https://github.com/Aryankhare1225/zoo-cwl-runners/actions/workflows/test.yml/badge.svg)

## CI Overview
- **Unit job**: runs `pytest -v tests/unit` with Python 3.10; no external runners required.
- **Integration job**: checks out runner/common repos under `deps/`, installs them, and runs `pytest -v -m integration -k "not calrissian"`.
- Calrissian is currently skipped in CI due to `pycalrissian` distribution constraints; tested locally as needed.
