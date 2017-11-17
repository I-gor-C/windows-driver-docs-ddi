---
UID: NC.irb.IDE_CHANNEL_INIT
title: IDE_CHANNEL_INIT
author: windows-driver-content
description: 
ms.assetid: 499fac8e-84b8-4760-9e7a-9754e8fd8777
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

# IDE_CHANNEL_INIT callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

IDE_CHANNEL_INIT IdeChannelInit; 

// Definition

BOOLEAN IdeChannelInit 
(
	PVOID ChannelExtension
	PIDE_CHANNEL_INTERFACE ChannelInterface
	PVOID InitContext
)
{...}

IDE_CHANNEL_INIT 


```

## -parameters

### -param ChannelExtension: 
### -param ChannelInterface: 
### -param InitContext: 



## -returns

Returns BOOLEAN that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also