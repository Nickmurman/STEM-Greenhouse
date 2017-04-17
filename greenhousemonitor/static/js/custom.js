$(document).ready(function() {
	
	'use strict';
	
	/* ==== Preloader ==== */
	$('.spinner').fadeOut('slow');
	$('.preloader').delay(350).fadeOut();
	
	/* ==== Intro height ==== */
	$(function(){
		$('#intro').css({'height':($(window).height())+'px'});
		$(window).resize(function(){
		$('#intro').css({'height':($(window).height())+'px'});
		});
	});
	
	/* ==== Skills Tabs ==== */
	var tabContainers = $('.skills-description-wrapper .skill-description-item');

	tabContainers.hide().filter(':first').show();
	
	$('.skills-wrapper a').click(function () {
		tabContainers.hide();
		tabContainers.filter(this.hash).fadeIn("slow");
		$('.skills-wrapper a').removeClass('selected');
		$(this).addClass('selected');
		return false;
	}).filter(':first').click();
	
	/* ==== Carousel Intro ==== */
	$('#carousel-intro').carousel({
		interval: 3500,
		pause: "false"
	});
	
	/* ==== Boxer ==== */
	$('.boxer').boxer();
	
	/* ==== Contact Form ==== */
	var options = {
		target: '.message .alert',
		beforeSubmit: showRequest,
		success: showResponse
	};

	$('#contactForm').ajaxForm(options);
	function showRequest(formData, jqForm, options) {
		var queryString = $.param(formData);
			return true;
		}
	function showResponse(responseText, statusText) {}

});