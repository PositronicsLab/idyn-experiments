function [] = compare_js_err(test_name,exp_path,start_iter,end_iter,num_tests)
    % start_iter =1000;
    % end_iter = 60000;
    c = ['k';'b';'r';'m';'g';'y';'c'];
    %% COM 
    %{
    figure;
    for i = 1:num_tests
        hold on;
        data_path = [exp_path,'/',test_name,'/',num2str(i-1),'/']
        x = dlmread([data_path,'com.mat'],' ');
%         % plot3(x(:,1),x(:,2),x(:,3),c(i,:))
        plot(x(start_iter:end_iter,1),x(start_iter:end_iter,2),c(i,:))
        axis tight;
    end
    legend('this work','pid','idyn (sensed cfs)')
%     view([0,90])
    ylabel('y [m]')
    xlabel('x [m]')   
    %}
    %% Q err & Qd err     %{
    figure;
    for i = 1:num_tests
        data_path = [exp_path,'/',test_name,'/',num2str(i-1),'/']
        subplot(3,1,1)
                hold on;
        q = dlmread([data_path,'q.mat'],' ');
        q_des = dlmread([data_path,'q_des.mat'],' ');
        q_err = q_des(start_iter:end_iter-1,:) - q(start_iter+1:end_iter,:) ;
        plot(sum((q_err(:,:).^2)')',c(i));
        q_err_norm = mean(sum(q_err(:,:).^2')')
        title('position Error')
        xlabel('iteration (0.001 sec)')
        ylabel('q error: SSE(q_des - q)')
        axis tight;

        subplot(3,1,2)
                hold on;
        qd = dlmread([data_path,'qd.mat'],' ');
        qd_des = dlmread([data_path,'qd_des.mat'],' ');
        qd_err = qd_des(start_iter:end_iter-1,:) - qd(start_iter+1:end_iter,:) ;
        plot(sum((qd_err(:,:).^2)')',c(i));
        qd_err_norm = mean(sum(qd_err(:,:).^2')')
        title('velocity Error')
        xlabel('iteration (0.001 sec)')
        ylabel('qd error: SSE(qd_des - qd)')
                axis tight;

        subplot(3,1,3)
                hold on;
        u = dlmread([data_path,'u.mat'],' ');
        ufb = dlmread([data_path,'ufb.mat'],' ');
        uff = dlmread([data_path,'uff.mat'],' ');
        qdd_des = dlmread([data_path,'qdd_des.mat'],' ');
        plot(u(:,8),c(i))
%         plot(uff(:,8),'r')
%         plot(ufb(:,8),'b')
%         plot(qdd_des(:,8)./1000,'c')
        u_norm = mean(sum(u(:,:).^2')')
        axis tight;
    end
    %}
    %% RPY 
    %{
    figure;
    for i = 1:num_tests
        data_path = [exp_path,'/',test_name,'/',num2str(i-1),'/']
        rpy = dlmread([data_path,'rpy.mat'],' ');
        subplot(2,1,1)
        hold on;
        plot(rpy(:,1),c(i));
        title('roll')
        xlabel('iteration (0.001 sec)')
        ylabel('rad')
        axis tight;

        subplot(2,1,2)
        hold on;
        plot(rpy(:,2),c(i));
        title('pitch')
        xlabel('iteration (0.001 sec)')
        ylabel('rad')
        axis tight;
    end
    %}
    
    %% COM XD 
    %{
     figure;
    for i = 1:num_tests
        data_path = [exp_path,'/',test_name,'/',num2str(i-1),'/']
        xd = dlmread([data_path,'comxd.mat'],' ');
        subplot(2,1,1)
        hold on;
        plot(xd(:,1),c(i));
        title('roll')
        xlabel('iteration (0.001 sec)')
        ylabel('v')
        axis tight;

        subplot(2,1,2)
        hold on;
        plot(xd(:,2),c(i));
        title('pitch')
        xlabel('iteration (0.001 sec)')
        ylabel('v')
        axis tight;
    end
    %}
    
    %{
    figure;
    for i = 1:size(ds,1)
        ds(i,:)
        subplot(size(ds,1),2,i*2-1)
        x_err = dlmread(['../',ds(i,:),'/x_err.mat'],' ');
        plot(sum((x_err(start_iter:end_iter,:).^2),2)','k');
        title([ds(i,:), ' velocity Error, AVG:',num2str(mean(sum(x_err(start_iter:end_iter,:).^2,2)'))])
        xlabel('iteration (0.001 sec)')
        ylabel('SS x error: SS(x_err)')

        subplot(size(ds,1),2,i*2)
        xd_err = dlmread(['../',ds(i,:),'/xd_err.mat'],' ');
        plot(sum((xd_err(start_iter:end_iter,:).^2),2)','k');
        title([ds(i,:), ' position Error, AVG:',num2str(mean(sum(xd_err(start_iter:end_iter,:).^2,2)'))])
        xlabel('iteration (0.001 sec)')
        ylabel('SS xd error: SS(xd_err)')
    end
        figure;
    for i = 1:size(ds,1)
        ds(i,:)
        subplot(size(ds,1),2,i*2)
        ufb = dlmread(['../',ds(i,:),'/ufb.mat'],' ');
        plot(sum((ufb(start_iter:end_iter,:).^2),2)','k');
        title([ds(i,:), ' Feedback Forces, AVG:',num2str(mean(sum(ufb(start_iter:end_iter,:).^2,2)'))])
        xlabel('iteration (0.001 sec)')
        ylabel('SS ufb')
        
        subplot(size(ds,1),2,i*2-1)
        u = dlmread(['../',ds(i,:),'/uff.mat'],' ') + ufb;
        plot(sum((u(start_iter:end_iter,:).^2),2)','k');
        title([ds(i,:), ' Feedforward Forces, AVG:',num2str(mean(sum(u(start_iter:end_iter,:).^2,2)'))])
        xlabel('iteration (0.001 sec)')
        ylabel('SS u')
    end
        %}

end
