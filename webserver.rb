#!/usr/bin/env ruby
require 'webrick'
include WEBrick

s = HTTPServer.new(:Port => 8090,  :DocumentRoot => Dir::pwd)
trap("INT"){ s.shutdown }
s.start
