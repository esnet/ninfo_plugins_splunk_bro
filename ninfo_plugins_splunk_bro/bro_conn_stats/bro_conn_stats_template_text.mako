%if events:
%for x in events:
    %if int(x['count']):
        Day: ${x['_time']} Connections: ${x['count']}
    %endif
%endfor
%endif
