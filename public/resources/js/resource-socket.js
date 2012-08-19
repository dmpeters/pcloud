var Ppcloud = Ppcloud || {};

// events
Ppcloud.ResourceEvents = {
	"Connected": 'connected',
	"Progress":  'progress',
	'MetaReceived': 'metaReceived',
	"Ready":     'ready',
	"Error":     'error'
};

// socket io wrapper
Ppcloud.ResourceSocket = function(){
	var self = {};
	var socket = false;
	var dispatcher = false;
	var events = Ppcloud.ResourceEvents;

	var status = {
		'meta': {},
		'percent': 0,
		'pending': 0,
		'total': 0,
		'last_completed': {'network':false, 'url':false}
	}

	function __new__(){
		__init__();

		self.register = register;
		self.on        = dispatcher.on;
		self.off       = dispatcher.off;

		return self;
	}
	function __init__(){
		socket = io.connect('/status');
		
		dispatcher = Itsy.Dispatcher();

		// socket connection stuff
		socket.on('connect', socketWasConnected);
		socket.on('progress_meta', resourceMetaWasReceived);
		socket.on('resource_complete', resourceCompleted);
		socket.on('finished', resourceReady);
	}

	// public functions
	function register(token){
		socket.emit('register', token);
	}

	// socket io delegates
	function socketWasConnected(){
		dispatcher.dispatch(events.Connected, true);
	}
	// payload {'facebook':22, 'instagram': 10, 'total': 32}
	function resourceMetaWasReceived(data){
		var meta = JSON.parse(data);

		status.meta = meta;
		status.pending = meta.total;
		status.total = meta.total;

		dispatcher.dispatch(events.MetaReceived, status);
	}
	// payload {'network': 'facebook', 'url': 'http://the-path-to-img/img.jpg'}
	function resourceCompleted(data){
		status.pending--;
		status.percent = 1 - (status.pending / status.meta.total);
		status.last_completed = data;
		dispatcher.dispatch(events.Progress, status);
	}
	// payload {'url': 'http://pickup-your-stuff/file.zip'}
	function resourceReady(data){
		dispatcher.dispatch(events.Ready, data);
	}
	
	return __new__();

}