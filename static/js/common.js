$(document).ready(function()
{
    $('#tab1').click(function(){
        $('#content1').css('display','block');
        $('.tab-item').removeClass('active');
        $(this).addClass('active');
        $('#content2').css('display','none');
    });
	
    $('#tab2').click(function(){
        $('#content2').css('display','block');
        $('#content1').css('display','none');
        $('.tab-item').removeClass('active');
        $(this).addClass('active');
    });
	
    $('#content1').slick({
        dots:true,
        nav:false
    });
    $('.header .xs-menu').click(function(){
    	$('.right').slideToggle();
	});
    $(".settings-tabs").lightTabs();
	//$(".chat__content").scrollTop($(".chat__content")[0].scrollHeight);
	
	function screen_size()
	{
		var screen_size = $('input[name=screen-size]');
		if(screen_size.attr('name') != '') { screen_size.attr('value',screen.width + 'x' + screen.height); }
	}
	
	screen_size();
	
	$('input[name=phone], input[name=login], input[name=username]').mask("0000000000");
	$('input[name=date]').mask("00/00/0000");
	
	function url()
	{
		var url		= location.hash.substr(1);
		var regV	= /\//gi;
		var result	= url.replace(regV,'');
		return url;
	}
	
	var url = url();
	
	if($('.select[name=cat]')[0] && url != '')
	{
		$('.select[name=cat]').val(url);
	}
	
	$('#form').on('submit',
	function(e)
	{
		if(!confirm("Вы действительно хотите забрать средства?"))
		{
			e.preventDefault();
		}
	});
	
	$('a.btn[rel=submit]').on('click',
	function()
	{
		if($('input[name=sum]').val() != '')
		{
			$('#form').submit();
		}
	});
	
	var domain = window.location.protocol + '//' + window.location.hostname;

	$('.rating-r').on('click',
	function(e)
	{
		if(!$(this).hasClass('active'))
		{
			var token, data, value;		
			value = $(this).attr('class').split(' ');
			
			function addVotes(a)
			{
				$.ajax({
					type: 'POST',
					url: domain + atob('L3ZvdGU='),
					data: {data:value[1]},
					beforeSend: function () {
						// Enabled preloader
					},
					success: function(data)
					{
						obj = JSON.parse(data);

						if(obj.result != null && obj.result != '')
						{
							if(obj.result == 'success')
							{
								$('.rating-r.active').html(parseInt($('.rating-r.active').html()) - 1);
								$('.rating-r.active').removeClass('active');
								a.addClass('active').html(parseInt(a.html()) + + 1);
								alert(obj.message);
							}
							if(obj.result == 'voted')
							{
								alert(obj.message);
							}							
						}
					}
				});
			}
			
			return addVotes($(this));
		}
	});
	
	$('.sidebar-menu').on('click',
	function()
	{
		if($(this).hasClass('active')) {
			$(this).removeClass('active');
		} else {
			$(this).addClass('active');
		}
	});
	
	$( '.upload input[type=file]' ).change(
	function()
	{
		if($('.upload input[type=file]').val() != ''){	
			$('#upload input[type=submit]').click();
		}
	});
	
	$('#upload input[type=submit]').click( function ()
	{
		$('#upload').ajaxForm({
			beforeSubmit:function(formData, jqForm, options){
				$('.progress-bar').show();
				var n = formData[0].value.name;
				var ext = n.substr(n.lastIndexOf('.') + 1);
				var et = ext.toUpperCase();
				var array = ['png','jpg','jpeg','gif','PNG','JPG','JPEG','GIF'];
				var there = $.inArray(et, array);
				if(there == -1)
				{
					$('.progress-bar').hide(); alert('Error'); return false;
				}	
				else{
					return true;
				}	
			},
			uploadProgress:function(event,position,total,percentComplete){
				$('.progress-bar .meter span').width(percentComplete+'%'); $('.upload').hide();
			},
			success:function(){
				$('.progress-bar .meter span, .upload').hide();
			},
			complete:function(response){
				if(response.responseText=='error')
				{
					alert('Error'); return false;
				} 
				else
				{
					document.location.reload(true);
				}
			}
		});
	});
	
	function clear(str)
	{
		var str = str.replace(/<br>/gi, "<br />");
		var str = str.replace(/<p.*>/gi, "\n");
		var str = str.replace(/<img.*src="(.*?)">/gi, "[img scr='$1']");
		var str = str.replace(/<a.*href="(.*?)".*>(.*?)<\/a>/gi, " $2 (Link->$1) ");
		var str = str.replace(/<(?:.|\s)*?>/g, "");
		return str;
	}
	
	function updateChat()
	{
		var c_content, txt, hlem, c_div;
			c_content	= $('.chat__content');
			c_div 		= c_content[0].scrollHeight;
			txt			= $('.chat__item:last').attr('data-value');
			
			$.ajax({
				type: 'POST',
				url: domain + atob('L2NoYXQtY29udGVudA=='),
				data: {txt:txt},
				success: function(response)
				{
					c_content.append(response).attr('data-value','1');
						
					if(response != '' && c_content.attr('data-value') == 1)
					{
						c_content.animate({scrollTop: + c_div}).attr('data-value','0');
					}
				}
			});
			
			if(c_content.attr('data-value') == 0)
			{
				c_content.animate({scrollTop: + c_div}, 800).attr('data-value','1');
			}
		
		setTimeout(updateChat, 2000)
	}
	
	if($('.chat__content').hasClass('chat__content'))
	{
		updateChat();
	}

	function chat(data)
	{
		if(data != null && data != "")
		{			
			$.ajax({
				type: 'POST',
				url: domain + atob('L2NoYXQ='),
				data: {msg:data},
				success: function(data)
				{
					obj = JSON.parse(data);

					if(obj.result != null && obj.result != '')
					{
						if(obj.result == 'success')
						{
							$('.new-message').val([]).removeAttr('disabled');
						}
						else
						{
							$('.new-message').val([]).removeAttr('disabled');
						}
						
						if(obj.redirect != null)
						{
							document.location=obj.redirect;
						}
						
						if(obj.message != null)
						{
							alert(obj.message);
						}
					}
				}
			});
		}
	}
	
	$('.new-message').on('keypress',
	function(e)
	{
		if(e.keyCode === 13)
		{
			var val = clear($(this).val());

			if(val.length > 0 && val != "")
			{
				$(this).blur().attr('disabled','disabled');
				chat(val);
			}
		}
	});
	
});
(function($){
    jQuery.fn.lightTabs = function(options){

        var createTabs = function(){
            tabs = this;
            i = 0;

            showPage = function(i){
                $(tabs).children("div").children("div").hide();
                $(tabs).children("div").children("div").eq(i).show();
                $(tabs).children("ul").children("li").removeClass("active");
                $(tabs).children("ul").children("li").eq(i).addClass("active");
            }

            showPage(0);

            $(tabs).children("ul").children("li").each(function(index, element){
                $(element).attr("data-page", i);
                i++;
            });

            $(tabs).children("ul").children("li").click(function(){
                showPage(parseInt($(this).attr("data-page")));
            });
        };
        return this.each(createTabs);
    };
})(jQuery);