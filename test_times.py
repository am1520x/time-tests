from times import compute_overlap_time, time_range

def test_given_input():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    result = compute_overlap_time(large, short)
    expected = [('2010-01-12 10:30:00', '2010-01-12 10:45:00'), ('2010-01-12 10:31:00', '2010-01-12 10:45:00')]
    print("Result:", result)
    print("Expected:", expected)
    assert result == expected, "Test failed!"

if __name__ == "__main__":
    test_given_input()
