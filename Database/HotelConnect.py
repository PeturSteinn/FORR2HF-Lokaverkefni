from mysql.connector import MySQLConnection, Error
from .python_mysql_dbconfig import read_db_config


class DbConnector:
    def __init__(self):
        self.db_config = read_db_config()
        self.status = ' '
        try:
            self.conn = MySQLConnection(**self.db_config)
            if self.conn.is_connected():
                self.status = 'OK'
            else:
                self.status = 'connection failed.'
        except Error as error:
            self.status = error

    def execute_function(self, func_header=None, argument_list=None):
        cursor = self.conn.cursor()
        try:
            if argument_list:
                func = func_header % argument_list
            else:
                func = func_header
            cursor.execute(func)
            result = cursor.fetchone()
        except Error as e:
            self.status = e
            result = None
        finally:
            cursor.close()
        return result[0]

    def execute_procedure(self, proc_name, argument_list=None):
        result_list = list()
        cursor = self.conn.cursor()
        try:
            if argument_list:
                cursor.callproc(proc_name, argument_list)
            else:
                cursor.callproc(proc_name)
            self.conn.commit()
            for result in cursor.stored_results():
                result_list = [list(elem) for elem in result.fetchall()]
        except Error as e:
            self.status = e
            print(e)
        finally:
            cursor.close()
        return result_list


class Address(DbConnector):
    def __init__(self):
        DbConnector.__init__(self)
    '''Höldum áfram með öll table-in í databaseinu...'''


class CommonPS(DbConnector):
    def __init__(self):
        DbConnector.__init__(self)

    def HireEmployee(self, Param_Zip, Param_CityName, Param_CountryName, Param_StreetName, Param_BuildingNum, Param_HotelID, Param_EmpSSN, Param_Title, Param_LName, Param_FName, Param_Email, Param_Phone, Param_User, Param_Pass, Param_ApartNum=None,):
        rows_affected = 0
        result = self.execute_procedure('EmployeeHire_Bundle', [Param_Zip, Param_CityName, Param_CountryName, Param_StreetName, Param_BuildingNum, Param_ApartNum, Param_HotelID, Param_EmpSSN, Param_Title, Param_LName, Param_FName, Param_Email, Param_Phone, Param_User, Param_Pass])
        if result:
            rows_affected = int(result[0][0])
        return rows_affected

    def RegisterCustomer(self, Param_Zip, Param_CityName, Param_CountryName, Param_StreetName, Param_BuildingNum, Param_CusSSN, Param_LName, Param_FName, Param_Email, Param_Phone, Param_User, Param_Pass, Param_ApartNum=None):
        rows_affected = 0
        result = self.execute_procedure('CustomerRegister_Bundle', [Param_Zip, Param_CityName, Param_CountryName, Param_StreetName, Param_BuildingNum, Param_ApartNum, Param_CusSSN, Param_LName, Param_FName, Param_Email, Param_Phone, Param_User, Param_Pass])
        if result:
            rows_affected = int(result[0][0])
        return rows_affected

    def CheckAvailability(self, New_Start, New_End, Param_HotelID, Param_TypeID):
        rows_affected = 0
        result = self.execute_procedure('CheckAvailability', [New_Start, New_End, Param_HotelID, Param_TypeID])
        if result:
            return result
        else:
            return list()
