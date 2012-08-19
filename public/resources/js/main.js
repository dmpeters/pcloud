var Ppcloud = Ppcloud || {};

Ppcloud.application = function() {
	var my = my || {};
	var self = {};
	var fb, ig;
	var fb_token = ''
	var ig_code = ''

	var CACHE = {
		$done : $('#done'),
		$progress : $('#progress')
	}

	/* initialization */
	function __init__() {
		fb = Ppcloud.facebook()
		fb.onConnect = onFbConnect
		ig = Ppcloud.instagram()
		ig.onConnect = onIgConnect

		CACHE.$done.on('click', function() {
			doStartDownload()
		})
	}

	function onFbConnect(c) {
		fb_token = c
		connected()
	}

	function onIgConnect(c) {
		ig_code = c
		connected()
	}

	function connected() {
		showStartBtn()
	}

	function showStartBtn() {
		CACHE.$done.removeClass('hide')
	}

	function doStartDownload() {
		data = {
			'ig_code':ig_code,
			'fb_code':fb_token,
            'csrfmiddlewaretoken': $('form input[name="csrfmiddlewaretoken"]').val()
		}

		//START SOCKET CONNECTION HERE!!!!!!
		$.ajax({
			type : 'POST',
			url : '/',
			data : data, 
			success: onFormSubmit
		});
		CACHE.$progress.removeClass('hide')
	}
	
	function onFormSubmit(data){
		console.log(data);
	}

	__init__();
}

// run application
$(function() {
	Ppcloud.application()
})
