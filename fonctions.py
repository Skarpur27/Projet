import requests

def get_day_avg_volume(days, coin, currency="usd"):
    """
    Récupère la moyenne du volume quotidien d'une cryptomonnaie donnée sur une période spécifiée en jours.
    """
    url = f"https://api.coingecko.com/api/v3/coins/{coin}/market_chart"

    params = {
        'vs_currency': currency,
        'days': days,
        'interval': 'daily',
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Provoque une exception pour les réponses HTTP non réussies
        data = response.json()
        volumes = [item[1] for item in data['total_volumes']]
        avg_volume = sum(volumes) / len(volumes)
        return avg_volume
    except requests.RequestException as e:
        print(f"Erreur lors de la requête: {e}")
        return None  # ou une valeur par défaut ou une autre gestion d'erreur


def get_top_cryptos(exclude=[], top_n=10):
    """
    Récupère les 'top_n' premières cryptomonnaies en excluant celles listées dans 'exclude'.
    """
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        'vs_currency': 'usd',
        'order': 'volume_desc',  # Tri par volume de trading décroissant
        'per_page': top_n + len(exclude),  # Permet de récupérer suffisamment de cryptos pour exclure certaines
        'page': 1
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        # Filtrer pour exclure les cryptos spécifiées
        filtered_cryptos = [crypto for crypto in data if crypto['id'] not in exclude][:top_n]
        return [crypto['id'] for crypto in filtered_cryptos]
    except requests.RequestException as e:
        print(f"Erreur lors de la requête: {e}")
        return []


def get_pairs_volume(base_currencies):
    """
    Récupère et renvoie le volume de trading des paires cotées en BTC ou ETH.
    """
    url = "https://api.coingecko.com/api/v3/exchanges/binance/tickers"
    volumes = []

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()['tickers']

        for ticker in data:
            if ticker['base'].lower() not in base_currencies and ticker['target'].lower() in base_currencies:
                pair = f"{ticker['base']}/{ticker['target']}"
                volume = ticker['converted_volume']['usd']  # volume converti en USD
                volumes.append((pair, volume))

    except requests.RequestException as e:
        print(f"Erreur lors de la requête: {e}")
        return []

    # Tri par volume décroissant et sélection des 3 premiers
    return sorted(volumes, key=lambda x: x[1], reverse=True)[:3]

def get_top_stablecoin_pairs_for_crypto(crypto_id):
    """
    Récupère et renvoie les trois principaux stablecoins par volume de trading pour une cryptomonnaie donnée.
    """
    url = "https://api.coingecko.com/api/v3/exchanges/binance/tickers"
    stablecoins = ['USDT', 'USDC', 'TUSD', 'DAI', 'PAX', 'BUSD']  # Liste des stablecoins
    crypto_pairs = []

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()['tickers']

        for ticker in data:
            if ticker['base'].upper() == crypto_id.upper() and ticker['target'] in stablecoins:
                pair = f"{ticker['base']}/{ticker['target']}"
                volume = ticker['converted_volume']['usd']  # Volume en USD
                crypto_pairs.append((pair, volume))

    except requests.RequestException as e:
        print(f"Erreur lors de la requête: {e}")
        return []

    # Tri par volume décroissant et sélection des 3 premiers
    return sorted(crypto_pairs, key=lambda x: x[1], reverse=True)[:3]