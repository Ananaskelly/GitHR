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
                    "viewA": {templateUrl: "/static/app/template/main.html"},
                    "viewB": {templateUrl: "/static/app/template/navbar.html"}
                },
                controller: 'mainCtrl'
            }).
          state('search', {
                url: '/search',
                views: {
                    "viewA": {templateUrl: "/static/app/template/search.html"},
                    "viewB": {templateUrl: "/static/app/template/innerNavbar.html"}
                },
                controller: 'searchCtrl'
            })
}]);
