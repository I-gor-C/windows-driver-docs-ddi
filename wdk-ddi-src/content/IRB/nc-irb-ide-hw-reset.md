---
UID: NC.irb.IDE_HW_RESET
title: IDE_HW_RESET
author: windows-driver-content
description: 
ms.assetid: 1bd81ec5-fe4b-4fd2-98b6-5b91fb1d0e67
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

# IDE_HW_RESET callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

IDE_HW_RESET IdeHwReset; 

// Definition

BOOLEAN IdeHwReset 
(
	PVOID ChannelExtension
)
{...}

IDE_HW_RESET 


```

## -parameters

### -param ChannelExtension: 



## -returns

Returns BOOLEAN that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also