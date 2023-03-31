"""""
VARIABILE – CONSTANTE
- Variabila este un container din memorie care stocheaza diferite valori.
- Constanta, la fel ca si variabila, e o locatie in memorie unde o valoare poate.
fi stocata. Spre deosebire de variabile, acestea nu isi schimba niciodata valorile.

TIPURI DE DATE
Cele mai folosite tipuri de date sunt:
- integer (int) - numar intreg (a = 125)
- float - numar zecimal (a = 12.5)
- bool - adevarat/fals (a = True, b = False)
- string - sir de caractere, delimitate de ghilimele (fruct = "mar")

CONDITIONALUL IF-ELSE
- Are tot timpul 2 ramuri. If are conditie urmata de : .Else nu mai are 
nevoie de conditie, deoarece inseamna in celalalt caz. De exemplu, 
daca un numar nu este par, automat este impar.

 STRUCTURI DE DATE
- LISTA - pastreaza mai multe valori intr-o singura variabila si diferite 
tipuri de date. Fiecare element din lista are index, incepand de la 0. 
Lista este ordonata, cand adaugam un element nou, acesta se va pune la final. 
De asemenea, este mutabila, adica putem adauga, sterge sau schimba 
elemente din ea si putem pune valori duplicate.
- TUPLU - Pastreaza mai multe valori intr-o singura variabila, valori care 
sunt imutabile, ordonate si pot fi duplicate. Din tuplu nu pot fi sterse sau 
adaugate valori.
- SET - Set-urile pastreaza mai multe valori unice, imutabile, intr-o 
variabila. Nu sunt ordonate sau indexate si pot fi adaugate sau sterse elemente.
- DICTIONAR - Pastreaza date de tip cheie : valoare. Sunt ordonate, 
mutabile, asadar valorile pot fi schimbate. Cheile sunt unice, nu putem avea 
chei duplicate.

FUNCTIE – PARAMETRU
- Functia este o zona de cod care poate fi folosita/refolosita de oricate 
ori avem nevoie. 
- Parametru reprezinta datele de intrare (input) intr-o functie, variabile 
declarate dar neinitializate.

CLASA – OBIECT
- Clasa reprezinta o structura logica care defineste comportamentul si 
starea obiectelor. Clasele in sine sunt obiecte. Dupa definire, aceasta 
poate fi utilizata pentru a crea obiecte de tipul respectiv.
- Obiectul reprezinta instanta clasei.
- Diferenta dintre cele doua este data de faptul ca o clasa este o tehnica 
folosita pentru a lega impreuna datele si functiile asociate iar obiectul 
este instanta creata a clasei.

SELECTOR
- Ajuta la identificare elementelor web in pagina.
- Tipuri de selectori:
         Id
         Link Text
         Partial Link Text
         Name
         Tag
         Class name
         CSS
         Xpath

TDD
- Este o abordare de software development in centrul careia stau testele 
automate scris pentru testarea aplicatiei.

AVANTAJE TDD
- Este scris doar codul necesar, simplu;
- Are design modular, codul avand o interfata clara si fiind usor de verificat;
- Este usor de intretinut, datorita interfetei clare;
- Mai usor de refactorizat;
- Are acoperire mare de testare;
- Testele documenteaza codul, aratand modalitatile in care ar trebui sa 
fie utilizat codul;
- Necesita mai putina depanare.

TESTARE UNITARA
- Termenul de „testare unitara” se refera la testarea individuala 
a unor unitati separate dintr-un sistem software.

BDD
- O abordare de software development in centrul careia stau scenariile 
de testare bazate pe asteptarile functionale ale clientului pentru aplicatie.

AVANTAJE
1. Oricine se va uita pe suita de teste automate, va intelege usor 
ce a fost testat si ce functionalitati ale aplicatiei au fost acoperite.
2. Focusul/atentia se muta pe scenariile de testare, astfel incat sansele 
de a asigura calitatea aplicatiei cresc.

GHERKIN
- Este un limbaj descriptiv folosit pentru maparea testelor automate 
cu o descriere de business usor de inteles de catre toti participantii 
la proiect.

API
- Reprezinta interfata de programare a aplicatiilor, niste comenzi bine 
documentate. Are rolul de a ajuta  programatorul sau interafata aplicatiei 
sa comunice cu logica din spate.

METODE HTTP
1. GET - utilizata pentru a prelua informatii din serverul de internet 
folosind un URI de solicitare specificat (Uniform Resource Identifier). 
2. HAD - este identica cu metoda GET, cu exceptia faptului ca serverul 
transfera doar linia de stare si sectiunea antet, fara corpul de raspuns.
3. POST -utilizata pentru a transmite date structurate importante catre 
servr, cum ar fi date despre clienti, incarcari de fisiere etc.
4. OPTIONS - utilizata pentru identificarea capaciatilor serverului Web, 
inainte de a face o cerere.
5. PUT - utilizata pentru a depune documente pe server, fiind inversul metodei GET.
6. DELETE – utilizata pentru a sterge resurse.
7. TRACE - utilizata de obicei pentru diagnosticare, putand da mai multe 
informatii despre traseul urmat de legatura HTTP.
8. CONNECT – utilizata in general de serverele intermediare.
"""""