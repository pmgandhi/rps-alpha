desc "Run custom module rake tasks"
task :custom do
  custom_rakefiles = FileList['modules/*/Rakefile']

  custom_rakefiles.each do |fn|
    name = File.dirname(fn)
    Dir.chdir(name) do
      $stderr.puts "---> Running custom tests for #{name}"
      namespace name do
        instance_eval File.read('Rakefile')
        Rake::Task["#{name}:default"].invoke
      end
    end
  end
end
