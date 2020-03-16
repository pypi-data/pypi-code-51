# Copyright 2018 Camptocamp SA
# Copyright 2016-19 ForgeFlow S.L. (https://www.forgeflow.com)
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

from odoo import api, fields, models


class StockQuant(models.Model):
    _inherit = "stock.quant"

    contains_unreserved = fields.Boolean(
        string="Contains unreserved products",
        compute="_compute_contains_unreserved",
        store=True,
    )

    @api.depends("product_id", "location_id", "quantity", "reserved_quantity")
    def _compute_contains_unreserved(self):
        for record in self:
            # Avoid error when adding a new line on manually Update Quantity
            if isinstance(record.id, models.NewId):
                record.contains_unreserved = False
                continue
            available = record._get_available_quantity(
                record.product_id, record.location_id
            )
            record.contains_unreserved = True if available > 0 else False
