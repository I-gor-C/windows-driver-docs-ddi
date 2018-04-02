---
UID: NS:dxva._DXVA_VideoPropertyRange
title: "_DXVA_VideoPropertyRange"
author: windows-driver-content
description: The DXVA_VideoPropertyRange structure specifies the range of allowed values for ProcAmp control properties.
old-location: display\dxva_videopropertyrange.htm
old-project: display
ms.assetid: e78fa9ba-7573-47db-b4d8-9b7584d5b432
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: "*LPDXVA_VideoPropertyRange, DXVA_VideoPropertyRange, DXVA_VideoPropertyRange structure [Display Devices], LPDXVA_VideoPropertyRange, LPDXVA_VideoPropertyRange structure pointer [Display Devices], _DXVA_VideoPropertyRange, display.dxva_videopropertyrange, dxva/DXVA_VideoPropertyRange, dxva/LPDXVA_VideoPropertyRange, dxvaref_0e7bc2aa-0404-4025-908a-5d4c528e020b.xml"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: dxva.h
req.include-header: Dxva.h
req.target-type: Windows
req.target-min-winverclnt: DirectX 9.0 and later versions only.
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
-	dxva.h
api_name:
-	DXVA_VideoPropertyRange
product: Windows
targetos: Windows
req.typenames: DXVA_VideoPropertyRange, *LPDXVA_VideoPropertyRange
---

# _DXVA_VideoPropertyRange structure
The DXVA_VideoPropertyRange structure specifies the range of allowed values for ProcAmp control properties.

## Syntax
```
typedef struct _DXVA_VideoPropertyRange {
  FLOAT MinValue;
  FLOAT MaxValue;
  FLOAT DefaultValue;
  FLOAT StepSize;
} *LPDXVA_VideoPropertyRange, DXVA_VideoPropertyRange;
```

## Members


`MinValue`

Specifies the minimum value allowed for a given property.

`MaxValue`

Specifies the maximum value allowed for a given property.

`DefaultValue`

Specifies the default value for a given property.

`StepSize`

Specifies the step size increment for a given property.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | DirectX 9.0 and later versions only. DirectX 9.0 and later versions only. |
| **Header** | dxva.h (include Dxva.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff564070">DXVA_VideoDesc</a>