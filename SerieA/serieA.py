#! /usr/bin/env python3
import sys


class Squadra:
  def __init__(self,nome):
    self.nome = nome  # nome della squadra
    self.punti = 0    # punteggio iniziale
    self.golf = self.gols = 0  # gol fatti e subiti


  def __lt__(self,other):
    if self.punti == other.punti and self.golf==other.golf and self.gols==other.gols:
      return self.nome > other.nome
    return self.punti < other.punti or \
           (self.punti == other.punti and self.golf-self.gols < other.golf-other.gols)
  
  
  def __str__(self):
    return f"{self.nome:<12} {self.punti:>2}  {self.golf:>2}  {self.gols:>2}"
    # stampa in maniera incolonnata nome, punti, gol fatti e gol subiti  
    #<12 vuol dire usare 12 spazi e giustificare a sinistra
    # >2 vuol dire usare   2 spazi e giustificare a destra 

  
  def aggiungiPunti(self,punti):
    self.punti += punti

  
  def aggiungiGolf(self,golf):
    self.golf += golf

  
  def aggiungiGols(self,gols):
    self.gols += gols


# aggiorna per s1 e s2 i punti i gol fatti e subiti
def aggiorna_classifica(c,s1,g1,s2,g2):
  if g1>g2:
    p1=3
    p2=0
  elif g1<g2:
    p1=0
    p2=3
  else:
    p1=p2=1
  # aggiorno punti e gol delle due squadre
  if s1 not in c:
    c[s1] = Squadra(s1) # prima occorrenza di s1
    c[s1].aggiungiPunti(p1)
    c[s1].aggiungiGolf(g1)
    c[s1].aggiungiGols(g2)
  else:
    c[s1].aggiungiPunti(p1)
    c[s1].aggiungiGolf(g1)
    c[s1].aggiungiGols(g2)
    
  if s2 not in c:
    c[s2] = Squadra(s2) # prima occorrenza di s2
    c[s2].aggiungiPunti(p2)
    c[s2].aggiungiGolf(g2)
    c[s2].aggiungiGols(g1)
  else:
    c[s2].aggiungiPunti(p2)
    c[s2].aggiungiGolf(g2)
    c[s2].aggiungiGols(g1)


def crea_classifica(f):
  """legge le righe dei risultsti dal file f
  e aggiorna e crea la classifica risultante"""
  c = {}     # crea classifica vuota
  for linea in f:
    # suddivido la stringa in corrispondenza degli spazi
    a = linea.split()
    if len(a) == 0:
      continue   # linea senza risultati
    if len(a) != 4:
      raise RuntimeError(f"Linea non corretta: {linea}")
    # la linea ha 4 componenti, procediamo a valutare la partita
    g1 = int(a[0])
    g2 = int(a[1]) 
    aggiorna_classifica(c, a[2], g1, a[3], g2) 
  return c


def main(nomefile):
  with open(nomefile,"r") as f:
    # viene restituito il dizionario c contenente la classifica
    c = crea_classifica(f)
  # all'uscita del with il file f viene automaticamente chiuso
  squadre = [c[squadra] for squadra in c] # crea un array con le chiavisquadre
  #squadre.sort(reverse=True) # opzione 1
  squadre = sorted(squadre, reverse=True) # opzione 2

  # stampa intestazione classifica
  print("-----------------------")
  print("Squadra      Pu  GF  GS")
  print("-----------------------")
  
  # stampo la classifica secondo l'ordinamento ottenuto
  for s in squadre:
    print(s)
  return


if len(sys.argv)==2:
  main(sys.argv[1])
else:
  print(f"Uso:\n\t{sys.argv[0]} nomefile")