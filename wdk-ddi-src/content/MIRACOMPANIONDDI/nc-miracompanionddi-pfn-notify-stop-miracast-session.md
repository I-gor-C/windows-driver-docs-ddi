---
UID: NC.miracompanionddi.PFN_NOTIFY_STOP_MIRACAST_SESSION
title: PFN_NOTIFY_STOP_MIRACAST_SESSION
author: windows-driver-content
description: 
ms.assetid: df44c761-2203-4318-81e1-286d12d6a8ba
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: miracompanionddi.h
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

# PFN_NOTIFY_STOP_MIRACAST_SESSION callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_NOTIFY_STOP_MIRACAST_SESSION PfnNotifyStopMiracastSession; 

// Definition

HRESULT PfnNotifyStopMiracastSession 
(
	void const *pSessionContext
)
{...}

PFN_NOTIFY_STOP_MIRACAST_SESSION 


```

## -parameters

### -param *pSessionContext: 



## -returns

Returns HRESULT that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also