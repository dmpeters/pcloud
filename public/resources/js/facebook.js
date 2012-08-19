var Ppcloud = Ppcloud || {};

Ppcloud.facebook = function() {
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
				//document.location = '/?fb_code=' + response.authResponse.accessToken;
				//$('#facebook-btn').text("Sync'd");
				self.onConnect(response.authResponse.accessToken)
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
	
	self.onConnect = function(){}

	// do not delete //
	__new__();
	__init__();
	return self;
	// #eo do not delete //
	
}
