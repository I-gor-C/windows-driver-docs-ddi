---
UID: NC.61883.PCIP_NOTIFY_ROUTINE
title: PCIP_NOTIFY_ROUTINE
author: windows-driver-content
description: 
ms.assetid: 4ee2fa83-cde6-4917-a456-1607ce653680
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: 61883.h
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

# PCIP_NOTIFY_ROUTINE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PCIP_NOTIFY_ROUTINE PcipNotifyRoutine; 

// Definition

ULONG PcipNotifyRoutine 
(
	PCIP_NOTIFY_INFO NotifyInfo
)
{...}

PCIP_NOTIFY_ROUTINE 


```

## -parameters

### -param NotifyInfo: 



## -returns

Returns ULONG that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also