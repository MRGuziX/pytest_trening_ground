class TestFeatureName:

    def test_prompt_tuning(self, universal_step, feature_step):
        universal_step.clean_up_step()
        feature_step.use_changed_id()
