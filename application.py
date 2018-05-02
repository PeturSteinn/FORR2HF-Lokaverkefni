from Database.HotelConnect import *


Common = CommonPS()

# Nokkur dæmi um virkni
#result = Common.HireEmployee(Param_Zip='000', Param_CityName='samplecity', Param_CountryName='samplecountry', Param_StreetName='samplestreet', Param_BuildingNum='45', Param_ApartNum=None, Param_HotelID=3, Param_EmpSSN='0000000000', Param_Title='Recept', Param_LName='samplelname', Param_FName='samplefname', Param_Email='sample@sample.com', Param_Phone='000-000-0000', Param_User='sampleuser', Param_Pass='samplepass')

#result = Common.RegisterCustomer(Param_Zip='000', Param_CityName='samplecity', Param_CountryName='samplecountry', Param_StreetName='samplestreet', Param_BuildingNum='100', Param_ApartNum='5C3', Param_CusSSN='0000000000', Param_LName='samplelname', Param_FName='samplefname', Param_Email='sample@sample.com', Param_Phone='000-000-0000', Param_User='sampleuser', Param_Pass='samplepass')

result = Common.CheckAvailability(New_Start='2018-05-08 13:00:00', New_End='2018-05-20 13:00:00', Param_HotelID=3, Param_TypeID=1)

print(result)
