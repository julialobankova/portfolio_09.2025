
DROP VIEW data.v_sales_day;

CREATE VIEW data.v_sales_day AS
(
	WITH sales_day AS 
	(
		SELECT p.people_id,"name", sales_id, date_sales, "month",pr.price as sales, cost_pack, cost_product, name_product, type_product, category_product
		FROM data.sales s
			JOIN data.sales_product sp ON sp.id_sales = s.sales_id
			JOIN data.product pr ON pr.id_product = sp.id_product
			JOIN data.people p ON s.cashier_id = p.people_id 
	),
	
	
	salary AS
	(
		SELECT date_work, SUM(salary*work_hours) AS sum_salary
		FROM data.schedule
			JOIN data.people USING(people_id)
		GROUP BY date_work
		ORDER BY date_work
)


	SELECT people_id,
			"name", 
			sales_id,
			sales_day.date_sales, 
			"month", 
			sales,
			cost_pack+cost_product as sum_cost_product,
        	(SELECT SUM(cost_rub) 
			FROM data.all_cost ),
			name_product, 
			type_product, 
			category_product, 
			COALESCE
				(
					(SELECT plan_sales 
					FROM data.plan_sales 
					WHERE data_sales = sales_day.date_sales
					)
				) /
			count(*) OVER 
						(
							PARTITION BY sales_day.date_sales 
							ORDER BY sales_day.date_sales 
							ROWS BETWEEN  UNBOUNDED PRECEDING and UNBOUNDED FOLLOWING
						) as plan_sales
	FROM sales_day
	LEFT JOIN salary ON sales_day.date_sales=date_work
	LEFT JOIN data.plan_sales ON sales_day.date_sales=data_sales
	ORDER BY date_sales	
);




