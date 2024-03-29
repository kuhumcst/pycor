import argparse
import pathlib

import pandas as pd
from pycor.utils import preprocess
from pycor.utils.lemmatizer import form_in_sentence


############# THIS SCRIPT CLEANS QUOTES #################
# when the script is running, the user has to input the index of the target token.
# this is a "quick solution" so the code will fail if anything but a number is inputted
# (bad, I know, but that is how it is. I don't have time to fix it)

def clean_citater(anno_file: pathlib.Path, input_quotes: pathlib.Path, save_path: pathlib.Path) -> None:
    citater = pd.read_csv(input_quotes,
                          sep='\t',
                          encoding='utf-8'
                          )

    annotated = pd.read_csv(anno_file,
                            sep='\t',
                            encoding='utf-8',
                            na_values=['n', ' '],
                            usecols=['ddo_entryid', 'ddo_lemma', 'ddo_homnr',
                                     'ddo_ordklasse', 'ddo_betyd_nr', 'ddo_dannetsemid'
                                     ],
                            index_col=False
                            )
    citater['ddo_dannetsemid'] = citater['ddo_dannetsemid'].astype('int64')

    citater = citater.merge(annotated, how='outer', on=['ddo_dannetsemid'])
    citater = citater.dropna(subset=['ddo_lemma', 'ddo_dannetsemid', 'citat'])

    # clean for special characters
    citater['citat'] = citater['citat'].apply(preprocess.remove_special_char)
    # find the target in sentence
    citater['citat'] = citater.apply(lambda row: form_in_sentence(row.citat, row.ddo_lemma.lower()), axis=1)

    citater.to_csv(save_path, sep='\t', encoding='utf8')


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("input_quotes", type=pathlib.Path)  # quote_file to clean
    parser.add_argument("anno_file", type=pathlib.Path)  # annotated file
    parser.add_argument("save_path", type=pathlib.Path)  # path to save cleaned quotes

    args = parser.parse_args()

    clean_citater(args.anno_file, args.input_quotes, args.save_path)

    input_quotes = '../../data/citat/citater_mellemfrekvente.tsv'  # quote_file to clean
    anno_file = '../../data/hum_anno/mellemfrek_18_08_22.tsv'  # annotated file
    save_path = '../../data/citat/mellem_citater_ren.tsv'  # path to save cleaned quotes
