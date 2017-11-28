---
UID: NS.d3dumddi._D3DDDICB_FREEGPUVIRTUALADDRESS
title: D3DDDICB_FREEGPUVIRTUALADDRESS
author: windows-driver-content
description: D3DDDICB_FREEGPUVIRTUALADDRESS is used with pfnFreeGpuVirtualAddressCb to release a range of graphics processing unit (GPU) virtual addresses that were previously reserved or mapped.
old-location: display\d3dddicb_freegpuvirtualaddress.htm
old-project: display
ms.assetid: 5E11C1BB-7E9E-4D9C-A15A-B9CCB29622C3
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DDDICB_FREEGPUVIRTUALADDRESS, D3DDDICB_FREEGPUVIRTUALADDRESS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dumddi.h
req.include-header: D3dumddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DDDICB_FREEGPUVIRTUALADDRESS
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

# D3DDDICB_FREEGPUVIRTUALADDRESS structure



## -description
<p><b>D3DDDICB_FREEGPUVIRTUALADDRESS</b> is used with <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-freegpuvirtualaddresscb.md">pfnFreeGpuVirtualAddressCb</a> to release a range of graphics processing unit (GPU) virtual addresses that were previously reserved or mapped.</p>


## -syntax

````
typedef struct _D3DDDICB_FREEGPUVIRTUALADDRESS {
  D3DGPU_VIRTUAL_ADDRESS BaseAddress;
  D3DGPU_SIZE_T          Size;
} D3DDDICB_FREEGPUVIRTUALADDRESS;
````


## -struct-fields
<dl>

### -field <b>BaseAddress</b>

<dd>
<p>Specifies the base virtual address, in bytes, of the range to free. Must be aligned to 4 KB.</p>
</dd>

### -field <b>Size</b>

<dd>
<p>Specifies the size, in bytes, of the range to free. Must be aligned to 4 KB.</p>
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
<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-freegpuvirtualaddresscb.md">pfnFreeGpuVirtualAddressCb</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DDDICB_FREEGPUVIRTUALADDRESS structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
