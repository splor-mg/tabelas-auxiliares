# tabelas-auxiliares

[![Updated](https://github.com/splor-mg/tabelas-auxiliares/actions/workflows/all.yaml/badge.svg)](https://github.com/splor-mg/tabelas-auxiliares/actions/)

## Pré-requisitos

Esse projeto utiliza Docker para gerenciamento das dependências. Para fazer _build_  da imagem execute:

```bash
docker build --tag tabelas-auxiliares .
```

## Uso

Para executar o container

```bash
docker run -it --rm --mount type=bind,source=$(PWD),target=/project tabelas-auxiliares bash
```

Uma vez dentro do container execute os comandos do make

```bash
make all
```

_Gerado a partir de [cookiecutter-datapackage@60f473f](https://github.com/splor-mg/cookiecutter-datapackage/commit/60f473f84c3e7fc9db0c193eecb09f2599013d7d)_
