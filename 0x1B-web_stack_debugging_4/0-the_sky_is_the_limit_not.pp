# puppet to fix nginx processes for workers

file { '/etc/nginx/nginx.conf':
  ensure  => present,
  content => template('nginx/nginx.conf.erb'),
  notify  => Exec['restart nginx'],
}

exec { 'restart nginx':
  command     => '/usr/sbin/service nginx restart',
  refreshonly => true,
}
