from openerp import http
import math


class MRPOnline(http.Controller):
    @http.route(['/mrp/mo/',
                 '/mrp/mo/page/<int:page>/'], auth='public', website=True)
    def index(self, page=1, **kw):
        pagelines = 10
        model = http.request.env['mrp.production']
        search = kw.get('search', None)
        domain = []
        if search:
            domain.append(('name', 'ilike', search))

        records = model.search(domain, (page-1) * pagelines, pagelines)
        count = model.search_count(domain)
        page_count = int(math.ceil(float(count)/pagelines))

        return http.request.render('mrp_online.index', {
            'records': records,
            'search': search,
            'page_count': page_count,
            'page': page
        })


