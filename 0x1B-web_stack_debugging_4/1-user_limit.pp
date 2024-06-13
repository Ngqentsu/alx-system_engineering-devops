# Puppet to fix limits on open files

exec { 'set soft nofile limit':
  command => '/bin/sed -i "holberton soft nofile 4/holberton hard nofile 1500/" /etc/security/limits.conf'
}

exec { 'set hard nofile limit':
  command => '/bin/sed -i "holberton hard nofile 5/holberton hard nofile 1500/" /etc/security/limits.conf'
}

exec { 'set file limits':
  command => '/usr/sbin/sysctl -p'
}
