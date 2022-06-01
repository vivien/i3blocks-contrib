const $ = require('jquery')
var fs = require('fs')
const path = require('path')
var { remote, ipcRenderer } = require('electron')
const { cie_to_rgb, rgb_to_cie } = require("./convert-color")
const { lightState, HueApi } = require("node-hue-api")

const LIGHT_ID = 1
const NS_PER_SEC = 1e9

const config = remote.getGlobal('sharedObject').config

var host = config[0],
    username = config[1],
    api = new HueApi(host, username),
    state = lightState.create()

function componentToHex(c) {
    var hex = c.toString(16)
    return hex.length == 1 ? "0" + hex : hex
}

function rgbToHex(r, g, b) {
    return "#" + componentToHex(r) + componentToHex(g) + componentToHex(b)
}

$(() => {

    // create canvas and context objects
    var canvas = document.getElementById('picker')
    var ctx = canvas.getContext('2d')

    var last_api_call = process.hrtime()

    // drawing active image
    var image = new Image()
    image.onload = function () {
        ctx.drawImage(image, 0, 0, image.width, image.height) // draw the image on the canvas
    }

    image.src = path.join(__dirname, 'images/colorwheel.png')

    $('#picker').mousemove(function(e) { // mouse move handler
        // get coordinates of current position
        var canvasOffset = $(canvas).offset()
        var canvasX = Math.floor(e.pageX - canvasOffset.left)
        var canvasY = Math.floor(e.pageY - canvasOffset.top)

        // get current pixel
        var imageData = ctx.getImageData(canvasX, canvasY, 1, 1)
        var pixel = imageData.data

        // update controls
        $('#rVal').val(pixel[0])
        $('#gVal').val(pixel[1])
        $('#bVal').val(pixel[2])
        $('#rgbVal').val(pixel[0]+','+pixel[1]+','+pixel[2])

        var dColor = pixel[2] + 256 * pixel[1] + 65536 * pixel[0]
        var hex = dColor.toString(16)
        $('#hexVal').val('#' + hex)

        let diff = process.hrtime(last_api_call)

        if(diff[0] > 0 || diff[1] > 1e8) {
            last_api_call = process.hrtime()

            let xy = rgb_to_cie(pixel[0],pixel[1],pixel[2])

            let state = lightState.create().on().xy(xy[0], xy[1])

            api.setLightState(LIGHT_ID, state)
                .done()
        }

    })

    $('#picker').click(function(e) { // click event handler
        ipcRenderer.sendSync('hide', 'hide')
    }) 
})