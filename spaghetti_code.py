def convert_address_to_latlong(end_location):
    """"This function takes the user's input for where they want to go and convert_address_to_latlong

    it to latitude and longitude coordinates"""
#     pip install geocoder 

    r = geocoder.google(end_location)
    return r.latlng 


# need a function to convert the end address to lat/long
# http://maps.googleapis.com/maps/api/geocode/json?address="end_location"&key=


# need a function to ask the user if they want a direct route

key = os.environ.get('KEY_KEY') #gets the server key and assigns it to a variable

<!-- <span id="end-location" data-lat="{{ latlng[0] }}" data-long="{{ latlng[1] }}"> </span>
 -->

 https://maps.googleapis.com/maps/api/place/nearbysearch/json?key=AIzaSyAZPdIeAGcyvKhKXgAqaNbsyEz4Sg1qBX4&location=37.7749,122.4194&radius=50000

# import pdb; pdb.set_trace()
# print "\n\n\n\n\n\n\n\ " , r #to see what this looks like when it's "ready"

# #search_json = search_req.json()
# json_object = r.json() 
# print "\n\n\n\n\n\n\n\ " , json_object

# search_payload = {"key": key, "location": str(end_lat) + "," + str(end_lng), "open_now": True, "type": activity}
# print search_payload




