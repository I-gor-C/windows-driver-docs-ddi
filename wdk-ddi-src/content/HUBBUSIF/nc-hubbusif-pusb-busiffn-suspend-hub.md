---
UID: NC.hubbusif.PUSB_BUSIFFN_SUSPEND_HUB
title: PUSB_BUSIFFN_SUSPEND_HUB
author: windows-driver-content
description: 
ms.assetid: 5a30023b-7c35-4935-b0de-c9a8dbdae8a0
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: hubbusif.h
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

# PUSB_BUSIFFN_SUSPEND_HUB callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PUSB_BUSIFFN_SUSPEND_HUB PusbBusiffnSuspendHub; 

// Definition

NTSTATUS PusbBusiffnSuspendHub 
(
	PDEVICE_OBJECT Pdo
)
{...}

PUSB_BUSIFFN_SUSPEND_HUB 


```

## -parameters

### -param Pdo: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also