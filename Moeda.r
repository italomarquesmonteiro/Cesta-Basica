#
library(tidyverse)

moedas <- tibble::tribble(
  ~nome, ~cifrao, ~inicio, ~fim,
  "Cruzeiro", "Cr$", "01/11/1942", "12/12/1967",
  "Cruzeiro Novo", "NCr$", "13/12/1967", "14/05/1970",
  "Cruzeiro", "NCr$", "13/12/1967", "14/05/1970",
  "Cruzeiro", "Cr$", "15/5/1970", "27/2/1986",
  "Cruzado", "Cz$", "28/02/1986", "15/01/1989",
  "Cruzado Novo", "NCz$", "16/01/1989", "15/03/1990",
  "Cruzeiro", "Cr$", "16/03/1990", "31/07/1993",
  "Cruzeiro Real", "CR$", "01/08/1993", "30/06/1994",
  "Real", "R$", "01/07/1994", "26/07/2024") |>
  dplyr::mutate(
    inicio = lubridate::dmy(inicio),
    fim = lubridate::dmy(fim),
    tempo_anos = round(lubridate::time_length(lubridate::interval(inicio, fim), "years")
    )) |> 
  readr::write_csv(".github\\.vscode\\Dataset\\Moedas.csv")
