## TODO

### Input da file locale `config.py`
1. **[DONE]** api key 
2. path della directory in cui scaricare i file (output)
 
### Input dall'utente run-time:
1. number of images to download
2. query
3. max number of threads


#### 1. Ottenere la lista degli url delle immagini da scaricare (`get_images_urls` function)
- rendere più parametrica la funzione
- **[DONE]** controllare di non superare il numero totale dei link disponibili per quella query (è nel campo "totalHits" della response)
- NOTA: se si vogliono scaricare più di 200 immagini
    - API di pixabay ha limite di 200 link per pagina: aggiustare, scaricando più di una pagina, in modo da superare tale limite
    
#### 2. Definire cosa fa ogni singolo thread in una funzione:
- ottenere un link dalla lista immagini ancora da scaricare
- scaricare il file immagine dal link
- salvarlo nella directory stabilita
    
#### 3. Gestire i thread
    
Esempio banale:
    
    finché non ho scaricato tutte le immagini
        scorro tutti i thread 
            se ce n'è uno che ha finito (non "isalive")
                prendo dalla lista il primo link e lo assegno da scaricare al thread
    