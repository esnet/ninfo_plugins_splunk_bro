%if days:
%for day, count in days:
    %if count:
Day: ${day} Connections: ${count}
    %endif
%endfor
%endif
