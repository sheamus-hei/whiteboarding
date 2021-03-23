// given an array of people objects, return the  two people with the smallest difference in birthdays

let people = [
  {
    name: "Erik",
    bday: new Date(1995, 6, 9)
  },
  {
    name: "Zack",
    bday: new Date(1992, 10, 16)
  },
  {
    name: "Barry",
    bday: new Date(1960, 4, 21)
  },
  {
    name: "Jackie",
    bday: new Date(1968, 2, 6)
  }
]

function findClosest(people){
  if (people.length < 2) {
    return people
  }
  people.sort((a, b) =>  a.bday - b.bday)
  // console.log(people)
  let output = []
  let smallestDiff = Number.MAX_VALUE
  for (let i = 1; i <  people.length; i++) {
    // compare birthdays for people[i - 1] and people[i]
    if (people[i].bday - people[i-1].bday < smallestDiff) {
      smallestDiff = people[i].bday - people[i-1].bday;
      output = [people[i-1], people[i]]
    }
  }
  return output
}

console.log(findClosest(people))

