class UniversalSteps:
    space_id = None
    space_status = "x"

    def clean_up_step(self):
        print("BEFORE CHANGE")
        print(UniversalSteps.space_id)

        if UniversalSteps.space_status == "x":
            UniversalSteps.space_id = "changed id"

            print("AFTER CHANGE")
            print(UniversalSteps.space_id)



