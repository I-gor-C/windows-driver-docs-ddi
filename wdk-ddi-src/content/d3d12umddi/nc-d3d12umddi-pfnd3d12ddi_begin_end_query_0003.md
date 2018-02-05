---
UID : NC:d3d12umddi.PFND3D12DDI_BEGIN_END_QUERY_0003
title : PFND3D12DDI_BEGIN_END_QUERY_0003
author : windows-driver-content
description : The pfnBeginQuery callback function defines the beginning of the portion of a command list to which a query applies.
old-location : display\pfnd3d12ddi_begin_end_query_0003.htm
old-project : display
ms.assetid : 9EBF7E0C-BF6D-4E99-B289-8C6581A2DEA5
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : display.pfnd3d12ddi_begin_end_query_0003, pfnBeginQuery callback function [Display Devices], pfnBeginQuery, PFND3D12DDI_BEGIN_END_QUERY_0003, PFND3D12DDI_BEGIN_END_QUERY_0003, d3d12umddi/pfnBeginQuery
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : callback
req.header : d3d12umddi.h
req.include-header : D3d12umddi.h
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
req.irql : 
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : D3D11_1DDI_GETCAPTUREHANDLEDATA
---


# PFND3D12DDI_BEGIN_END_QUERY_0003 callback function
The <i>pfnBeginQuery</i> callback function defines the beginning of the portion of a command list to which a query applies.

## Syntax

```
PFND3D12DDI_BEGIN_END_QUERY_0003 Pfnd3d12ddiBeginEndQuery0003;

void Pfnd3d12ddiBeginEndQuery0003(
   D3D12DDI_HCOMMANDLIST,
   D3D12DDI_HQUERYHEAP,
   D3D12DDI_QUERY_TYPE,
   UINT
)
{...}
```

## Parameters

`D3D12DDI_HCOMMANDLIST`



`D3D12DDI_HQUERYHEAP`



`D3D12DDI_QUERY_TYPE`



`UINT`




## Return Value

This callback function does not return a value.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | d3d12umddi.h (include D3d12umddi.h) |