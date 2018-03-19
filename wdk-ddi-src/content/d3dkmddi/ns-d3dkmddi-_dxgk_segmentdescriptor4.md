---
UID: NS:d3dkmddi._DXGK_SEGMENTDESCRIPTOR4
title: "_DXGK_SEGMENTDESCRIPTOR4"
author: windows-driver-content
description: The DXGK_SEGMENTDESCRIPTOR4 structure describes a programmable CPU host aperture.
old-location: display\dxgk_segmentdescriptor4.htm
old-project: display
ms.assetid: 0958443F-1554-47B0-83B9-283D98D927CE
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: DXGK_SEGMENTDESCRIPTOR4, DXGK_SEGMENTDESCRIPTOR4 structure [Display Devices], _DXGK_SEGMENTDESCRIPTOR4, d3dkmddi/DXGK_SEGMENTDESCRIPTOR4, display.dxgk_segmentdescriptor4
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmddi.h
req.include-header: D3dkmddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
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
-	DXGK_SEGMENTDESCRIPTOR4
product: Windows
targetos: Windows
req.typenames: DXGK_SEGMENTDESCRIPTOR4
---

# _DXGK_SEGMENTDESCRIPTOR4 structure
The <b>DXGK_SEGMENTDESCRIPTOR4</b> structure describes a programmable CPU host aperture.

## Syntax
````
typedef struct _DXGK_SEGMENTDESCRIPTOR4 {
  DXGK_SEGMENTFLAGS Flags;
  PHYSICAL_ADDRESS  BaseAddress;
  SIZE_T            Size;
  SIZE_T            CommitLimit;
  SIZE_T            SystemMemoryEndAddress;
  union {
    PHYSICAL_ADDRESS     CpuTranslatedAddress;
    DXGK_CPUHOSTAPERTURE CpuHostAperture;
  };
  UINT              NumInvalidMemoryRanges;
} DXGK_SEGMENTDESCRIPTOR4;
````

## Members


`Flags`

Segment bit field flags

`BaseAddress`

The physical base address for the segment in the GPU.

`Size`

The size of the segment in bytes.

`CommitLimit`

The maximum number of bytes that can be committed to this segment. 

<div class="alert"><b>Note</b>  This applies to the aperture segment only.</div>
<div> </div>

`SystemMemoryEndAddress`

For segments that are partially composed of system memory, all allocations ending after this address are purged during hibernate.

`NumInvalidMemoryRanges`

The number of invalid memory ranges in the segment. If this value is not zero, the kernel mode driver will be called with DdiQueryAdapterInfo(DXGKQAITYPE_SEGMENTMEMORYSTATE) to get information about invalid memory ranges.

`VprRangeStartOffset`



`VprRangeSize`



`VprAlignment`



`NumVprSupported`



`VprReserveSize`



`NumUEFIFrameBufferRanges`




## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 10 Windows 10 |
| **Header** | d3dkmddi.h (include D3dkmddi.h) |