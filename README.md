# PathSnap-ML-Hackathon

Distributed GPS map-matching and route reconstruction for the PathSnap ML hackathon.

## Development checkpoint

The five-model baseline has been run on the supplied 80 training trips and 10 student-testing trips. The final evaluator partition is not used for development.

- `pathsnap_real_training.py`: spatially indexed candidate generation, feature preparation, five-model training, trip-grouped cross-validation, student-test evaluation, model export and plots.
- `pathsnap_real_tune.py`: Optuna TPE search for Histogram Gradient Boosting. Code prepared; execution and final tuned results not yet verified at this checkpoint.
- `src/hmm/hmm_decoder.py`: HMM/Viterbi decoder, tested with a separate practice trip.
- `deployment/practice_api.py` and `deployment/practice_ui.html`: working practice API and dashboard; cross-laptop access demonstrated. These still use the practice model, not the real-data seven-feature model.
- The older training notebook is a synthetic practice experiment, not the official baseline.

## Installation and actual development training

Use a compatible Python environment and run from the repository root.

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

Place the organiser-supplied data in `data/train/<trip_id>/` and `data/student_test/<trip_id>/`. Each trip directory must contain matching .track, .nodes, .arcs and .route files. Raw data and processed caches are kept local.

```bash
python -u pathsnap_real_training.py prepare
python -u pathsnap_real_training.py train
python -u pathsnap_real_tune.py
```

The baseline writes model artifacts to `artifacts/official_baseline/` and metrics, confusion matrices and plots to `results/official_baseline/`. The tuning stage writes to `artifacts/official_tuning/` and `results/official_tuning/`. Generated artifacts and full experiment logs from the executed Mac run are not included in this checkpoint and must be uploaded separately, subject to the event's sharing and repository size rules.

## Baseline status

See [development results checkpoint](docs/development-checkpoint.md) for rounded metrics transcribed from the completed training terminal output. These are provisional reference-label metrics, not independently verified per-GPS-fix accuracy.

Histogram Gradient Boosting is the provisional selection by mean training-trip cross-validation Macro F1. Random Forest is slightly stronger on student-test Macro F1 and Top-1 proxy accuracy.

## Practice deployment

The existing practice API requires the previously generated local `/tmp/pathsnap_practice_tuned.joblib` and practice trip files in `~/Downloads/PathSnap_practice/`. Without these prerequisites it cannot run from a fresh clone.

```bash
python -m uvicorn deployment.practice_api:app --host 0.0.0.0 --port 8001
```

Open `http://localhost:8001/ui` or `/docs`. Use a trusted network for remote access. The practice UI is currently served from the API; separate UI hosting on Laptop 2 and real-model integration are still pending.

## Remaining work

- Validate the provisional reference alignment and resolve numerical warnings.
- Complete and verify real-data Bayesian optimisation.
- Compare classifier-only and HMM/Viterbi routes on permitted development trips.
- Integrate the real trained model into the API and UI, then support the reserved trips for final evaluation.
- Retain actual experiment artifacts and complete the technical report.

AI assistance has been used for implementation guidance and scripts; the team must review and understand its work and comply with event disclosure requirements.
