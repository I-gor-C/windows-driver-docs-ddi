---
UID: NC.d3d12umddi.PFND3D12DDI_BEGIN_END_QUERY
title: PFND3D12DDI_BEGIN_END_QUERY
author: windows-driver-content
description: 
ms.assetid: 96f861d2-368f-4c82-8240-8cb55814e2ea
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: d3d12umddi.h
req.include-header:
req.target-type:
req.target-min-winverclnt:
req.target-min-winversvr:
req.kmdf-ver:
req.umdf-ver:
req.lib:
req.dll:
req.irql: 
req.ddi-compliance:
req.alt-api:
req.alt-loc:
req.unicode-ansi:
req.idl:
req.max-support:
req.namespace:
req.assembly:
req.type-library:
---

# PFND3D12DDI_BEGIN_END_QUERY callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3D12DDI_BEGIN_END_QUERY Pfnd3d12ddiBeginEndQuery; 

// Definition

VOID Pfnd3d12ddiBeginEndQuery 
(
	 D3D12DDI_HCOMMANDLIST
	 D3D12DDI_HQUERYHEAP
	 UINT
	 D3D12DDI_QUERY_TYPE
)
{...}

PFND3D12DDI_BEGIN_END_QUERY 


```

## -parameters

### -param D3D12DDI_HCOMMANDLIST: 
### -param D3D12DDI_HQUERYHEAP: 
### -param UINT: 
### -param D3D12DDI_QUERY_TYPE: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also