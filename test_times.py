import pytest
import yaml
from times import compute_overlap_time, time_range

# Load the fixture data from the YAML file
with open('fixtures.yaml', 'r') as file:
    fixtures = yaml.safe_load(file)

# Prepare the test data
test_data = []
for fixture in fixtures:
    for key, value in fixture.items():
        time_range_1 = time_range(*value['time_range_1'])
        time_range_2 = time_range(*value['time_range_2'])
        expected = [tuple(e) for e in value['expected']]
        test_data.append((time_range_1, time_range_2, expected))

@pytest.mark.parametrize("first_range, second_range, expected_overlap", test_data)
def test_time_range_overlap(first_range, second_range, expected_overlap):
    assert compute_overlap_time(first_range, second_range) == expected_overlap
