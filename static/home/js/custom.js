// get latitude and longitude of current location

$(document).ready(function () {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(function (position) {
            let latitude = position.coords.latitude;
            let longitude = position.coords.longitude;

            console.log(`Latitude: ${latitude}, Longitude: ${longitude}`);

            let city = sessionStorage.getItem(`${latitude},${longitude}`);

            if (city) {
                $('#loc').text(city);
            } else {
                $.ajax({
                    url: "/matrimony/ajax/get_current_city/",
                    type: 'POST',
                    data: {
                        'latitude': latitude,
                        'longitude': longitude
                    },
                    success: function (data) {
                        if (data.city) {
                            $('#loc').text(data.city);
                            sessionStorage.setItem(`${latitude},${longitude}`, data.city);
                        }
                    }
                })
            }
        })
    }
})