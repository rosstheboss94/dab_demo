import pytest

@pytest.fixture(scope="session")
def spark():
    from databricks.connect import DatabricksSession
    spark = DatabricksSession.builder.getOrCreate()
    return spark
