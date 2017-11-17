---
UID: NC.ntddk.PFN_IN_USE_PAGE_OFFLINE_NOTIFY
title: PFN_IN_USE_PAGE_OFFLINE_NOTIFY
author: windows-driver-content
description: 
ms.assetid: 74c79806-b319-4f71-8665-d2ad80424a10
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

# PFN_IN_USE_PAGE_OFFLINE_NOTIFY callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_IN_USE_PAGE_OFFLINE_NOTIFY PfnInUsePageOfflineNotify; 

// Definition

BOOLEAN PfnInUsePageOfflineNotify 
(
	PFN_NUMBER Page
	BOOLEAN PlatformDirected
	BOOLEAN Poisoned
	PVOID Context
)
{...}

PFN_IN_USE_PAGE_OFFLINE_NOTIFY 


```

## -parameters

### -param Page: 
### -param PlatformDirected: 
### -param Poisoned: 
### -param Context: 



## -returns

Returns BOOLEAN that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also