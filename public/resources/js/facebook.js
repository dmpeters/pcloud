var Ppcloud = Ppcloud || {};

Ppcloud.facebook = function(spec, my) {
	var my = my || {};
	var self = {};

	function __new__() {
		fbInit();
	}

	/* initialization */
	function __init__() {
		$('#facebook-btn').on('click', function() {
			doLogin()
			return false
		})
	}

	function fbInit() {
		FB.init({
          appId		: '230178707104819',
          status	: true,
          cookie	: true
        });
	}

	function doLogin() {
		FB.login(function(response) {
			if (response.authResponse.accessToken) {
				document.location = '/?fb_code=' + response.authResponse.accessToken;
				//$('#facebook-btn').text("Sync'd");
			} else if (response.session) {
				alert("We are in a session");
				//document.location = '/?ig_uid=' + response.session.id;
			}
		}, 
		{
			scope: 'user_photos',
			response_type : 'token'
		});
	}

	// do not delete //
	__new__();
	__init__();
	//return self;
	// #eo do not delete //
}
$(function() {
	Ppcloud.facebook()
})