%if times:
%for time, count in times:
    %if count:
time: ${time} Connections: ${count}
    %endif
%endfor
%endif
