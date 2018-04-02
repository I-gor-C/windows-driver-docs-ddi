---
UID: NS:d3dkmdt._D3DKMDT_FREQUENCY_RANGE
title: "_D3DKMDT_FREQUENCY_RANGE"
author: windows-driver-content
description: The D3DKMDT_FREQUENCY_RANGE structure contains the minimum and maximum refresh rates supported by a monitor.
old-location: display\d3dkmdt_frequency_range.htm
old-project: display
ms.assetid: f826f949-b37f-4c48-80d9-b6ef640e1f00
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: D3DKMDT_FREQUENCY_RANGE, D3DKMDT_FREQUENCY_RANGE structure [Display Devices], DmStructs_63b22220-c9fc-4eac-a725-caa0f5c38eba.xml, _D3DKMDT_FREQUENCY_RANGE, d3dkmdt/D3DKMDT_FREQUENCY_RANGE, display.d3dkmdt_frequency_range
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmdt.h
req.include-header: D3dkmdt.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
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
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	d3dkmdt.h
api_name:
-	D3DKMDT_FREQUENCY_RANGE
product: Windows
targetos: Windows
req.typenames: D3DKMDT_FREQUENCY_RANGE
---

# _D3DKMDT_FREQUENCY_RANGE structure
The D3DKMDT_FREQUENCY_RANGE structure contains the minimum and maximum refresh rates supported by a monitor.

## Syntax
```
typedef struct _D3DKMDT_FREQUENCY_RANGE {
  D3DDDI_RATIONAL MinVSyncFreq;
  D3DDDI_RATIONAL MaxVSyncFreq;
  D3DDDI_RATIONAL MinHSyncFreq;
  D3DDDI_RATIONAL MaxHSyncFreq;
} D3DKMDT_FREQUENCY_RANGE;
```

## Members


`MinVSyncFreq`

The minimum vertical refresh rate, in Hz, supported by the monitor.

`MaxVSyncFreq`

The maximum vertical refresh rate, in Hz, supported by the monitor.

`MinHSyncFreq`

The minimum horizontal refresh rate, in Hz, supported by the monitor.

`MaxHSyncFreq`

The maximum horizontal refresh rate, in Hz, supported by the monitor.

## Remarks
The <b>RangeLimits</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff546103">D3DKMDT_MONITOR_FREQUENCY_RANGE</a> structure is a D3DKMDT_FREQUENCY_RANGE structure.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems. Available in Windows Vista and later versions of the Windows operating systems. |
| **Header** | d3dkmdt.h (include D3dkmdt.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff568430">Monitor Frequency Range Set Interface</a>