#!/usr/bin/python

#
# Program: To get the stats of running instance in AWS region>
#
# Author: Roshan Bhave < roshan dot bhave at gmail dot com> 
#
# Current Version: 1.0
#

import boto
import boto.ec2

reg = next(x for x in boto.ec2.regions() if x.name=='us-west-1')
conn = boto.ec2.EC2Connection(region=reg)
reservations = conn.get_all_instances(filters={'instance-state-name': 'running'})
instances = [ i for r in reservations for i in r.instances]
print conn
for i in instances:
    print(i.__dict__)
    break


