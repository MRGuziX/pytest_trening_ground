class TestFeatureName:

    def test_prompt_tuning(self, universal_step, feature_step, module_name_data_storage):
        universal_step.clean_up_step()
        feature_step.use_changed_id()

        universal_step.create_obj_step()
        feature_step.get_into_created_model_step()

        # module_name_data_storage.prompt_tuned = "FooBar"
