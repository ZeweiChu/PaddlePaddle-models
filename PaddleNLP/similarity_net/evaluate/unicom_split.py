#   Copyright (c) 2019 PaddlePaddle Authors. All Rights Reserved.
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
"""
split unicom file
"""

with open("../data/unicom", "r") as unicom_file:
    with open("./unicom_infer", "w") as infer_file:
        with open("./unicom_label", "w") as label_file:
            for line in unicom_file:
                line = line.strip().split('\t')
                infer_file.write("\t".join(line[:2]) + '\n')
                label_file.write(line[2] + '\n')
