---
UID: NC.hubbusif.PUSB_BUSIFFN_RESUME_HUB
title: PUSB_BUSIFFN_RESUME_HUB
author: windows-driver-content
description: 
ms.assetid: 10a5643f-61f2-4c8d-96cf-96ce102dcc6e
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

# PUSB_BUSIFFN_RESUME_HUB callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PUSB_BUSIFFN_RESUME_HUB PusbBusiffnResumeHub; 

// Definition

NTSTATUS PusbBusiffnResumeHub 
(
	PDEVICE_OBJECT Pdo
)
{...}

PUSB_BUSIFFN_RESUME_HUB 


```

## -parameters

### -param Pdo: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also