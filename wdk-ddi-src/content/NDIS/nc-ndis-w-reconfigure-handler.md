---
UID: NC.ndis.W_RECONFIGURE_HANDLER
title: W_RECONFIGURE_HANDLER
author: windows-driver-content
description: 
ms.assetid: d9439e67-228f-4cac-8c53-e94e5b6caff4
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

# W_RECONFIGURE_HANDLER callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

W_RECONFIGURE_HANDLER WReconfigureHandler; 

// Definition

NDIS_STATUS WReconfigureHandler 
(
	PNDIS_STATUS OpenErrorStatus
	NDIS_HANDLE MiniportAdapterContext
	NDIS_HANDLE WrapperConfigurationContext
)
{...}

W_RECONFIGURE_HANDLER 


```

## -parameters

### -param OpenErrorStatus: 
### -param MiniportAdapterContext: 
### -param WrapperConfigurationContext: 



## -returns

Returns NDIS_STATUS that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also