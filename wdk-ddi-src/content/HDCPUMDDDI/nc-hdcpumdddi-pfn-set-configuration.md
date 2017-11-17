---
UID: NC.hdcpumdddi.PFN_SET_CONFIGURATION
title: PFN_SET_CONFIGURATION
author: windows-driver-content
description: 
ms.assetid: a77a6b81-da3d-419d-844f-997d8738a77c
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: hdcpumdddi.h
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

# PFN_SET_CONFIGURATION callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_SET_CONFIGURATION PfnSetConfiguration; 

// Definition

VOID PfnSetConfiguration 
(
	PVOID pDriverContext
	UINT uMaxResolutionHorizontal
	UINT uMaxResolutionVertical
	UINT uMaxAudioBitarate
	HDCP_TRANSPORT_TYPE TransportType
	UINT uMaxLocalHdcpVersion
)
{...}

PFN_SET_CONFIGURATION 


```

## -parameters

### -param pDriverContext: 
### -param uMaxResolutionHorizontal: 
### -param uMaxResolutionVertical: 
### -param uMaxAudioBitarate: 
### -param TransportType: 
### -param uMaxLocalHdcpVersion: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also