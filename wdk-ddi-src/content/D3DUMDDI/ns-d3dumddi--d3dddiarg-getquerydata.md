---
UID: NS.d3dumddi._D3DDDIARG_GETQUERYDATA
title: D3DDDIARG_GETQUERYDATA
author: windows-driver-content
description: The D3DDDIARG_GETQUERYDATA structure contains query information that was retrieved from the user-mode display driver.
old-location: display\d3dddiarg_getquerydata.htm
ms.assetid: 98c6ada1-89a4-4cbd-bb6c-98c190fa15d8
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: d3dumddi.h
req.include-header: D3dumddi.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DDDIARG_GETQUERYDATA
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
ms.keywords: D3DDDIARG_GETQUERYDATA, D3DDDIARG_GETQUERYDATA
req.iface: 
---

# D3DDDIARG_GETQUERYDATA structure



## -description
<p>The D3DDDIARG_GETQUERYDATA structure contains query information that was retrieved from the user-mode display driver.</p>


## -syntax

````
typedef struct _D3DDDIARG_GETQUERYDATA {
  HANDLE hQuery;
  VOID   *pData;
} D3DDDIARG_GETQUERYDATA;
````


## -struct-fields
<dl>

### -field <b>hQuery</b>

<dd>
<p>[in] The handle to the query that was created by the <a href="https://msdn.microsoft.com/ac63b77b-2704-4d5b-bf1d-9d85e8a1e336">CreateQuery</a> function.</p>
</dd>

### -field <b>pData</b>

<dd>
<p>[out] A pointer to a buffer that the driver fills with data that is related to a query, if the query type is one that requires data. </p>
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
<a href="https://msdn.microsoft.com/ac63b77b-2704-4d5b-bf1d-9d85e8a1e336">CreateQuery</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/64daec14-8e16-4df3-bb0c-27760223b86c">GetQueryData</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DDDIARG_GETQUERYDATA structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
