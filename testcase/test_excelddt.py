#import openpyxl
#import pytest
#import yaml
#class TestData:
#
#    def getexcel(filename,sheetname):
#        workbook=openpyxl.open(filename)
#        sheet=workbook[sheetname]
#        data=[]
#
#        for row in sheet.iter_rows(min_row=2,values_only=True):
#         data.append(row)
#        return data
#
#    testdata=getexcel("test_data.xlsx","logindata")
#    @pytest.mak.parameterize("username,password",testdata)
#
#
#    def testyml(filename):
#       with open(filename,"r",encoding="utf-8") as f:
#
#          return yaml.safe(f)
#
#    testyaml=testyml("test_yaml.yaml")
#    params=[(item["username"],item["password"],item["expected"]) for item in testyaml]
#
#    @pytest.mark.parametrize("username,password,expected",params)
#
#    def getExcel(filename,sheetname):
#
#        workbook=openpyxl.load_workbook(filename=)
#        sheet=workbook[sheetname]
#        data=[]
#
#        for row in sheet.iter_rows(min_row=2,values_only=True)
#            data.append(row)
#        return data
#    testexcel=getexcel("test_data.xslx","logindata")
#    @pytest.mark.parametrize("username,paswword",testexcel)
#
#
#    def yaml(filename):
#
#       with open(filename,"r",encoding="utf-8") as f:
#          return yaml.safe_load(f)
#
#    testyaml=yaml("test_yaml.yaml")
#
#    testyml=[(item["username"],item["password"],item["expected"]) for item in testyaml]
#
#    @pytest.mark.parametrize("username,password,expected",testyml)
#
