%if events:
%for x in events:
Time: ${x['_time']}
Notice: ${x['note']}
SRC IP: ${x['src']}
DST IP: ${x['dst']}
MSG: ${x['msg']}  
SUB: ${x['sub']}  

%endfor
%endif
