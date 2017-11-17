---
UID: NC.irb.IDE_HW_INTERRUPT
title: IDE_HW_INTERRUPT
author: windows-driver-content
description: 
ms.assetid: 2ae43193-dc89-4d9b-9799-9b851d6d3d2d
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

# IDE_HW_INTERRUPT callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

IDE_HW_INTERRUPT IdeHwInterrupt; 

// Definition

BOOLEAN IdeHwInterrupt 
(
	PVOID ChannelExtension
)
{...}

IDE_HW_INTERRUPT 


```

## -parameters

### -param ChannelExtension: 



## -returns

Returns BOOLEAN that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also