var Ppcloud = Ppcloud || {};

Ppcloud.application = function() {
	var my = my || {};
	var self = {};
	var fb, ig;
	var fb_token = ''
	var ig_code = ''
	var resourceSocket = Ppcloud.ResourceSocket();
	var resourceEvents = Ppcloud.ResourceEvents;

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

		resourceSocket.on(resourceEvents.Connected, onResourceConnected);
		resourceSocket.on(resourceEvents.MetaReceived, onResourceMetaReceived);		
		resourceSocket.on(resourceEvents.Progress, onResourceProgress);
		resourceSocket.on(resourceEvents.Ready, onResourceReady);
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
	
	function hideStartBtn() {
		CACHE.$done.addClass('hide');
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
			success: onFormSubmit,
			error: onFormSubmitError
		});
		CACHE.$progress.removeClass('hide');
		hideStartBtn();
	}
	function onFormSubmitError(data){
		console.log('form submit ERROR!', data);
	}
	function onFormSubmit(data){
		resourceSocket.register(data.token);
	}

	// ppcloud socket event delegates
	function onResourceConnected(e){
		var data = e.data;
		console.log('resoucre connected!', data);
	}
	function onResourceMetaReceived(e){
		console.log('resource meta received', data);

		var jq_progress = CACHE.$progress.find('.progress');
		jq_progress.removeClass('progress-striped').addClass('progress');
	}
	function onResourceProgress(e){
		var data        = e.data;
		var percent     = data.percent * 100;
		var jq_progress = CACHE.$progress.find('.progress');
		var jq_bar      = CACHE.$progress.find('.bar');
		
		jq_bar.css({'width': percent + '%'});

		// show busy bar (100%);
		// on first progress update progress bar
		// on 100% bring back to busy bar
		// on ready kill loader
		// display link
	}
	function onResourceReady(e){
		var data = e.data;
		console.log('resource ready!', data);
	}

	__init__();
}

// run application
$(function() {
	Ppcloud.application()
})
