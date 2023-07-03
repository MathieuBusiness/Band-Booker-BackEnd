import call_api as api

def get_specific_band_by_id(specific_id):
    allBands = api.get_all_bands()
    for band in allBands:
        if band["id"] == specific_id:
            response = {
                "status": 200,
                "content": band
            }
            return response
    return {"status": 400}


