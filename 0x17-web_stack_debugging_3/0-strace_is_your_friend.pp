# Ensure a backup is created before modifying the file
file { '/var/www/html/wp-settings.php':
  ensure  => 'file',
  backup  => '.bak',
}

# Apply the fix using Puppet native resources
file { 'replace_phpp_with_php':
  path    => '/var/www/html/wp-settings.php',
  content => inline_template('<%= File.read("/var/www/html/wp-settings.php").gsub("phpp", "php") %>'),
  notify  => Exec['fix'],
}

# Execute the sed command to apply the fix
exec { 'fix':
  command     => 'echo "Fix applied"',  # Update with the actual command you want to run
  path        => '/usr/local/bin/:/bin/',
  refreshonly => true,
}
