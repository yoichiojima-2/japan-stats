# frozen_string_literal: true

require 'uri'
require 'net/http'
require 'json'
require 'dotenv'

Dotenv.load

stats_id_list = {
  population: '0000010101',
  environment: '0000010102',
  economics: '0000010103',
  administration: '0000010104',
  education: '0000010105',
  labour: '0000010106',
  calture: '0000010107',
  housing: '0000010108',
  medical_care: '0000010109',
  social_security: '0000010110',
  household_finance: '0000010111',
  daily_routine: '0000010112'
}

def get_data(id)
  base_url = "https://api.e-stat.go.jp/rest/#{ENV['API_VERSION']}/app/json/getStatsData"
  params = {
    appId: ENV['APP_ID'],
    statsDataId: id,
  }
  uri = URI(base_url)
  uri.query = URI.encode_www_form(params)
  res = Net::HTTP.get_response(uri)
  JSON.parse(res.body)['GET_STATS_DATA']['STATISTICAL_DATA']
end

def extract_classes(data)
  data['CLASS_INF']['CLASS_OBJ']
end

def extract_values(data)
  data['DATA_INF']['VALUE']
end

data = get_data(stats_id_list[:population])
classes = extract_classes(data)