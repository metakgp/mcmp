require 'json'

mcmp_list1 = (File.exists? "finallist.json") ? JSON.parse(File.read("finallist.json")) : [ ]
puts "#{mcmp_list1.length} objects initially exists in finallist.json file."
mcmp_list2 = mcmp_list1.uniq
puts "#{mcmp_list2.length} objects finally exists in finallist.json file."
puts "No. of duplicate entries deleted : #{mcmp_list1.length - mcmp_list2.length}."
File.delete("finallist.json") if File.exists? "finallist.json"
File.open("finallist.json", "a") { |file| file.write(JSON.pretty_generate(mcmp_list2)) }