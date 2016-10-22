'use strict';
angular.module('myApp', [
  'ui.router',
  'app.controller'
]).
config(['$locationProvider', '$stateProvider', function($locationProvider, $stateProvider) {
        $stateProvider.
          state('auth', {
            url: '/auth',
            views: {
              "viewA": {templateUrl: "app/template/auth.html"}
            },
            controller: 'authCtrl'
          }).
          state('main', {
                url: '/',
                views: {
                    "viewA": {templateUrl: "app/template/main.html"}
                },
                controller: 'mainCtrl'
            })
}]);
