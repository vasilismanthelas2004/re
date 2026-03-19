# 🏛️ Wikipedia City Scraper

![Python](https://img.shields.io/badge/python-3.x-blue.svg)
![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-4.x-green.svg)
![Requests](https://img.shields.io/badge/Requests-2.x-orange.svg)

Ένα Python script που εξάγει αυτόματα γεωγραφικά, δημογραφικά και μετεωρολογικά δεδομένα για πόλεις από τη Wikipedia. 

**Αυτό το project αναπτύχθηκε στα πλαίσια του μαθήματος "Θεωρία Υπολογισμού".** Βασίζεται σε μεγάλο βαθμό στη χρήση **Κανονικών Εκφράσεων (Regular Expressions - Regex)** για την αναζήτηση και εξαγωγή συγκεκριμένων μοτίβων πληροφορίας μέσα από το αδόμητο κείμενο (HTML/Text) της Wikipedia.

---

## 🚀 Δυνατότητες (Features)

Το πρόγραμμα λαμβάνει το URL μιας πόλης στη Wikipedia και εξάγει τα παρακάτω στοιχεία:

* **Όνομα** (Name)
* **Χώρα** (Country)
* **Πληθυσμός** (Population)
* **Έκταση** (Area σε km²)
* **Διοικητική Περιφέρεια** (Administrative Region)
* **Συντεταγμένες** (Coordinates)
* **Υψόμετρο** (Elevation σε m)
* **Ζώνη Ώρας** (Timezone)
* **Ετήσιες Θερμοκρασίες** (Υψηλότερη / Χαμηλότερη / Μέση)

---

## 🛠️ Εγκατάσταση & Εκτέλεση (Installation & Usage)

Για να τρέξετε το πρόγραμμα, βεβαιωθείτε ότι έχετε εγκατεστημένη την **Python 3**.

1. **Κατεβάστε** το project τοπικά στον υπολογιστή σας.
2. **Ανοίξτε** ένα τερματικό (Command Prompt, PowerShell ή Terminal) μέσα στον φάκελο του project.
3. **Εγκαταστήστε** τις απαραίτητες εξωτερικές βιβλιοθήκες εκτελώντας την παρακάτω εντολή:
   ```bash
   pip install -r requirements.txt
   ```
4. **Τρέξτε** το πρόγραμμα περνώντας το URL της πόλης που θέλετε με το flag `--url`:
   ```bash
   python main.py --url https://en.wikipedia.org/wiki/Larissa
   ```
   *(Εναλλακτικά, αν τρέξετε απλά `python main.py`, το πρόγραμμα θα σας ζητήσει να κάνετε επικόλληση το URL διαδραστικά).*

---

## 📦 Χρήση ως Module (Importing)

Λόγω της αντικειμενοστρεφούς αρχιτεκτονικής του, μπορείτε εύκολα να ενσωματώσετε αυτό το scraper σε δικά σας Python projects, κάνοντας import τις κλάσεις `scraperPage` και `Find`.

**Παράδειγμα χρήσης:**

```python
from main import scraperPage, Find

# 1. Δώστε το URL και πάρτε το αντικείμενο soup
url = "https://en.wikipedia.org/wiki/Thessaloniki"
scraper = scraperPage(url)
page_soup = scraper.getPage()

# 2. Αν η σελίδα κατέβηκε επιτυχώς, περάστε την στην κλάση Find
if page_soup:
    finder = Find(page_soup)
    
    # 3. Καλέστε όποια μέθοδο χρειάζεστε!
    city_name = finder.findName()
    population = finder.findPopulation()
    
    print(f"Η πόλη {city_name} έχει {population} κατοίκους.")
```

---

## 🧩 Αρχιτεκτονική Κώδικα (Under the Hood)

Ο κώδικας είναι οργανωμένος σε δύο βασικές Κλάσεις:

* **`scraperPage`**: Χρησιμοποιεί το `requests` και το `BeautifulSoup` για να ανακτήσει την HTML σελίδα με custom headers (`User-Agent`).
* **`Find`**: Περιέχει όλη τη λογική της ανάλυσης κειμένου. Δέχεται το καθαρό κείμενο της σελίδας και μέσω στοχευμένων συναρτήσεων `re.findall()` και `re.search()` απομονώνει τις ζητούμενες πληροφορίες. Διαθέτει μηχανισμούς `try...except` για την αποφυγή σφαλμάτων (IndexError) σε περίπτωση ελλιπών δεδομένων στη Wikipedia.