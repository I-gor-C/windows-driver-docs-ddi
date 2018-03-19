---
UID: NS:d3d10umddi.D3D10_DDI_QUERY_DATA_PIPELINE_STATISTICS
title: D3D10_DDI_QUERY_DATA_PIPELINE_STATISTICS
author: windows-driver-content
description: The D3D10_DDI_QUERY_DATA_PIPELINE_STATISTICS structure describes statistics for each stage of the graphics pipeline that is used in a call to the CreateQuery(D3D10) function to create a D3D10DDI_QUERY_PIPELINESTATS query type and in a call to the QueryGetData function to return information about the query.
old-location: display\d3d10_ddi_query_data_pipeline_statistics.htm
old-project: display
ms.assetid: 5e481453-1e01-46b4-a04e-e9c575cd65b9
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: D3D10_DDI_QUERY_DATA_PIPELINE_STATISTICS, D3D10_DDI_QUERY_DATA_PIPELINE_STATISTICS structure [Display Devices], UMDisplayDriver_Dx10param_Structs_66e61d2d-0a0d-41aa-a25d-a7fa3ef08b4c.xml, d3d10umddi/D3D10_DDI_QUERY_DATA_PIPELINE_STATISTICS, display.d3d10_ddi_query_data_pipeline_statistics
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
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
-	d3d10umddi.h
api_name:
-	D3D10_DDI_QUERY_DATA_PIPELINE_STATISTICS
product: Windows
targetos: Windows
req.typenames: D3D10_DDI_QUERY_DATA_PIPELINE_STATISTICS
---

# D3D10_DDI_QUERY_DATA_PIPELINE_STATISTICS structure
The D3D10_DDI_QUERY_DATA_PIPELINE_STATISTICS structure describes statistics for each stage of the graphics pipeline that is used in a call to the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi_createquery.md">CreateQuery(D3D10)</a> function to create a D3D10DDI_QUERY_PIPELINESTATS query type and in a call to the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi_querygetdata.md">QueryGetData</a> function to return information about the query.

## Syntax
````
typedef struct D3D10_DDI_QUERY_DATA_PIPELINE_STATISTICS {
  UINT64 IAVertices;
  UINT64 IAPrimitives;
  UINT64 VSInvocations;
  UINT64 GSInvocations;
  UINT64 GSPrimitives;
  UINT64 CInvocations;
  UINT64 CPrimitives;
  UINT64 PSInvocations;
} D3D10_DDI_QUERY_DATA_PIPELINE_STATISTICS;
````

## Members


`IAVertices`

The number of input assembler (IA) veritces.

`IAPrimitives`

The number of IA primitives.

`VSInvocations`

The number of vertex shader (VS) invocations.

`GSInvocations`

The number of geometry shader (GS) invocations.

`GSPrimitives`

The number of GS primitives.

`CInvocations`

The number of clipper invocations.

`CPrimitives`

The number of clipper primitives.

`PSInvocations`

The number of pixel shader (PS) invocations.

## Remarks
The driver associates a D3D10_DDI_QUERY_DATA_PIPELINE_STATISTICS structure with the D3D10DDI_QUERY_PIPELINESTATS query type value from the <a href="..\d3d10umddi\ne-d3d10umddi-d3d10ddi_query.md">D3D10DDI_QUERY</a> enumeration.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems. Available in Windows Vista and later versions of the Windows operating systems. |
| **Header** | d3d10umddi.h (include D3d10umddi.h) |

## See Also

<a href="..\d3d10umddi\ne-d3d10umddi-d3d10ddi_query.md">D3D10DDI_QUERY</a>



<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi_querygetdata.md">QueryGetData</a>



<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi_createquery.md">CreateQuery(D3D10)</a>