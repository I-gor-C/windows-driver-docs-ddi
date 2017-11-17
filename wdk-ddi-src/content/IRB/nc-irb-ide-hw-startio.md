---
UID: NC.irb.IDE_HW_STARTIO
title: IDE_HW_STARTIO
author: windows-driver-content
description: 
ms.assetid: fcaebabd-80cf-47b8-a7e3-34bca99fbb11
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

# IDE_HW_STARTIO callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

IDE_HW_STARTIO IdeHwStartio; 

// Definition

BOOLEAN IdeHwStartio 
(
	PVOID ChannelExtension
	PIDE_REQUEST_BLOCK Irb
)
{...}

IDE_HW_STARTIO 


```

## -parameters

### -param ChannelExtension: 
### -param Irb: 



## -returns

Returns BOOLEAN that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also