import collections

from helpers.DBHelper import DbHelper

import sys


class RoleControlHelper:
    failed = 0

    def find_missing_roles(self, db_user, db_pass, url, port):
        con = DbHelper.get_db_connection(db_user, db_pass, url, port)
        full_set = DbHelper.read_from_table(con)
        missing_yetki_detays = []
        temp_id_list = []
        for x in full_set:
            if x[0] not in temp_id_list:
                temp_id_list.append(x[0])
                missing_yetki_detays.append(x)
            else:
                missing_yetki_detays=[dupl_id for dupl_id in missing_yetki_detays if dupl_id[0] != x[0]]

        if missing_yetki_detays.__len__() != 0:
            print("kul_yetki_detay check mismatch. Found no matching kul_yetki_detay record for the following: ")
            print(missing_yetki_detays)
            sys.exit(1)
        else:
            print("kul_yetki_detay check finished- No Mismatch")
            sys.exit(0)
