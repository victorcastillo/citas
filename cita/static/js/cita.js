jQuery(document).ready(function($) {
	rome(fecha_hora_llamada);
	rome(fecha_hora_visita);
	rome(filtro_fecha_llamada);
	if($('#cp').val()){
		crear_mapas();
	}
	$('#formulario_cita').on('submit', function(event){
		event.preventDefault();
		var form = new FormData($('#formulario_cita')[0]);
		form.append('tipo_calle', $('input[name="direccion"]:checked').val() || '');
		form.append('tipo_entrada', $('input[name="tipo_puerta"]:checked').val() || '');
		form.append('tipo_habitacional', $('input[name="tipo_vecindario"]:checked').val() || '');
		form.append('ultimo_destino', $('input[name="tipo_transporte"]:checked').val() || '');
		$.ajax({
			url: '/citas/',
			data: form,
			processData: false,
			contentType: false,
			type: 'POST',
			success: function(data){
				$.fancybox(data);
				window.location.path = "/citas/buscador/";
			}
		});
	});
});

function crear_mapas(){
	$('#map-canvas').empty();
	$.get('http://maps.googleapis.com/maps/api/geocode/json?address=' +$('#cp').val()+ ',+MX&sensor=false',{},function(data){
		if(data.status == "OK"){
			var map;
			var mapa = data.results[0];
			var geometria = mapa.geometry.location;
			var mapOptions = {
				zoom: 8,
				center: new google.maps.LatLng( geometria.lat, geometria.lng)
			};
			map = new google.maps.Map(document.getElementById('map-canvas'),mapOptions);
			var marker = new google.maps.Marker({
				position: new google.maps.LatLng( geometria.lat, geometria.lng),
				map: map,
				title: mapa.formatted_address
			});
		}
	});

}

function buscar_id_cita(){
	$.get('/citas/',{"id_cita": $('#id_cita').val()}, function(data) {
		var newDoc = document.open("text/html", "replace");
		newDoc.write(data);
		newDoc.close();
	});
}