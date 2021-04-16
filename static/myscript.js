$(document).ready(function() {
	var test = $("#my_variable").val();
	if(test == 1){
		$("#less").toggle();
	}
	if(test > 1){
		$("#more").toggle();
	}
});
