---
UID: NS:d3dkmddi._DXGK_QUERYSEGMENTOUT4
title: "_DXGK_QUERYSEGMENTOUT4"
author: windows-driver-content
description: The DXGK_QUERYSEGMENTOUT4 structure contains memory segment information returned from the driver.
old-location: display\dxgk_querysegmentout4.htm
old-project: display
ms.assetid: AE6988E6-81D7-47FB-986A-B5DEE9B7215B
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: DXGK_QUERYSEGMENTOUT4, DXGK_QUERYSEGMENTOUT4 structure [Display Devices], _DXGK_QUERYSEGMENTOUT4, d3dkmddi/DXGK_QUERYSEGMENTOUT4, display.dxgk_querysegmentout4
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
-	DXGK_QUERYSEGMENTOUT4
product: Windows
targetos: Windows
req.typenames: DXGK_QUERYSEGMENTOUT4
---

# _DXGK_QUERYSEGMENTOUT4 structure
The <b>DXGK_QUERYSEGMENTOUT4</b> structure contains memory segment information  returned from the driver.

## Syntax
````
typedef struct _DXGK_QUERYSEGMENTOUT4 {
  UINT   NbSegment;
  BYTE   *pSegmentDescriptor;
  UINT   PagingBufferSegmentId;
  UINT   PagingBufferSize;
  UINT   PagingBufferPrivateDataSize;
  SIZE_T SegmentDescriptorStride;
} DXGK_QUERYSEGMENTOUT4;
````

## Members


`NbSegment`

Number of elements in the <b>pSegmentDescriptor</b> array. The <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi_queryadapterinfo.md">DxgkDdiQueryAdapterInfo</a> (<b>DXGKQAITYPE_QUERYSEGMENT4</b>) will be called twice. First time, <b>NbSegment</b> will be set to 0. The driver should return <b>STATUS_SUCCESS</b> and set <b>NbSegment</b> to the number of GPU memory segments in the adapter without accessing any other member of the structure. Second time, the driver will be called with the reported number of segments and the driver should fill all required information.

`pSegmentDescriptor`

Pointer to the array of <a href="..\d3dkmddi\ns-d3dkmddi-_dxgk_segmentdescriptor4.md">DXGK_SEGMENTDESCRIPTOR4</a> structures. The size of the array element is defined by <b>SegmentDescriptorStride</b>. The <b>pSegmentDescriptor</b> type has been changed to a <b>BYTE*</b> to help enforce the use of the stride as the method of iterating the array. The driver fills the array with information about each memory segment.

`PagingBufferSegmentId`

Segment identifier of the paging buffer. This is the index (starting from 1) of the segment in the <b>pSegmentDescriptor </b>array.

`PagingBufferSize`

Paging buffer size.

`PagingBufferPrivateDataSize`

Size, in bytes, of the driver-private data that will be provided with each paging buffer.

`SegmentDescriptorStride`

Size of the elements in the <b>pSegmentDescriptor</b> array in bytes.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 10 Windows 10 |
| **Header** | d3dkmddi.h (include D3dkmddi.h) |

## See Also

<a href="..\d3dkmddi\ns-d3dkmddi-_dxgk_querysegmentin4.md">DXGK_QUERYSEGMENTIN4</a>