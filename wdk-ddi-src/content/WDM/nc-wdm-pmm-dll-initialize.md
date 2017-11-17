---
UID: NC.wdm.PMM_DLL_INITIALIZE
title: PMM_DLL_INITIALIZE
author: windows-driver-content
description: 
ms.assetid: 2adb682d-a795-4e03-87c4-fd56f196d202
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdm.h
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

# PMM_DLL_INITIALIZE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PMM_DLL_INITIALIZE PmmDllInitialize; 

// Definition

NTSTATUS PmmDllInitialize 
(
	PUNICODE_STRING RegistryPath
)
{...}

PMM_DLL_INITIALIZE 


```

## -parameters

### -param RegistryPath: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also