# Enable holberton user to login and open a file without any error message

# Increase hard file limit for Holberton user.
exec { 'hard-limit-holberton':
  command => "sed -i '/^holberton hard/s/5/50000/' /etc/security/limits.conf",
  path    => '/usr/local/bin/:/bin/',
  notify  => Exec['restart-service'],
}

# Increase soft file limit for Holberton user.
exec { 'soft-limit-holberton':
  command => 'sed -i "/^holberton soft/s/4/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/',
  notify  => Exec['restart-service'],
}

# Define a service restart
exec { 'restart-service':
  command     => '/bin/systemctl restart <your-service-name>',
  refreshonly => true,
}
