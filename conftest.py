def pytest_sessionfinish(session, exitstatus):
    if exitstatus == 0:
        print("\nDeployed")
