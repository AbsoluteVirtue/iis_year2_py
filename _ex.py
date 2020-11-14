import requests


if __name__ == '__main__':
    result = []
    for i in range(1, 11):
        try:
            res = requests.get((
                'https://www.kickstarter.com/discover/advanced'
                '?state=successful&category_id=34&sort=most_backed&format=json'
                '&page=%s' % i))
            data = res.json()
        except Exception as ex:
            pass
        else:
            for project in data.get('projects', []):
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

    print(result)
