var repasswderror = "비밀번호가 다릅니다"

$(document).ready(function(){
    $("form[name='inputform']").on("submit", function(event){
        if($("input[name='pw'").val() != $("input[name='repw'").val()){
            alert(repasswderror);
			$("input[name='repw']").focus();
			return false;
        }
    })

	//ajaxSetup 장고토큰 설정
	$.ajaxSetup({
		headers: {"X-CSRFToken" : $("input[name='csrfmiddlewaretoken']").val()}
	});
	
	//아이디중복 ajax
	$("input[name='id']").keyup(function(){
		
		var id = $("input[name='id']").val();
		
		$.ajax({
			type : "POST",
			url : "idchk",
			data : { "id" : id },
			success : function(data){
				//alert("OK");
				$("#chk").html("아이디가 있습니다");
			},
			error : function(error){
				//alert("aaaaaaa")
				//$("#chk").html(error);
				//$("#chk").html("아이디가 없습니다");
				$("#chk").html("");
			}
		});
		
	});
});

//비밀번호 4자리이상
function pwchk(){
	var pwlen = $("input[name='pw']").val().length; 
	if(pwlen < 4){
		$("#pwchk").html("비밀번호는 4자리 이상입니다");
	}else{
		$("#pwchk").html("");
	}
}

//비밀번호 확인
function repwchk(){
	//var pw = $("input[name'passwd']").val();
	var pw = $("input[name='pw']").val();
	var repw = $("input[name='repw']").val();
	if(pw != repw){
		$("#repwchk").html("비밀번호가 다릅니다");
	}else{
		$("#repwchk").html("");
	}
}



