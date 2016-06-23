#!/bin/bash

REGIONS=(us-east-1 us-west-1 us-west-2 eu-west-1 eu-central-1 ap-northeast-1 ap-northeast-2 ap-southeast-1 ap-southeast-2 sa-east-1)

for region in ${REGIONS[@])}; do

	INSTANCES=(`aws ec2 describe-instances --filter "Name=instance-state-name,Values=running" --query 'Reservations[*].Instances[*].[InstanceId]' --output text --region=$region| tr '\n' ' '`)
	
	echo "${#INSTANCES[@]} instances in Region $region"

	if [ ${#INSTANCES[@]} -gt 0 ]
	then
		echo "Stopping instances ${INSTANCES[@]} in Region $region"
		aws ec2 stop-instances --instance-ids ${INSTANCES[@]} --region=$region
	fi

done
exit 0