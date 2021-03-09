# InstaBot
Piccolo programma scritto in Python che permette di ricavare una lista contenente tutte le persone che non ricambiano il follow nel social network Instagram.
### NOTA BENE: Non supporta 2FA, se si vuole utilizzarlo bisogna quindi disabilitare temporaneamente l'autenticazione a due fattori nel proprio account Instagram.

Prima di poter utilizzare il programma bisogna avere Python installato nella propria macchina e bisogna aver installato le seguenti librerie:
- NumPy
- Instaloader

In caso non siano già installate eseguire i seguenti comandi a riga di comando:
  pip install numpy
  pip install instaloader
  
Arrivati a questo punto, per poter utilizzare lo script, scarica il file python, posizionalo arbitrariamente dove vuoi e segui questo format per avviarlo:
  
  __python bot.py YourInstagramUsername YourInstagramPassword__
  
E' importante sottolineare che il programma non memorizza alcun username o password dell'utente che lo utilizza. 
Il programmma è ad uno stato molto primitivo e sicuramente in futuro evolverà, integrando una lista di persona che unfollowano l'user e che non necessariamente quest'ultimo segue.
