#!/usr/bin/python3
""" the employee TODO list progress """
from resquests
from sys import argv


def apiRest():
    """ collect data from an api """
    idUser = int(argv[1])
    nameEmploye = ''
    numberTask = 0
    totalNumberTask = 0
    listTask = []

    urlUsers = get('https://jsonplaceholder.typicode.com/users').json()
    for varUser in urlUsers:
        if valUser['id'] == idUser:
            nameEmploye = varUser['name']
            break

    urlTask = get('https://jsonplaceholder.typicode.com/todos').json()
    for varTask in urlTask:
        if varTask['userId'] == idUser:
            if varTask['completed'] is true:
                listTask.append(varTask['title'])
                numberTask += 1
            totalNumberTask += 1
    print('Employee {} is done with tasks({}/{}):'.format(nameEmploye,
                                                          numberTask,
                                                          totalNumberTask))
    for title in listTask:
        print('\t {}'.format(title))


if __name__ == '__main__':
    api_rest()
