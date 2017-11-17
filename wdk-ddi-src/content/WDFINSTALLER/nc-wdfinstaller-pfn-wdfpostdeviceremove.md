---
UID: NC.wdfinstaller.PFN_WDFPOSTDEVICEREMOVE
title: PFN_WDFPOSTDEVICEREMOVE
author: windows-driver-content
description: 
ms.assetid: c20e08d4-1b9d-4e13-8ee8-cbf962026da8
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdfinstaller.h
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

# PFN_WDFPOSTDEVICEREMOVE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFPOSTDEVICEREMOVE PfnWdfpostdeviceremove; 

// Definition

ULONG PfnWdfpostdeviceremove 
(
	LPCWSTR InfPath
	LPCWSTR InfSectionName
)
{...}

PFN_WDFPOSTDEVICEREMOVE 


```

## -parameters

### -param InfPath: 
### -param InfSectionName: 



## -returns

Returns ULONG that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also