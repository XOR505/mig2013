""" Constantes globales """
# pour le recorder:
CHUNK = 1024 # nombre de bits enregistr�s par boucle
FORMAT = pyaudio.paInt16
CHANNELS = 1 # On est en mono
RATE = 44100 #Fr�quence

# Synchro:
COEFF_LISSAGE 3 # � d�terminer empiriquement
T_MIN 50 # blanc minimum avant le son
COEFF_COUPE 0.25 # en pourcent