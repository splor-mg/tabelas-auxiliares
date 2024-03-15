library(data.table)

diretorio <- 'data-raw/misc/'
 
arquivos <- list.files(path = diretorio, pattern = "tbl-aux-acao-desc.* *\\.csv$"
                    , full.names = TRUE)

for (arquivo in arquivos){
  dados <- fread(arquivo, sep = ",")
  fwrite(dados, arquivo, sep = ",", quote ="")
}

