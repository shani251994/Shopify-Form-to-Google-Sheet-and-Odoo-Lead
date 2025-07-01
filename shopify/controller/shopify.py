from odoo import http
from odoo.http import request
import json
import logging

_logger = logging.getLogger(__name__)

class ShopifyLeadController(http.Controller):

    @http.route('/shopify/lead', type='http', auth='public', csrf=False, methods=['OPTIONS', 'POST'])
    def create_lead(self, **kwargs):
        if request.httprequest.method == 'OPTIONS':
            # Handle preflight request
            return http.Response(
                status=200,
                headers=[
                    ('Access-Control-Allow-Origin', '*'),
                    ('Access-Control-Allow-Methods', 'POST, OPTIONS'),
                    ('Access-Control-Allow-Headers', 'Content-Type'),
                ]
            )

        try:

            data = json.loads(request.httprequest.data)

            name = data.get("name")
            email = data.get("email")
            phone = data.get("phone")
            message = data.get("message")

            partner = request.env['res.partner'].sudo().search([('email', '=', email)], limit=1)

            if not partner:
                partner = request.env['res.partner'].sudo().create({
                    'name': name,
                    'email': email,
                    'phone': phone,
                    'customer_rank': 1,
                })

            lead = request.env['crm.lead'].sudo().create({
                'name': name or "Shopify Lead",
                'contact_name': name,
                'email_from': email,
                'phone': phone,
                'description': message,
                'partner_id': partner.id,

            })

            return http.Response(
                json.dumps({'status': 'success', 'lead_id': lead.id, 'partner_id': partner.id}),
                content_type='application/json',
                status=200,
                headers=[('Access-Control-Allow-Origin', '*')]
            )

        except Exception as e:
            _logger.exception("Error creating lead from Shopify")
            return http.Response(
                json.dumps({'status': 'error', 'error': str(e)}),
                content_type='application/json',
                status=500,
                headers=[('Access-Control-Allow-Origin', '*')]
            )
