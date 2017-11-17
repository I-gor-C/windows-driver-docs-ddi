---
UID: NC.wdm.PIO_CONTAINER_NOTIFICATION_FUNCTION
title: PIO_CONTAINER_NOTIFICATION_FUNCTION
author: windows-driver-content
description: 
ms.assetid: 73373d49-e1af-4999-aec9-683b001c6375
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

# PIO_CONTAINER_NOTIFICATION_FUNCTION callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PIO_CONTAINER_NOTIFICATION_FUNCTION PioContainerNotificationFunction; 

// Definition

NTSTATUS PioContainerNotificationFunction 
(
	 VOID
)
{...}

PIO_CONTAINER_NOTIFICATION_FUNCTION 


```

## -parameters

### -param VOID: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also