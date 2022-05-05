# Filtrado de variantes

<p align="center"><a href="http://www.inmegen.gob.mx/" target="_blank" rel="noopener noreferrer"><img width="2000" height= '250' src="public/INMEGEN_logo.jpg" alt="INMEGEN logo"></a></p>

# Propósito

Comparar las variantes de pacientes con las variantes de la base de datos de cosmos, el programa deberia de darle la opcion al usuario de poder agregar informacion como cual archivo o directorio con pacientes le gustaria comparar.

# Como usar este codigo

## Cosmic

<img width="1000" height= '200' src="public/cosmicLogo.jpg" alt="consmic_logo">
Para poder usar este codigo tendras que hacer una cuenta en  <a href="https://cancer.sanger.ac.uk/cosmic/register">COSMIC</a> e incluir tu usuario y contrasena en el file install.sh en la carpeta root.

# Instalacion

Para poder correr el programa con todas sus funcionalidades tendremos que descargar un par de dependencias de software, para ello necesitaremos correr un script en shell el cual esta en el directorio principal.

(Ubuntu)

- sudo chmod +x install.sh
- sudo ./install.sh

# Testing

<img width="1000" height= '350' src="public/testing-1.jpg" alt="INMEGEN logo">
El framework para testing que usaremos sera <a href="https://robotframework.org/">Robot</a>

Sobre el directorio prueba vamos a usar robot para los tests

python ../json_to_tsv.py input/test.json output/

python3 ../filter_variants.py input/cosmic_prueba.csv output/CA1154-1RNA_475686108_full.tsv output/

## Recursos
- https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5425734/
- https://www.youtube.com/watch?v=ErTN5rE6t8s
- https://www.youtube.com/watch?v=le6wV8x8l-c
- https://researchtweet.com/free-bioinformatics-tools-for-genomic-testing/

<img width="2000" height= '350' src="public/inmegen.jpg" alt="INMEGEN logo">
