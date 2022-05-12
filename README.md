# Filtrado de variantes

<p align="center"><a href="http://www.inmegen.gob.mx/" target="_blank" rel="noopener noreferrer"><img width="2000" height= '250' src="public/INMEGEN_logo.jpg" alt="INMEGEN logo"></a></p>

# Propósito

Comparar las variantes de pacientes con las variantes de la base de datos de cosmos, el programa deberia de darle la opcion al usuario de poder agregar informacion como cual archivo o directorio con pacientes le gustaria comparar.

# Como usar este codigo

## Cosmic

<img width="1000" height= '200' src="public/cosmicLogo.jpg" alt="consmic_logo">
Para poder usar este codigo tendras que hacer una cuenta en  <a href="https://cancer.sanger.ac.uk/cosmic/register">COSMIC</a> e incluir tu usuario y contrasena en el file install.sh en la carpeta root remplazando las variables "email" y "pass" con sus credenciales correspondientes.

# Corre el programa

Para poder correr el programa con todas sus funcionalidades tendremos que descargar un par de dependencias de software, para ello necesitaremos correr un script en shell el cual esta en el directorio principal.

(Ubuntu)

- sudo chmod +x run.sh
- sudo ./run.sh

# Testing

Para poder correr los tests

<img width="900" height= '300' src="public/testing-1.jpg" alt="INMEGEN logo">
El framework para testing que usaremos sera

Sobre el directorio prueba vamos a usar robot para los tests

python ../json_to_tsv.py input/test.json output/

python3 ../filter_variants.py input/cosmic_prueba.csv output/CA1154-1RNA_475686108_full.tsv output/

<img width="2000" height= '350' src="public/inmegen.jpg" alt="INMEGEN logo">

# ¿Dudas? Pregúntale a nuestros desarrolladores 📱

- Alejandra Cervera Taboada

Correo electrónico: acerverat@inmegen.gob.mx

Github: https://github.com/acerverat

- Carmen? (quien sea que sea rana-frog) xD

Correo electrónico: ?

Github: https://github.com/rana-frog

- Yonathan Jaramillo Ramírez

Número de celular: 5549134787

Correo electrónico: dercomputerschamane@gmail.com

Github: https://github.com/Yony6041
