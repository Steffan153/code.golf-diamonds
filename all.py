import json

with open('all.json') as f:
  j = json.loads(f.read())
  a = []
  for x in j:
    if x['login'] == 'Shanethegamer' and all(y['scoring'] != x['scoring'] or y['login'] == x['login'] or y['hole'] != x['hole'] or y['lang'] != x['lang'] or y[x['scoring']] > x[x['scoring']] for y in j):
      a += [x]
  open('d.json', 'w').write(json.dumps(a))
