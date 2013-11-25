<%
    host = config['splunk']['web']
%>
%if events:
<table border="1" cellpadding="1" cellspacing="0">
<tbody>
<thead>
<tr><th>Day</th><th>Connections</th></tr>
</thead>
<tbody>
%for x in events:
<tr>
    <td> ${x['_time']} </td>
    <td> ${x['count']} </td>
</tr>
%endfor
</tbody>
</table>
<a href="https://${host}:8000/en-US/app/search/flashtimeline?q=search source=*conn* ${arg}&earliest=-30d%40h&latest=now">Full Conn Info</a>
%endif
