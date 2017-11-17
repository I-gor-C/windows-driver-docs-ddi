---
UID: NC.engextcpp.PEXT_DLL_MAIN
title: PEXT_DLL_MAIN
author: windows-driver-content
description: 
ms.assetid: ee90a53b-7a86-4aa8-b96d-15de3b79882f
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: engextcpp.hpp
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

# PEXT_DLL_MAIN callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PEXT_DLL_MAIN PextDllMain; 

// Definition

BOOL PextDllMain 
(
	HANDLE Instance
	ULONG Reason
	PVOID Reserved
)
{...}

PEXT_DLL_MAIN 


```

## -parameters

### -param Instance: 
### -param Reason: 
### -param Reserved: 



## -returns

Returns BOOL that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also