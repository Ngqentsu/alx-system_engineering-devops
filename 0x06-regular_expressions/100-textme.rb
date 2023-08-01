#!/usr/bin/env ruby

puts ARGV[0].scan(/\[(from:|to:|flags:)([^\]]+)\]/).map { |label, value| value }.join(',')
