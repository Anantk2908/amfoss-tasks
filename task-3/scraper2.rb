require 'nokogiri'
require 'httparty'
require 'byebug'

def scraper
	puts "Pls Enter a word to search"
	a= gets.chomp
	url = "https://www.google.com/search?q="+a+"&oq="+a+"&aqs=chrome.0.69i59l2j69i60.1301j0j1&sourceid=chrome&ie=UTF-8"
	unparsed_page = HTTParty.get(url)
	parsed_page = Nokogiri::HTML(unparsed_page)
	jobs = Array.new
	search_lists = parsed_page.css('div.kCrYT')
	search_lists.each do |search_list|
		search ={
				title: search_list.css('div.vvjwJb').text
		}
		jobs << search	
		puts "#{search[:title]}"
	end

end
scraper

