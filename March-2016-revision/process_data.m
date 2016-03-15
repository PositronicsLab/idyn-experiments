mu = {'1';
      '100'}
  numel(mu)
ctrl = {'cfqp';
    'nocp';
    'nsqp';
    'pd';
    'sensed'}
numel(ctrl)
for i = 1:numel(mu)
    figure; hold on;
    y = [];
    for j = 1:numel(ctrl)
        try
        q = dlmread([mu{i},'/',ctrl{j},'/','q.mat'],' ');
        catch
           continue;
        end
        qdes = dlmread([mu{i},'/',ctrl{j},'/','qdes.mat'],' ');
        qerr = (q-qdes); 
        qerr_norm = arrayfun(@(idx) mean(abs(qerr(idx,1:end-4))), 1:size(qerr,1)); 
        plot(qerr_norm);
        y = [y, qerr_norm'];
    end
    dlmwrite([mu{i},'/','qerr.mat'],y,' ');
    axis tight;
end
