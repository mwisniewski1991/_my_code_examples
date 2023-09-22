package com.basic

object Main extends App {
    
    println("Hello Functions")

    val doubler = new Function1[Int, Int] {
        override def apply(v1: Int): Int = 2 * v1
    }
    val doublerValue = doubler(10)
    val doublerValueApply = doubler.apply(10)

    println(s"doubler value is: $doublerValue")
    println(s"doubler value apply is: $doublerValueApply")

    //syntax sugar
    val doublerSecond: Function1[Int, Int] = (v1: Int) => 2 * v1
    val doublerSecondValue = doublerSecond(20)
    println(s"doublerSecond value is: $doublerSecondValue")

    val doublerThird: Int => Int = (v1: Int) => 2 * v1
    val doublerThirdValue = doublerThird(30)
    println(s"doublerThird value is: $doublerThirdValue")

}
