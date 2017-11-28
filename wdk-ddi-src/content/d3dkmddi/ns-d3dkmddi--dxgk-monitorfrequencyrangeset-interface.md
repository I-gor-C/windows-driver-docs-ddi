---
UID: NS.d3dkmddi._DXGK_MONITORFREQUENCYRANGESET_INTERFACE
title: DXGK_MONITORFREQUENCYRANGESET_INTERFACE
author: windows-driver-content
description: The DXGK_MONITORFREQUENCYRANGESET_INTERFACE structure contains pointers to functions that belong to the Monitor Frequency Range Set interface, which is implemented by the video present network (VidPN) manager.
old-location: display\dxgk_monitorfrequencyrangeset_interface.htm
old-project: display
ms.assetid: 4a973ecd-341f-4766-9fed-f56e55f8deae
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGK_MONITORFREQUENCYRANGESET_INTERFACE, DXGK_MONITORFREQUENCYRANGESET_INTERFACE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmddi.h
req.include-header: D3dkmddi.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGK_MONITORFREQUENCYRANGESET_INTERFACE
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
req.iface: 
---

# DXGK_MONITORFREQUENCYRANGESET_INTERFACE structure



## -description
<p>The DXGK_MONITORFREQUENCYRANGESET_INTERFACE structure contains pointers to functions that belong to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff568430">Monitor Frequency Range Set interface</a>, which is implemented by the video present network (VidPN) manager.</p>


## -syntax

````
typedef struct _DXGK_MONITORFREQUENCYRANGESET_INTERFACE {
  DXGKDDI_MONITORFREQUENCYRANGESET_GETNUMFREQUENCYRANGES          pfnGetNumFrequencyRanges;
  DXGKDDI_MONITORFREQUENCYRANGESET_ACQUIREFIRSTFREQUENCYRANGEINFO pfnAcquireFirstFrequencyRangeInfo;
  DXGKDDI_MONITORFREQUENCYRANGESET_ACQUIRENEXTFREQUENCYRANGEINFO  pfnAcquireNextFrequencyRangeInfo;
  DXGKDDI_MONITORFREQUENCYRANGESET_RELEASEFREQUENCYRANGEINFO      pfnReleaseFrequencyRangeInfo;
} DXGK_MONITORFREQUENCYRANGESET_INTERFACE;
````


## -struct-fields
<dl>

### -field <b>pfnGetNumFrequencyRanges</b>

<dd>
<p>A pointer to the <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi-monitorfrequencyrangeset-getnumfrequencyranges.md">pfnGetNumFrequencyRanges</a> function.</p>
</dd>

### -field <b>pfnAcquireFirstFrequencyRangeInfo</b>

<dd>
<p>A pointer to the <a href="display.dxgk_monitorfrequencyrangeset_interface_pfnacquirefirstfrequencyrangei">pfnAcquireFirstFrequencyRangeInfo</a> function.</p>
</dd>

### -field <b>pfnAcquireNextFrequencyRangeInfo</b>

<dd>
<p>A pointer to the <a href="display.dxgk_monitorfrequencyrangeset_interface_pfnacquirenextfrequencyrangein">pfnAcquireNextFrequencyRangeInfo</a> function.</p>
</dd>

### -field <b>pfnReleaseFrequencyRangeInfo</b>

<dd>
<p>A pointer to the <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi-monitorfrequencyrangeset-releasefrequencyrangeinfo.md">pfnReleaseFrequencyRangeInfo</a> function.</p>
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
<dt>D3dkmddi.h (include D3dkmddi.h)</dt>
</dl>
</td>
</tr>
</table>