const tmi = require("tmi.js");

// Define configuration options
const opts = {
	identity: {
		username: process.env.BOT_USERNAME,
		password: process.env.OAUTH_TOKEN
	},
	channels: [process.env.CHANNEL_NAME]
};

// Create a client with our options
const client = new tmi.client(opts);

// Register our event handlers (defined below)
client.on("message", onMessageHandler);
client.on("connected", onConnectedHandler);

// Connect to Twitch:
client.connect();

// Called every time a message comes in
function onMessageHandler(target, context, msg, self) {
	if (self) {
		return;
	} // Ignore messages from the bot

	const commandName = msg.trim();
	console.log(`js got chatting ${commandName}`)
	const spawn = require('child_process').spawn;
	const result_02 = spawn('C:\\Users\\rophini\\PycharmProjects\\TwitchPlaysComputer\\venv\\Scripts\\python.exe', ['bot.py', commandName]);

	result_02.stdout.on('data', (result)=>{
		console.log(result.toString());
	});

}


// Called every time the bot connects to Twitch chat
function onConnectedHandler(addr, port) {
	console.log(`* Connected to ${addr}:${port}`);
}
