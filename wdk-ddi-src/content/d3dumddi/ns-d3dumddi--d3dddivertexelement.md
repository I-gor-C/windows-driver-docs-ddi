---
UID: NS.d3dumddi._D3DDDIVERTEXELEMENT
title: D3DDDIVERTEXELEMENT
author: windows-driver-content
description: The D3DDDIVERTEXELEMENT structure describes an element in the array for a vertex shader declaration.
old-location: display\d3dddivertexelement.htm
old-project: display
ms.assetid: acb0fc1d-e360-4cb9-9b3b-7d8d03146cfd
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DDDIVERTEXELEMENT, D3DDDIVERTEXELEMENT
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
req.alt-api: D3DDDIVERTEXELEMENT
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

# D3DDDIVERTEXELEMENT structure



## -description
<p>The D3DDDIVERTEXELEMENT structure describes an element in the array for a vertex shader declaration.</p>


## -syntax

````
typedef struct _D3DDDIVERTEXELEMENT {
  USHORT Stream;
  USHORT Offset;
  UCHAR  Type;
  UCHAR  Method;
  UCHAR  Usage;
  UCHAR  UsageIndex;
} D3DDDIVERTEXELEMENT;
````


## -struct-fields
<dl>

### -field <b>Stream</b>

<dd>
<p>[in] The number of the stream.</p>
</dd>

### -field <b>Offset</b>

<dd>
<p>[in] The offset (if any), in bytes, from the beginning of the stream to the start of the data.</p>
</dd>

### -field <b>Type</b>

<dd>
<p>[in] One of several predefined data types that define the data size. For more information about these types, see the D3DDECLTYPE enumeration type in the Microsoft Windows SDK documentation.</p>
</dd>

### -field <b>Method</b>

<dd>
<p>[in] The tessellator processing method. This method determines how the tessellator interprets and operates on the vertex data. For more information about these methods, see the D3DDECLMETHOD enumeration type in the Windows SDK documentation.</p>
</dd>

### -field <b>Usage</b>

<dd>
<p>[in] The intended use of the vertex data. For more information about the possible uses, see the D3DDECLUSAGE enumeration type in the Windows SDK documentation.</p>
</dd>

### -field <b>UsageIndex</b>

<dd>
<p>[in] A modification to the usage data that is specified in the <b>Usage</b> member. This modification enables multiple usage types to be specified.</p>
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
<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-createvertexshaderdecl.md">CreateVertexShaderDecl</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DDDIVERTEXELEMENT structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
