var Ppcloud = Ppcloud || {};

Ppcloud.instagram = function(spec, my) {
	var my = my || {};
	var self = {};

	function __new__() {
		igInit();
	}

	/* initialization */
	function __init__() {
		$('#instagram-btn').on('click', function() {
			doLogin()
			return false
		})
	}

	function igInit() {
		IG.init({
			client_id : '8b6d72cafbfb449fb5330c520b5102ed',
			logging : true,
			check_status : false
		});

	}

	function doLogin() {
		IG.login(function(response) {
			if (response.code) {
				console.log(response.code)
				document.location = '/?instagram_code=' + response.code;
			} else if (response.session) {
				console.log(response.session)
				document.location = '/?instagram_user_id=' + response.session.id;
			}
		}, {
			response_type : 'code'
		});
	}

	// do not delete //
	__new__();
	__init__();
	//return self;
	// #eo do not delete //
}
$(function() {
	Ppcloud.instagram()
})
