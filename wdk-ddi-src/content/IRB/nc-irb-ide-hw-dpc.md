---
UID: NC.irb.IDE_HW_DPC
title: IDE_HW_DPC
author: windows-driver-content
description: 
ms.assetid: 355f7f95-42cd-4082-b698-14dc17a42553
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: irb.h
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

# IDE_HW_DPC callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

IDE_HW_DPC IdeHwDpc; 

// Definition

VOID IdeHwDpc 
(
	PVOID ChannelExtension
)
{...}

IDE_HW_DPC 


```

## -parameters

### -param ChannelExtension: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also