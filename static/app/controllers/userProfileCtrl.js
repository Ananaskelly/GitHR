angular.module('app.controller')
	.controller('userProfileCtrl', function($scope, Content, $stateParams){
		var repos = {};
		$scope.shownRepos = [];
		$scope.user = {};
		$scope.selectedLangs = [];
		var selected = 0;
		var login = $stateParams.login;
		var langs = {};
		$scope.user.relevantLangs = [];
		Content.getUserInfo(login).then(function(response){
			$scope.user = response;
		});
		Content.getUserRepos(login).then(function(response){
			repos = response;
			for (var key in response){
				$scope.shownRepos.push(response[key]);
				var lang = response[key].language;
				if (langs.hasOwnProperty(lang)) {
					langs[lang].amount ++;
					langs[lang].associatedKeys.push(key);
				} else {
					langs[lang] = {
						'amount': 1,
						'associatedKeys': [key]
					};
				}
			}
			$scope.user.relevantLangs = Object.keys(langs).sort(
				function(a,b){
					return langs[b].amount-langs[a].amount
			});
		})
		$scope.selectByLang = function(index){
			var choosenLang = $scope.user.relevantLangs[index];
			if ($scope.selectedLangs.indexOf(choosenLang) !== -1){
				return 
			}
			$scope.selectedLangs.push(choosenLang);
			if (selected === 0){
				$scope.shownRepos.length = 0;
			}
			selected ++;
			for (var i=0; i<langs[choosenLang].associatedKeys.length; i++) {
				$scope.shownRepos.push(repos[langs[choosenLang].associatedKeys[i]]);
			}
			console.log(langs[choosenLang].associatedKeys);
		}
		
		$scope.deleteFromSet = function(index){
			var choosenLang = $scope.selectedLangs[index];
			$scope.selectedLangs.splice(index,1);
			selected --;
			if (selected === 0){
				$scope.shownRepos.length = 0;
				for (var key in repos){
					$scope.shownRepos.push(repos[key]);
				}
			}
			for (var i=0; i<langs[choosenLang].associatedKeys.length; i++) {
				var repInd = $scope.shownRepos.indexOf(repos[langs[choosenLang].associatedKeys[i]])
				$scope.shownRepos.pop(repInd,1);
			}
			
		}		
	})