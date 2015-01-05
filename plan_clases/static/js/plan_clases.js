jQuery(document).ready(function($) {
	$('#formulario_plan_clases').on('submit', function(event){
		event.preventDefault();
		var form = new FormData($('#formulario_plan_clases')[0]);
		form.append('uso_pedagogico_1', $('input[name="uso_pedagogico_1"]:checked').val() || '');
		form.append('uso_pedagogico_2', $('input[name="uso_pedagogico_2"]:checked').val() || '');
		form.append('uso_pedagogico_3', $('input[name="uso_pedagogico_3"]:checked').val() || '');
		form.append('uso_pedagogico_4', $('input[name="uso_pedagogico_4"]:checked').val() || '');
		form.append('uso_pedagogico_5', $('input[name="uso_pedagogico_5"]:checked').val() || '');
		$.ajax({
			url: '/plan_clases/',
			data: form,
			processData: false,
			contentType: false,
			type: 'POST',
			success: function(data){
				$.fancybox(data);
				window.location.path = "/plan_clases/";
			}
		});
	});
});