# Odoo MODEL details

# sale.order model

location: odoo16/odoo/addons/sale/models/sale_order.py

```
    @api.depends('price_unit', 'discount')
    def _compute_price_reduce(self):
        for line in self:
            line.price_reduce = line.price_unit * (1.0 - line.discount / 100.0)
```

Postoje ove proračunate vrijednosti
```
    # The price_reduce field should not be used for amounts computations
    # because of its digits precision. It will be removed in next version.
    price_reduce = fields.Float(
        string="Price Reduce",
        compute='_compute_price_reduce',
        digits='Product Price',
        store=True, precompute=True)
    price_subtotal = fields.Monetary(
        string="Subtotal",
        compute='_compute_amount',
        store=True, precompute=True)
    price_tax = fields.Float(
        string="Total Tax",
        compute='_compute_amount',
        store=True, precompute=True)
    price_total = fields.Monetary(
        string="Total",
        compute='_compute_amount',
        store=True, precompute=True)
    price_reduce_taxexcl = fields.Monetary(
        string="Price Reduce Tax excl",
        compute='_compute_price_reduce_taxexcl',
        store=True, precompute=True)
    price_reduce_taxinc = fields.Monetary(
        string="Price Reduce Tax incl",
        compute='_compute_price_reduce_taxinc',
        store=True, precompute=True)

```

# XML template

Prikaz opisa

```
<td name="td_name"><span t-field="line.name"/></td>
```

