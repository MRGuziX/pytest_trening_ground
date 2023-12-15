from data_storage.data_storage import DataStorage
from tests.universal_steps_lib.universal_steps import UniversalSteps


class FeatureSteps:

    def use_changed_id(self):
        print("BEFORE NEW FUNC USE")
        print(DataStorage.space_id)

        if DataStorage.space_id == "changed id":
            print("TRUE")
        else:
            print("False")

    # def get_into_created_model_step(self):
    #     pass
