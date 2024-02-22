data = {}
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file', type=str, help='Input file')
parser.add_argument('-o', '--output', type=str, help='Output directory')
args = parser.parse_args()


count = 0
with open(args.file,'r') as texto:
	for line in texto:
		if count < 2:
			count+=1
		else:
			if 'Name' in line:
				header = line
				linha = line.split()
				patients = {}
				for i, patient in enumerate(linha):
					if i > 2:
						patients[patient] = i
			else:
				linha = line.split()
				gene = linha[2]
				data[gene] = {}
				for patient in patients.keys():
					data[gene][patient] = linha[patients[patient]]



patient_data = {}
		
for gene, value in data.items():
	for patient in value.keys():
		if patient not in patient_data.keys():
			patient_data[patient] = {gene:value[patient]}
		else:
			patient_data[patient][gene] = value[patient]

for patient, genes in patient_data.items():
	with open(args.output+'/'+patient+'.tabular','w') as texto:
		texto.write('Gene Counts\n')
		for gene in genes.keys():
			texto.write(f'{gene} {genes[gene]}\n')
	

