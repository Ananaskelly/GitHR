angular.module('app.service', [])
    .factory('Content', function($q, $http){
		return {
			getRights : function(){
				var getting = $q.defer();
                $http({
                    method: 'GET',
                    url: '/token_profile'
                }).success(function (response) {
                    return getting.resolve(response);
                })
                    .error(function (error, status) {
                        return getting.reject(error);
                    });
                return getting.promise;
			}
		}		
    });