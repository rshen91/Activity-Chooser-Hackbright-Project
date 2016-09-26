"use strict";


$(document).ready(function () {
console.log("HEY YOU, I AM HERE in the document.ready");
var chosen_phone = ('#business_name_{{business.phone}}').val()
 
//when the button with the business is clicked I want it to trigger the python function activity_chosen
$('#btnsend').click(function() {
    $.ajax({
        type: 'POST',
        url:'/choose',
        success: function(data) {
            ;
        }
    });
});
// function submitBusiness(evt) {
//   var formInputs = {
//     .val()
//   }
//   // $.post("/choose", submitBusiness)
// }

// // $("#submit").on("click", )

}); //end documentReady


@app.route('/choose', methods=['POST'])
def activity_chosen():
    """Get the form variable chosen for the business the user wants in between"""
    
    chosen_phone = request.form.get("business_phone")
    
    # each business has a unique phone number to select information only from the chosen business
    chosen_business = request.form.get("business_name_"+ chosen_phone)
    chosen_business_lat = request.form.get("business_lat_" + chosen_phone) 
    chosen_business_lng = request.form.get("business_lng_" + chosen_phone) 
    chosen_business_rating = request.form.get("business_rating_" + chosen_phone)
    chosen_business_image = request.form.get("business_image_" + chosen_phone)
    chosen_business_url = request.form.get("business_url_"+ chosen_phone)
    chosen_business_street = request.form.get("business_street_" + chosen_phone)
    chosen_business_city = request.form.get("business_city_" + chosen_phone)
    chosen_business_zipcode = request.form.get("business_zipcode_" + chosen_phone)
    
    # variables from hidden text fields in choose_activity.html 
    user_lat = request.form.get("user_lat")
    user_lng = request.form.get("user_lng")
    end_lat = request.form.get("end_lat")
    end_lng = request.form.get("end_lng")
    start_location = request.form.get("start_location")
    end_location = request.form.get("end_location")

    return render_template("final_route.html",
                            business_name=chosen_business,
                            business_rating=chosen_business_rating,
                            activity_lat=chosen_business_lat,
                            activity_lng=chosen_business_lng,
                            business_image=chosen_business_image,
                            business_url=chosen_business_url,
                            business_street=chosen_business_street,
                            business_city=chosen_business_city,
                            business_zipcode=chosen_business_zipcode,
                            user_lat=user_lat,
                            user_lng=user_lng,
                            end_lat=end_lat,
                            end_lng=end_lng,
                            end_location=end_location,
                            start_location=start_location)

