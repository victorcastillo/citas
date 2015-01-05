jQuery(document).ready(function($) {
	$('#formulario_lista_asistentes').on('submit', function(event){
		event.preventDefault();
		var form = new FormData($('#formulario_lista_asistentes')[0]);
		$.ajax({
			url: '/lista_asistentes/',
			data: form,
			processData: false,
			contentType: false,
			type: 'POST',
			success: function(data){
				$.fancybox(data);
				window.location.path = "/lista_asistentes/";
			}
		});
	});
});