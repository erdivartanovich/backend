from flask import Blueprint, render_template, request, jsonify, redirect
from app.controllers.main_controller import MainController
from app.services.helper import Helper
from app.middlewares.rbac import get_previllege

main = Blueprint('main', __name__)


@main.route('/init/<param>', methods=["POST"])
@get_previllege
def init(param, *args, **kwargs):
    accessible = jsonify(kwargs['accessible'])
    return accessible


@main.route('/upss')
def not_found():
    return render_template("admin/base/404.html")

@main.route('/home')
def index(*args, **kwargs):
    return MainController.index()


@main.route('/attendees')
def get_attendees():
    return MainController.getAttendees()


@main.route('/purchased-attendees')
def get_purchased_attendees():
    return MainController.getPurchasedAttendees()


@main.route('/payments')
def getPayments():
    return MainController.getPayments()


@main.route('/authorize-payments')
def getPaymentsAuthorize():
    return MainController.getAuthorizePayments()


@main.route('/tickets')
def get_tickets():
    return MainController.getTickets()


@main.route('/referals')
def get_referals():
    return MainController.getReferals()


@main.route('/booths')
def get_booths():
    return MainController.getBooths()

@main.route('/checkin-list')
def get_checkin_list():
    return MainController.getCheckinList()

@main.route('/')
def login():
    return render_template('admin/auth/login.html')

@main.route('/login')
def gotologin():
    return render_template('admin/auth/login.html')

@main.route('/accounts')
def get_accounts():
    return MainController.getAccounts()


@main.route('/hackatonproposals')
def get_proposal():
    return MainController.getHackatonProposal()


@main.route('/speakers')
def get_speakers():
    return MainController.getSpeakers()


@main.route('/events')
def get_events():
    return MainController.getEvents()


@main.route('/events/kanban')
def event_kanban():
    return MainController.show_event_kanban()


@main.route('/stages')
def get_stages():
    return MainController.getStages()


@main.route('/schedules')
def schedules():
    return MainController.getSchedules(request)


@main.route('/adduserphoto')
def adduserphoto():
    return render_template('admin/users/user_photos_add.html')


@main.route('/manual-certificate')
def manual_certificate():
    return render_template('admin/accounts/manual_certificate.html')

@main.route('/email-certificate')
def manual_account_certificate():
    return render_template('admin/accounts/manual_account_certificate.html')


@main.route('/partners', methods=['GET', 'POST'])
def partners():
    if(request.method == 'GET'):
        return MainController.getPartners()

@main.route('/hackers')
def getHackers():
    return MainController.getHackers()


@main.route('/checkedin_hackers')
def getHackersCheckin():
    return MainController.getCheckedInHackers()


@main.route('/partnerspj', methods=['GET'])
def partners_pj():
    if(request.method == 'GET'):
        return MainController.getPartnersPj()


@main.route('/entrycashlogs')
def entrycashlog():
    return MainController.getEntryCashLogs()


@main.route('/sponsors')
def sponsors():
    return MainController.getSponsors()


@main.route('/password')
def changepassword():
    return MainController.changepassword()


@main.route('/rundownlist')
def rundownlist():
    return MainController.getRundownList()


@main.route('/redeemcodes')
def redeemcodes():
    return MainController.getRedeemCodes()


@main.route('/speaker-candidates')
def speaker_candidates():
    return MainController.showSpeakerCandidates()


@main.route('/admin_order')
def admin_order():
    return MainController.admin_order()


@main.route('/entrycashlogsfilter')
def report_finance_source():
    return MainController.getReportFinance(request)


@main.route('/notification')
def notification():
    return render_template('admin/communication/notification.html')


@main.route('/post')
def post():
    return render_template('admin/communication/post.html')


def site_map():
    routes_list = Helper.site_map()
    print(routes_list)
    return jsonify(routes_list)


@main.route('/sources')
def source():
    return MainController.getSource(request)


@main.route('/invoices')
def invoices():
    return MainController.getInvoice()


@main.route('/invoices/<id>')
def invoice(id):
    return MainController.showInvoice(id)


@main.route('/report-feed')
def report_feed():
    return MainController.getReportFeed(request)


@main.route('/sponsor-feeds')
def sponsor_feed():
    return MainController.getSponsorFeed(request)


@main.route('/sponsor-post')
def sponsor_post():
    return MainController.getSponsorPost(request)


@main.route('/packages')
def package_management():
    return MainController.getPackageManagement(request)


@main.route('/package-purchase')
def package_purchase():
    return MainController.getPackagePurchase(request)


@main.route('/ticket-transfer-logs')
def ticket_transfer_logs():
    return MainController.getTransferLog(request)


@main.route('/payment-verification')
def verification_list():
    return MainController.verification_list()


@main.route('/admin-verification')
def admin_verification_list():
    return MainController.admin_verification_list()


@main.route('/payment-verification/submit-proof')
def submit_proof():
    return MainController.submit_proof(request)


@main.route('/email-verification', methods=['GET'])
def email_address_verification():
    token = request.args.get('token')
    return MainController.verify_email_address(token)


@main.route('/reset-password')
def reset_password_user():
    return MainController.reset_password_user(request)

@main.route('/referal_details/<id>')
def referal_info(id):
    return MainController.get_referal_info(id)

@main.route('/questioners')
def questioner_list():
    booth_id = request.args.get('booth_id', 'null')
    return render_template('admin/questioners/questioners.html', booth_id=booth_id)

@main.route('/regions')
def region_list():
    return MainController.region_list()

@main.route('/regions/<id>')
def region_show(id):
    return MainController.region_show(id)

@main.route('/regions/create')
def region_add():
    return MainController.region_add()

@main.route('/certificate-<id>.pdf')
def get_certificate(id):
    return MainController.get_certificate(id)


@main.route('/certificate-email-<name>.pdf')
def email_certificate(name):
    return MainController.email_certificate(name)
