# Install flask from pip3

python::pip{ 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
