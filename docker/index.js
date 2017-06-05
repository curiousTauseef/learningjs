'use strict'

let http = require('http')
let port = process.env.PORT || 3000

let server = http.createServer((req, res) => {

  let body = 'Hello, world!'

  res.writeHead(200, {
    'Content-Type': 'text/plain',
    'Content-Length': Buffer.byteLength(body)
  })

  res.end(body)
})

server.listen(port, () => console.log(`Server starter on port ${port}`))
