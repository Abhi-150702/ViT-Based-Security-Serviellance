from langchain_core.prompts import PromptTemplate
# from langchain_community.llms import Ollama
from langchain.chains import LLMChain
from langchain_ollama import OllamaLLM


class LLAMA:
    """
    Uses LLaMA2 model using LangChain to generate alerts from descriptions.
    """

    def __init__(self):
        self.llm = OllamaLLM(model="llama2")
        self.rules = {
            "loitering": ["person loitering", "standing"],
            "vehicle": ["car", "truck", "ship", "vehicle", "cruise", "bike"],
            "arson": ["fire", "arson", 'explosion'],
            "night activites": ['night', 'dark', 'suspicious activites', 'night activites']
        }

        self.prompt = PromptTemplate(
            input_variables=["description", "rules"],
            template="""
            You are a security analyst AI.

            You are given:
            - A list of rule categories and their related keywords
            - A description of what’s happening in an image

            Rules:
            {rules}

            Image Description:
            {description}

            Task:
            If the description semantically matches any rule or its keywords, generate a concise security alert (1–2 lines).

            If none match, return: "No alert triggered."
            """
        )

    def format_rules(self):
        """
        This function format rules dictionary to make readable string
        """

        formatted = []
        for category, keywords in self.rules.items():
            formatted.append(f"- {category.capitalize()}: " + ", ".join(keywords))
        return "\n".join(formatted)

    def generate_alert(self, description):
        """
        Pass description to LLaMA and get alert message.
        """

        rules_text = self.format_rules()

        # chain = LLMChain(llm=self.llm, prompt=self.prompt)
        chain = self.prompt | self.llm

        # getting response from the model based on the description and predefined rules.
        result = chain.invoke({
            "description": description,
            "rules": rules_text
        })

        try:
            print('result: ', result['text'].strip()[16:])
            return result['text'].strip()[16:]
        except Exception as e:
            print('result: ', result.strip()[16:])
            return result.strip()[16:]
