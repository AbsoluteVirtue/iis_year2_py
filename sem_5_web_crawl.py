import datetime
import requests
import xlwt


def get_list():
    url = ('https://www.kickstarter.com/discover/advanced?'
           'state=successful&category_id=34&sort=most_backed&format=json&page=%s')

    result = []

    for i in range(1, int(11270/12)):
        try:
            res = requests.get(url=url % i)
            projects = res.json()['projects']
        except Exception as ex:
            print(ex)
            break
        else:
            for project in projects:
                result.append({
                    'name': project.get('name', '-'),
                    'description': project.get('blurb', '-'),
                    'url': project.get('urls', {}).get('web', {}).get('project', '-'),
                    'amount': project.get('pledged', 0.0),
                    'currency': project.get('currency', '-'),
                    'author': project.get('creator', {}).get('name', '-'),
                    'backers': project.get('backers_count', 0),
                    'date': project.get('launched_at', 0),
                    '_id': project['id'],
                })

    return result


def generate_xls(rows):
    wb = xlwt.Workbook()
    ws = wb.add_sheet('Kickstarter TTG')

    ws.write(0, 0, u"no.")
    ws.write(0, 1, u"title")
    ws.write(0, 2, u"pub.")
    ws.write(0, 3, u"backers")
    ws.write(0, 4, u"pledged")
    ws.write(0, 5, u"desc.")
    ws.write(0, 6, u"date.")
    ws.write(0, 7, u"url")

    row = 1
    for i, r in enumerate(rows):
        ws.write(row, 0, i + 1)
        ws.write(row, 1, r['name'].strip(), xlwt.Style.easyxf("font: bold on"))
        ws.write(row, 2, r['author'].strip())
        ws.write(row, 3, r['backers'])
        ws.write(row, 4, '%s %s' % (r['amount'], r['currency'].strip()))
        ws.write(row, 5, r['description'].strip())
        ws.write(row, 6, str(datetime.datetime.fromtimestamp(r['date'])))
        ws.write(row, 7, r['url'].strip())

        row += 1

    wb.save("kick_ttg.xlsx")


if __name__ == '__main__':
    generate_xls(get_list())
