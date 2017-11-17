---
UID: NC.ntddk.pHalReferenceBusHandler
title: pHalReferenceBusHandler
author: windows-driver-content
description: 
ms.assetid: b5bdefa5-b6b9-42a8-a40f-b2aa9b572750
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: ntddk.h
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

# pHalReferenceBusHandler callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

pHalReferenceBusHandler Phalreferencebushandler; 

// Definition

VOID Phalreferencebushandler 
(
	PBUS_HANDLER BusHandler
)
{...}

pHalReferenceBusHandler 


```

## -parameters

### -param BusHandler: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also