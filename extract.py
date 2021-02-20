import json

f = open('train_features_5.jsonl')
my_lines = f.readlines()

label = []
inputs = []

for i in range(0, len(my_lines)):
    lines_dict = json.loads(my_lines[i])  # returns a dictionary

    label = lines_dict['label']
    if label == 0 or label == 1:

        new_input = [label, lines_dict['general']['has_debug'], lines_dict['general']['has_tls'],
                     lines_dict['general']['has_relocations'], lines_dict['general']['has_signature'],
                     lines_dict['general']['has_resources']]

        if lines_dict['general']['imports'] > 0:  # if has imports 1 if not 0
            new_input.append(1)
        else:
            new_input.append(0)

        if lines_dict['general']['exports'] > 0:  # if has exports 1 if not 0
            new_input.append(1)
        else:
            new_input.append(0)

        for section in lines_dict['section']['sections']:
            new_input.append(section['entropy'])
            break  # extract entropy from first section

        inputs.append(new_input)

