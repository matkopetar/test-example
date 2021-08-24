
let db_records = [
  {
    "user_id": 1,
    "device": "Windows 10",
    "action": "start",
    "date_actioned": 100,
  },
  {
    "user_id": 2,
    "device": "OSX 15.4",
    "action": "start",
    "date_actioned": 200,
  },
  {
    "user_id": 1,
    "device": "iPhone 8s",
    "action": "start",
    "date_actioned": 250,
  },
  {
    "user_id": 1,
    "device": "Windows 10",
    "action": "stop",
    "date_actioned": 370,
  },
  {
    "user_id": 1,
    "device": "iPhone 8s",
    "action": "stop",
    "date_actioned": 410,
  },
  {
    "user_id": 2,
    "device": "OSX 15.4",
    "action": "stop",
    "date_actioned": 490,
  },
  {
    "user_id": 3,
    "device": "Android 9.1",
    "action": "start",
    "date_actioned": 700,
  },
]

  
function getUsers(records, action, start, end) {
  let users = []
  records.forEach(record => {
    if (record.action === action && record.date_actioned >= start && record.date_actioned <= end) {
      users.push(record.user_id)
    }
  })
  return users
}
  
function getPlaybackTime(user_id, records) {
  user_records = records.filter(record => record.user_id === user_id )
  user_records.sort((a,b) => (a.date_actioned > b.date_actioned) ? 1 : ((b.date_actioned > a.date_actioned) ? -1 : 0))
  let total = 0
  let previous = null
  let previous_action = null
  user_records.forEach(record => {
    if (record.action === "start" && previous_action !== "start") {
      previous = record.date_actioned
      previous_action = "start"
    } else if (record.action === "stop") {
      total = total + record.date_actioned - previous
      previous_action = "stop"
      previous = record.date_actioned
    }
  })
  return total
};

module.exports =  {db_records, getUsers, getPlaybackTime}

console.log(getUsers(db_records, "start", 700, 900))
console.log(getPlaybackTime(1, db_records))
