var xhr = new XMLHttpRequest();

xhr.open("GET", "https://www.googleapis.com/youtube/v3/search?part=id&q=khul+kabhi&type=video&key=AIzaSyDf-TCgD54NNSlg_PbqeJyhXWhn0B4WBzw", true);

xhr.onreadystatechange = function() {
	if (xhr.readyState === 4) {
	    var status = xhr.status;

	    if ((status >= 200 && status < 300) || status === 304) {
	        var rss = JSON.parse(xhr.responseText);
	        var el = document.getElementById('video');
	        el.innerHTML = ('<iframe id="ytplayer" type="text/html" width="640" height="390" src="https://www.youtube.com/embed/'+rss.items[0].id.videoId+'?autoplay=1"  frameborder="0"></iframe>');
	        //document.write();
	        //alert(rss.items[0].id.videoId);
	    } else {
	        alert("Request unsuccessful");
	    }
	}
};
xhr.send(null);