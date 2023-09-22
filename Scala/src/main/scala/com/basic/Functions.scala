package com.basic

object Main extends App {

    println("----------------")
    println("High Order Functions")

    val mappedList = List(1,2,3).map(x => x * 2)
    println(s"mappedList: $mappedList")

    val flatMapListInList = List(1,2,3).map(x => List(x, 2 * x))
    println(s"flatMapListInList: $flatMapListInList")

    val flatMapList = List(1,2,3).flatMap(x => List(x, 2 * x))
    println(s"flatMapList: $flatMapList")

    val filteredList = List(1,2,3,4,5,6).filter(x => x > 3)
    println(s"filteredList: $filteredList")

    val filteredList2 = List(1,2,3,4,5,6).filter(_ > 3)
    println(s"filteredList2: $filteredList2")

    val matrix = List(1,2,3).flatMap(number => List("a","b","c").map(letter => s"$number::$letter"))
    println(s"matrix: $matrix")

    val matrixAlt = for {
        number <- List(1,2,3)
        letter <- List("a","b","c")
    } yield s"$number::$letter"
    println(s"matrixAlt: $matrixAlt")
    
    val matrixAdvanced = for {
        number <- List(1,2,3,4,5,6)
        if number <= 2
        letter <- List("a","b","c")
        if letter == "a"
    } yield s"$number::$letter"
    println(s"matrixAdvanced: $matrixAdvanced")


}
