---
UID: NC.wdfinstaller.PFN_WDFPOSTDEVICEINSTALL
title: PFN_WDFPOSTDEVICEINSTALL
author: windows-driver-content
description: 
ms.assetid: 11f7cde5-a032-469c-9f3d-88817f5416bd
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

# PFN_WDFPOSTDEVICEINSTALL callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFPOSTDEVICEINSTALL PfnWdfpostdeviceinstall; 

// Definition

ULONG PfnWdfpostdeviceinstall 
(
	LPCWSTR InfPath
	LPCWSTR InfSectionName
)
{...}

PFN_WDFPOSTDEVICEINSTALL 


```

## -parameters

### -param InfPath: 
### -param InfSectionName: 



## -returns

Returns ULONG that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also