from times import compute_overlap_time, time_range
import pytest

"""
Uses pytest.mark.parametrize to define multiple test cases.
Each test case includes:
first_range (first set of time intervals)
second_range (second set of time intervals)
expected_overlap (the expected overlapping intervals)
This is for the 4 test cases:
1) Overlapping intervals within the same time range
2) Non-overlapping intervals
3) Overlapping intervals
4) Adjacent but non-overlapping intervals.
"""
@pytest.mark.parametrize("first_range, second_range, expected_overlap",
[(time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00"),
  time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60),
  [("2010-01-12 10:30:00","2010-01-12 10:37:00"), ("2010-01-12 10:38:00", "2010-01-12 10:45:00")]),
  (time_range("2010-01-12 10:00:00", "2010-01-12 11:00:00"),
  time_range("2010-01-12 12:30:00", "2010-01-12 12:45:00", 2, 60),
  []),
  (time_range("2010-01-12 10:00:00", "2010-01-12 13:00:00", 3, 900),
  time_range("2010-01-12 10:40:00", "2010-01-12 11:20:00", 2, 120),
  [("2010-01-12 10:40:00","2010-01-12 10:50:00"), ("2010-01-12 11:05:00", "2010-01-12 11:20:00")]),
  (time_range("2010-01-12 10:00:00", "2010-01-12 11:00:00"),
  time_range("2010-01-12 11:00:00", "2010-01-12 12:45:00"),
  [])
])
def test_time_range_overlap(first_range, second_range, expected_overlap):
    """
    Asserts that the output of compute_overlap_time matches the expected_overlap for each set of inputs.
    """
    assert compute_overlap_time(first_range, second_range) == expected_overlap