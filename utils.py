# encoding: utf-8


from __future__ import unicode_literals

import ftplib
import logging
import os
#from dateutil import parser
import datetime
import time

logger = logging.getLogger(__name__)


def ftp_check_abonent_params(abonent):
    error = False
    for param in ['ftp_server', 'ftp_login', 'ftp_dir_in', 'ftp_dir_in_bak', 'ftp_dir_in_err', 'ftp_dir_out']:
        if not getattr(abonent, param):
            error = True
            logger.error('Не заполен обязательный параметр {0}'.format(param))

    return not error


def ftp_get_abonent_messages_list(abonent):
    # Получение списка файлов и проверка существования директорий
    try:
        ftp_timeout = abonent.ftp_timeout if abonent.ftp_timeout else 10
        ftp_connect = ftplib.FTP(
            host=abonent.ftp_server,
            user=abonent.ftp_login,
            passwd=abonent.ftp_password,
            timeout=ftp_timeout)

    except ConnectionRefusedError as error:
        logger.error('Ошибка соединения с FTP-сервером {0}. {1}'.format(abonent.ftp_server, error))
        return None

    except ftplib.error_perm:
        logger.error('Ошибка соединения с FTP-сервером {0}. Не верный логин или пароль'.format(abonent.ftp_server))
        return None

    else:
        for param in ['ftp_dir_in', 'ftp_dir_in_bak', 'ftp_dir_in_err', 'ftp_dir_out', 'ftp_copy_exp_dir']:
            if getattr(abonent, param):
                try:
                    ftp_connect.cwd('/')
                    ftp_connect.cwd(getattr(abonent, param))

                except Exception as error:
                    logger.error(
                        'Не удалось сменить директорию {0}: \'{1}\'. {2}'.format(param, getattr(abonent, param), error))
                    ftp_connect.close()
                    return None

        try:
            ftp_connect.cwd('/')
            ftp_connect.cwd(abonent.ftp_dir_in)

        except Exception as error:
            logger.error('Не удалось сменить директорию ftp_dir_in: \'{0}\'. {1}'.format(abonent.ftp_dir_in, error))
            ftp_connect.close()
            return None

        try:
            file_list = [message_name for message_name in
                         ftp_connect.nlst() if message_name.split('.')[1] == '260']

        except Exception as error:
            logger.error('Не удалось получить список файлов. {0}'.format(error))
            ftp_connect.close()
            return None

        ftp_connect.close()

        file_list = [message_name for message_name, _ in file_list]
        #logger.info(file_list)
        return file_list


def ftp_download_abonent_files(abonent, files_list, dst_path):
    # Загрузка файлов с ftp сервера

    try:
        ftp_timeout = abonent.ftp_timeout if abonent.ftp_timeout else 10
        ftp_connect = ftplib.FTP(
            host=abonent.ftp_server,
            user=abonent.ftp_login,
            passwd=abonent.ftp_password,
            timeout=ftp_timeout)

    except Exception as error:
        logger.error('Ошибка соединения с FTP-сервером: {0}. {1}'.format(abonent.ftp_server, error))
        return False

    try:
        ftp_connect.cwd(abonent.ftp_dir_in)
    except Exception as error:
        logger.error('Не удалось сменить директорию ftp_dir_in: \'{0}\'. {1}'.format(abonent.ftp_dir_in, error))
        ftp_connect.close()
        return False

    for message_name in files_list:
        file_path = os.path.join(dst_path, message_name)
        try:
            timestamp = ftp_connect.voidcmd("MDTM {}".format(message_name))[4:].strip()
            ftime = time.mktime(datetime.datetime.strptime(timestamp, "%Y%m%d%H%M%S").timetuple())
            with open(file_path, 'wb') as new_file:
                ftp_connect.retrbinary('RETR ' + message_name, new_file.write, 1024)
            os.utime(file_path, (ftime, ftime))
            logger.info('save from ftp file {0}, datetime {1}'.format(message_name, timestamp))
        except Exception as error:
            logger.error('Ошибка получения файла {0}. {1}'.format(message_name, error))

            try:
                os.remove(file_path)
            except Exception as error:
                logger.debug('Ошибка удаления файла {0}. {1}'.format(file_path, error))

            continue

        try:
            ftp_connect.delete(message_name)
        except Exception as error:
            logger.error('Невозможно удалить файл {0}. {1}'.format(message_name, error))

    ftp_connect.close()

    return True


def ftp_upload_abonent_file(abonent, file_path, ftp_path, copy=False):
    #   Выгрузка файла на ftp сервер


    try:
        ftp_timeout = abonent.ftp_timeout if abonent.ftp_timeout else 10
        ftp_connect = ftplib.FTP(
            host=abonent.ftp_server,
            user=abonent.ftp_login,
            passwd=abonent.ftp_password,
            timeout=ftp_timeout)

    except Exception as error:
        logger.error('Ошибка соединения с FTP-сервером: {0}. {1}'.format(abonent.ftp_server, error))
        return False

    try:
        ftp_connect.cwd(ftp_path)

    except Exception as error:
        logger.error('Не удалось сменить директорию: \'{0}\'. {1}'.format(ftp_path, error))
        ftp_connect.close()
        return False

    file_name = os.path.split(file_path)[1]
    #logger.info(file_path)

    try:
        with open(file_path, 'rb') as f:
            ftp_connect.storbinary('STOR {0}'.format(file_name), f, 1024)

    except Exception as error:
        logger.error('Не удалось выгрузить файл: {0}. {1}'.format(file_path, error))
        ftp_connect.close()
        return False

    if copy:

        try:
            ftp_connect.cwd('/')
            ftp_connect.cwd(abonent.ftp_copy_exp_dir)
            #logger.info(abonent.ftp_copy_exp_dir)
        except Exception as error:
            logger.error(
                'Не удалось сменить директорию ftp_copy_exp_dir: \'{0}\'. {1}'.format(abonent.ftp_copy_exp_dir, error))
            ftp_connect.close()
            return False

        try:
            with open(file_path, 'rb') as f:
                ftp_connect.storbinary('STOR {0}'.format(file_name), f, 1024)
        except Exception as error:
            logger.error('Не удалось выгрузить файл: {0}. {1}'.format(file_path, error))
            ftp_connect.close()
            return False

    ftp_connect.close()
    return True