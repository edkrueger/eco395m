-- check the total length of each of the datasets
select count(*) from us_counties_2000;
select count(*) from us_counties_2010;

-- check if county_fips is an identifier - its not
select
	county_fips,
	count(*) county_count
from
	us_counties_2000
group by
	county_fips
having
	count(*) > 1
order by
	county_count desc
	
	
select
	*
from
	us_counties_2000
where
	county_fips in (
	select
		county_fips
	from
		us_counties_2000
	group by
		county_fips
	having
		count(*) > 1)
order by county_fips 

-- check if state_fips and county_fips together is an identifier - it is!

select
	count(*) count_
from
	us_counties_2000
group by
	state_fips , county_fips

select distinct state_fips from us_counties_2000
order by state_fips

select distinct state_fips from us_counties_2010
order by county_fips

select distinct county_fips from us_counties_2000
order by county_fips

select distinct county_fips from us_counties_2010
order by county_fips

-- inner join count

select count(*) from us_counties_2000 uc join us_counties_2010 uc2 on uc.state_fips = uc2.state_fips and uc.county_fips  = uc2.county_fips

-- outer join count

select count(*) from us_counties_2000 uc full join us_counties_2010 uc2 on uc.state_fips = uc2.state_fips and uc.county_fips  = uc2.county_fips

-- left join count

select count(*) from us_counties_2000 uc left join us_counties_2010 uc2 on uc.state_fips = uc2.state_fips and uc.county_fips  = uc2.county_fips

-- right join count

select count(*) from us_counties_2000 uc right join us_counties_2010 uc2 on uc.state_fips = uc2.state_fips and uc.county_fips  = uc2.county_fips


-- "anti-join"

select
	uc.geo_name,
	uc.state_us_abbreviation ,
	uc.state_fips,
	uc.county_fips,
	uc2.geo_name,
	uc2.state_us_abbreviation ,
	uc2.state_fips,
	uc2.county_fips
from
	us_counties_2000 uc
full join us_counties_2010 uc2 on
	uc.state_fips = uc2.state_fips
	and uc.county_fips = uc2.county_fips
where uc.state_fips is null or uc.state_fips is null or uc2.state_fips is null or uc2.state_fips is null

-- change in state population with fips
select
	uc.state_us_abbreviation, sum(uc.p0010001) pop_2000, sum(uc2.p0010001) pop_2010, sum(uc2.p0010001) - sum(uc.p0010001) pop_change
from
	us_counties_2000 uc
join us_counties_2010 uc2 on
	uc.state_fips = uc2.state_fips
	and uc.county_fips = uc2.county_fips
group by uc.state_us_abbreviation
order by pop_change desc

-- change in county population with fips
select
	uc2.geo_name, uc2.state_us_abbreviation, sum(uc.p0010001) pop_2000, sum(uc2.p0010001) pop_2010, sum(uc2.p0010001) - sum(uc.p0010001) pop_change
from
	us_counties_2000 uc
join us_counties_2010 uc2 on
	uc.state_fips = uc2.state_fips
	and uc.county_fips = uc2.county_fips
group by uc2.geo_name, uc2.state_us_abbreviation 
order by pop_change
