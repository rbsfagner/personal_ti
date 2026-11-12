SELECT seller_id,
        sum(t1.price) as totalRevenue,
        count(DISTINCT t1.order_id) as qtSalles


FROM tb_order_items AS T1

GROUP BY seller_id

 
