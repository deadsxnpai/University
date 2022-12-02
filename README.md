# University
Repo for labs and courseworks


select sum(price) total from items inner join purchases on purchases.itemId = Items.itemId  inner join users on users.userId = purchases.userId where users.age between 18 and 25 and purchases.date > date_trunc('month', current_timestamp - interval '1 month') and date < date_trunc('month', current_timestamp);
