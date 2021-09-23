import argparse
import sys

from decouple import config
from helpers.RoleControlHelper import RoleControlHelper

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='details',
                                     usage='use "%(prog)s --help" for more information')
    parser.add_argument(
        '--argument', default=None,
        help='Usage python PATHTO/kimly_authz_check.py url port *** ' +
             '\n requires following external files; ' +
             '\n query.sql' +
             '\n .env  ' +
             '\n ***' +
             '\n .env file contents:' +
             '\n db_user=...' +
             '\n db_pass=...' +
             '\n ***  ')
    parser.add_argument('url', nargs='*', default=[1], help='URL of db being checked for kimly yetki bundles.')
    parser.add_argument('port', nargs='*', default=5432, help='PORT of db')
    args = parser.parse_args()

    db_user = config('db_user', default='')
    db_pass = config('db_pass', default='')
    if sys.argv.__len__() > 2 and sys.argv[2] is not None:
        db_port=sys.argv[2]
    else:
        db_port='5432'

    print("Accessing db: " + sys.argv[1] + ":" + db_port)
    roleControlHelper = RoleControlHelper()
    roleControlHelper.find_missing_roles(db_user, db_pass, sys.argv[1], db_port)
