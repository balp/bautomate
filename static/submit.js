/*
 * This script will handle pushing the light bulb, telling the server and then
 * reload the bulb with the right image.
 */

// When document loaded, override some stuff
$(document).ready(function() {
	
	// All the submits are in the lightchange class.
	$(".lightchange").submit(function() {
		event.preventDefault(); 
		var $form = $(this);
		var csrf = $form.find( 'input[name="csrfmiddlewaretoken"]' ).val();
		var value = $form.find( 'input[name="to"]' ).val();
		var url = $form.attr('action');
		var posting = $.post( url, { csrfmiddlewaretoken: csrf , to: value } );
		posting.done(function( data ) {
			if(data.on) {
				$form.find( 'input[name="to"]' ).val('off')
				$form.find( 'input[name="Switch"]' ).attr("src",
						STATIC_URL + "worked-awhile-lights-icons-by-artbees/png/96/OnLamp.png");
			} else {
				$form.find( 'input[name="to"]' ).val('on')	
				$form.find( 'input[name="Switch"]' ).attr("src",
						STATIC_URL + "worked-awhile-lights-icons-by-artbees/png/96/OffLamp.png");
			}
	    });
		
	});
});

