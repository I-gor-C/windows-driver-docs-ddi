---
UID: NC.wdbgexts.PWINDBG_OLDKD_EXTENSION_ROUTINE
title: PWINDBG_OLDKD_EXTENSION_ROUTINE
author: windows-driver-content
description: 
ms.assetid: f441c364-5ceb-44d5-8952-48f0b70146c9
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

# PWINDBG_OLDKD_EXTENSION_ROUTINE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PWINDBG_OLDKD_EXTENSION_ROUTINE PwindbgOldkdExtensionRoutine; 

// Definition

VOID PwindbgOldkdExtensionRoutine 
(
	ULONG dwCurrentPc
	PWINDBG_OLDKD_EXTENSION_APIS lpExtensionApis
	PCSTR lpArgumentString
)
{...}

PWINDBG_OLDKD_EXTENSION_ROUTINE 


```

## -parameters

### -param dwCurrentPc: 
### -param lpExtensionApis: 
### -param lpArgumentString: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also