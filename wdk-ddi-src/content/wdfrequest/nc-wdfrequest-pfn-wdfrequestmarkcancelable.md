---
UID: NC.wdfrequest.PFN_WDFREQUESTMARKCANCELABLE
title: PFN_WDFREQUESTMARKCANCELABLE
author: windows-driver-content
description: 
ms.assetid: 7a88ec42-5b44-455a-96b5-e10d53d7333c
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdfrequest.h
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

# PFN_WDFREQUESTMARKCANCELABLE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFREQUESTMARKCANCELABLE PfnWdfrequestmarkcancelable; 

// Definition

WDFAPI PfnWdfrequestmarkcancelable 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFREQUEST Request
	PFN_WDF_REQUEST_CANCEL EvtRequestCancel
)
{...}

PFN_WDFREQUESTMARKCANCELABLE 


```

## -parameters

### -param DriverGlobals: 
### -param Request: 
### -param EvtRequestCancel: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also