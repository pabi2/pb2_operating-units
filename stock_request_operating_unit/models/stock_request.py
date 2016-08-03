# -*- coding: utf-8 -*-
from openerp import models, fields, api


class StockRequest(models.Model):

    _inherit = 'stock.request'

    operating_unit_id = fields.Many2one(
        'operating.unit',
        string='Operating Unit',
        default=lambda self: self.env['res.users'].
        operating_unit_default_get(self._uid),
    )

    @api.model
    def _prepare_picking(self, request):
        res = super(StockRequest, self)._prepare_picking(request)
        res['operating_unit_id'] = request.operating_unit_id.id
        return res

    @api.onchange('operating_unit_id')
    def _onchange_operating_unit_id(self):
        types = self.env['stock.picking.type'].search(
            [('code', '=', 'internal'), ('warehouse_id.operating_unit_id',
                                         '=', self.operating_unit_id.id)])
        print types
        self.picking_type_id = types and types[0] or False
        res = {'domain': {'picking_type_id': [('id', 'in', types._ids)]}}
        return res
