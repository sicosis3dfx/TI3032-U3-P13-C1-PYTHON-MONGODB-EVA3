db.pedidos.aggregate(
    [
        {
            $match: {
                monto_total : {$gt: 500},
                fecha_pedido : {$gte: "2025-06-22T00:00:00Z"}
            }

        },
        {
            $lookup: {
                from: "clientes",
                localField: "cliente_id",
                foreignField: "_id",
                as: "cliente"

            }
        },
        {
            $unwind: "$cliente"
        },
        { $project: { _id: 0, cliente:1 } }
    ]
)