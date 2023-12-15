from tests.universal_steps_lib.universal_steps import UniversalSteps


class FeatureSteps:

    def use_changed_id(self):
        print("\n" + UniversalSteps.space_id + "BEFORE NEW FUNC USE")

        if UniversalSteps.space_id == "changed id":
            print("TRUE")
        else:
            print("False")
