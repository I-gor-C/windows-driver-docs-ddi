---
UID: NC.d3d12umddi.PFND3D12DDI_CLOSECOMMANDLIST
title: PFND3D12DDI_CLOSECOMMANDLIST
author: windows-driver-content
description: 
ms.assetid: 63b1b63a-e18e-4ff0-aa92-fbabb559a23b
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

# PFND3D12DDI_CLOSECOMMANDLIST callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3D12DDI_CLOSECOMMANDLIST Pfnd3d12ddiClosecommandlist; 

// Definition

VOID Pfnd3d12ddiClosecommandlist 
(
	 D3D12DDI_HCOMMANDLIST
)
{...}

PFND3D12DDI_CLOSECOMMANDLIST 


```

## -parameters

### -param D3D12DDI_HCOMMANDLIST: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also