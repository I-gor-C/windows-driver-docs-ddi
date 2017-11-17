---
UID: NC.dbghelp.PTRANSLATE_ADDRESS_ROUTINE
title: PTRANSLATE_ADDRESS_ROUTINE
author: windows-driver-content
description: 
ms.assetid: b4c25459-1d53-48a5-b60f-7ff49529b6e4
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

# PTRANSLATE_ADDRESS_ROUTINE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PTRANSLATE_ADDRESS_ROUTINE PtranslateAddressRoutine; 

// Definition

DWORD PtranslateAddressRoutine 
(
	HANDLE hProcess
	HANDLE hThread
	LPADDRESS lpaddr
)
{...}

PTRANSLATE_ADDRESS_ROUTINE 


```

## -parameters

### -param hProcess: 
### -param hThread: 
### -param lpaddr: 



## -returns

Returns DWORD that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also