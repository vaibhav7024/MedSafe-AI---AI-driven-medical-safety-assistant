import json
import os
from thefuzz import process, fuzz

DB_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'medicine_db.json')

class MedicineDatabase:
    def __init__(self):
        self.medicines = self._load_db()
        # Create a list of names and salts for fuzzy matching
        self.medicine_names = [med['name'] for med in self.medicines]
        self.salt_names = [med['active_salt'] for med in self.medicines]
        
    def _load_db(self):
        try:
            with open(DB_PATH, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def fuzzy_match_medicine(self, query, threshold=80):
        """
        Attempts to match a user query to a known medicine in the database.
        Checks both brand names and active salts.
        """
        if not query:
            return None
            
        # Match against names
        name_match = process.extractOne(query, self.medicine_names, scorer=fuzz.token_sort_ratio)
        if name_match and name_match[1] >= threshold:
             return self.get_medicine_by_name(name_match[0])
             
        # Match against salts
        salt_match = process.extractOne(query, self.salt_names, scorer=fuzz.token_sort_ratio)
        if salt_match and salt_match[1] >= threshold:
             return self.get_medicine_by_salt(salt_match[0])
             
        return None

    def get_medicine_by_name(self, name):
        for med in self.medicines:
            if med['name'].lower() == name.lower():
                return med
        return None

    def get_medicine_by_salt(self, salt):
        for med in self.medicines:
            if med['active_salt'].lower() == salt.lower():
               return med
        return None

    def check_interactions(self, medicine_list):
        """
        Checks for interactions among a list of identified medicines.
        """
        interactions_found = []
        n = len(medicine_list)
        
        for i in range(n):
            for j in range(i + 1, n):
                med1 = medicine_list[i]
                med2 = medicine_list[j]
                
                if med1 and med2:
                    # Check med1's interactions for med2's salt
                    for interaction in med1.get('interactions', []):
                         # Loose match on salt for interactions
                         if fuzz.token_sort_ratio(interaction['interacting_drug_salt'].lower(), med2['active_salt'].lower()) > 85:
                             interactions_found.append({
                                 "med1": med1['name'],
                                 "med2": med2['name'],
                                 "severity": interaction['severity'],
                                 "description": interaction['description']
                             })
                             
                    # Check med2's interactions for med1's salt
                    for interaction in med2.get('interactions', []):
                         if fuzz.token_sort_ratio(interaction['interacting_drug_salt'].lower(), med1['active_salt'].lower()) > 85:
                             # ensure we don't add duplicates
                             duplicate = False
                             for existing in interactions_found:
                                 if (existing['med1'] == med2['name'] and existing['med2'] == med1['name']) or \
                                    (existing['med1'] == med1['name'] and existing['med2'] == med2['name']):
                                    duplicate = True
                                    break
                             if not duplicate:
                                 interactions_found.append({
                                     "med1": med2['name'],
                                     "med2": med1['name'],
                                     "severity": interaction['severity'],
                                     "description": interaction['description']
                                 })
                                 
        return interactions_found
