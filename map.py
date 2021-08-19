# import re
# import difflib
# import openpyxl
#
#
# def load_excel():
#     wb = openpyxl.load_workbook('data/data.xlsx')
#     ws_p = wb['要求']
#     ws_data = wb['原始数据']
#
#     if wb.__contains__('筛选数据'):
#         ws_filter = wb['筛选数据']
#         wb.remove(ws_filter)
#     ws_filter = wb.create_sheet('筛选数据')
#     title_list = ['客户分类', '负责人', '单价', '金额', '报价', '销售额（报价）', '限价', '销售额（限价）', '代理商']
#     data_title_row = ws_data[1]
#     for cell in reversed(data_title_row):
#         title_list.insert(0, cell.value)
#     ws_filter.append(tuple(title_list))
#     for cell in ws_filter[1]:
#         cell.fill = PatternFill("solid", fgColor="47A1A1")
#
#     if wb.__contains__('未筛选数据'):
#         ws_un_filter = wb['未筛选数据']
#         wb.remove(ws_un_filter)
#     ws_un_filter = wb.create_sheet('未筛选数据')
#     ws_un_filter.append(tuple(title_list))
#     for cell in ws_un_filter[1]:
#         cell.fill = PatternFill("solid", fgColor="47A1A1")
#
#     count = 0
#     for data_row in ws_data.iter_rows(min_row=2, values_only=True):
#         data_name = data_row[2]
#         data_owner = data_row[6]
#         data_num = data_row[7] or 0
#         selected = False
#
#         for row in ws_p.iter_rows(min_row=2, values_only=True):
#             product_name = row[0]
#             product_owner = row[4]
#             product_ext = row[5:11]
#             print('product name: %s, product owner: %s' % (product_name, product_owner))
#             print('data name: %s, data owner: %s' % (data_name, data_owner))
#             ratio = difflib.SequenceMatcher(None, product_name, data_name).quick_ratio()
#             product_owner_suffix = re.sub(r'.*市|.*县|医院', '', product_owner)
#             data_owner_suffix = re.sub(r'.*市|.*县|医院', '', data_owner)
#             print('product_owner_suffix: %s, data_owner_suffix: %s' % (product_owner_suffix, data_owner_suffix))
#             ratio2 = difflib.SequenceMatcher(None, product_owner_suffix, data_owner_suffix).quick_ratio()
#             print('%s  %s' % (ratio, ratio2))
#             if product_name == data_name and is_equal(product_owner, data_owner):
#                 amount1 = (product_ext[2] or 0) * data_num
#                 amount2 = (product_ext[3] or 0) * data_num
#                 amount3 = (product_ext[4] or 0) * data_num
#                 product_ext_list = list(product_ext)
#                 product_ext_list.insert(5, amount3)
#                 product_ext_list.insert(4, amount2)
#                 product_ext_list.insert(3, amount1)
#                 data_row += tuple(product_ext_list)
#                 ws_filter.append(data_row)
#                 print(data_row)
#                 count += 1
#                 selected = True
#                 break
#
#         if not selected:
#             ws_un_filter.append(data_row)
#
#     print('数据处理完成...\n共生成%d条记录' % count)
#     wb.save('data/data.xlsx')
#
#
# if __name__ == '__main__':
#     load_excel()