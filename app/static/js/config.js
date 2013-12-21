(function() {
  require.config({
    paths: {
      'jquery': '../components/jquery',
      'underscore': '../components/lodash',
      'moment': '../components/moment',
      'socket-io': '../components/socket.io'
    },
    shim: {
      'socket-io': {
        exports: 'io'
      },
      'underscore': {
        exports: '_'
      }
    }
  });

}).call(this);
