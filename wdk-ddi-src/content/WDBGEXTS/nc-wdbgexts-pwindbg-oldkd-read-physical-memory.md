---
UID: NC.wdbgexts.PWINDBG_OLDKD_READ_PHYSICAL_MEMORY
title: PWINDBG_OLDKD_READ_PHYSICAL_MEMORY
author: windows-driver-content
description: 
ms.assetid: 631ca4d6-4ec4-4dc6-a76c-c6592e161d0f
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdbgexts.h
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

# PWINDBG_OLDKD_READ_PHYSICAL_MEMORY callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PWINDBG_OLDKD_READ_PHYSICAL_MEMORY PwindbgOldkdReadPhysicalMemory; 

// Definition

ULONG PwindbgOldkdReadPhysicalMemory 
(
	ULONGLONG address
	PVOID buffer
	ULONG count
	PULONG bytesread
)
{...}

PWINDBG_OLDKD_READ_PHYSICAL_MEMORY 


```

## -parameters

### -param address: 
### -param buffer: 
### -param count: 
### -param bytesread: 



## -returns

Returns ULONG that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also