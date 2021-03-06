#!/usr/bin/env python
# $Id$

"""An RFC-4217 asynchronous FTPS server supporting both SSL and TLS.

Requires PyOpenSSL module (http://pypi.python.org/pypi/pyOpenSSL).
"""

import os

from pyftpdlib import ftpserver
from pyftpdlib.contrib.handlers import TLS_FTPHandler

CERTFILE = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                        "keycert.pem"))

def main():
    authorizer = ftpserver.DummyAuthorizer()
    authorizer.add_user('user', '12345', '.', perm='elradfmw')
    authorizer.add_anonymous('.')
    ftp_handler = TLS_FTPHandler
    ftp_handler.certfile = CERTFILE
    ftp_handler.authorizer = authorizer
    # requires SSL for both control and data channel
    #ftp_handler.tls_control_required = True
    #ftp_handler.tls_data_required = True
    ftpd = ftpserver.FTPServer(('', 8021), ftp_handler)
    print "Serving FTPS on %s:%s" % ftpd.address
    ftpd.serve_forever()

if __name__ == '__main__':
    main()
