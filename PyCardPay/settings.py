from collections import namedtuple

Settings = namedtuple(
    'Settings',
    [
        'url_status_change',
        'url_status',
        'url_pay',
    ],
)


test_settings = Settings(
    url_pay = 'https://sandbox.cardpay.com/MI/cardpayment.html',
    url_status = 'https://sandbox.cardpay.com/MI/service/order-report',
    url_status_change = 'https://sandbox.cardpay.com/MI/service/order-change-status',
)

live_settings = Settings(
    url_pay = 'https://cardpay.com/MI/cardpayment.html',
    url_status = 'https://cardpay.com/MI/service/order-report',
    url_status_change = 'https://cardpay.com/MI/service/order-change-status',
)
