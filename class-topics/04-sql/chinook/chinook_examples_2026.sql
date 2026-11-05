select
	ar."ArtistId" ,
	ar."Name" ,
	al."AlbumId" ,
	al."Title"
from
	"Artist" ar
join "Album" al on
	ar."ArtistId" = al."ArtistId";

select
*
from
	"Artist" ar
left join "Album" al on
	ar."ArtistId" = al."ArtistId"
where al."ArtistId" is null

create view artists_with_no_albums as (
	select
		ar."ArtistId" ,
		ar."Name" ,
		al."AlbumId" ,
		al."Title"
	from
		"Artist" ar
	left join "Album" al on
		ar."ArtistId" = al."ArtistId"
	where al."ArtistId" is null
)

select * from artists_with_no_albums awna;

explain analyze select
	ar."Name",
	count(al."AlbumId") "Album Count"
from
	"Artist" ar
join "Album" al on
	ar."ArtistId" = al."ArtistId"
where ar."Name" != 'Led Zeppelin'
group by ar."ArtistId" , ar."Name"
having  count(al."AlbumId") >= 10
order by "Album Count" desc


explain analyze select "ArtistId", "Name", "Album Count"
from (select
	ar."ArtistId",
	ar."Name",
	count(al."AlbumId") "Album Count"
from
	"Artist" ar
join "Album" al on
	ar."ArtistId" = al."ArtistId"
where ar."Name" != 'Led Zeppelin'
group by ar."ArtistId" , ar."Name")
where  "Album Count" >= 10
order by "Album Count" desc
