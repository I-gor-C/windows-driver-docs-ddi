---
UID: NC.ndis.W_INITIALIZE_HANDLER
title: W_INITIALIZE_HANDLER
author: windows-driver-content
description: 
ms.assetid: d3e77bb0-feb4-48fe-ac3d-96086e9c3901
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

# W_INITIALIZE_HANDLER callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

W_INITIALIZE_HANDLER WInitializeHandler; 

// Definition

NDIS_STATUS WInitializeHandler 
(
	PNDIS_STATUS OpenErrorStatus
	PUINT SelectedMediumIndex
	PNDIS_MEDIUM MediumArray
	UINT MediumArraySize
	NDIS_HANDLE MiniportAdapterContext
	NDIS_HANDLE WrapperConfigurationContext
)
{...}

W_INITIALIZE_HANDLER 


```

## -parameters

### -param OpenErrorStatus: 
### -param SelectedMediumIndex: 
### -param MediumArray: 
### -param MediumArraySize: 
### -param MiniportAdapterContext: 
### -param WrapperConfigurationContext: 



## -returns

Returns NDIS_STATUS that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also