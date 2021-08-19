# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import re
import difflib
import time
import openpyxl
from openpyxl.styles import PatternFill, Border, Side
from concurrent.futures import ThreadPoolExecutor

thin = Side(border_style="thin", color="000000")
double = Side(border_style="double", color="ff0000")

wb_map = openpyxl.load_workbook('data/map.xlsx')
ws_map_owner = wb_map['厂家']
ws_map_name = wb_map['名称']
ws_map_unit = wb_map['规格']

if wb_map.__contains__('相似名称'):
    ws_same_name = wb_map['相似名称']
    wb_map.remove(ws_same_name)
ws_same_name = wb_map.create_sheet('相似名称')
ws_same_name.append(['要求名称', '数据名称'])
for cell in ws_same_name[1]:
    cell.fill = PatternFill("solid", fgColor="47A1A1")

if wb_map.__contains__('相似厂家'):
    ws_same_owner = wb_map['相似厂家']
    wb_map.remove(ws_same_owner)
ws_same_owner = wb_map.create_sheet('相似厂家')
ws_same_owner.append(['要求厂家', '数据厂家'])
for cell in ws_same_owner[1]:
    cell.fill = PatternFill("solid", fgColor="47A1A1")


wb = openpyxl.load_workbook('data/data.xlsx')
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


def load_excel():
    print('开始处理...')
    with ThreadPoolExecutor(100) as t:
        for data_row in ws_data.iter_rows(min_row=2, values_only=False):
            t.submit(filter_data, data_row)

    # for data_row in ws_data.iter_rows(min_row=2, values_only=False):
    #     filter_data(data_row)

    print('数据处理完成...\n共生成%d条记录' % count)
    wb.save('data/data.xlsx')
    wb_map.save('data/map.xlsx')


def filter_data(data_row):
    global count
    data_value_list = list(map(lambda v: v.value, data_row))
    data_name = data_row[2].value
    data_unit = data_row[3].value
    data_owner = data_row[6].value
    data_num = data_row[7].value or 0
    selected = False

    for row in ws_p.iter_rows(min_row=2, values_only=True):
        product_name = row[0]
        product_unit = row[1]
        product_owner = row[4]
        product_ext = row[5:11]
        # print('product name: %s, product owner: %s' % (product_name, product_owner))
        # print('data name: %s, data owner: %s' % (data_name, data_owner))
        ratio = difflib.SequenceMatcher(None, product_name, data_name).quick_ratio()
        product_owner_suffix = re.sub(r'.*市|.*县|医院|卫生院', '', product_owner)
        data_owner_suffix = re.sub(r'.*市|.*县|医院|卫生院', '', data_owner)
        # print('product_owner_suffix: %s, data_owner_suffix: %s' % (product_owner_suffix, data_owner_suffix))
        ratio2 = difflib.SequenceMatcher(None, product_owner_suffix, data_owner_suffix).quick_ratio()
        # print('%s  %s' % (ratio, ratio2))

        is_owner_equal = is_equal(ws_map_owner, product_owner, data_owner)
        is_name_equal = is_equal(ws_map_name, product_name, data_name)
        is_unit_equal = is_equal(ws_map_unit, product_unit, data_unit)

        if ratio2 > 0.6 and not is_owner_equal:
            print('异常数据：%s' % data_value_list)
            data_row[6].fill = PatternFill("solid", fgColor="FF0000")
            ws_same_name.append([product_owner, data_owner])

        if is_name_equal and is_owner_equal and is_unit_equal:
            amount1 = (product_ext[2] or 0) * data_num
            amount2 = (product_ext[3] or 0) * data_num
            amount3 = (product_ext[4] or 0) * data_num
            product_ext_list = list(product_ext)
            product_ext_list.insert(5, amount3)
            product_ext_list.insert(4, amount2)
            product_ext_list.insert(3, amount1)

            data_value_list.extend(product_ext_list)
            ws_filter.append(tuple(data_value_list))
            print(data_value_list)
            selected = True
            count += 1
            break

    if not selected:
        ws_un_filter.append(data_value_list)


def uni_product_name():
    print('开始统一筛选列表数据...')
    for row in ws_filter.iter_rows(min_row=2):
        owner = row[6].value
        for r in ws_map_owner.iter_rows(min_row=2, values_only=True):
            if list(r).__contains__(owner):
                default_name = r[0]
                if default_name != owner:
                    print('统一厂家：%s -> %s' % (owner, default_name))
                    row[6].value = default_name

        name = row[2].value
        for r in ws_map_name.iter_rows(min_row=2, values_only=True):
            if list(r).__contains__(name):
                default_name = r[0]
                if default_name != name:
                    print('统一名称：%s -> %s' % (name, default_name))
                    row[2].value = default_name

        unit = row[3].value
        for r in ws_map_unit.iter_rows(min_row=2, values_only=True):
            if list(r).__contains__(unit):
                default_name = r[0]
                if default_name != unit:
                    print('统一规格：%s -> %s' % (unit, default_name))
                    row[3].value = default_name

    print('统一筛选列表数据完成...')
    wb.save('data/data.xlsx')


def is_equal(sheet, str1, str2):
    str1.strip()
    str2.strip()

    if str1 == str2:
        return True

    for row in sheet.iter_rows(min_row=2, values_only=True):
        if list(row).__contains__(str1) and list(row).__contains__(str2):
            return True

    return False


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    time_start = time.time()
    load_excel()
    uni_product_name()
    time_end = time.time()
    duration = time_end - time_start
    print('总共用时：%s' % duration)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
