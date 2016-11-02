angular.module('app.controller')
	.controller('innerNavbarCtrl', function($scope, Content, $rootScope){
		$scope.user = $rootScope.user || {};
		console.log($rootScope.user);
		if (!$rootScope.user) {
			Content.getCurrentUser().then(function(response){
				if (response){
					$scope.user.login = response.login;
					$scope.user.avatar_url = response.avatar_url;
					$rootScope.user = $scope.user;
				}
			})
		}
	})