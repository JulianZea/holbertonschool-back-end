#!/usr/bin/python3
''' Return information about his/her TODO list progress from an REST API '''
from requests import get
from sys import argv


def apiRest():
    ''' Gather data from an API '''
    idUser = int(argv[1])
    nameEmploye = ''
    numberTask = 0
    totalNumberTask = 0
    listTask = []

    urlUsers = get('https://jsonplaceholder.typicode.com/users').json()
    for varuser in urlUsers:
        if varuser['id'] == idUser:
            nameEmploye = varuser['name']
            break

    urlTask = get('https://jsonplaceholder.typicode.com/todos').json()
    for vartask in urlTask:
        if vartask['userId'] == idUser:
            if vartask['completed'] is True:
                listTask.append(vartask['title'])
                numberTask += 1
            totalNumberTask += 1
    print('Employee {} is done with tasks({}/{}):'.format(nameEmploye,
                                                          numberTask,
                                                          totalNumberTask))
    for title in listTask:
        print('\t {}'.format(title))


if __name__ == '__main__':
    api_rest()
