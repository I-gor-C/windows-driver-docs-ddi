---
UID: NC.trustedruntimeclx.EVT_TR_CREATE_SECURE_SERVICE_CONTEXT
title: EVT_TR_CREATE_SECURE_SERVICE_CONTEXT
author: windows-driver-content
description: 
ms.assetid: 46df48a2-521e-4b19-a0cd-73f109460c97
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: trustedruntimeclx.h
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

# EVT_TR_CREATE_SECURE_SERVICE_CONTEXT callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

EVT_TR_CREATE_SECURE_SERVICE_CONTEXT EvtTrCreateSecureServiceContext; 

// Definition

NTSTATUS EvtTrCreateSecureServiceContext 
(
	WDFDEVICE MasterDevice
	LPCGUID ServiceGuid
	WDFDEVICE ServiceDevice
)
{...}

EVT_TR_CREATE_SECURE_SERVICE_CONTEXT PFN_TR_CREATE_SECURE_SERVICE_CONTEXT


```

## -parameters

### -param MasterDevice: 
### -param ServiceGuid: 
### -param ServiceDevice: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also