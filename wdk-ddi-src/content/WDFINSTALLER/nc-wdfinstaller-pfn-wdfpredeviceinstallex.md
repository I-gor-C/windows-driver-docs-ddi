---
UID: NC.wdfinstaller.PFN_WDFPREDEVICEINSTALLEX
title: PFN_WDFPREDEVICEINSTALLEX
author: windows-driver-content
description: 
ms.assetid: d05efba8-1888-4cfe-ad84-fa20889c8362
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

# PFN_WDFPREDEVICEINSTALLEX callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFPREDEVICEINSTALLEX PfnWdfpredeviceinstallex; 

// Definition

ULONG PfnWdfpredeviceinstallex 
(
	LPCWSTR InfPath
	LPCWSTR InfSectionName
	PWDF_COINSTALLER_INSTALL_OPTIONS ClientOptions
)
{...}

PFN_WDFPREDEVICEINSTALLEX 


```

## -parameters

### -param InfPath: 
### -param InfSectionName: 
### -param ClientOptions: 



## -returns

Returns ULONG that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also