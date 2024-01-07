require 'uri'
require 'net/http'
require 'dotenv'

Dotenv.load

base_url = "https://api.e-stat.go.jp/rest/#{ENV['API_VERSION']}/app/json/getStatsData"
params = {
  appId: ENV['APP_ID'],
  statsDataId: '0000010101',
}

uri = URI(base_url)
uri.query = URI.encode_www_form(params)
puts uri
res = Net::HTTP.get_response(uri)

puts res.body