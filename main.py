import requests
from fonctions import get_day_avg_volume,get_top_cryptos,get_pairs_volume,get_top_stablecoin_pairs_for_crypto

"""
# Test de la fonction pour BTC et ETH en différentes devises
btc_vol_usd = get_day_avg_volume(7, 'bitcoin', 'usd')
eth_vol_eur = get_day_avg_volume(7, 'ethereum', 'eur')

print("Volume moyen quotidien de Bitcoin (USD):", btc_vol_usd)
print("Volume moyen quotidien d'Ethereum (EUR):", eth_vol_eur)

# Récupération des 10 premières cryptomonnaies les plus liquides après BTC et ETH
#top_cryptos = get_top_cryptos(exclude=['bitcoin', 'ethereum'], top_n=10)

# Calcul du volume moyen quotidien pour chaque cryptomonnaie
for crypto in top_cryptos:
    avg_vol = get_day_avg_volume(7, crypto)
    print(f"Volume moyen quotidien de {crypto.upper()} (USD): {avg_vol}")


# Base currencies (BTC et ETH)
base_currencies = ['btc', 'eth']

# Obtention des top 3 des paires avec le plus de volume
top_pairs_volume = get_pairs_volume(base_currencies)

# Affichage des résultats
for pair, volume in top_pairs_volume:
    print(f"Pair: {pair}, Volume (USD): {volume}") 
"""

# Exemple avec Bitcoin
top_btc_stablecoin_pairs = get_top_stablecoin_pairs_for_crypto("BTC")

# Affichage des résultats
for pair, volume in top_btc_stablecoin_pairs:
    print(f"Pair: {pair}, Volume (USD): {volume}")