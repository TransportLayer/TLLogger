###############################################################################
#   TransportLayer Logger - Logging setup utility                             #
#   Copyright (C) 2017  TransportLayer                                        #
#                                                                             #
#   This program is free software: you can redistribute it and/or modify      #
#   it under the terms of the GNU Affero General Public License as published  #
#   by the Free Software Foundation, either version 3 of the License, or      #
#   (at your option) any later version.                                       #
#                                                                             #
#   This program is distributed in the hope that it will be useful,           #
#   but WITHOUT ANY WARRANTY; without even the implied warranty of            #
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the             #
#   GNU Affero General Public License for more details.                       #
#                                                                             #
#   You should have received a copy of the GNU Affero General Public License  #
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.     #
###############################################################################

import logging
from time import gmtime

def setup_logger(level_string, log_file, no_file=False, no_stdout=False):
    numeric_level = getattr(logging, level_string.upper(), None)
    if not isinstance(numeric_level, int):
        raise ValueError("Invalid log level: {}".format(level_string))

    verbose_formatter = logging.Formatter("[%(asctime)s] [%(name)s/%(levelname)s] %(message)s")
    file_formatter = verbose_formatter
    stdout_formatter = verbose_formatter if numeric_level == logging.DEBUG else logging.Formatter("[%(asctime)s] [%(levelname)s] %(message)s", "%H:%M:%S")

    verbose_formatter.converter = gmtime
    stdout_formatter.converter = gmtime

    root_logger = logging.getLogger()
    root_logger.setLevel(numeric_level)

    if not no_file:
        file_logger = logging.FileHandler(log_file)
        file_logger.setFormatter(file_formatter)
        root_logger.addHandler(file_logger)

    if not no_stdout:
        stdout_logger = logging.StreamHandler()
        stdout_logger.setFormatter(stdout_formatter)
        root_logger.addHandler(stdout_logger)

def get_logger(logger):
    return logging.getLogger(logger)

def shutdown():
    logging.shutdown()
