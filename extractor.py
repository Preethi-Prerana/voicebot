import nltk
from stop_words import get_stop_words
sw_nltk = get_stop_words('english')

symptoms=['itching','rashes','nodal','sneezing','shivering','chills','joint','stomach','acidity','ulcers','wasting','vomiting',
    'burning_micturition','spotting_urination','fatigue','gain','anxiety','cold','mood','loss','restlessness','lethargy','throat',
    'sugar','cough','high','sunken','breathlessness','sweating','dehydration','indigestion','headache','skin','dark','vomitting',
    'loss_of_appetite','behind','back','constipation','abdominal','diarrhoea','mild','yellow','yellowing','liver','fluid','swelling',
    'swelled','malaise','vision','phlegm','irritation','redness','sinus','runny','congestion','chest','limbs','heart','bowel','anal',
    'stool','anus','neck','dizziness','cramps','bruising','obesity','legs','vessels','puffy','thyroid','brittle','swollen','hungry',
    'extra_marital_contacts','lips','speech','knee','hip','weakness','stiff','joints','stiffness','spinning','balance','unsteadiness',
    'body','smell','bladder','foul','continuous','gases','internal','toxic','depression','irritability','muscle','sensorium','spots',
    'belly','abnormal','dischromic','watery','increased','polyuria','heredity','mucoid','rusty','concentration','visual','transfusion',
    'unsterile','coma','bleeding','distention','alcohol','sputum','veins','palpitations','walking','pimples','blackheads','scurring',
    'peeling','dusting','dents','inflamatory','blister','nose','ooze']

def extract_symptoms(text):
    words = [word for word in text.split() if word.lower() not in sw_nltk]
    symps=[symp for symp in words if symp.lower() in symptoms]
    new_text = ",".join(symps)
    return new_text