
library(bayesrules)
library(tidyverse)

data(climbers_sub)
climbers <- climbers_sub %>% 
  select(expedition_id, member_id, success, year, season,
         age, expedition_role, oxygen_used)

write.csv(climbers, "climbers.csv",row.names = F)

data(airbnb)
write.csv(airbnb, "airbnb.csv", row.names  = F)