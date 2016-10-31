angular.module('app.controller')
	.controller('innerNavbarCtrl', function($scope, Content){
		$scope.user = {};
		Content.getCurrentUser().then(function(response){
			if (response){
				$scope.user.login = response.login;
				$scope.user.avatar_url = response.avatar_url;
			}
		})
	})