# Google Directions API 
def whereto():
    """start with the user's location and get to the first marker?"""

    maps_url = "https://maps.googleapis.com/maps/api/directions/json" #&key=SERVER_KEY

    search_payload = {"origin": user_location, "destination": end_location, "key": key}
    r = requests.post('maps_url', data=search_payload)

    json_object = r.json()


    [{u'status': u'OK', u'html_attributions': [], u'results': 
    [{u'name': u'Saratoga', u'reference': 
    u'CnRuAAAATAI6JVMumCoubeTkqANoxQFFc076uPvUYGxQd614LNpy7F3LFUGs82SCVFFKDZ2JM5S1zK6DoYVgMKl_yFvmsi9P_mkz1HEyuqiJwBfe0koYGhJUhC4BNWmxZ96uQE1cgGOleDPdE88tp7cbhCBGURIQwkHiPlv90NhyB2zY4OODbBoUQgWYUlt8hKUY_VbABmTzVcgHUVI', 
    u'geometry': {u'location': {u'lat': 37.2638324, u'lng': -122.0230146}, 
    u'viewport': {u'northeast': {u'lat': 37.2969239, u'lng': -121.9851448}, 
    u'southwest': {u'lat': 37.236015, u'lng': -122.067696}}}, 
    u'place_id': u'ChIJqT9-TMRKjoARzFYL1IfICIM', u'vicinity': u'Saratoga', 
    u'photos': [{u'photo_reference': u'CoQBdwAAAAISszxhcKiYmxUvu9bS6pvuR6pAxZmBiFk4fC9W9Bhitu93kkpQkDt3qveY8ZKWCdHDkEqfTPoGVGq0BfY0ehY3uJaal3xBMcgRnyvKqiTJDGKFZgoCSCsTyW8bwFyvx7WO7MMpL2MkaNLU3dEGI-c5hS0a2Q4m2CfiKHxs967rEhDWRjBhvTcvf0xj73Eo2UJ5GhQGCZfqfcRmjHio9Bo1OrbHkjYgyQ', 
    u'width': 5312, u'html_attributions': [u'<a href="https://maps.google.com/maps/contrib/112027485535166778583/photos">Nikolay Ayrapetov</a>'], 
    u'height': 2988}], u'scope': u'GOOGLE', u'id': u'f4c826cfcafab74d211dc6f35e10ed2eb6c8151f', 
    u'types': [u'locality', u'political'], u'icon': u'https://maps.gstatic.com/mapfiles/place_api/icons/geocode-71.png'}, 
    {u'name': u'Golden Triangle', u'reference': u'CpQBhgAAAAQ1Y5bAlSANNRWgAQdx3dTF2hC7_Ao38IsTL0wMp0AaNtl_7ytTo_CSWx3TwJHFiMR4pf3d6-JfdVuPhTjVsGf3FkqcgNyOg2oNF7S7iRAlj3XnxF2y2M19ioZ8h510Ygx6Bf4ScIWMhW1nfvREdRmMwYNNrCcE7kDa1VkrX1j2eQDvuXrn0E596GAc1J8ZrRIQLqeIbhF6ffZZEGbH0we1VxoU3aKKXC37uJ1vu-ovIJGeoawWbrg', 
    u'geometry': {u'location': {u'lat': 37.2878187, u'lng': -122.0169703}, u'viewport': {u'northeast': {u'lat': 37.2939421, u'lng': -122.0063066}, u'southwest': {u'lat': 37.2782359, u'lng': -122.0258569}}}, 
    u'place_id': u'ChIJr7-N_km1j4ARkkm8VM74PJY', u'vicinity': u'Saratoga', u'photos': [{u'photo_reference': u'CoQBdwAAAHhDomEN0apVejz3o324LUhKQ6QO6Vxvv-ZRCV94UpnGzdMCG4wbQr-uURTfcYSOclDRrw97SQ13NIooXkrEVJN9huuTdy9IEZJPcG0xVBNm9i0mqWZF-fC4LrhEiWbEXFM8S4JLZXMS3685NV77vUmExfmmjkj_5YOPz5Yrc5wOEhCm9MFhp04ohlMRRJ10jucMGhToBfq-NjCkpa_nk5JwGgTX7vyB0w', 
    u'width': 654, u'html_attributions': [u'<a href="https://maps.google.com/maps/contrib/106463295137047856245/photos">Partha Narasimhan</a>'], u'height': 435}], u'scope': u'GOOGLE', u'id': u'233520d6a66bde89c9483d7396436160762dfc33', u'types': [u'neighborhood', u'political'], u'icon': u'https://maps.gstatic.com/mapfiles/place_api/icons/geocode-71.png'}]}, 

    {u'status': u'OK', u'html_attributions': [], u'results': [{u'name': u'Saratoga', u'reference': u'CnRuAAAAum0suFZbK5wMmkDPcm4YVyckdWEOTe_o44KQetAdsa-2E2_DA5aeVid-JHJsDL_Yju3l5-FZS0DuZykfFnl1eICBId3qsneO8phatbeTfnpQ3KlY0Xz3xvMCpWTWJs13wzmR3d2v7K_Js5NVuil7uhIQ71bdaYB3nO0mfme6y4V0DhoU7PP3S28g7UbewuwtLOsrIwr8y7c', u'geometry': {u'location': {u'lat': 37.2638324, u'lng': -122.0230146}, u'viewport': {u'northeast': {u'lat': 37.2969239, u'lng': -121.9851448}, u'southwest': {u'lat': 37.236015, u'lng': -122.067696}}}, u'place_id': u'ChIJqT9-TMRKjoARzFYL1IfICIM', u'vicinity': u'Saratoga', u'photos': [{u'photo_reference': u'CoQBdwAAAERaOiTzD56uJdeuOugFPHQ5AsCBtbVShRnOMBXM2HGslh4ZE382ALay5CSOkf6MGWhou6R5H_wfYoTbks8hkby4a0N2M95lw0MlVvmywJo2rZ_GeUI_J649TZFoAISIKQCkscjoKefk_W3wvF5jSzH9ZN1q5IypV1mKqYmS-NFXEhCItqhNhfHg-A_CrGmJJuXSGhQ9EJtB6xlaXAi7s1W8GnqLVQdrxg', u'width': 5312, u'html_attributions': [u'<a href="https://maps.google.com/maps/contrib/112027485535166778583/photos">Nikolay Ayrapetov</a>'], u'height': 2988}], u'scope': u'GOOGLE', u'id': u'f4c826cfcafab74d211dc6f35e10ed2eb6c8151f', u'types': [u'locality', u'political'], u'icon': u'https://maps.gstatic.com/mapfiles/place_api/icons/geocode-71.png'}, {u'name': u'Golden Triangle', u'reference': u'CpQBhgAAANuixw9yZ8fQ9dzaxR-Xz4MzkTx-ag02Wy2JU21dE4LyihEDPdiRM81HsWIqfDsEHuYfVa_dac9NxFr9nYq3mlZzqiPwhJvEXDkUbfJ6qjwvqujzCvo2Fh4rM1ghaMbJ0xN9l5PpShuVHtJMKys33hMbSa2Q_NEq3D8zbDU6oST2GgKvfa18_554bPBzECuiRxIQerqnmEXHITtAACtB7cqlWxoUeYVubispweUXTQl9pbXHSPdmESE', u'geometry': {u'location': {u'lat': 37.2878187, u'lng': -122.0169703}, u'viewport': {u'northeast': {u'lat': 37.2939421, u'lng': -122.0063066}, u'southwest': {u'lat': 37.2782359, u'lng': -122.0258569}}}, u'place_id': u'ChIJr7-N_km1j4ARkkm8VM74PJY', u'vicinity': u'Saratoga', u'photos': [{u'photo_reference': u'CoQBdwAAABn8M-EeBkaGF1faLoxMsoQSz9EZTvF3l9AxxfOlo0B7aiy3SVLfSRGEMybq0Fzu5FaTb2QMAU0srpNLnfOE5OlRAHQylzKHOUFgzYpmhJ7oOxy4ShMfe1LR1A0CaHEEZPww8YPkk5ZE2u7c_4vimENkWo7xt9g_nhCIGR894YTBEhAbykNDxI5J4CN50_yjQW19GhS5EWj_m5Tw-QjFjttytQMDJHM12g', u'width': 654, u'html_attributions': [u'<a href="https://maps.google.com/maps/contrib/106463295137047856245/photos">Partha Narasimhan</a>'], u'height': 435}], u'scope': u'GOOGLE', u'id': u'233520d6a66bde89c9483d7396436160762dfc33', u'types': [u'neighborhood', u'political'], u'icon': u'https://maps.gstatic.com/mapfiles/place_api/icons/geocode-71.png'}]}, {u'status': u'OK', u'html_attributions': [], u'results': [{u'name': u'Saratoga', u'reference': u'CnRuAAAAlpmOeCWltFEuOiDYVh6nbYgKEUzHI-zFXZLG2qo0con6Zo7dje-W6n8y9lz2VecMstsdPQ-vLXSR9Le-QgGdX1yDxpRevaIVAau1GYCr1n3MRDW99XMTyB23CDzAAuENvL8oHJBzen5sIda8XpNzVRIQHAGquk0IK4yJg8fLFOzqwBoU-GZorP2GtpYsKpg8ePcy9rO4Y_k', u'geometry': {u'location': {u'lat': 37.2638324, u'lng': -122.0230146}, u'viewport': {u'northeast': {u'lat': 37.2969239, u'lng': -121.9851448}, u'southwest': {u'lat': 37.236015, u'lng': -122.067696}}}, u'place_id': u'ChIJqT9-TMRKjoARzFYL1IfICIM', u'vicinity': u'Saratoga', u'photos': [{u'photo_reference': u'CoQBdwAAAJySot-rWpsO7-5NT3aM40MdwvtKST09_jNWPqxq4duUu5PpvBfWIYI3CjynAUTms8mOTc8BSCYV9EYSUv9o64RxGtlLVC_Pblfx6b24z7MviL_MZsLLlfue98yZZJfFvlEjOaFEj63hlX2yIVE0MowUz3vrhN5xsvfmN1fhKB8bEhBvG3ohcMcO0FVMYqBO-v_sGhTg0OqRVZPSic0j8Q3JbN-j4kuKVg', u'width': 5312, u'html_attributions': [u'<a href="https://maps.google.com/maps/contrib/112027485535166778583/photos">Nikolay Ayrapetov</a>'], u'height': 2988}], u'scope': u'GOOGLE', u'id': u'f4c826cfcafab74d211dc6f35e10ed2eb6c8151f', u'types': [u'locality', u'political'], u'icon': u'https://maps.gstatic.com/mapfiles/place_api/icons/geocode-71.png'}, {u'name': u'Golden Triangle', u'reference': u'CpQBhgAAADxhJdjHSBND-TW9oZ8WLwzLlxl1AnI8_hYvRKkpXGapB7-I6Bkr4T-ooyTpwSMnxfllHULDTN7ZFrH5qNIK9kLeLeIgl-JeV67AHdEqZyXUB5q_hJl66QtQAXC41bcv8baUhxslD9OgiQRyvXLGRvPxVgWsUiWFZ1CcWXNVYZ4QGL0sQqIFQdDl4tQeJqGHSxIQYBSlEXNySaEU0HVdQPpBhxoUjrLCgywBCo1IuctgxthNd3hBDUs', u'geometry': {u'location': {u'lat': 37.2878187, u'lng': -122.0169703}, u'viewport': {u'northeast': {u'lat': 37.2939421, u'lng': -122.0063066}, u'southwest': {u'lat': 37.2782359, u'lng': -122.0258569}}}, u'place_id': u'ChIJr7-N_km1j4ARkkm8VM74PJY', u'vicinity': u'Saratoga', u'photos': [{u'photo_reference': u'CoQBdwAAANc6iCFr8qNw1_2-oy4GSOVXN15jtdt3MCYUzA6sdOjSypPshQtmYLD9nf9krFtBw2TkSLVaAuR6c1nLpckEOK2Uk9FAoG0_HgLUT3QxCtK3MAn4wNcB4VoGQ7-tcRb9F56PZaNdPMeqULM1GDmrr970OvgcLbhb_U5TNHQ5S7w-EhCsKcDEdH14MOOy4Hr3365-GhRySlArZGwX81qmu_KZYpUuiQxs9w', u'width': 654, u'html_attributions': [u'<a href="https://maps.google.com/maps/contrib/106463295137047856245/photos">Partha Narasimhan</a>'], u'height': 435}], u'scope': u'GOOGLE', u'id': u'233520d6a66bde89c9483d7396436160762dfc33', u'types': [u'neighborhood', u'political'], u'icon': u'https://maps.gstatic.com/mapfiles/place_api/icons/geocode-71.png'}]}, {u'status': u'OK', u'html_attributions': [], u'results': [{u'name': u'Saratoga', u'reference': u'CnRuAAAAY6ppwM2A5XTS_x_n_yH1-R-2T4R6IHBWrXllYxn9ozZHetd_hWwQbsvQ5fuNJZsjfZ4TdrCWFgJ5OadTdRlT0wBZd6awefVvUMWCFeRJj_C9LN0cH16Vne0OakvlVvaYk-SXK90vd2AuRSxo4TUo5RIQMBEjYSXiYH-Kbgg8JsypgxoU-yOWdQPzzGhaiiSvw6xj_zyXYFw', u'geometry': {u'location': {u'lat': 37.2638324, u'lng': -122.0230146}, u'viewport': {u'northeast': {u'lat': 37.2969239, u'lng': -121.9851448}, u'southwest': {u'lat': 37.236015, u'lng': -122.067696}}}, u'place_id': u'ChIJqT9-TMRKjoARzFYL1IfICIM', u'vicinity': u'Saratoga', u'photos': [{u'photo_reference': u'CoQBdwAAAO9uD0NBI-J1_Mfg_1OrYbgkihMtO4u0mcLOxm5CChjOtQnVqu4Sa0DrloKs0b2V1eCpYHVqK_nidzzGGQSOhXO415pFAJE-YDWirF-Smr9Iuxzj83YcRBeea1n1gE32VslDayUBSCBYEL0VwO_eW6GRyOVhdmsKlGkZHYJyNXp_EhB3Mo25tbUrnjTZQ-6Yl8j6GhSs_IHMdIcM8k7odMfMHf86-ScknA', u'width': 5312, u'html_attributions': [u'<a href="https://maps.google.com/maps/contrib/112027485535166778583/photos">Nikolay Ayrapetov</a>'], u'height': 2988}], u'scope': u'GOOGLE', u'id': u'f4c826cfcafab74d211dc6f35e10ed2eb6c8151f', u'types': [u'locality', u'political'], u'icon': u'https://maps.gstatic.com/mapfiles/place_api/icons/geocode-71.png'}, {u'name': u'Golden Triangle', u'reference': u'CpQBhgAAAAfQXNxi5N3XKJtoGR2Sjmgqq1_bhwX6pH7rR3IXfpsoeakmwQMcQ-qjZAjkqB6nh6CczG6b-gXBE7GpeQoi7U7HEslUfnH2hOJAQQpo4IbOPBa3oCzBBVv8wI13JqEdeuJ_raWoxL_VYclz5lpC7dyusP-QnEXhbavc83513lCAeffnBCIauaGRkh2GTCmluRIQY-de-e9s7PRYFFwUpUPIJBoUelzelqNcF_Tw254x-rzL8_nA_PE', u'geometry': {u'location': {u'lat': 37.2878187, u'lng': -122.0169703}, u'viewport': {u'northeast': {u'lat': 37.2939421, u'lng': -122.0063066}, u'southwest': {u'lat': 37.2782359, u'lng': -122.0258569}}}, u'place_id': u'ChIJr7-N_km1j4ARkkm8VM74PJY', u'vicinity': u'Saratoga', u'photos': [{u'photo_reference': u'CoQBdwAAAJ4g1-xQXaybUwpe3nuIxpJEPdYzf8-VUso07WUbQouRZo3xDDx5eTilrGiJxUlxUlEQQvNbblu0NXPI6n-ev_PUT0RHn5MwtSQoaFxcxCuhOFfeb70wQMo1Cj_ozSsQpQzqByJxzFXNHCp5ZH52tv9ujx0jyWWqVy5q9n7WVrcSEhCTUSlMz0xjplDoi4av4zraGhTsf5Zebl1iyn3C4fY1zdAM8fr3MA', u'width': 654, u'html_attributions': [u'<a href="https://maps.google.com/maps/contrib/106463295137047856245/photos">Partha Narasimhan</a>'], u'height': 435}], u'scope': u'GOOGLE', u'id': u'233520d6a66bde89c9483d7396436160762dfc33', u'types': [u'neighborhood', u'political'], u'icon': u'https://maps.gstatic.com/mapfiles/place_api/icons/geocode-71.png'}]}]
