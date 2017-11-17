---
UID: NC.1394.PBUS_NOTIFICATION_ROUTINE
title: PBUS_NOTIFICATION_ROUTINE
author: windows-driver-content
description: 
ms.assetid: 385f54f1-cd78-4615-94e6-4d50d174f4cb
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

# PBUS_NOTIFICATION_ROUTINE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PBUS_NOTIFICATION_ROUTINE PbusNotificationRoutine; 

// Definition

void PbusNotificationRoutine 
(
	PNOTIFICATION_INFO NotificationInfo
)
{...}

PBUS_NOTIFICATION_ROUTINE 


```

## -parameters

### -param NotificationInfo: 



## -returns

Returns void that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also