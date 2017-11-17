---
UID: NC.ntpoapi.ENTER_STATE_SYSTEM_HANDLER
title: ENTER_STATE_SYSTEM_HANDLER
author: windows-driver-content
description: 
ms.assetid: 03143ce0-382a-428a-9b12-70e3c4cd10be
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: ntpoapi.h
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

# ENTER_STATE_SYSTEM_HANDLER callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

ENTER_STATE_SYSTEM_HANDLER EnterStateSystemHandler; 

// Definition

NTSTATUS EnterStateSystemHandler 
(
	PVOID SystemContext
)
{...}

ENTER_STATE_SYSTEM_HANDLER 


```

## -parameters

### -param SystemContext: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also