class AIServices:
    @staticmethod
    def analyze_report(prompt:str) -> str:

        #-------------------
        # We will call an API but for now lets just return
        #-------------------
        return f"""
                prompt:{prompt[:30]},
                AI response: Response
                """