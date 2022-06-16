(function($) {

    var form = $("#signup-form");
    form.validate({
        errorPlacement: function errorPlacement(error, element) {
            element.before(error);
        },
        rules: {
            username: {
                required: true,
            },
            email: {
                required: true,
                email: true
            }
        },
        messages: {
            email: {
                email: 'Not a valid email address <i class="zmdi zmdi-info"></i>'
            }
        },
        onfocusout: function(element) {
            $(element).valid();
        },
    });
    form.steps({
        headerTag: "h3",
        bodyTag: "fieldset",
        transitionEffect: "slideLeft",
        labels: {
            previous: 'Previous',
            next: 'Next',
            finish: 'Submit',
            current: ''
        },
        titleTemplate: '<div class="title"><span class="number">#index#</span>#title#</div>',
        onStepChanging: function(event, currentIndex, newIndex) {
            form.validate().settings.ignore = ":disabled,:hidden";
            // console.log(form.steps("getCurrentIndex"));
            return form.valid();
        },
        //onFinishing: function(event, currentIndex) {
        // form.validate().settings.ignore = ":disabled";

        //onsole.log(getCurrentIndex);
        //return form.valid();
        // },
        onFinished: $('#signup-form').on('submit', function(event, currentIndex) {

            e.preventDefault();

            $.ajax({
                type: "POST",
                url: "{% url 'submit_prediction' %}",
                data: {
                    Month: $('#Month').val(),
                    WeekOfMonth: $('#WeekOfMonth').val(),
                    DayOfWeek: $('#DayOfWeek').val(),
                    Make: $('#Make').val(),
                    AccidentArea: $('#AccidentArea').val(),
                    DayOfWeekClaimed: $('#DayOfWeekClaimed').val(),
                    MonthClaimed: $('#MonthClaimed').val(),
                    WeekOfMonthClaimed: $('#WeekOfMonthClaimed').val(),
                    Sex: $('#Sex').val(),
                    MaritalStatus: $('#MaritalStatus').val(),
                    Age: $('#Age').val(),
                    Fault: $('#Fault').val(),
                    PolicyType: $('#PolicyType').val(),
                    VehicleCategory: $('#VehicleCategory').val(),
                    VehiclePrice: $('#VehiclePrice').val(),
                    PolicyNumber: $('#PolicyNumber').val(),
                    RepNumber: $('#RepNumber').val(),
                    Deductible: $('#Deductible').val(),
                    DriverRating: $('#DriverRating').val(),
                    Days_Policy_Accident: $('#Days_Policy_Accident').val(),
                    AgeOfVehicle: $('#AgeOfVehicle').val(),
                    PoliceReportFiled: $('#PoliceReportFiled').val(),
                    WitnessPresent: $('#WitnessPresent').val(),
                    AgentType: $('#AgentType').val(),
                    NumberOfCars: $('#NumberOfCars').val(),
                    Year: $('#Year').val(),
                    csrfmiddlewaretoken: '{{ csrf_token }}',
                    dataType: "json",

                },

                success: function(data) {
                    $('#output').html(data.msg) /* response message */
                },

                failure: function() {

                }


            });


        })

        // $("#signup-form").submit();
        //alert('Sumited');


        // onInit : function (event, currentIndex) {
        //     event.append('demo');
        // }
    });


    jQuery.extend(jQuery.validator.messages, {
        required: "",
        remote: "",
        url: "",
        date: "",
        dateISO: "",
        number: "",
        digits: "",
        creditcard: "",
        equalTo: ""
    });


    $.dobPicker({
        daySelector: '#expiry_date',
        monthSelector: '#expiry_month',
        yearSelector: '#expiry_year',
        dayDefault: 'DD',
        yearDefault: 'YYYY',
        minimumAge: 0,
        maximumAge: 120
    });

    $('#password').pwstrength();

    $('#button').click(function() {
        $("input[type='file']").trigger('click');
    })

    $("input[type='file']").change(function() {
        $('#val').text(this.value.replace(/C:\\fakepath\\/i, ''))
    })

})(jQuery);