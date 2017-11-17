---
UID: NC.wdbgexts.PWINDBG_EXTENSION_DLL_INIT64
title: PWINDBG_EXTENSION_DLL_INIT64
author: windows-driver-content
description: 
ms.assetid: 20197762-3697-491e-8ea5-0af03e901724
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

# PWINDBG_EXTENSION_DLL_INIT64 callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PWINDBG_EXTENSION_DLL_INIT64 PwindbgExtensionDllInit64; 

// Definition

VOID PwindbgExtensionDllInit64 
(
	PWINDBG_EXTENSION_APIS64 lpExtensionApis
	USHORT MajorVersion
	USHORT MinorVersion
)
{...}

PWINDBG_EXTENSION_DLL_INIT64 


```

## -parameters

### -param lpExtensionApis: 
### -param MajorVersion: 
### -param MinorVersion: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also