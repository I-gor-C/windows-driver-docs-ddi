---
UID : NS:d3dkmddi._DXGK_SET_TIMING_RESULTS
title : "_DXGK_SET_TIMING_RESULTS"
author : windows-driver-content
description : Structure to report result flags from the SetTiming call which apply to the complete call rather than individual paths.
old-location : display\dxgk_set_timing_results.htm
old-project : display
ms.assetid : EA5C845B-76FD-40AD-B4E8-78601CA847CE
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : "_DXGK_SET_TIMING_RESULTS, PDXGK_SET_TIMING_RESULTS structure pointer [Display Devices], display.dxgk_set_timing_results, d3dkmddi/PDXGK_SET_TIMING_RESULTS, DXGK_SET_TIMING_RESULTS structure [Display Devices], d3dkmddi/DXGK_SET_TIMING_RESULTS, PDXGK_SET_TIMING_RESULTS, *PDXGK_SET_TIMING_RESULTS, DXGK_SET_TIMING_RESULTS"
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : d3dkmddi.h
req.include-header : 
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : PASSIVE_LEVEL
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : "*PDXGK_SET_TIMING_RESULTS, DXGK_SET_TIMING_RESULTS"
---

# _DXGK_SET_TIMING_RESULTS structure
Structure to report result flags from the SetTiming call which apply to the complete call rather than individual paths.

## Syntax
````
typedef struct _DXGK_SET_TIMING_RESULTS {
  union {
    struct {
      UINT ConnectionStatusChanges  :1;
      UINT Reserved  :31;
    };
    UINT Value;
  };
} DXGK_SET_TIMING_RESULTS, *PDXGK_SET_TIMING_RESULTS;
````

## Members



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | d3dkmddi.h |