import unittest

from chargeback_evidence_builder.models import Record
from chargeback_evidence_builder.scoring import score_record


class DepthCheck17(unittest.TestCase):
    def test_017_control_mapping(self):
        record = Record(id="dispute-017", exposure=4686, signal=0.415, urgency=8)
        self.assertGreaterEqual(score_record(record), 0)
        self.assertLessEqual(score_record(record), 1)


if __name__ == "__main__":
    unittest.main()
