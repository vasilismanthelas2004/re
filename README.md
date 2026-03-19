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

## 🛠️ Εγκατάσταση (Installation)

Για να τρέξετε το πρόγραμμα, βεβαιωθείτε ότι έχετε εγκατεστημένη την **Python 3** στο σύστημά σας.

**Βήμα 1:** Κατεβάστε το project τοπικά στον υπολογιστή σας.

**Βήμα 2:** Ανοίξτε ένα τερματικό (Command Prompt, PowerShell ή Terminal) μέσα στον φάκελο του project.

**Βήμα 3:** Εγκαταστήστε τις απαραίτητες εξωτερικές βιβλιοθήκες εκτελώντας την παρακάτω εντολή:

```bash
pip install -r requirements.txt
```
τελος τραβα