---
UID: NS.d3dumddi._D3DDDIARG_QUERYRESOURCERESIDENCY
title: D3DDDIARG_QUERYRESOURCERESIDENCY
author: windows-driver-content
description: The D3DDDIARG_QUERYRESOURCERESIDENCY structure describes a list of resources on which residency is verified through the QueryResourceResidency function.
old-location: display\d3dddiarg_queryresourceresidency.htm
ms.assetid: 14c0cb12-3ed0-4c78-befa-6da9e8cd7dbc
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
req.alt-api: D3DDDIARG_QUERYRESOURCERESIDENCY
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
ms.keywords: D3DDDIARG_QUERYRESOURCERESIDENCY, D3DDDIARG_QUERYRESOURCERESIDENCY
req.iface: 
---

# D3DDDIARG_QUERYRESOURCERESIDENCY structure



## -description
<p>The D3DDDIARG_QUERYRESOURCERESIDENCY structure describes a list of resources on which residency is verified through the <a href="https://msdn.microsoft.com/5b9a2a59-b2d1-468e-998b-902bc2a75cb3">QueryResourceResidency</a> function. </p>


## -syntax

````
typedef struct _D3DDDIARG_QUERYRESOURCERESIDENCY {
  const HANDLE *pHandleList;
  UINT         NumResources;
} D3DDDIARG_QUERYRESOURCERESIDENCY;
````


## -struct-fields
<dl>

### -field <b>pHandleList</b>

<dd>
<p>[in] An array of handles to resources whose residency is queried. <b>pHandleList</b> cannot be <b>NULL</b>. A resource can be an object, which is derived from the <b>IDirect3DResource9</b> interface for a texture, volume texture, cube texture, vertex buffer, index buffer, or surface. For more information about <b>IDirect3DResource9</b>, see the DirectX SDK documentation.</p>
</dd>

### -field <b>NumResources</b>

<dd>
<p>[in] The number of resources in the array in the <b>pHandleList</b> member. The range is from 1 through 0xFFFFF.</p>
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
<a href="https://msdn.microsoft.com/5b9a2a59-b2d1-468e-998b-902bc2a75cb3">QueryResourceResidency</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DDDIARG_QUERYRESOURCERESIDENCY structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
