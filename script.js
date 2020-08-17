console.log("hello");
var a = Object() ;
a.firstname="kavan"; 
a.lastname="dalal";
a.game= Object();
a.game.fps = "csgo";
a["full name"] = "kavan dalal";
console.log("full name : " + a["full name"]);
console.log(a);

var social = {
	steam : "kd", 
	reddit : {
		name : "jiraiya", 
		karma : 420
	},
	insta :"kavan",
	"full name" : "kavandalal"
}
console.log(social);
