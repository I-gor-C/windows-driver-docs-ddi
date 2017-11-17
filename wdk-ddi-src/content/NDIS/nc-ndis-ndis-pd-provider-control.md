---
UID: NC.ndis.NDIS_PD_PROVIDER_CONTROL
title: NDIS_PD_PROVIDER_CONTROL
author: windows-driver-content
description: 
ms.assetid: 13198800-1870-4db3-bab6-762fb59fc6ad
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: ndis.h
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

# NDIS_PD_PROVIDER_CONTROL callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

NDIS_PD_PROVIDER_CONTROL NdisPdProviderControl; 

// Definition

NTSTATUS() NdisPdProviderControl 
(
	NDIS_PD_PROVIDER_HANDLE ProviderHandle
	NDIS_PD_CONTROL_TYPE ControlType
	NDIS_PD_PROVIDER_CONTROL_CODE ControlCode
	PVOID InBuffer
	ULONG InBufferSize
	PVOID OutBuffer
	ULONG OutBufferSize
	ULONG * BytesReturned
)
{...}

NDIS_PD_PROVIDER_CONTROL NDIS_PD_PROVIDER_CONTROL_HANDLER


```

## -parameters

### -param ProviderHandle: 
### -param ControlType: 
### -param ControlCode: 
### -param InBuffer: 
### -param InBufferSize: 
### -param OutBuffer: 
### -param OutBufferSize: 
### -param BytesReturned: 



## -returns

Returns NTSTATUS() that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also