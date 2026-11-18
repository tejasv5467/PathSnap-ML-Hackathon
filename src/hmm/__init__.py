"""
src/hmm
=======
HMM + Viterbi route reconstruction for PathSnap GPS map-matching.

Modules
-------
hmm_decoder    : HMMDecoder class — build road graph, compute transitions,
                 run Viterbi decoding.
route_evaluator: Metrics for evaluating predicted routes against ground truth.
"""

from .hmm_decoder import HMMDecoder
from .route_evaluator import (
    pointwise_accuracy,
    route_continuity,
    sequence_f1,
    evaluate_full,
)

__all__ = [
    "HMMDecoder",
    "pointwise_accuracy",
    "route_continuity",
    "sequence_f1",
    "evaluate_full",
]
