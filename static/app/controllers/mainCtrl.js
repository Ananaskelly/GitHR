
angular.module('app.controller')
    .controller('mainCtrl', function($scope, Content){
		Content.getRights().then(function(response){
			console.log(response);
		}
		)	
    });