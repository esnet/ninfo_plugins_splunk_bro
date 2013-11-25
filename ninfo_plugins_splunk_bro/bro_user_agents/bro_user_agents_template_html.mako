<%
    host = config['splunk']['web']
%>
%if events:
<ul>
%for x in events:
    <li> ${x['unparsed_version']} </li>
%endfor
</ul>
<a href="https://${host}:8000/en-US/app/search/flashtimeline?q=search index=security source=*user-agent* ${arg}&earliest=-10h%40h&latest=now">Full User-Agent Info</a>
%endif
