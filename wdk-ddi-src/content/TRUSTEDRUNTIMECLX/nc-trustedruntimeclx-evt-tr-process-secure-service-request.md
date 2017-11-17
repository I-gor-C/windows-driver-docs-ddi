---
UID: NC.trustedruntimeclx.EVT_TR_PROCESS_SECURE_SERVICE_REQUEST
title: EVT_TR_PROCESS_SECURE_SERVICE_REQUEST
author: windows-driver-content
description: 
ms.assetid: 376f4eca-dbc1-4474-9dfa-fa316b465a06
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

# EVT_TR_PROCESS_SECURE_SERVICE_REQUEST callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

EVT_TR_PROCESS_SECURE_SERVICE_REQUEST EvtTrProcessSecureServiceRequest; 

// Definition

NTSTATUS EvtTrProcessSecureServiceRequest 
(
	WDFDEVICE ServiceDevice
	WDFOBJECT SessionContext
	PVOID RequestHandle
	KPRIORITY Priority
	PTR_SERVICE_REQUEST Request
	ULONG Flags
	PULONG_PTR BytesWritten
	PVOID * RequestContext
)
{...}

EVT_TR_PROCESS_SECURE_SERVICE_REQUEST PFN_TR_PROCESS_SECURE_SERVICE_REQUEST


```

## -parameters

### -param ServiceDevice: 
### -param SessionContext: 
### -param RequestHandle: 
### -param Priority: 
### -param Request: 
### -param Flags: 
### -param BytesWritten: 
### -param RequestContext: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also