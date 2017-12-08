---
UID: NS.D3DKMDDI._DXGK_MONITORFREQUENCYRANGESET_INTERFACE
title: _DXGK_MONITORFREQUENCYRANGESET_INTERFACE
author: windows-driver-content
description: The DXGK_MONITORFREQUENCYRANGESET_INTERFACE structure contains pointers to functions that belong to the Monitor Frequency Range Set interface, which is implemented by the video present network (VidPN) manager.
old-location: display\dxgk_monitorfrequencyrangeset_interface.htm
old-project: display
ms.assetid: 4a973ecd-341f-4766-9fed-f56e55f8deae
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: _DXGK_MONITORFREQUENCYRANGESET_INTERFACE, DXGK_MONITORFREQUENCYRANGESET_INTERFACE
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
---

# _DXGK_MONITORFREQUENCYRANGESET_INTERFACE structure



## -description
The DXGK_MONITORFREQUENCYRANGESET_INTERFACE structure contains pointers to functions that belong to the <a href="display.monitor_frequency_range_set_interface">Monitor Frequency Range Set interface</a>, which is implemented by the video present network (VidPN) manager.


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

### -field pfnGetNumFrequencyRanges

A pointer to the <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi_monitorfrequencyrangeset_getnumfrequencyranges.md">pfnGetNumFrequencyRanges</a> function.

### -field pfnAcquireFirstFrequencyRangeInfo

A pointer to the <a href="display.dxgk_monitorfrequencyrangeset_interface_pfnacquirefirstfrequencyrangei">pfnAcquireFirstFrequencyRangeInfo</a> function.

### -field pfnAcquireNextFrequencyRangeInfo

A pointer to the <a href="display.dxgk_monitorfrequencyrangeset_interface_pfnacquirenextfrequencyrangein">pfnAcquireNextFrequencyRangeInfo</a> function.

### -field pfnReleaseFrequencyRangeInfo

A pointer to the <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi_monitorfrequencyrangeset_releasefrequencyrangeinfo.md">pfnReleaseFrequencyRangeInfo</a> function.

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Version
</th>
<td width="70%">
Available in Windows Vista and later versions of the Windows operating systems.
</td>
</tr>
<tr>
<th width="30%">
Header
</th>
<td width="70%">
<dl>
<dt>D3dkmddi.h (include D3dkmddi.h)</dt>
</dl>
</td>
</tr>
</table>