from odoo import models, fields, api


class BaseDocumentLayout(models.TransientModel):

    _inherit = 'base.document.layout'

    header_image = fields.Binary(string="Header Image", related='company_id.header_image', readonly=False)
    footer_image = fields.Binary(string="Footer Image", related='company_id.footer_image', readonly=False)
    # header_center_image = fields.Binary(string="Header Center Image", related='company_id.header_center_image', readonly=False)
    # header_right_image = fields.Binary(string="Header Right Image", related='company_id.header_right_image', readonly=False)

    def document_layout_save(self):
        res = super(BaseDocumentLayout, self).document_layout_save()
        for wizard in self:
            wizard.company_id.header_image
            wizard.company_id.footer_image
            # wizard.company_id.header_center_image
            # wizard.company_id.header_right_image
        return res

