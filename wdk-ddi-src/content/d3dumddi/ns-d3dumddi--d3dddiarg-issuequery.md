---
UID: NS.d3dumddi._D3DDDIARG_ISSUEQUERY
title: D3DDDIARG_ISSUEQUERY
author: windows-driver-content
description: The D3DDDIARG_ISSUEQUERY structure describes how to process a query that was created by the CreateQuery function.
old-location: display\d3dddiarg_issuequery.htm
old-project: display
ms.assetid: af52d1a3-b537-48d2-ab57-3f798ec83c98
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DDDIARG_ISSUEQUERY, D3DDDIARG_ISSUEQUERY
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dumddi.h
req.include-header: D3dumddi.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DDDIARG_ISSUEQUERY
req.alt-loc: d3dumddi.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
req.iface: 
---

# D3DDDIARG_ISSUEQUERY structure



## -description
<p>The D3DDDIARG_ISSUEQUERY structure describes how to process a query that was created by the <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-createquery.md">CreateQuery</a> function. </p>


## -syntax

````
typedef struct _D3DDDIARG_ISSUEQUERY {
  HANDLE                 hQuery;
  D3DDDI_ISSUEQUERYFLAGS Flags;
} D3DDDIARG_ISSUEQUERY;
````


## -struct-fields
<dl>

### -field <b>hQuery</b>

<dd>
<p>[in] The handle to the query that was created by the <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-createquery.md">CreateQuery</a> function.</p>
</dd>

### -field <b>Flags</b>

<dd>
<p>[in] A <a href="https://msdn.microsoft.com/library/windows/hardware/ff544575">D3DDDI_ISSUEQUERYFLAGS</a> structure that identifies the type of query to issue. The driver can ignore query requests with <b>Flags</b> set to 0. </p>
<p>For many query types, start query is never specified (that is, the <b>Begin</b> bit-field flag is never set for many query types). For more information about whether the <b>Begin</b> bit-field flag is set for a query type, see the <b>QueryType</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff542958">D3DDDIARG_CREATEQUERY</a> structure.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows Vista and later versions of the Windows operating systems.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3dumddi.h (include D3dumddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-createquery.md">CreateQuery</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544575">D3DDDI_ISSUEQUERYFLAGS</a>
</dt>
<dt>
<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-issuequery.md">IssueQuery</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DDDIARG_ISSUEQUERY structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
