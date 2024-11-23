# =========== Copyright 2023 @ CAMEL-AI.org. All Rights Reserved. ===========
# Licensed under the Apache License, Version 2.0 (the “License”);
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an “AS IS” BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# =========== Copyright 2023 @ CAMEL-AI.org. All Rights Reserved. ===========
from pydantic import BaseModel

from camel.agents import ChatAgent
from camel.configs import ChatGPTConfig
from camel.models import ModelFactory
from camel.types import ModelPlatformType, ModelType


class Student(BaseModel):
    name: str
    age: str


class StudentList(BaseModel):
    studentLlst: list[Student]


openai_model = ModelFactory.create(
    model_platform=ModelPlatformType.OPENAI,
    model_type=ModelType.GPT_4O_MINI,
    model_config_dict=ChatGPTConfig(
        temperature=0.0, response_format=StudentList
    ).as_dict(),
)

# Set agent
camel_agent = ChatAgent(model=openai_model)

# Set user message
user_msg = """give me some student infos."""

# Get response information
response = camel_agent.step(user_msg)
print(response.msgs[0].content)
'''
===============================================================================
{"studentLlst":[{"name":"Alice Johnson","age":"20"},{"name":"Brian Smith",
"age":"22"},{"name":"Catherine Lee","age":"19"},{"name":"David Brown",
"age":"21"},{"name":"Eva White","age":"20"}]}
===============================================================================
'''
