import pytest

from tests.feature_steps_lib.feature_steps import FeatureSteps
from tests.universal_steps_lib.universal_steps import UniversalSteps


@pytest.fixture(scope="session", name="universal_step")
def fixture_universal_class_init():
    return UniversalSteps()


@pytest.fixture(scope="session", name="feature_step")
def fixture_feature_class_init():
    return FeatureSteps()
