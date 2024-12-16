CREATE TABLE teachers (
    id bigserial,
    first_name varchar(25),
    last_name varchar(50),
    school varchar(50),
    hire_date date,
    salary numeric
);

INSERT INTO teachers (first_name, last_name, school, hire_date, salary)
VALUES ('Janet', 'Smith', 'F.D. Roosevelt HS', '2011-10-30', 36200),
       ('Lee', 'Reynolds', 'F.D. Roosevelt HS', '1993-05-22', 65000),
       ('Samuel', 'Cole', 'Myers Middle School', '2005-08-01', 43500),
       ('Samantha', 'Bush', 'Myers Middle School', '2011-10-30', 36200),
       ('Betty', 'Diaz', 'Myers Middle School', '2005-08-30', 43500),
       ('Kathleen', 'Roush', 'F.D. Roosevelt HS', '2010-10-22', 38500);

select first_name, last_name from teachers;
select * from teachers;

select * from teachers
where hire_date >= '2000-01-01'

select * from teachers
where hire_date >= '2000-01-01' and school = 'Myers Middle School'

select * from teachers
where hire_date >= '2000-01-01' or school != 'F.D. Roosevelt HS'

select * from teachers
where school like '%HS%'

select * from teachers
where school ilike '%hs%'

select * from teachers order by school desc

select * from teachers order by school asc, salary desc 

select concat(first_name, ' ', last_name) name, salary from teachers order 
by salary desc

select avg(salary) from teachers

select
	school,
	max(salary) max_salary,
	avg(salary) avg_salary,
	min(salary) min_salary
from
	teachers
where
	first_name != 'Janet'
group by
	school
having
	max(salary) > 60000
order by
	school





