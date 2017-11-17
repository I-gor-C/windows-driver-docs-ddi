---
UID: NC.trustedruntimeclx.EVT_TR_ENUMERATE_SECURE_SERVICES
title: EVT_TR_ENUMERATE_SECURE_SERVICES
author: windows-driver-content
description: 
ms.assetid: c3f67ed4-afd4-4749-b380-19da90bebc86
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

# EVT_TR_ENUMERATE_SECURE_SERVICES callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

EVT_TR_ENUMERATE_SECURE_SERVICES EvtTrEnumerateSecureServices; 

// Definition

NTSTATUS EvtTrEnumerateSecureServices 
(
	WDFDEVICE MasterDevice
	ULONG Index
	PUCHAR SecureServiceDescription
	ULONG * DescriptionSize
)
{...}

EVT_TR_ENUMERATE_SECURE_SERVICES PFN_TR_ENUMERATE_SECURE_SERVICES


```

## -parameters

### -param MasterDevice: 
### -param Index: 
### -param SecureServiceDescription: 
### -param DescriptionSize: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also