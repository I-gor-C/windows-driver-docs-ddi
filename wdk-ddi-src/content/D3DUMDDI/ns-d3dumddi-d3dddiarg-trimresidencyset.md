---
UID: NS.d3dumddi.D3DDDIARG_TRIMRESIDENCYSET
title: D3DDDIARG_TRIMRESIDENCYSET
author: windows-driver-content
description: D3DDDIARG_TRIMRESIDENCYSET is used with pfnTrimResidencySet by a user mode driver to trim the residency list for a given device.
old-location: display\d3dddiarg_trimresidencyset.htm
ms.assetid: DEF219B9-115A-4B61-8014-266730CEBD30
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: d3dumddi.h
req.include-header: D3dumddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DDDIARG_TRIMRESIDENCYSET
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
ms.keywords: D3DDDIARG_TRIMRESIDENCYSET, D3DDDIARG_TRIMRESIDENCYSET
req.iface: 
---

# D3DDDIARG_TRIMRESIDENCYSET structure



## -description
<p><b>D3DDDIARG_TRIMRESIDENCYSET</b> is used with <a href="https://msdn.microsoft.com/192F419C-F38F-4B42-8111-86D58D6781DA">pfnTrimResidencySet</a> by a user mode driver to trim the residency list for a given device.</p>


## -syntax

````
typedef struct D3DDDIARG_TRIMRESIDENCYSET {
  D3DDDI_TRIMRESIDENCYSET_FLAGS TrimFlags;
  UINT64                        NumBytesToTrim;
} D3DDDIARG_TRIMRESIDENCYSET;
````


## -struct-fields
<dl>

### -field <b>TrimFlags</b>

<dd>
<p>The trimming behavior flags.</p>
</dd>

### -field <b>NumBytesToTrim</b>

<dd>
<p>When <b>TrimToBudget</b> is set, this value specifies how much the application should evict in order to meet its current memory budget.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 10</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2016</p>
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
<a href="https://msdn.microsoft.com/192F419C-F38F-4B42-8111-86D58D6781DA">pfnTrimResidencySet</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DDDIARG_TRIMRESIDENCYSET structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
