#!/usr/bin/node
const request = require('request');

const url = process.argv[2];
request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const todos = JSON.parse(body);
    const completedTasksCount = {};
    todos.forEach(todo => {
      if (todo.completed) {
        const userId = todo.userId;
        completedTasksCount[userId] = (completedTasksCount[userId] || 0) + 1;
      }
    });
    console.log(completedTasksCount);
  }
});
