import os
from configparser import ConfigParser

class Config:
    def __init__(self, config_file="ui_config.ini"):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.config_file = os.path.join(base_dir, config_file)
        self.config = ConfigParser()
        self.config.read(self.config_file)
        if not os.path.exists(self.config_file):
            raise FileNotFoundError(f"Config file not found at: {self.config_file}")
        
    def get_page_title(self):
        return self.config["DEFAULT"].get("PAGE_TITLE")
    
    def get_llm_option(self):
        return self.config["DEFAULT"].get("LLM_OPTIONS").split(", ")
        
    def get_usecase_option(self):
        return self.config["DEFAULT"].get("USECASE_OPTION").split(", ")
        
    def get_groq_model_option(self):
        return self.config["DEFAULT"].get("GROQ_ALL_MODEL_OPTION").split(", ")