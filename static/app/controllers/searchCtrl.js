angular.module('app.controller')
    .controller('searchCtrl', function($scope, $state){
		$scope.user = {};
		$scope.search = function() {
			$state.go('userProfile', {'login': $scope.user.login})
		}		
    });