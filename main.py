import pytest
import conftest

if __name__ == "__main__":
    # Specify the test name to be executed
    test_name = "test_title"  # Replace with your desired test name

    # Specify test data to be passed
    test_data = "test-data"  # Replace with your desired test data

    # Pass the test name and test data as command-line arguments
    pytest_args = ["-v", "--test-name", test_name,  "-k", test_name, "--test-data", test_data, "MyTests.py"]

    # Execute the test
    pytest.main(pytest_args)
