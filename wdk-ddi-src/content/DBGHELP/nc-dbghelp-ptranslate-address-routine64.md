---
UID: NC.dbghelp.PTRANSLATE_ADDRESS_ROUTINE64
title: PTRANSLATE_ADDRESS_ROUTINE64
author: windows-driver-content
description: 
ms.assetid: 7504625a-735f-4fe4-a634-3e97c5cf3bfa
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: dbghelp.h
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

# PTRANSLATE_ADDRESS_ROUTINE64 callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PTRANSLATE_ADDRESS_ROUTINE64 PtranslateAddressRoutine64; 

// Definition

DWORD64 PtranslateAddressRoutine64 
(
	HANDLE hProcess
	HANDLE hThread
	LPADDRESS64 lpaddr
)
{...}

PTRANSLATE_ADDRESS_ROUTINE64 


```

## -parameters

### -param hProcess: 
### -param hThread: 
### -param lpaddr: 



## -returns

Returns DWORD64 that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also