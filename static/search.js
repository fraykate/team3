#!/usr/bin/env node


var count1 =(function () {
            
            var counter = 276;
            return function () {return counter +=1;}
        })();
            
        var count2 =(function () {
            
            var counter = 52;
            return function () {return counter +=1;}
        })();
            
        var count3 =(function () {
            
            var counter = 133;
            return function () {return counter +=1;}
        })();
            
        function displaycount1(){
            document.getElementById("carrier1").innerHTML = count1();
            
        }
            
        function displaycount2(){
            document.getElementById("carrier2").innerHTML = count2();
           
        }
            
        function displaycount3(){
            
            document.getElementById("carrier3").innerHTML = count3();
        }
