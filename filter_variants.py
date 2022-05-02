import pandas as pd
import numpy as np
import sys

# se requiere un archivo de cosmic
# Descargue CosmicMutantExport.tsv de https://cancer.sanger.ac.uk/cosmic/download 
# Quite entradas duplicadas y me quede con las columnas: GENOMIC_MUTATION_ID     LEGACY_MUTATION_ID      HGVSG
# con eso anoto el cosmic id al final del procesamiento

#sampleId = sys.argv[4]
cosmic  = sys.argv[1]
myFile = sys.argv[2]
outDir = sys.argv[3]

df = pd.read_csv(myFile,delimiter="\t")
#print(df.info())

sampleId = df.iloc[1,0].split('_')[0]
print("Filtrando muestra:", sampleId)

# columnas y orden sugerido por Carmen 25 feb
new_cols = ['muestra',
            'chromosome',
            'v_transcripts_hgnc',
            'v_transcripts_hgvsc',
            'v_transcripts_hgvsp',
            's_variantFrequencies',
            'alleleDepths',
            's_totalDepth',
            'v_dbsnp',
            'v_transcripts_exons',
            'HGVSG',
            'v_transcripts_consequence',
            'v_clinvar_alleleOrigins',
            'v_clinvar_phenotypes',
            'v_clinvar_significance',
            'v_gnomad_allAf',
            'v_gnomad_amrAf',
            'v_revel',
            'v_transcripts_polyPhenPrediction',
            'v_transcripts_siftPrediction',
            'v_transcripts_introns',
            'cytogeneticBand']

#print(list(df.columns))
print("Total variantes:",df.shape[0])
new_df = df.loc[df['filters'] == "['PASS']"]
print("Total variantes filtro pass:",new_df.shape[0])
new_df = new_df.loc[new_df['v_clinvar_significance'] != "['benign']"]

new_df = new_df.loc[new_df['v_clinvar_significance'] != "['likely benign']"]
new_df = new_df.loc[new_df['v_clinvar_significance'] != "['benign', 'likely benign']"]
print("Total variantes filtro clinvar:",new_df.shape[0])
new_df = new_df.loc[(new_df['v_gnomad_allAf'] < 0.01) | (new_df['v_clinvar_significance'].notna())]
new_df = new_df.loc[(new_df['v_gnomad_allAf'] < 0.01) | (new_df['v_clinvar_significance'] != "['not provided']")]
new_df = new_df.loc[(new_df['v_gnomad_amrAf'] < 0.01) | (new_df['v_clinvar_significance'].notna())]
new_df = new_df.loc[(new_df['v_gnomad_amrAf'] < 0.01) | (new_df['v_clinvar_significance'] != "['not provided']")]
print("Total variantes filtro frecuencia < 0.01:",new_df.shape[0])
new_df = new_df.loc[new_df['v_transcripts_consequence'] != "['synonymous_variant']"]
new_df = new_df.loc[new_df['v_transcripts_consequence'] != "['upstream_gene_variant']"]
new_df = new_df.loc[new_df['v_transcripts_consequence'] != "['downstream_gene_variant']"]
new_df = new_df.loc[new_df['v_transcripts_bioType'] == 'protein_coding']
print("Total variantes filtro locus:",new_df.shape[0])
new_df = new_df.loc[new_df['s_totalDepth'] > 10]
print("Total variantes filtro cobertura > 10:",new_df.shape[0])

# Inicia seccion formateo y limpieza de campos
new_df['v_revel'] = new_df['v_revel'].apply(lambda x: pd.to_numeric(x.split(':')[1].split("}")[0]) if pd.notna(x) else '0')
new_df['s_variantFrequencies']=new_df['s_variantFrequencies'].apply(lambda x: str(x).replace("[","").replace("]",""))
new_df['alleleDepths']=new_df['s_alleleDepths'].apply(lambda x: str(x).replace("[","").replace("]",""))
new_df['v_dbsnp'] = new_df['v_dbsnp'].apply(lambda x: str(x).replace("[","").replace("]","").replace("'",""))
new_df['v_transcripts_consequence'] = new_df['v_transcripts_consequence'].apply(lambda x: str(x).replace("[","").replace("]","").replace("'",""))
new_df['v_clinvar_alleleOrigins'] = new_df['v_clinvar_alleleOrigins'].apply(lambda x: str(x).replace("[","").replace("]","").replace("'",""))
new_df['v_clinvar_phenotypes'] = new_df['v_clinvar_phenotypes'].apply(lambda x: str(x).replace("[","").replace("]",""))
new_df['v_clinvar_significance'] = new_df['v_clinvar_significance'].apply(lambda x: str(x).replace("[","").replace("]","").replace("'",""))
new_df['HGVSG_1'] = new_df['chromosome'].apply(lambda x: str(x).replace("chr",""))
new_df['HGVSG_2'] = new_df['v_hgvsg'].apply(lambda x: str(x).split(":")[1])
new_df['HGVSG'] = new_df.apply(lambda x: x.HGVSG_1 + ":" + x.HGVSG_2, axis=1)

# Extraer columnas para tabla final
new_df = new_df[new_cols]
#print(new_df.shape)

# Mas formateo y limpieza
new_df.columns = new_df.columns.str.replace("v_", "")
new_df.columns = new_df.columns.str.replace('^s_','',regex=True)
new_df.columns = new_df.columns.str.replace("transcripts_", "")
new_df = new_df.replace(np.NaN, '-')

#revisar por que tengo que volverla a definir y no se conserva del archivo anterior
new_df['muestra'] = sampleId

new_df.to_csv(outDir+"/"+sampleId+"_topVariants.tsv",sep="\t",index=False)

#new_df['begin'] = pd.Series([], dtype=int)
#new_df['end'] = pd.Series([], dtype=int)
#new_df.loc[new_df['v_begin']<=new_df['v_end'],'begin'] = new_df['v_begin']
#new_df.loc[new_df['v_begin']>new_df['v_end'],'begin'] = new_df['v_end']
#new_df.loc[new_df['v_end']<new_df['v_begin'],'end'] = new_df['v_begin']
#new_df.loc[new_df['v_end']>=new_df['v_begin'],'end'] = new_df['v_end']
#new_df['begin'] = new_df['begin'].values.astype(np.int64)
#new_df['end'] = new_df['end'].values.astype(np.int64)

cosmic = pd.read_csv(cosmic,delimiter="\t",skipinitialspace=True)
print("Leyendo archivo cosmic:",cosmic.shape)

merged = pd.merge(new_df,cosmic,left_on='HGVSG',right_on='HGVSG',how="left")
print("Tabla final (renglones,columnas):",merged.shape)
outfile=outDir+"/"+sampleId+"_topVariants_cosmic.tsv"
print("Tabla final:",outfile)
merged.to_csv(outfile,sep="\t",index=False)

