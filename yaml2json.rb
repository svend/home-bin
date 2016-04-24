#!/usr/bin/env ruby

require 'json'
require 'yaml'

data = YAML.load(STDIN)
json = data.to_json

puts json
