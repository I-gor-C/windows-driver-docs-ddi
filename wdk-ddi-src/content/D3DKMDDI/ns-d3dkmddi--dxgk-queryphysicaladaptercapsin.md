---
UID: NS.d3dkmddi._DXGK_QUERYPHYSICALADAPTERCAPSIN
title: DXGK_QUERYPHYSICALADAPTERCAPSIN
author: windows-driver-content
description: The DXGK_QUERYPHYSICALADAPTERCAPSIN structure is used to query the display driver for the capabilities of the physical display adapter.
old-location: display\dxgk_queryphysicaladaptercapsin.htm
ms.assetid: 4B01E62F-5E5B-4316-B237-EADAA3C72242
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: d3dkmddi.h
req.include-header: D3dkmddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGK_QUERYPHYSICALADAPTERCAPSIN
req.alt-loc: d3dkmddi.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
ms.keywords: DXGK_QUERYPHYSICALADAPTERCAPSIN, DXGK_QUERYPHYSICALADAPTERCAPSIN
req.iface: 
---

# DXGK_QUERYPHYSICALADAPTERCAPSIN structure



## -description
<p>The <b>DXGK_QUERYPHYSICALADAPTERCAPSIN</b> structure is used to query the display driver for the capabilities of the physical display adapter.</p>


## -syntax

````
typedef struct _DXGK_QUERYPHYSICALADAPTERCAPSIN {
  UINT PhysicalAdapterIndex;
} DXGK_QUERYPHYSICALADAPTERCAPSIN;
````


## -struct-fields
<dl>

### -field <b>PhysicalAdapterIndex</b>

<dd>
<p>Index of a physical adapter in a link.</p>
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
<dt>D3dkmddi.h (include D3dkmddi.h)</dt>
</dl>
</td>
</tr>
</table>