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
		$progress : $('#progress'),
		$link_context: $('#link')
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
		CACHE.$progress.addClass('hide');
		CACHE.$link_context.addClass('hide');

		var data = {
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

		hideStartBtn();
	}
	function onFormSubmitError(data){
		// console.log('form submit ERROR!', data);
		// TODO: handle
	}
	function onFormSubmit(data){
		CACHE.$progress.removeClass('hide');
		resourceSocket.register(data.token);
	}

	// ppcloud socket event delegates
	function onResourceConnected(e){
		var data = e.data;
	}
	function onResourceMetaReceived(e){
		var data = e.data;
		var jq_progress = CACHE.$progress.find('.progress');
		var jq_bar      = CACHE.$progress.find('.bar');

		jq_progress.removeClass('progress-striped').addClass('progress');
		jq_bar.css({'width': '0%'})
	}
	function onResourceProgress(e){
		var data        = e.data;
		var percent     = data.percent * 100;
		var jq_progress = CACHE.$progress.find('.progress');
		var jq_bar      = CACHE.$progress.find('.bar');
		
		jq_bar.css({'width': percent + '%'});
		console.log(percent);
		if(percent === 100){
			setTimeout(function(){
				jq_progress.parent().removeClass('progress').addClass('progress-striped');
			}, 600);
		}
	}
	function onResourceReady(e){
		var data = e.data;
		var url = data.url;
		var jq_progress = CACHE.$progress.find('.progress');
		var jq_link = CACHE.$link_context.find('.link');
		
		jq_link.attr('href', url);
		// jq_progress.addClass('hide');
		CACHE.$progress.fadeOut('fast', function(){
			CACHE.$progress.css({'display': ''}).addClass('hide');
			CACHE.$link_context.removeClass('hide');
		});
	}

	__init__();
}

// run application
$(function() {
	Ppcloud.application()
})
