# Copyright (c) 2023 Zeeland
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Copyright Owner: Zeeland
# GitHub Link: https://github.com/Undertone0809/
# Project Link: https://github.com/Undertone0809/promptulate
# Contact Email: zeeland@foxmail.com

# from prompt_me.utils import logger
from promptulate.utils.singleton import Singleton, AbstractSingleton
from promptulate.utils.logger import get_logger, enable_log, enable_log_no_file
from promptulate.utils.utils import get_project_root_path, get_default_storage_path, get_cache

__all__ = [
    'get_logger',
    'enable_log',
    'enable_log_no_file',
    'get_cache',
    'get_project_root_path',
    'get_default_storage_path',
    'Singleton',
    'AbstractSingleton',

]
