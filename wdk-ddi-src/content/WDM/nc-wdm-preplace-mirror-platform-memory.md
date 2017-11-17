---
UID: NC.wdm.PREPLACE_MIRROR_PLATFORM_MEMORY
title: PREPLACE_MIRROR_PLATFORM_MEMORY
author: windows-driver-content
description: 
ms.assetid: 57918105-9fad-4991-8318-e771a780bfd2
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

# PREPLACE_MIRROR_PLATFORM_MEMORY callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PREPLACE_MIRROR_PLATFORM_MEMORY PreplaceMirrorPlatformMemory; 

// Definition

NTSTATUS PreplaceMirrorPlatformMemory 
(
	PVOID Context
)
{...}

PREPLACE_MIRROR_PLATFORM_MEMORY 


```

## -parameters

### -param Context: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also