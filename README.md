# Instrucciones de uso

## Instación mediante Poetry

### Requisito previo: 

- Python ^3.8
- Poetry ^1.0

### Instalación

```
poetry install
```

### Uso

```
# Mostrar ayuda general
poetry run example --help

# Mostrar ayuda de la función contar palabras
poetry run example count-words --help

# Listar las <N_PALABRAS> mas frecuentes de un <ARCHIVO>
# N_PALABRAS es 10 por defecto
poetry run my-script count-words ARCHIVO -n N_PALABRAS
```

