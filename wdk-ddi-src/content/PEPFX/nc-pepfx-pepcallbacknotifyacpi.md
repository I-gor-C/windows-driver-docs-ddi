---
UID: NC.pepfx.PEPCALLBACKNOTIFYACPI
title: PEPCALLBACKNOTIFYACPI
author: windows-driver-content
description: 
ms.assetid: 5f4e492d-f1f7-4750-abe0-5cdda5c5f352
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: pepfx.h
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

# PEPCALLBACKNOTIFYACPI callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PEPCALLBACKNOTIFYACPI Pepcallbacknotifyacpi; 

// Definition

BOOLEAN Pepcallbacknotifyacpi 
(
	ULONG Notification
	PVOID Data
)
{...}

PEPCALLBACKNOTIFYACPI PPEPCALLBACKNOTIFYACPI


```

## -parameters

### -param Notification: 
### -param Data: 



## -returns

Returns BOOLEAN that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also