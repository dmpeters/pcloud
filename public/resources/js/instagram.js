var Ppcloud = Ppcloud || {};

Ppcloud.instagram = function() {
	var my = my || {};
	var self = {};
	
	CACHE = {
		$igBtn:$('#instagram-btn'),
	}
	

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
			console.log(response)
			if (response.code) {
				//document.location = '/?ig_code=' + response.code;
				self.onConnect(response.code)
				CACHE.$igBtn.html("Instagram Sync'd");
			} else if (response.session) {
				//document.location = '/?ig_uid=' + response.session.id;
			}
		}, {
			response_type : 'code'
		});
	}
	
	self.onConnect = function(){}

	// do not delete //
	__new__();
	__init__();
	return self;
	// #eo do not delete //
}

