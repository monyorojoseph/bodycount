
    // when ready
    $(document).ready(function(){
        $("body").addClass("welcome")
    })
    // email key up
    $("#id_email").focusout(function(e){
        const data = {"email":e.target.value}

        // get coookies
        function getCookie(name) {
            let cookieValue = null;
            if (document.cookie && document.cookie !== '') {
                const cookies = document.cookie.split(';');
                for (let i = 0; i < cookies.length; i++) {
                    const cookie = cookies[i].trim();
                    // Does this cookie string begin with the name we want?
                    if (cookie.substring(0, name.length + 1) === (name + '=')) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }
            return cookieValue;
        }
        const csrftoken = getCookie('csrftoken');
        
        $.ajax({
            url:"{% url 'users:check_mail' %}",
            type: "POST",
            processData: false,
            contentType: false,
            headers: {
                "X-Requested-With": "XMLHttpRequest",
                'X-CSRFToken': csrftoken
            },
            data: JSON.stringify(data),
            success: (response)=> {
                console.log("am ready to suffer")
                console.log(response.valid)
            },
            error: (error)=> {
                console.log(error.message)
            }
        })
    })
    // username
    $("#id_username").focusout(function(e){
        const data = {"username":e.target.value}

        // get coookies
        function getCookie(name) {
            let cookieValue = null;
            if (document.cookie && document.cookie !== '') {
                const cookies = document.cookie.split(';');
                for (let i = 0; i < cookies.length; i++) {
                    const cookie = cookies[i].trim();
                    // Does this cookie string begin with the name we want?
                    if (cookie.substring(0, name.length + 1) === (name + '=')) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }
            return cookieValue;
        }
        const csrftoken = getCookie('csrftoken');
        
        $.ajax({
            url:"{% url 'users:check_username' %}",
            type: "POST",
            processData: false,
            contentType: false,
            headers: {
                "X-Requested-With": "XMLHttpRequest",
                'X-CSRFToken': csrftoken
            },
            data: JSON.stringify(data),
            success: (response)=> {
                console.log("am ready to suffer")
                console.log(response.valid)
            },
            error: (error)=> {
                console.log(error.message)
            }
        })
        
    })
    // Registering user
    $("#form").submit(function(e){
        e.preventDefault();

        $("#submit").text("Registering ...")
        $("#submit").prop('disabled',true)


        let data = new FormData($(this).get(0))


        // get coookies
        function getCookie(name) {
            let cookieValue = null;
            if (document.cookie && document.cookie !== '') {
                const cookies = document.cookie.split(';');
                for (let i = 0; i < cookies.length; i++) {
                    const cookie = cookies[i].trim();
                    // Does this cookie string begin with the name we want?
                    if (cookie.substring(0, name.length + 1) === (name + '=')) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }
            return cookieValue;
        }
        const csrftoken = getCookie('csrftoken');
        
        $.ajax({
            url:"{% url 'body:welcome' %}",
            type: "POST",
            processData: false,
            contentType: false,
            headers: {
                "X-Requested-With": "XMLHttpRequest",
                'X-CSRFToken': csrftoken
            },
            data: data,
            success: (response)=> {
                console.log(response.message)
                window.location.href = 'home/'
            },
            error: (error)=> {
                console.log(error.message)
            }
        })
    });