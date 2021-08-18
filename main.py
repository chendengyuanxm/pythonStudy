# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import re

import openpyxl
from openpyxl.styles import PatternFill, Border, Side

thin = Side(border_style="thin", color="000000")
double = Side(border_style="double", color="ff0000")


def create_excel():
    wb = openpyxl.Workbook()
    ws = wb.active

    table_title = ['客户', '客户类别', '负责人（一级）', '负责人（二级）', '数量', '单价', '金额', '报价', '报价金额', '限价', '限价金额', '备注', '代理商']
    for col in range(len(table_title)):
        cell = ws.cell(row=1, column=col+1)
        cell.value = table_title[col]
        cell.fill = PatternFill("solid", fgColor="FFFF00")
        cell.border = Border(top=double, left=thin, right=thin, bottom=double)

    # table_values = [['Alex', '18065033929', 15, 'test'], ['Devin', '18064344334', 20, 'test2']]
    # for row in range(len(table_values)):
    #     ws.append(table_values[row])

    wb.save('医药.xlsx')
    print('create excel successful...\n')


def load_excel():
    wb = openpyxl.load_workbook('data.xlsx')
    ws_p = wb['要求']
    ws_data = wb['原始数据']

    if wb.__contains__('筛选数据'):
        ws_filter = wb['筛选数据']
        wb.remove(ws_filter)
    ws_filter = wb.create_sheet('筛选数据')
    title_list = ['客户分类', '负责人', '单价', '金额', '报价', '销售额（报价）', '限价', '销售额（限价）', '代理商']
    data_title_row = ws_data[1]
    for cell in reversed(data_title_row):
        title_list.insert(0, cell.value)
    ws_filter.append(tuple(title_list))
    for cell in ws_filter[1]:
        cell.fill = PatternFill("solid", fgColor="47A1A1")

    if wb.__contains__('未筛选数据'):
        ws_un_filter = wb['未筛选数据']
        wb.remove(ws_un_filter)
    ws_un_filter = wb.create_sheet('未筛选数据')
    ws_un_filter.append(tuple(title_list))
    for cell in ws_un_filter[1]:
        cell.fill = PatternFill("solid", fgColor="47A1A1")

    count = 0
    for data_row in ws_data.iter_rows(min_row=2, values_only=True):
        data_name = data_row[2]
        data_owner = data_row[6]
        data_num = data_row[7] or 0
        selected = False

        for row in ws_p.iter_rows(min_row=2, values_only=True):
            product_name = row[0]
            product_owner = row[4]
            product_ext = row[5:11]
            # print('product name: %s, product owner: %s' % (product_name, product_owner))
            if product_name == data_name and product_owner == data_owner:
                amount1 = (product_ext[2] or 0) * data_num
                amount2 = (product_ext[3] or 0) * data_num
                amount3 = (product_ext[4] or 0) * data_num
                product_ext_list = list(product_ext)
                product_ext_list.insert(5, amount3)
                product_ext_list.insert(4, amount2)
                product_ext_list.insert(3, amount1)
                data_row += tuple(product_ext_list)
                ws_filter.append(data_row)
                print(data_row)
                count += 1
                selected = True
                break

        if not selected:
            ws_un_filter.append(data_row)

    print('数据处理完成...\n共生成%d条记录' % count)
    wb.save('data.xlsx')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # create_excel()
    load_excel()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
