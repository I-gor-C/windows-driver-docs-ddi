---
UID: NS:d3dkmddi._DXGK_SET_TIMING_RESULTS
title: "_DXGK_SET_TIMING_RESULTS"
author: windows-driver-content
description: Structure to report result flags from the SetTiming call which apply to the complete call rather than individual paths.
old-location: display\dxgk_set_timing_results.htm
old-project: display
ms.assetid: EA5C845B-76FD-40AD-B4E8-78601CA847CE
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: "*PDXGK_SET_TIMING_RESULTS, DXGK_SET_TIMING_RESULTS, DXGK_SET_TIMING_RESULTS structure [Display Devices], PDXGK_SET_TIMING_RESULTS, PDXGK_SET_TIMING_RESULTS structure pointer [Display Devices], _DXGK_SET_TIMING_RESULTS, d3dkmddi/DXGK_SET_TIMING_RESULTS, d3dkmddi/PDXGK_SET_TIMING_RESULTS, display.dxgk_set_timing_results"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmddi.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
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
req.irql: PASSIVE_LEVEL
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	d3dkmddi.h
api_name:
-	DXGK_SET_TIMING_RESULTS
product:
- Windows
targetos: Windows
req.typenames: DXGK_SET_TIMING_RESULTS, *PDXGK_SET_TIMING_RESULTS
---

# _DXGK_SET_TIMING_RESULTS structure
Structure to report result flags from the SetTiming call which apply to the complete call rather than individual paths.

## Syntax
```
typedef struct _DXGK_SET_TIMING_RESULTS {
  union {
    struct {
      UINT  : 1  ConnectionStatusChanges;
      UINT  : 31 Reserved;
    };
    UINT Value;
  };
} DXGK_SET_TIMING_RESULTS, *PDXGK_SET_TIMING_RESULTS;
```

## Members



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | d3dkmddi.h |