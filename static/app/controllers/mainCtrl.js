
angular.module('app.controller')
    .controller('mainCtrl', function($scope, Content, $state){
		Content.getRights().then(function(response){
			if (JSON.parse(response.toLowerCase())) {
				$state.go('search');
			}
		}
		)	
    });