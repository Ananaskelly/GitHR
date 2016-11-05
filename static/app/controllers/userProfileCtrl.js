angular.module('app.controller')
	.controller('userProfileCtrl', function($scope, Content, $stateParams, $http){
		var login = $stateParams.login;
		$scope.user = {};
		Content.getUserInfo(login).then(function(response){
			$scope.user = response;
		});
		$scope.repos = {};
		Content.getUserRepos(login).then(function(response){
			$scope.repos = response;
		})
		$http({
                    method: 'GET',
                    url: '/api/repos/tfoote'
                }).success(function (response) {
                    console.log(response);
                })
                    .error(function (error, status) {
                       
                    });
                
	})