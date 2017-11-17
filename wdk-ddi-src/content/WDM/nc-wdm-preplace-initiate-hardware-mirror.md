---
UID: NC.wdm.PREPLACE_INITIATE_HARDWARE_MIRROR
title: PREPLACE_INITIATE_HARDWARE_MIRROR
author: windows-driver-content
description: 
ms.assetid: 29eddfe2-e901-4462-b7b9-3c3538a1dd14
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

# PREPLACE_INITIATE_HARDWARE_MIRROR callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PREPLACE_INITIATE_HARDWARE_MIRROR PreplaceInitiateHardwareMirror; 

// Definition

NTSTATUS PreplaceInitiateHardwareMirror 
(
	PVOID Context
)
{...}

PREPLACE_INITIATE_HARDWARE_MIRROR 


```

## -parameters

### -param Context: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also