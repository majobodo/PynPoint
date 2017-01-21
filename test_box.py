import fpf_calculator
import glob, os
import numpy as np
import operator

folder_list = ["results_0_0/",
               "results_0_2/",
               "results_0_4/",
               "results_0_6/",
               "results_0_8/",

               "results_1_0/",
               "results_1_2/",
               "results_1_4/",
               "results_1_6/",
               "results_1_8/",

               "results_2_0/",
               "results_2_2/",
               "results_2_4/",
               "results_2_6/",
               "results_2_8/",

               "results_3_0/",
               "results_3_2/",
               "results_3_4/",
               "results_3_6/",
               "results_3_8/",

               "results_4_0/",
               "results_4_2/",
               "results_4_4/",
               "results_4_6/",
               "results_4_8/",

               "results_5_0/",
               "results_5_2/",
               "results_5_4/",
               "results_5_6/",
               "results_5_8/"]

planet_pos = (65, 63) # BP 29
#planet_pos = (58.5, 67.5)  # HR8799

# shifts = np.linspace(-3.0, 3.0, num= 20) #

shifts = np.linspace(-1.0, 1.0, num= 5)  # BP 29
planet_shifts = [(planet_pos[0] + x, planet_pos[1] + y) for x in shifts for y in shifts]

print "BP 29"

for tmploc in folder_list:
    print "------------- " + tmploc + "---------------"
    tmp_location = "/Users/markusbonse/Desktop/BetaPic_29/results_BP_29/" + tmploc

    last_planet_pos = planet_pos

    # get all fits files in the directory
    os.chdir(tmp_location)
    for file in glob.glob("*.fits"):

        snr_result_list = []
        planet_pos_list = []

        for shift in planet_shifts:
            tmp_result = fpf_calculator.fpf_calculator(tmp_location + str(file),
                                                       filetype="fits",
                                                       planet_position=shift,
                                                       radius=3.6/2.0,
                                                       method="exact",
                                                       plot=False,
                                                       save=False)

            snr_result_list.append(tmp_result[2])
            planet_pos_list.append(tmp_result[3])

        result_fit = fpf_calculator.fpf_calculator(tmp_location + str(file),
                                                   filetype="fits",
                                                   planet_position=planet_pos,
                                                   radius=3.6/2.0,
                                                   method="fit",
                                                   plot=False,
                                                   save=False)
        snr_result_list.append(result_fit[2])
        planet_pos_list.append(result_fit[3])

        index, value = max(enumerate(snr_result_list), key=operator.itemgetter(1))
        #print planet_pos_list[index]
        print value
        #print index

        '''
        fpf_calculator.fpf_calculator(tmp_location + str(file),
                                      filetype="fits",
                                      planet_position=planet_pos_list[index],
                                      radius=3.6 / 2.0,
                                      method="exact",
                                      plot=True,
                                      save=False)'''


