-- check the total length of each of the datasets
select count(*) from 
-- check if county_fips is an identifier - its not
select county_flips, count(*) county_count from 2000 group by county_flips having count(*)>1 order by county_count
select * from where countu_flips in ('001','002','003')

-- check if state_fips is an identifier - its not

-- investigate the fips

-- look into matching names to state_fips

-- check if state_fips and county_fips together is an identifier - it is!

-- notice that fips are sometimes 0 padded, try to convert to integer to make them match

-- inner join count

-- outer join count

-- left join count

-- right join count

-- "anti-join"

-- cleaned up missing data report

-- change in state population with fips

-- change in state population with abbr

-- change in county population with fips
