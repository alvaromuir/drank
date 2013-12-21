# Main config file
# Paths reflect the 'dev|dist directory that grunt exports'
require.config
  paths:
    'jquery'    : '../components/jquery'
    'underscore': '../components/lodash'
    'moment'    : '../components/moment'
    'socket-io' : '../components/socket.io'

  shim:
    'socket-io':
      exports: 'io'
      
    'underscore':
      exports: '_'