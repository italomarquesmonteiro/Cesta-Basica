salario_minimo <- readr::read_csv(".github\\.vscode\\Dataset\\Salário-Mínimo.csv")

# Transformar a coluna Data e Salário mínimo vigente
salario_minimo <- salario_minimo |>
  dplyr::mutate(
    Data = stringr::str_replace_all(Data, "\\.", "-"),  # Substituir pontos por hífens
    Data = lubridate::ym(Data),                         # Converter para tipo Date
    `Salário mínimo vigente` = as.integer(`Salário mínimo vigente`)  # Converter notação científica para inteiro
  ) |>
  dplyr::rename(smv = `Salário mínimo vigente`, data = Data)

# Verificar o resultado
print(salario_minimo)

salario_minimo |>
    dplyr::filter(data >= "1994-07-01") |>
    ggplot(aes(x = data, y = smv)) +
    geom_line()