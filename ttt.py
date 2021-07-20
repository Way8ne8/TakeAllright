# encoding: utf-8

#from __future__ import unicode_literals

import ftplib
import logging
import os
#from dateutil import parser
import datetime
import time

logger = logging.getLogger(__name__)



def ftp_get_abonent_messages_list(abonent):
    # Получение списка файлов и проверка существования директорий
    try:
        #ftp_timeout = abonent.ftp_timeout if abonent.ftp_timeout else 10
        ftp_connect = ftplib.FTP(
            host='10.54.1.165',
            user='u32106622',
            passwd='buK-gaHO',
            timeout=15)

    except ConnectionRefusedError as error:
        logger.error('Ошибка соединения с FTP-сервером {0}. {1}'.format(abonent.ftp_server, error))
        return None

    except ftplib.error_perm:
        logger.error('Ошибка соединения с FTP-сервером {0}. Не верный логин или пароль'.format(abonent.ftp_server))
        return None

    else:

        try:
            ftp_connect.cwd('/')
            ftp_connect.cwd('/in')
            print(ftp_connect.nlst())

        except Exception as error:
            logger.error('Не удалось сменить директорию ftp_dir_in: \'{0}\'. {1}'.format(abonent.ftp_dir_in, error))
            ftp_connect.close()
            return None
        file_list = [(message_name, ftp_connect.sendcmd("MDTM " + message_name)[4:]) for message_name in ftp_connect.nlst()
                     if (message_name != 'bak' and message_name != 'err') and message_name.split('.')[1] == '260']
        # for message_name in ftp_connect.nlst():
        #     print (ftp_connect.size(message_name))
        print(file_list)
        try:
            file_list = [(message_name, ftp_connect.sendcmd('MDTM ' + message_name)[4:]) for message_name in
                         ftp_connect.nlst() if message_name.split('.')[1] == '260']
        #     print(file_list)
        #
        # except Exception as error:
        #     logger.error('Не удалось получить список файлов. {0}'.format(error))
        #     ftp_connect.close()
        #     return None

        ftp_connect.close()

        file_list = [message_name for message_name, _ in file_list]
        print(file_list)
        #logger.info(file_list)
        return file_list



ftp_get_abonent_messages_list([32106622])
