var Ppcloud = Ppcloud || {};

Ppcloud.facebook = function() {
	var my = my || {};
	var self = {};
	var CACHE = {
		$fbBtn:$('#fb-btn')
	} 

	function __new__() {
		fbInit();
	}

	/* initialization */
	function __init__() {
		CACHE.$fbBtn.on('click', function() {
			doLogin()
			return false
		})
		test_authorized()
	}

	function test_authorized() {
		FB.getLoginStatus(function(response) {
			if (response.status === 'connected') {
				isAuthorized(response.authResponse.accessToken)
			}
		})
	}

	function fbInit() {
		FB.init({
			appId : '230178707104819',
			status : true,
			cookie : true
		});
	}

	function doLogin() {

		FB.login(function(response) {
			if (response.authResponse.accessToken) {
				isAuthorized(response.authResponse.accessToken)
			}
		}, {
			scope : 'user_photos',
			response_type : 'token'
		});
	}
	
	function isAuthorized(token){
		self.onConnect(token)
		CACHE.$fbBtn.html("Facebook Sync'd");
	}


	self.onConnect = function() {
	}
	// do not delete //
	__new__();
	__init__();
	return self;
	// #eo do not delete //

}
