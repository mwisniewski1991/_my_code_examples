package com.basic

object Main extends App {

    println("----------------")
    println("Data Structure")

    println("----")
    println("List")
    val myList = List(1,2,3,4,5)
    println(s"myList.head $myList.head")
    println(s"myList.tail $myList.tail")

    val prependedList = 0 :: myList
    println(s"prependedList: $prependedList")
    val extendedList = 0 +: myList :+ 6
    println(s"extendedList: $extendedList")


    println("----")
    println("Sequence")
    val mySeq: Seq[Int] = Seq(1,2,3)
    println(s"seq $mySeq")

    val seqElement = mySeq(1)
    println(s"seqElement $seqElement")


    println("----")
    println("Vector") //Fast Sequence Implementation
    val myVector = Vector(1,2,3,4,5)
    println(s"myVector $myVector")


    println("----")
    println("Set") //No duplicates
    val mySet = Set(1,2,3,1,2,3)
    println(s"mySet $mySet")

    val setHas5 = mySet.contains(5)
    println(s"setHas5 $setHas5")

    val addedSet = mySet + 4
    println(s"addedSet $addedSet")
    
    val removedSet = addedSet - 1
    println(s"removedSet $removedSet")


    println("----")
    println("Range")
    val myRange = 1 to 1000
    val twoByTwo = myRange.map(x => 2 * x).toList //List(2, 4, 6, ... , 2000)


    println("----")
    println("Tuple")
    val myTuple = ("Mat", "Pat", 1991)
    println(s"myTuple $myTuple")


    println("----")
    println("Maps")
    val myMap: Map[String, Int] = Map(
        ("Mat", 123123),
        "Pat" -> 456456,
    )
    println(s"myMap $myMap")

}
