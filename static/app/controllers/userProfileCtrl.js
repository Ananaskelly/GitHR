angular.module('app.controller')
	.controller('userProfileCtrl', function($scope, Content, $stateParams){
		var login = $stateParams.login;
		$scope.user = {};
		Content.getUserInfo(login).then(function(response){
			$scope.user = response;
		});
	})