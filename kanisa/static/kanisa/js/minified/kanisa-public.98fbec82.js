function toggle_document_details(c){c.preventDefault();var b=$(this);b.toggle();var a=b.attr("class");if(a=="document_details_short"){b.siblings(".document_details_full").toggle()}else{b.siblings(".document_details_short").toggle()}}$(document).ready(function(){$(".document_details_short").click(toggle_document_details);$(".document_details_full").click(toggle_document_details)});jQuery(document).ajaxSend(function(c,f,b){function a(g){var l=null;if(document.cookie&&document.cookie!=""){var k=document.cookie.split(";");for(var j=0;j<k.length;j++){var h=jQuery.trim(k[j]);if(h.substring(0,g.length+1)==(g+"=")){l=decodeURIComponent(h.substring(g.length+1));break}}}return l}function e(h){var j=document.location.host;var k=document.location.protocol;var i="//"+j;var g=k+i;return(h==g||h.slice(0,g.length+1)==g+"/")||(h==i||h.slice(0,i.length+1)==i+"/")||!(/^(\/\/|http:|https:).*/.test(h))}function d(g){return(/^(GET|HEAD|OPTIONS|TRACE)$/.test(g))}if(!d(b.type)&&e(b.url)){f.setRequestHeader("X-CSRFToken",a("csrftoken"))}});function update_list_of_regular_events(c){c.preventDefault();var b=$(this);var a=b.attr("data-cat-id");$.get(update_regular_events_list,{category:a},function(d){$("#regular_event_list").html(d)});b.parent().parent().find(".active").removeClass("active");b.parent().addClass("active")}$(document).ready(function(){$(".event_category_filter").click(update_list_of_regular_events)});$(document).ready(function(){$(".kanisaloginform").find("#id_username").focus()});$(document).ready(function(){$(".carousel").carousel({interval:2000})});