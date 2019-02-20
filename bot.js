var botId       = "cs-49c2c2a8-b272-55b3-b89e-7dfed48a63ed";
var botName     = "webhook";
var sdk         = require("./lib/sdk");
var Promise     = sdk.Promise;
var request     = require("request");
var config      = require("./config");

const exec      = require("child-process-promise").exec;

module.exports = {
    botId   : botId,
    botName : botName,
               on_user_message : function(requestId, data, callback) {
				   sdk.sendBotMessage(data, callback);
    },
    on_bot_message : function(requestId, data, callback) {
                       sdk.sendUserMessage(data, callback);
    },
    on_webhook : function(requestId, data, componentName, callback) {
		console.log("Webhook:" + componentName);
	     var context = data.context;
		if(componentName === "webhook"){
			var question    = context.question;
			 var cmd = 'python ./manager.py -q "'+question+'"';
			 //console.log('[' + question + '] Print the question from the user');
			 exec(cmd)
			 .then(function (result) {
			 console.log(result.stdout)
		      data.context.result = result.stdout;
		      callback(null, data);
               })
               }
		/*if(componentName === "Allen1"){
			console.log(context.passages)
		     callback(null, data);
              }*/
	},
on_agent_transfer : function(requestId, data, callback){
        return callback(null, data);
    }
};
