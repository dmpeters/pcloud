var Ppcloud = Ppcloud || {};

// events
Ppcloud.SocketEvents = {
	"Connected": 'connected',
	"Progress":  'progress',
	"Complete":  'complete',
	"Ready":     'ready',
	"Error":     'error'
};

// socket io wrapper
Ppcloud.socket = function(){
	var self = {};
	var socket = false;
	var dispatcher = false;
	var events = Ppcloud.SocketEvents;

	function __new__(){
		__init__();

		self.sendToken = sendToken;
		self.on        = dispatcher.on;
		self.off       = dispatcher.off;

		return self;
	}
	function __init__(){
		console.log('Ppcloud socket init OK!');
		
		socket = io.connect('/status');
		dispatcher = Itsy.Dispatcher();

		// socket connection stuff
		socket.on('connect', socketWasConnected);
		socket.on('progress_meta', socketProcessProgress);
		socket.on('resource_complete', socketProcessComplete);
		socket.on('finished', socketResourceReady);
	}

	// public functions
	function sendToken(token){
		socket.emit('register', token);
	}

	// socket io delegates
	function socketWasConnected(){
		// console.log('socket connection OK!');
		dispatcher.dispatch(events.Connected, true);
	}
	// payload {'facebook':22, 'instagram': 10, 'total': 32}
	function socketProcessProgress(data){
		// console.log('socket progress', data);
		dispatcher.dispatch(events.Progress, data);
	}
	// payload {'network': 'facebook', 'url': 'http://the-path-to-img/img.jpg'}
	function socketProcessComplete(data){
		// console.log('resource complete', data);
		dispatcher.dispatch(events.Complete, data);
	}
	// payload {'url': 'http://pickup-your-shit/file.zip'}
	function socketResourceReady(data){
		// console.log('resource ready', data);
		dispatcher.dispatcher(events.Ready, data);
	}


	return __new__();

}