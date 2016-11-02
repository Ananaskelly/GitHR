angular.module('app.service', [])
    .factory('Content', function($q, $http){
		return {
			getRights : function(){
				var getting = $q.defer();
                $http({
                    method: 'GET',
                    url: '/token'
                }).success(function (response) {
                    return getting.resolve(response);
                })
                    .error(function (error, status) {
                        return getting.reject(error);
                    });
                return getting.promise;
			},
			getCurrentUser : function() {
				var getting = $q.defer();
                $http({
                    method: 'GET',
                    url: '/current'
                }).success(function (response) {
                    return getting.resolve(response);
                })
                    .error(function (error, status) {
                        return getting.reject(error);
                    });
                return getting.promise;
			}, 
			getUserInfo: function(login) {
				var getting = $q.defer();
                $http({
                    method: 'GET',
                    url: '/api/'+login
                }).success(function (response) {
                    return getting.resolve(response);
                })
                    .error(function (error, status) {
                        return getting.reject(error);
                    });
                return getting.promise;
			},
			getUserRepos: function(login) {
				var getting = $q.defer();
                $http({
                    method: 'GET',
                    url: '/api/repos/'+login
                }).success(function (response) {
                    return getting.resolve(response);
                })
                    .error(function (error, status) {
                        return getting.reject(error);
                    });
                return getting.promise;
			},
		}		
    });