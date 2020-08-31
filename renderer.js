// This file is required by the index.html file and will
// be executed in the renderer process for that window.
// All of the Node.js APIs are available in this process.
const $ = require('jquery');
const { remote } = require('electron');
const { electron } = require('process');

var win = remote.getCurrentWindow();
$('#Mask_Group_3').click(function (){
    win.minimize();
});
$('#Mask_Group_2').click(function (){
    eel.close_driver();
    win.close();
});
