---
UID: NC.irb.IDE_CHANNEL_ENABLED
title: IDE_CHANNEL_ENABLED
author: windows-driver-content
description: 
ms.assetid: 2ba4202b-eb60-49bf-a7d8-054568796530
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

# IDE_CHANNEL_ENABLED callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

IDE_CHANNEL_ENABLED IdeChannelEnabled; 

// Definition

ATA_CHANNEL_STATE IdeChannelEnabled 
(
	PVOID ControllerExtension
	ULONG Channel
)
{...}

IDE_CHANNEL_ENABLED 


```

## -parameters

### -param ControllerExtension: 
### -param Channel: 



## -returns

Returns ATA_CHANNEL_STATE that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also