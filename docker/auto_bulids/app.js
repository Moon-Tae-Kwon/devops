const express = require('express')
const app = express()

app.get('*', (req, res, next) => {
  return res.json('hello world')
})

app.listen(3000, () => console.log('server is running'))
