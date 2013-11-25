<%
    host = config['splunk']['web']
%>
%if events:
<table border="1" cellpadding="1" cellspacing="0">
<tbody>
<thead>
<tr><th>time</th><th>Notice</th><th>src</th><th>dst</th><th>msg</th><th>sub</th></tr>
</thead>
<tbody>
%for x in events:
<tr>
    <td> ${x['_time']} </td>
    <td> ${x['note']} </td>
    <td> ${x['src']} </td>
    <td> ${x['dst']} </td>
    <td> ${x['msg']} </td>
    <td> ${x['sub']} </td>
</tr>
%endfor
</tbody>
</table>
<a href="https://${host}:8000/en-US/app/search/flashtimeline?q=search index=security source=*bro* ${arg}&earliest=-30d%40h&latest=now">Full Bro Info</a>
%endif
