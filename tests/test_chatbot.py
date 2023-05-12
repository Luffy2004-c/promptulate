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

from promptulate import ChatBot
from unittest import TestCase, main

openai_key = 'yourkey'


class TestChatBot(TestCase):

    def test_send_and_recv(self):
        self.bot = ChatBot(key=openai_key)
        ret, conversation_id = self.bot.ask("hello")
        self.assertIsNotNone(ret)
        self.assertIsNotNone(conversation_id)

    def test_get_history(self):
        self.bot = ChatBot(key=openai_key)
        ret, conversation_id = self.bot.ask("please give me a bucket sort python code")
        output_str = self.bot.output(conversation_id)
        self.assertIsNotNone(output_str)


if __name__ == '__main__':
    main()
