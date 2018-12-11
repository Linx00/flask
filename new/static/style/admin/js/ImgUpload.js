var Img = {
		ChooseImg: function(did) {
			var canClick = true;
			var e = this;
			var input = document.createElement("input");
			input.setAttribute("type", "file");
			input.setAttribute("name", "file");
			input.style.display = "none";
			input.onchange = function() {
				var size = parseInt(this.files[0].size / 1024);
				var path = e.getRealUrl(this.files[0]);
				if (size > 0) {
					if (size > 200) {
    					alert('图片最大200kb 请重新选择！');
    				} else {
    					$('#'+did+' > img').attr('src', path);
					}
					canClick = true;
				}
			}
			$("#" + did).on("click", function(ev) {
				if (canClick == true) {
            		input.click();
                    setTimeout(function() {
                        canClick = true;
                    }, 6000);
				}
            	canClick = false;
			});
		},
		
		getBase64: function(did, callback) {
	        var dataURL = "";
	        var imgurl = $("#"+did+" > img").attr("src");
//	        if (imgurl == "" || imgurl == undefined) {
//	        	callback?callback(dataURL):null; //调用回调函数
//	        	return;
//	        }
	        var Img = new Image();
	        if (imgurl == null || imgurl.length < 1) {
	        	Img.src = "../Pages/images/default.jpg";
			} else {
				Img.src = imgurl;
			}
	        Img.onload = function() { // 确保图片完整获取到  异步事件
	            var canvas = document.createElement("canvas");
	            
	            var scale = 1; // 比例
	            if(Img.width > 220 || Img.height > 220){
					if(Img.width > Img.height) {
					    scale = 220 / Img.width;
					} else {
					    scale = 220 / Img.height;
					}
				}
	            
	            canvas.width = Img.width * scale;
	            canvas.height = Img.height * scale;
	            canvas.getContext("2d").drawImage(Img, 0, 0, canvas.width, canvas.height);
	            dataURL = canvas.toDataURL('image/jpeg');
	            
	            callback?callback(dataURL):null;
	        };
	    },
		
		getRealUrl: function(file) {
			var url = "";
			// 兼容各种浏览器
			if (window.createObjectURL != undefined){ // basic
                url = window.createObjectURL(file);
            } else if (window.URL != undefined) { // mozilla(firefox)
                url = window.URL.createObjectURL(file);
            } else if (window.webkitURL != undefined) { // webkit or chrome
                url = window.webkitURL.createObjectURL(file);
            }
            return url;
		}
}