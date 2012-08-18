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
          cookie	: true,
          xfbml		: true
        });
	}

	function doLogin() {
		FB.login(function(response) {
			if (response.code) {
				document.location = '/?fb_code=' + response.code;
				console.log(response.code);
			} else if (response.session) {
				//document.location = '/?ig_uid=' + response.session.id;
			}
		}, {
			response_type : 'code'
		});
		
		FB.api('/me', function(response) {
		  alert(response.name);
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