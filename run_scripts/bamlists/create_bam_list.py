nCopy_list = [1,3,5,7,10,12,15,20,25,30,40,50,60,70,80,90,100,120,150]


# with open('CACNA1A_grid.txt', 'w') as f:
# 	for nc1 in nCopy_list:
# 		for nc2 in nCopy_list:
# 			ll = '/storage/nmmsv/expansion-experiments/bam_list_CACNA1A_1_cov80_dist500_DIP_readLen_100/aligned_read/nc_'
# 			f.write(ll + str(nc1) + '_' + str(nc2) + '.sorted.bam\n')



with open('ATXN7_hap.txt', 'w') as f:
	for nc1 in nCopy_list:
		ll = '/storage/nmmsv/expansion-experiments/HAP_cpp_ATXN7_2_cov100_dist500_sd100_rl100/aligned_read/nc_'
		f.write(ll + str(nc1) + '.sorted.bam\n')
