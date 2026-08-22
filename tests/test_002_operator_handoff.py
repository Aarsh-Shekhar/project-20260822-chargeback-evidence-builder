import unittest

from chargeback_evidence_builder.models import Record
from chargeback_evidence_builder.scoring import score_record


class DepthCheck2(unittest.TestCase):
    def test_002_operator_handoff(self):
        record = Record(id="dispute-002", exposure=4405, signal=0.815, urgency=7)
        self.assertGreaterEqual(score_record(record), 0)
        self.assertLessEqual(score_record(record), 1)


if __name__ == "__main__":
    unittest.main()
