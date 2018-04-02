---
UID: NS:d3dkmddi._DXGK_STANDARD_COLORIMETRY_FLAGS
title: "_DXGK_STANDARD_COLORIMETRY_FLAGS"
author: windows-driver-content
description: Flags describing standard colorimetry and related support.
old-location: display\dxgk_standard_colorimetry_flags.htm
old-project: display
ms.assetid: 473C5D7B-8FDD-49E2-981A-00ECCA67671A
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: "*PDXGK_STANDARD_COLORIMETRY_FLAGS, DXGK_STANDARD_COLORIMETRY_FLAGS, DXGK_STANDARD_COLORIMETRY_FLAGS union [Display Devices], PDXGK_STANDARD_COLORIMETRY_FLAGS, PDXGK_STANDARD_COLORIMETRY_FLAGS union pointer [Display Devices], _DXGK_STANDARD_COLORIMETRY_FLAGS, d3dkmddi/DXGK_STANDARD_COLORIMETRY_FLAGS, d3dkmddi/PDXGK_STANDARD_COLORIMETRY_FLAGS, display.dxgk_standard_colorimetry_flags"
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
-	DXGK_STANDARD_COLORIMETRY_FLAGS
product: Windows
targetos: Windows
req.typenames: DXGK_STANDARD_COLORIMETRY_FLAGS, *PDXGK_STANDARD_COLORIMETRY_FLAGS
---

# _DXGK_STANDARD_COLORIMETRY_FLAGS structure
Flags describing standard colorimetry and related support.

## Syntax
```
typedef struct _DXGK_STANDARD_COLORIMETRY_FLAGS {
  struct {
    UINT  : 1  BT2020RGB;
    UINT  : 1  BT2020YCC;
    UINT  : 29 Reserved;
    UINT  : 1  ST2084;
  };
  ULONG  Value;
} *PDXGK_STANDARD_COLORIMETRY_FLAGS, DXGK_STANDARD_COLORIMETRY_FLAGS;
```

## Members


`Value`

The combined value that is operated on.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | d3dkmddi.h |