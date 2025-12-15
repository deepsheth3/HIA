class PromptBuilder:
    @staticmethod
    def build_health_report_prompt(extracted_text:str) ->str:
        return f"""
                You are a medical analysis assistant.

                Given the following blood test report, do the following:
                1. Identify key metrics (e.g. hemoglobin, cholesterol, glucose, etc.)
                2. Indicate whether each metric is normal, high, or low.
                3. Provide a simple explanation in plain English.
                4. Suggest general lifestyle advice (no diagnosis, no medication).

                Blood Report:
                {extracted_text}

                Respond in a clear, structured format.
                """
