from times import compute_overlap_time, time_range

def test_given_input():
    """
    Tests if the expected time matches the result of the code for a generic test
    """
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    result = compute_overlap_time(large, short)
    expected = [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]
    print("Result:", result)
    print("Expected:", expected)
    assert result == expected, "Test failed!"

def test_no_overlap():
    """
    Tests if the expected time matches the result of the code for time ranges that don't overlap
    """
    large = time_range("2010-01-12 10:46:00", "2010-01-12 12:45:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00")
    result = compute_overlap_time(large, short)
    expected = []
    print("Result:", result)
    print("Expected:", expected)
    assert result == expected, "Test failed!"


def test_multiple_intervals_in_input():
    """
    Tests if the expected time matches the result of the code for time ranges with multiple intervals
    """
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00", 2, 60)
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    result = compute_overlap_time(large, short)
    expected = [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]
    print("Result:", result)
    print("Expected:", expected)
    assert result == expected, "Test failed!"

def test_input_ends_at_start_of_next():
    """
    Tests if the expected time matches the result of the code for a generic test
    """
    large = time_range("2010-01-12 10:00:00", "2010-01-12 10:30:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    result = compute_overlap_time(large, short)
    expected = []
    print("Result:", result)
    print("Expected:", expected)
    assert result == expected, "Test failed!"

if __name__ == "__main__":
    test_given_input()
    test_no_overlap()
    test_multiple_intervals_in_input()
    test_input_ends_at_start_of_next()



