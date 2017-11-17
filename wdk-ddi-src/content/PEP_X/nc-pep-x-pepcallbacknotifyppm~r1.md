---
UID: NC.pep_x.PEPCALLBACKNOTIFYPPM~r1
title: PEPCALLBACKNOTIFYPPM
author: windows-driver-content
description: 
ms.assetid: 6ffd73fa-2094-4aa7-9c13-be456920e880
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: pep_x.h
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

# PEPCALLBACKNOTIFYPPM callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PEPCALLBACKNOTIFYPPM Pepcallbacknotifyppm; 

// Definition

BOOLEAN Pepcallbacknotifyppm 
(
	PEPHANDLE Handle
	ULONG Notification
	PVOID Data
)
{...}

PEPCALLBACKNOTIFYPPM PPEPCALLBACKNOTIFYPPM


```

## -parameters

### -param Handle: 
### -param Notification: 
### -param Data: 



## -returns

Returns BOOLEAN that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also