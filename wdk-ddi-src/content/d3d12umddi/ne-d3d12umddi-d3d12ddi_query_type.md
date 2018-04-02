---
UID: NE:d3d12umddi.D3D12DDI_QUERY_TYPE
title: D3D12DDI_QUERY_TYPE
author: windows-driver-content
description: Type of a query.
old-location: display\d3d12ddi_query_type.htm
old-project: display
ms.assetid: C411997A-0F01-4D88-816A-BD375D0744C7
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: D3D12DDI_QUERY_TYPE, D3D12DDI_QUERY_TYPE enumeration [Display Devices], D3D12DDI_QUERY_TYPE_0020_VIDEO_DECODE_STATISTICS, D3D12DDI_QUERY_TYPE_BINARY_OCCLUSION, D3D12DDI_QUERY_TYPE_OCCLUSION, D3D12DDI_QUERY_TYPE_PIPELINE_STATISTICS, D3D12DDI_QUERY_TYPE_SO_STATISTICS_STREAM0, D3D12DDI_QUERY_TYPE_SO_STATISTICS_STREAM1, D3D12DDI_QUERY_TYPE_SO_STATISTICS_STREAM2, D3D12DDI_QUERY_TYPE_SO_STATISTICS_STREAM3, D3D12DDI_QUERY_TYPE_TIMESTAMP, d3d12umddi/D3D12DDI_QUERY_TYPE, d3d12umddi/D3D12DDI_QUERY_TYPE_0020_VIDEO_DECODE_STATISTICS, d3d12umddi/D3D12DDI_QUERY_TYPE_BINARY_OCCLUSION, d3d12umddi/D3D12DDI_QUERY_TYPE_OCCLUSION, d3d12umddi/D3D12DDI_QUERY_TYPE_PIPELINE_STATISTICS, d3d12umddi/D3D12DDI_QUERY_TYPE_SO_STATISTICS_STREAM0, d3d12umddi/D3D12DDI_QUERY_TYPE_SO_STATISTICS_STREAM1, d3d12umddi/D3D12DDI_QUERY_TYPE_SO_STATISTICS_STREAM2, d3d12umddi/D3D12DDI_QUERY_TYPE_SO_STATISTICS_STREAM3, d3d12umddi/D3D12DDI_QUERY_TYPE_TIMESTAMP, display.d3d12ddi_query_type
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: d3d12umddi.h
req.include-header: D3d12umddi.h
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
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	D3d12umddi.h
api_name:
-	D3D12DDI_QUERY_TYPE
product:
- Windows
targetos: Windows
req.typenames: D3D12DDI_QUERY_TYPE
---

# D3D12DDI_QUERY_TYPE Enumeration
Type of a query.

## Syntax
```
typedef enum D3D12DDI_QUERY_TYPE {
  D3D12DDI_QUERY_TYPE_OCCLUSION                     ,
  D3D12DDI_QUERY_TYPE_BINARY_OCCLUSION              ,
  D3D12DDI_QUERY_TYPE_TIMESTAMP                     ,
  D3D12DDI_QUERY_TYPE_PIPELINE_STATISTICS           ,
  D3D12DDI_QUERY_TYPE_SO_STATISTICS_STREAM0         ,
  D3D12DDI_QUERY_TYPE_SO_STATISTICS_STREAM1         ,
  D3D12DDI_QUERY_TYPE_SO_STATISTICS_STREAM2         ,
  D3D12DDI_QUERY_TYPE_SO_STATISTICS_STREAM3         ,
  D3D12DDI_QUERY_TYPE_0020_VIDEO_DECODE_STATISTICS
} ;
```

## Constants

<table>
            
                <tr>
                    <td>D3D12DDI_QUERY_TYPE_OCCLUSION</td>
                    <td>Occlusion.</td>
                </tr>
            
                <tr>
                    <td>D3D12DDI_QUERY_TYPE_BINARY_OCCLUSION</td>
                    <td>Binary occlusion.</td>
                </tr>
            
                <tr>
                    <td>D3D12DDI_QUERY_TYPE_TIMESTAMP</td>
                    <td>Timestamp.</td>
                </tr>
            
                <tr>
                    <td>D3D12DDI_QUERY_TYPE_PIPELINE_STATISTICS</td>
                    <td>Pipeline statistics.</td>
                </tr>
            
                <tr>
                    <td>D3D12DDI_QUERY_TYPE_SO_STATISTICS_STREAM0</td>
                    <td>SO statistics for Stream0.</td>
                </tr>
            
                <tr>
                    <td>D3D12DDI_QUERY_TYPE_SO_STATISTICS_STREAM1</td>
                    <td>SO statistics for Stream1.</td>
                </tr>
            
                <tr>
                    <td>D3D12DDI_QUERY_TYPE_SO_STATISTICS_STREAM2</td>
                    <td>SO statistics for Stream2.</td>
                </tr>
            
                <tr>
                    <td>D3D12DDI_QUERY_TYPE_SO_STATISTICS_STREAM3</td>
                    <td>SO statistics for Stream3.</td>
                </tr>
            
                <tr>
                    <td>D3D12DDI_QUERY_TYPE_0020_VIDEO_DECODE_STATISTICS</td>
                    <td>Video decode statistics.</td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | d3d12umddi.h (include D3d12umddi.h) |