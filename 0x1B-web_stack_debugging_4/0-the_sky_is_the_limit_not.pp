# Increases the amount of traffic the Nginx server can handle.

# Use Augeas to modify ULIMIT in the Nginx configuration file
augeas { 'fix-for-nginx':
  lens    => 'Shellvars.lns',
  incl    => '/etc/default/nginx',
  changes => [
    'set ULIMIT 4096',
  ],
  notify  => Exec['nginx-restart'],
}

# Restart Nginx
exec { 'nginx-restart':
  command     => '/etc/init.d/nginx restart',
  path        => '/etc/init.d/',
  refreshonly => true,
}
