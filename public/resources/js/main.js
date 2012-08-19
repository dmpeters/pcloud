var Ppcloud = Ppcloud || {};

Ppcloud.application = function() {
	var my = my || {};
	var self = {};
	var fb, ig;
	var fb_token = ''
	var ig_code = ''
	var pcloud_socket = Ppcloud.socket();

	var CACHE = {
		$done : $('#done'),
		$progress : $('#progress')
	}

	/* initialization */
	function __init__() {
		fb = Ppcloud.facebook()
		ig = Ppcloud.instagram()
		
		fb.onConnect = onFbConnect
		ig.onConnect = onIgConnect

		CACHE.$done.on('click', function() {
			doStartDownload();
		});

		pcloud_socket.on(Ppcloud.SocketEvents.Connected, function(data){
			console.log('ppcloud socket connection OK!', data);
		});
	}

	function onFbConnect(c) {
		fb_token = c
		connected();
	}

	function onIgConnect(c) {
		ig_code = c
		connected();
	}

	function connected() {
		showStartBtn();
	}

	function showStartBtn() {
		CACHE.$done.removeClass('hide');
	}

	function doStartDownload() {
		data = {
			'ig_code':ig_code,
			'fb_code':fb_token,
            'csrfmiddlewaretoken': $('form input[name="csrfmiddlewaretoken"]').val()
		}

		console.log('start download OK!', data);


		//START SOCKET CONNECTION HERE!!!!!!
		$.ajax({
			type : 'POST',
			url : '/',
			data : data, 
			success: onFormSubmit
		});
		CACHE.$progress.removeClass('hide');
	}
	
	function onFormSubmit(data){
		console.log('form submit OK!', data);

		pcloud_socket.sendToken(data);
	}

	__init__();
}

// run application
$(function() {
	Ppcloud.application()
})
