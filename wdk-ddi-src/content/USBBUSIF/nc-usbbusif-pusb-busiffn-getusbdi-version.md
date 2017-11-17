---
UID: NC.usbbusif.PUSB_BUSIFFN_GETUSBDI_VERSION
title: PUSB_BUSIFFN_GETUSBDI_VERSION
author: windows-driver-content
description: 
ms.assetid: b30b49e4-7d63-457e-8518-79d0f0d1b5a9
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: usbbusif.h
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

# PUSB_BUSIFFN_GETUSBDI_VERSION callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PUSB_BUSIFFN_GETUSBDI_VERSION PusbBusiffnGetusbdiVersion; 

// Definition

VOID PusbBusiffnGetusbdiVersion 
(
	PVOID 
	PUSBD_VERSION_INFORMATION 
	PULONG 
)
{...}

PUSB_BUSIFFN_GETUSBDI_VERSION 


```

## -parameters

### -param : 
### -param : 
### -param : 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also