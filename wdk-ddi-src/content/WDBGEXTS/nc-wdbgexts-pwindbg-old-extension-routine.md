---
UID: NC.wdbgexts.PWINDBG_OLD_EXTENSION_ROUTINE
title: PWINDBG_OLD_EXTENSION_ROUTINE
author: windows-driver-content
description: 
ms.assetid: eac394a7-65a9-4a1c-9c4c-9dd8bf9caf94
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

# PWINDBG_OLD_EXTENSION_ROUTINE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PWINDBG_OLD_EXTENSION_ROUTINE PwindbgOldExtensionRoutine; 

// Definition

VOID PwindbgOldExtensionRoutine 
(
	ULONG dwCurrentPc
	PWINDBG_EXTENSION_APIS lpExtensionApis
	PCSTR lpArgumentString
)
{...}

PWINDBG_OLD_EXTENSION_ROUTINE 


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