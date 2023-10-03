#!/usr/bin/env ruby

puts ARGV[0].scan(/\[(from:|to:|flags:)([^\]]+)\]/).map { |sender_or_receiver, flag| flag }.join(',')
