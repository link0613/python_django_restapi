from django.core.management.base import BaseCommand
from restapi.models.Ad import Ad
from django.conf import settings

class Command(BaseCommand):

    def handle(self, *args, **options):
        settings.SYSTEM_USER = True
        ads = [
        	873049,873043,859147,859157,85614,263597,263610,263612,263614,269805,263615,263616,44988,269806,263621,45114,83415,46638,45119,269811,85683,269812,263629,263635,263645,263648,263671,263672,263675,273452,263532,3856,3868,3880,3892,413848,273454,273524,272134,269715,3865,3877,3889,29819,375735,415128,273426,272036,272733,272135,413814,413841,272268,272635,272734,272965,273533,3873,3885,30062,375722,375778,272276,272742,413842,273436,272013,375769,415278,415070,415069,415108,415286,375526,413840,3875,3887,375559,375779,415063,273438,272048,273439,273446,272023,272025,3860,3872,3884,3896,3858,3870,3882,3894,3906,415067,272027,273451,380835,378850,380809,380810,380837,380183,380864,351927,351956,380811,380757,379998,380892,378834,378859,380785,379999,378605,378836,351871,351890,351957,378846,380778,380859,380752,379987,380860,378823,379988,351723,351894,351932,380868,380895,378837,380788,380572,378838,380870,378839,351876,351147,351686,380796,380877,380797,351720,351682,351958,351873,351930,351855,351684,351931,351858,351148,351687,351897,351859,351688,351964,308842,308998,309034,309334,309250,309154,308830,309323,309335,309131,309325,308845,309337,309253,309301,292949,292476,229132,270981,292610,292742,292467,279132,279220,279121,270983,271049,292932,292943,292679,279135,279168,229126,269849,270975,269850,263686,229121,269851,860405,269852,281341,281337,309000,309300,309156,308832,308846,309074,309158,308930,308834,308847,309255,309303,309351,309075,292614,292471,293199,270987,270976,229130,293202,293235,292475,279294,229131,270980
        ]
        for ad in ads:
            data =  Ad.objects_raw.get(ad_id=ad)
            if data.attrs is None or data.attrs == '': # If none, set 1001
                data.attrs = '1001'
                print "Adding 1001 attr to Ad: ()".format(data.ad_id)
            else:
            	if data.attrs == '1001': # Already set
            		continue
            	else:
            		existing_attrs = data.attrs.split() # Multiple attrs, split to list
            		if '1001' not in existing_attrs: # Already in list
            			print "Appending 1001 attr to Ad: ()".format(data.ad_id)
            			existing_attrs.append('1001') # Append 1001 to list
            			data.attrs = ' '.join(existing_attrs) # To string

            data.save_raw()