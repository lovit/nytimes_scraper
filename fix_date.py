from glob import glob
import json

directory = 'output/korea'
paths = glob('{}/*.json'.format(directory))

for path in paths:
    with open(path, encoding='utf-8') as f:
        json_obj = json.load(f)
    date = path.split('/')[-1]
    date = '{}-{}-{}'.format(date[:4], date[4:6], date[6:])
    json_obj['date'] = date
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(json_obj, f, ensure_ascii=False, indent=2)