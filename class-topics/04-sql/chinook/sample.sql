select
	genre,
	sum(revenue)
from
	(
	select
		g."Name" genre,
		il."UnitPrice" * il."Quantity" revenue
	from
		"Genre" g
	join "Track" t on
		g."GenreId" = t."GenreId"
	join "InvoiceLine" il 
	on
		t."TrackId" = il."TrackId"
	join "Invoice" i 
	on
		il."InvoiceId" = i."InvoiceId"
)
where
	genre != 'Rock'
group by
	genre
having
	sum(revenue) >= 30
order by
	sum(revenue) desc
limit 5;

with cte1 as (
select
		g."Name" genre,
		il."UnitPrice" * il."Quantity" revenue
from
		"Genre" g
join "Track" t on
		g."GenreId" = t."GenreId"
join "InvoiceLine" il 
	on
		t."TrackId" = il."TrackId"
join "Invoice" i 
	on
		il."InvoiceId" = i."InvoiceId")
select
	genre,
	sum(revenue)
from
	cte1
where
	genre != 'Rock'
group by
	genre
having
	sum(revenue) >= 30
order by
	sum(revenue) desc
limit 5;


create or replace  view report as (select
		i."InvoiceDate" purchase_date,
		g."Name" genre, 
		t."Name" track,
		t."Composer" composer,
		t."UnitPrice" price,
		il."Quantity" qunatity,
		il."UnitPrice" * il."Quantity" revenue
from
		"Genre" g
join "Track" t on
		g."GenreId" = t."GenreId"
join "InvoiceLine" il 
	on
		t."TrackId" = il."TrackId"
join "Invoice" i 
	on
		il."InvoiceId" = i."InvoiceId")


select * from report r 

select count("ArtistId") as count from "Artist"
