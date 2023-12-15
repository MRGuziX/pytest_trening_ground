class UniversalSteps:
    space_id = None
    space_status = "x"

    def clean_up_step(self):
        print(UniversalSteps.space_id + "BEFORE CHANGE")

        if UniversalSteps.space_status == "x":
            UniversalSteps.space_id = "changed id"

            print(UniversalSteps.space_id + "AFTER CHANGE")



