# Debugging Apache and returning 500 error

exec { 'fix error':
  provider => 'shell',
  command  => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php'
}
