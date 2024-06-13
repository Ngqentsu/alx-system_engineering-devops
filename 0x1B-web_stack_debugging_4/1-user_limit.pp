# Puppet to fix limits on open files

exec { 'set soft nofile limit':
  command => '/bin/grep -q "holberton soft nofile 1500" /etc/security/limits.conf || echo "holberton soft nofile 1500" >> /etc/security/limits.conf',
}

exec { 'set hard nofile limit':
  command => '/bin/grep -q "holberton hard nofile 1500" /etc/security/limits.conf || echo "holberton hard nofile 1500" >> /etc/security/limits.conf',
}

exec { 'set file limits':
  command => '/bin/true',
  require => [ Exec['set soft nofile limit'], Exec['set hard nofile limit'] ],
}
