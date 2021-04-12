#coding:utf-8
import xlrd
class ExcelR():
    def __init__(self,excelpath,sheetName = "Sheet1"):
        self.date = xlrd.open_workbook("user.xlsx")
        self.table = self.date.sheet_by_name(sheetName)
        self.keys = self.table.row_values(0)
        self.rownum = self.table.nrows
        self.colnum = self.table.ncols

    def dict_data(self):
        if self.rownum<=1:
            print "总行数小于1"
        else:
            list1=[]
            j=1
            for i in range(self.rownum-1):
                s={}
                #从第二行取对应的value值
                values=self.table.row_values(j)

                for x in range(self.colnum):
                    s[self.keys[x]]=values[x]
                list1.append(s)
                j+=1
            return list1

if __name__=="__main__":
    filepath="user.xlsx"
    sheetName="Sheet1"
    data=ExcelR(filepath,sheetName)
    print data.dict_data()