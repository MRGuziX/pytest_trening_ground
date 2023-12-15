from data_storage.data_storage import DataStorage


class UniversalSteps:

    def clean_up_step(self):
        print("BEFORE CHANGE")
        print(DataStorage.space_id)

        if DataStorage.space_status == "x":
            DataStorage.space_id = "changed id"

            print("AFTER CHANGE")
            print(DataStorage.space_id)

    def create_obj_step(self):
        model = UniversalSteps()
        model.foo = "bar"



