import unittest

from chargeback_evidence_builder.models import Record
from chargeback_evidence_builder.scoring import score_record


class DepthCheck11(unittest.TestCase):
    def test_011_edge_case_review(self):
        record = Record(id="dispute-011", exposure=71419, signal=0.860, urgency=5)
        self.assertGreaterEqual(score_record(record), 0)
        self.assertLessEqual(score_record(record), 1)


if __name__ == "__main__":
    unittest.main()
