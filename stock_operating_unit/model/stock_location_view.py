# -*- coding: utf-8 -*-
from openerp import api, fields, models
from openerp import tools
from .stock import StockLocation


class StockLocationView(StockLocation, models.Model):
    # This class is solely for PABI2
    _name = 'stock.location.view'
    _auto = False

    def init(self, cr):
        tools.drop_view_if_exists(cr, self._table)
        cr.execute("""CREATE or REPLACE VIEW %s as (%s)""" %
                   (self._table,
                    "select * from stock.location",))
