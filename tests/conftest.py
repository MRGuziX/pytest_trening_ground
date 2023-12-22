import pytest

from data_storage.data_storage import DataStorage
from tests.feature_steps_lib.feature_steps import FeatureSteps
from tests.universal_steps_lib.universal_steps import UniversalSteps


@pytest.fixture(scope="function", name="data_storage")
def fixture_module_name_data_storage():
    return DataStorage()


@pytest.fixture(scope="function", name="universal_step")
def fixture_universal_class_init(data_storage):
    return UniversalSteps(data_storage)


@pytest.fixture(scope="function", name="feature_step")
def fixture_feature_class_init(data_storage):
    return FeatureSteps(data_storage)
