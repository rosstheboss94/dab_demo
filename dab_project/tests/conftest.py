import pytest
#comment
@pytest.fixture(scope="session")
def spark():
    # from databricks.connect import DatabricksSession
    # spark = DatabricksSession.builder.getOrCreate()
    # return spark

    try:
        from databricks.connect import DatabricksSession
        spark = DatabricksSession.builder.getOrCreate()
    except ImportError:
        try:
            from pyspark.sql import SparkSession
            spark = SparkSession.builder.getOrCreate()
        except:
            raise ImportError("Neither Databricks Session or Spark Session are available")
    return spark