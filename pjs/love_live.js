var picURL = 'http://tieba.baidu.com/p/2509293132#!/l/p1';
// var picURL = 'http://www.cnblogs.com/Fooo/archive/2011/10/13/2209581.html';
var jqURL = 'http://libs.baidu.com/jquery/2.0.0/jquery.js';

var page = require('webpage').create();
// var fs = require('fs');
// var path = 'output.txt';
// fs.touch(path);

page.onError = function(msg, trace) {
	var msgStack = ['ERROR: ' + msg];
	if (trace && trace.length) {
		msgStack.push('TRACE:');
		trace.forEach(function(t) {
			msgStack.push(' -> ' + t.file + ': ' + t.line + (t.function ? ' (in function "' + t.function + '")' : ''));
		});
	}
	// uncomment to log into the console 
	// console.error(msgStack.join('\n'));
};

page.open(picURL, function() {
	page.includeJs(jqURL, function() {
		var imageList = page.evaluate(function() {
			var imgs = [];
			var $allImages = $('img');
			var reg01 = new RegExp('http://imgsrc\.baidu\.com/forum/w%.*?\.jpg', 'i');
			var prefix = 'http://imgsrc.baidu.com/forum/pic/item/';

			for (var i=0; i<$allImages.length; ++i){
				var src = $allImages[i].src;
				if (reg01.test(src)) {
					imgs.push(prefix + src.split('/').pop());
				}
			}
			return imgs;
		});
		for (var i = 0; i < imageList.length; i++) {
			console.log(imageList[i]);
		}
		console.log('Tot pic: ' + imageList.length);
		phantom.exit();
	});
});
