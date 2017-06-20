angular
    .module('app.home')
    .controller('HomeController', HomeController);

HomeController.$inject = ['researchService', '$timeout'];

function HomeController(researchService, $timeout) {
    var vm = this;
    vm.results = false;
    vm.search = false;
    vm.query = function(apiNode, query){
        vm.search = true;
        researchService.search(apiNode, query).then(function (response) {
            vm.results = response;
            $timeout(function(){
                vm.search = false;
            }, 500);
        }).catch(function (error) {

        });
    };
    vm.query("csapractice", {"sub_practice_level__iexact":"Silvopasture"});
}