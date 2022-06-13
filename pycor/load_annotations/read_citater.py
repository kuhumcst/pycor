import pandas as pd
from pycor.utils import preprocess

citater = pd.read_csv('../../data/citat/keywords_citater.csv',
                      sep='\t',
                      encoding='utf-8'
                      )

annotated = pd.read_csv('../../data/hum_anno/keywords_07_03_2022.txt',
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

# extra_citat = pd.read_csv('../../data/citat/citatløs.tsv',
#                           sep='\t',
#                           encoding='utf-8'
#                           )

# anno = pd.read_csv('data/hum_anno/mellemfrekvente.txt',
#                    sep='\t',
#                    encoding='utf-8',
#                    na_values=['n', ' '])
#
# citater = pd.read_csv('H:/CST_COR/data/DDO_citater/citater_mellemfrekvente.tsv',
#                       sep='\t',
#                       encoding='utf-8')


citater = citater.dropna(subset=['ddo_lemma', 'ddo_dannetsemid', 'citat'])
#extra_citat = extra_citat.dropna(subset=['ddo_lemma', 'ddo_dannetsemid', 'citat'])


#citater = citater.merge(extra_citat,
#                        how='outer',
#                        on=['ddo_dannetsemid', 'ddo_lemma', 'citat']
#                        ).loc[:,['ddo_dannetsemid', 'ddo_lemma', 'citat']]

#extra_citat = extra_citat.dropna(subset=['citat2'])

#for row in extra_citat.itertuples():
#    citater = citater.append({'ddo_dannetsemid': row.ddo_dannetsemid,
#                              'ddo_lemma': row.ddo_lemma,
#                              'citat': row.citat2}, ignore_index=True)

citater['citat'] = citater['citat'].apply(preprocess.remove_special_char)
citater['citat'] = citater.apply(lambda row: preprocess.form_in_sentence(row.citat, row.ddo_lemma.lower()), axis=1)

citater.to_csv('../../data/keywords_citater_ren.tsv', sep='\t', encoding='utf8')