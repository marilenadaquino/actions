import csv
import yaml

types_csv = "./schema/Research Ecosystem Annotation Schema - component types.csv"
terms_csv = "./schema/Research Ecosystem Annotation Schema - component terms.csv"
output_yml = "./schema/annotation-schema.yml"

split_by = {
    'enum':',',
    'domain':'|'
}

def dictify(input_csv):
    in_dict = csv.DictReader(open(input_csv))
    dictionary = {}
    for row in in_dict:
        ID = row['ID']
        dictionary[ID] = {}
        for key in row:
            k = key.lower().replace(' ','-')
            v = row[key]
            if k in split_by.keys():
                v = v.split(split_by[k])
            if row[key]:
                dictionary[ID][k] = v
    return dictionary

types = dictify(types_csv)
terms = dictify(terms_csv)
schema = {}
schema['types'] = types
schema['terms'] = terms
yaml.dump(schema,open(output_yml,'w'))
