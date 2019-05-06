#!/usr/bin/env ruby
require 'csv'
require 'sass'
require 'sass/exec'
require 'mustache'
require 'markdown'

# compile scss
# opts = Sass::Exec::SassScss.new(["-C","sass/jekyll-theme-minimal.scss","css/minimal.css"], :sass)
# opts.parse!

# irc channel page map
$irc_channel_page_map = {
  "#alpine-linux" => "alpine",
  "#linuxmint-help" => "mint",
  "##proxmox" => "proxmox",
  "#NetBSD" => "netbsd",
  "#kali-linux" => "kali"
}

def get_irc_channel_page(name)
  if $irc_channel_page_map[name]
    $irc_channel_page_map[name]
  else
    name.tr('#','')
  end
end

# load IRC stats
irc = {}
csv_text = File.read('scripts/irc_stats.csv')
csv = CSV.parse(csv_text, :headers => true)
i = 1
csv.each do |row|
    irc_stat = {}
    irc_stat[:rating] = i
    irc_stat[:channel] = row[0].strip
    irc_stat[:network] = row[1].strip
    irc_stat[:users] = row[2].to_i
    irc[irc_stat[:channel]] = irc_stat
    i += 1
end

distros = {}

irc.each_value do |irc_stat|
  distro = get_irc_channel_page(irc_stat[:channel])
  distro_template = 'distros/'+distro+'.md'
  name = ''
  if File.exist?(distro_template)
    distro_template = File.read(distro_template)
    name = distro_template.lines()[0].strip()
  else
    puts 'distro page '+distro+' not found, using default.md'
    distro_template = File.read('distros/default.md')
    name = distro
  end
  rating = irc_stat[:rating]
  distros[rating] = {
    'page': distro,
    'name': name,
    'template': distro_template,
    'rating': rating,
    'irc_stat': irc_stat
  }
end

ratings = distros.keys.sort.map do |r|
  distros[r]
end

page_template = File.read('page.mustache')
date = DateTime.now.strftime("%Y-%m-%d")

# Render index.html
index_body = Markdown.new(
  Mustache.render(File.read('README.md'))
).to_html
f = File.new('index.html','w')
f.write(
  Mustache.render(page_template, ratings: ratings, body: index_body, title: '', date: date)
)
f.close()

Dir['pages/*.html'].each do |f|
  File.delete(f)
end

distros.values.each do |d|
  distro = d[:page]
  name = d[:name]
  distro_template = d[:template]
  irc_stat = d[:irc_stat]
  body = Markdown.new(
    Mustache.render(distro_template,
                       irc_channel: irc_stat[:channel],
                       irc_network: irc_stat[:network],
                       irc_users: irc_stat[:users],
                       rating: d[:rating])
  ).to_html
  f = File.new('pages/'+distro+'.html','w')
  f.write(
    Mustache.render(page_template, ratings: ratings, body: body, title: name, date: date)
  )
  f.close()
end
