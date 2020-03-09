BEGIN {FS = "[: ]" }
{
	if($1 ~ /[0-9][0-9]\/[0-9][0-9]/) #Only if the statment corresponds to DEBUGL print which starts with time stamp
	{
		
		echo $0
		previousTimeInHRs = presentTimeInHRs
		previousTimeInMs = presentTimeInMs
		previousTimeInMins = presentTimeInMins

		presentTimeInHRs = $2
		presentTimeInMins = $3
		presentTimeInMs = $4
		differenceInMs = (presentTimeInHRs - previousTimeInHRs)*60*60000 + (presentTimeInMins - previousTimeInMins)*60000 + int((presentTimeInMs - previousTimeInMs)/1000) # As the last field of timespamp is in microseconds we need to divide it by 1000
#		if (differenceInMs > 20 && differenceInMs < 100) { 
		if (differenceInMs > 20) { 
#		if (differenceInMs < -1000){
			print "Performance::",differenceInMs,"ms,  ", $0	#You can comment this line if you are intrested only in the differences in particulat range.
#			print "presentTimeInHRs = ", presentTimeInHRs, "presentTimeInMins = ", presentTimeInMins, "presentTimeInMs = ", presentTimeInMs
		}
		else{
			print differenceInMs,"ms,  " $0	
		}
	}
	else
	{
		print $0
	}
}
