import unittest

from chargeback_evidence_builder.models import Record
from chargeback_evidence_builder.scoring import score_record


class DepthCheck35(unittest.TestCase):
    def test_035_backlog_triage(self):
        record = Record(id="dispute-035", exposure=40226, signal=0.580, urgency=3)
        self.assertGreaterEqual(score_record(record), 0)
        self.assertLessEqual(score_record(record), 1)


if __name__ == "__main__":
    unittest.main()
