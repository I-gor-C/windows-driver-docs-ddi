---
UID: NC.1394.PBUS_BUS_RESET_NOTIFICATION
title: PBUS_BUS_RESET_NOTIFICATION
author: windows-driver-content
description: 
ms.assetid: db514a7b-ba35-4832-a9e0-5c23ea31d8b1
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: 1394.h
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

# PBUS_BUS_RESET_NOTIFICATION callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PBUS_BUS_RESET_NOTIFICATION PbusBusResetNotification; 

// Definition

void PbusBusResetNotification 
(
	PVOID Context
)
{...}

PBUS_BUS_RESET_NOTIFICATION 


```

## -parameters

### -param Context: 



## -returns

Returns void that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also