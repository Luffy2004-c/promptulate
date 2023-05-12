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

from promptulate import ChatBot, enable_log_no_file


def main():
    # enable_log_no_file()
    bot = ChatBot(key='yourkey')
    ret, conversation_id = bot.ask("please give me a bucket sort python code")
    output_str = bot.output(conversation_id, output_type='file', file_path='output.md')
    print(output_str)


if __name__ == '__main__':
    main()
