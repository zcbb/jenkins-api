# coding:utf-8

from jenkinsapi.jenkins import Jenkins
import sys

if len(sys.argv) != 4:
    raise Exception(u'参数缺失!')
else:
    __url__ = sys.argv[1]
    __username__ = sys.argv[2]
    __password__ = sys.argv[3]

_jenkins = Jenkins(baseurl=__url__, username=__username__, password=__password__)
_jobs = []
for i in _jenkins.get_jobs():
    _jobs.append(list(i)[0])
print "任务列表: %s" % str(_jobs)

_params = []
_dict = {}

for j in _jobs:
    _job = _jenkins.get_job(j)
    print _job.get_params_list()
    _dict[j] = _job.get_params_list()

print "任务参数: %s" % str(_dict)
