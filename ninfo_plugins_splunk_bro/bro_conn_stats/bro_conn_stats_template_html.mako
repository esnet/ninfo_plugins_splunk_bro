<%
    host = config['splunk']['web']
%>
%if events:
<table border="1" cellpadding="1" cellspacing="0">
<thead>
<tr><th>time</th><th>Connections</th></tr>
</thead>
<tbody>
%for time, count in times:
<tr>
    <td> ${time} </td>
    <td> ${count} </td>
</tr>
%endfor
</tbody>
</table>
<a href="https://${host}:8000/en-US/app/search/flashtimeline?q=search source=*conn* ${arg}&earliest=-30d%40h&latest=now">Full Conn Info</a>
%endif
