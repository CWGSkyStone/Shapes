import os 
import sys
import json

class ParseText:
    def __init__(self,  path):
        self.path = path
        self.data = self.load_json()
        
        
    @staticmethod    
    def resource_path(relative_path):
        if hasattr(sys, "_MEIPASS"):
            return os.path.join(sys._MEIPASS, relative_path)
        return os.path.join(os.path.abspath("."), relative_path)    
        
    def load_json(self):
        try:
            full_path = ParseText.resource_path(self.path)
            with open(full_path, "r", encoding="utf8") as file:
                return json.load(file)
        except FileNotFoundError:
            print("Hiba 404: A fájl nem található!")
            return {}
      
    def getMenu(self, name):
        menu = self.data.get(name, {})
        title = menu.get("title", "")
        options = menu.get("options", {})
        optionLines = "\n".join([f"[{key}.] {value}" for key, value in options.items()])
        return f"{title}\n\n{optionLines}"
    def getNoOption(self, name):
        return self.data.get(name, {}).get("no_option", "Érvénytelen opció!")