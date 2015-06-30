var http = require('http'); 
http.createServer(function (request, response) { 
    response.writeHead(200, {'Content-Type': 'text/plain'}); 
    response.end('Hello World!\n'); 
    }).listen(8000,'192.168.1.42');  

// call external scripts?
//childProcess.exec('ls /media/external/', movieCallback); //works

var request = require('request');

request.post(
    'http://remote-alert.herokuapp.com/post/4d343079-7fd5-4a05-82f8-4179a48dc632',
    { message: 'Hello from node'},
    function (error, response, body) {
        if (!error && response.statusCode == 200) {
            console.log(body)
        }
    }
);

console.log('Server running at http://192.168.1.42:8000/');

var Gpio = require('onoff').Gpio;
var pir = new Gpio(17, 'out');
 
 