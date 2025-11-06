select count(distinct fscskey) from pls_fy2009_pupld09a pfpa;
-- 9299

select count(*) from pls_fy2009_pupld09a pfpa;
-- 9299

select count(distinct stabr) from pls_fy2009_pupld09a pfpa;
-- 55

select distinct on (stabr) * from  pls_fy2009_pupld09a;

select count(distinct fscskey) from  pls_fy2009_pupld09a;
-- 9299

select count(distinct fscskey) from  pls_fy2014_pupld14a;
-- 9305

select count(distinct l09.fscskey) fscskey09_count, count(distinct l14.fscskey) fscskey14_count  from pls_fy2009_pupld09a l09 join pls_fy2014_pupld14a l14 on l09.fscskey = l14.fscskey
select count(distinct l09.fscskey) fscskey09_count, count(distinct l14.fscskey) fscskey14_count  from pls_fy2009_pupld09a l09 full join pls_fy2014_pupld14a l14 on l09.fscskey = l14.fscskey

select count(distinct l09.fscskey) - count(distinct l14.fscskey) num_old_libraries  from pls_fy2009_pupld09a l09 left join pls_fy2014_pupld14a l14 on l09.fscskey = l14.fscskey
select count(distinct l14.fscskey) - count(distinct l09.fscskey) num_new_libraries  from pls_fy2009_pupld09a l09 right join pls_fy2014_pupld14a l14 on l09.fscskey = l14.fscskey

select stabr, num_lib from  (select
	l09.stabr, count(l09.fscskey) num_lib
from
	pls_fy2009_pupld09a l09
left join pls_fy2014_pupld14a l14 on
	l09.fscskey = l14.fscskey
where l14.fscskey is null
group by l09.stabr) order by num_lib desc

select stabr, num_lib from  (select
	l14.stabr, count(l14.fscskey) num_lib
from
	pls_fy2009_pupld09a l09
right join pls_fy2014_pupld14a l14 on
	l09.fscskey = l14.fscskey
where l09.fscskey is null
group by l14.stabr) order by num_lib desc


select l09.*
from
	pls_fy2009_pupld09a l09
left join pls_fy2014_pupld14a l14 on
	l09.fscskey = l14.fscskey
where l14.fscskey is null and l09.stabr = 'TX'

select l14.*
from
	pls_fy2009_pupld09a l09
right join pls_fy2014_pupld14a l14 on
	l09.fscskey = l14.fscskey
where l09.fscskey is null and l14.stabr = 'TX'


