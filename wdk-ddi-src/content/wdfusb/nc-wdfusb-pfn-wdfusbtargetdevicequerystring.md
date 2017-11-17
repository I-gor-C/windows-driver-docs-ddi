---
UID: NC.wdfusb.PFN_WDFUSBTARGETDEVICEQUERYSTRING
title: PFN_WDFUSBTARGETDEVICEQUERYSTRING
author: windows-driver-content
description: 
ms.assetid: c44ed44a-b1ab-463e-9edd-24cdb38a9518
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdfusb.h
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

# PFN_WDFUSBTARGETDEVICEQUERYSTRING callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFUSBTARGETDEVICEQUERYSTRING PfnWdfusbtargetdevicequerystring; 

// Definition

WDFAPI PfnWdfusbtargetdevicequerystring 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFUSBDEVICE UsbDevice
	WDFREQUEST Request
	PWDF_REQUEST_SEND_OPTIONS RequestOptions
	PUSHORT String
	PUSHORT NumCharacters
	UCHAR StringIndex
	USHORT LangID
)
{...}

PFN_WDFUSBTARGETDEVICEQUERYSTRING 


```

## -parameters

### -param DriverGlobals: 
### -param UsbDevice: 
### -param Request: 
### -param RequestOptions: 
### -param String: 
### -param NumCharacters: 
### -param StringIndex: 
### -param LangID: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also