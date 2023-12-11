# %%
import nltk
from nltk import CFG

# %%
grammar = CFG.fromstring(
    """
S -> PROG
PROG -> 'PROGRAMA' '[id]' SENTS 'FINPROG'
SENTS -> SENT SENTS
SENTS -> SENT
SENT -> '[id]' '=' ELEM '[op_ar]' ELEM
SENT -> '[id]' '=' ELEM
SENT -> 'SI' COMPARA 'ENTONCES' SENTS 'SINO' SENTS 'FINSI'
SENT -> 'SI' COMPARA 'ENTONCES' SENTS 'FINSI'
SENT -> 'REPITE' ELEM 'VECES' SENTS 'FINREP'
SENT -> 'IMPRIME' ELEM
SENT -> 'IMPRIME' '[txt]'
SENT -> 'LEE' '[id]'
SENT -> '#' '[comentario]'
ELEM -> '[id]' | '[val]'
COMPARA -> '[id]' '[op_rel]' ELEM
"""
)

# %%
grammar.start()

# %%
grammar.productions()

# %%
