---
UID: NC.wdm.PREPLACE_END
title: PREPLACE_END
author: windows-driver-content
description: 
ms.assetid: 5a81d52c-c727-4bb9-b840-2754bdc277d9
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

# PREPLACE_END callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PREPLACE_END PreplaceEnd; 

// Definition

NTSTATUS PreplaceEnd 
(
	PVOID Context
)
{...}

PREPLACE_END 


```

## -parameters

### -param Context: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also