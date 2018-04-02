---
UID: NS:d3dkmddi._DXGK_POWER_COMPONENT_FLAGS
title: "_DXGK_POWER_COMPONENT_FLAGS"
author: windows-driver-content
description: Describes state transition information about a power component.
old-location: display\dxgk_power_component_flags.htm
old-project: display
ms.assetid: aa8cce5b-d582-4c5b-99e2-fad1f0e80128
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: DXGK_POWER_COMPONENT_FLAGS, DXGK_POWER_COMPONENT_FLAGS structure [Display Devices], _DXGK_POWER_COMPONENT_FLAGS, d3dkmddi/DXGK_POWER_COMPONENT_FLAGS, display.dxgk_power_component_flags
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmddi.h
req.include-header: D3dkmddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
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
-	D3dkmddi.h
api_name:
-	DXGK_POWER_COMPONENT_FLAGS
product:
- Windows
targetos: Windows
req.typenames: DXGK_POWER_COMPONENT_FLAGS
---

# _DXGK_POWER_COMPONENT_FLAGS structure
Describes state transition information about a power component.

## Syntax
```
typedef struct _DXGK_POWER_COMPONENT_FLAGS {
  union {
    struct {
      UINT  : 1  Reserved0;
      UINT  : 1  DriverCompletesFStateTransition;
      UINT  : 1  TransitionTo_F0_OnDx;
      UINT  : 1  NoDebounce;
      UINT  : 1  ActiveInD3;
      UINT  : 27 Reserved;
      UINT  : 29 Reserved;
    };
    UINT Value;
  };
} DXGK_POWER_COMPONENT_FLAGS;
```

## Members



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8 Windows 8 |
| **Header** | d3dkmddi.h (include D3dkmddi.h) |

## See Also

<a href="https://msdn.microsoft.com/69a6d9bc-44a9-4204-988e-e11c80f67f28">DxgkCbCompleteFStateTransition</a>