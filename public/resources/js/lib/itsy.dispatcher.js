var Itsy = Itsy || {};

/**
 * @namespace Itsy.Dispatcher
 * @description a simple event dispatcher
 * @param {object} my this is used to share secrets between objects; optional.
 *
 * @returns {object} the public interface for the Itsy.Dispatcher object
 */
Itsy.Dispatcher = function(){
    var self   = {};
    var events = [];

    function __new__(){
        self.name      = 'Itsy.Dispatcher';
        self.on        = on;
        self.off       = off;
        self.dispatch  = dispatch;

        __init__();
        return self;
    }
    
    function __init__(){
    }

    /* public methods */

    function on(eventStr, delegate, scope){
        var e = events[eventStr] = events[eventStr] || {};
        
        // init event
        e.delegates = e.delegates || [];
        e.delegates.push(delegate);
        e.scope = scope;

        if(typeof e.type === 'undefined') e.type = eventStr;

        return self;
    }
    function off(eventStr, delegate){
        var e = events[eventStr];

        //if
        if(typeof e !== 'undefined'){
            var dels = e.delegates || [];
            // for
            for(var i=0, len=dels.length; i<len; i++){
                // if
                if(dels[i] === delegate){
                    // remove delegate
                    dels.splice(i, 1);
                    
                    // if; no more delegates ? clean up refs : do nothing
                    if(dels.length === 0){
                        e.scope     = {};
                        e.delegates = [];
                    }
                }
                // #eo if
            }
            // #eo for
        }
        // #eo if
        return self;
    }
    function dispatch(eventStr, data){
        data = data || {};

        var e = events[eventStr];
        var dels;
        var del;
        var scope;
        var len;
        var exe;
        
        if(typeof e !== "undefined"){
            dels       = e.delegates || [];
            scope      = e.scope;
            len        = dels.length;
            data.scope = scope;
            exe        = (typeof scope !== 'undefined') ? executeWithScope : execute;

            // execute delegates
            while(len--){
                del = dels[len];
                exe(del, e, data, scope);
            }
        }
    }
    function executeWithScope(del, e, data, scope){
        del.apply(scope, [{'type': e.type, 'data': data}]);
    }
    function execute(del, e, data){
        del({'type': e.type, 'data':data});
    }

    return __new__();
};
/* #eo Itsy.Dispatcher */