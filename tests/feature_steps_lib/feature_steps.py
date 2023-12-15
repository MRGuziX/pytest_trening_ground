from tests.universal_steps_lib.universal_steps import UniversalSteps


class FeatureSteps:

    def use_changed_id(self):
        print("BEFORE NEW FUNC USE")
        print(UniversalSteps.space_id)

        if UniversalSteps.space_id == "changed id":
            print("TRUE")
        else:
            print("False")
