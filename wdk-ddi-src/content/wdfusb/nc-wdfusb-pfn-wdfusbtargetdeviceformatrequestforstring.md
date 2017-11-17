---
UID: NC.wdfusb.PFN_WDFUSBTARGETDEVICEFORMATREQUESTFORSTRING
title: PFN_WDFUSBTARGETDEVICEFORMATREQUESTFORSTRING
author: windows-driver-content
description: 
ms.assetid: ae419511-6a90-47b4-8104-15db942b6017
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

# PFN_WDFUSBTARGETDEVICEFORMATREQUESTFORSTRING callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFUSBTARGETDEVICEFORMATREQUESTFORSTRING PfnWdfusbtargetdeviceformatrequestforstring; 

// Definition

WDFAPI PfnWdfusbtargetdeviceformatrequestforstring 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFUSBDEVICE UsbDevice
	WDFREQUEST Request
	WDFMEMORY Memory
	PWDFMEMORY_OFFSET Offset
	UCHAR StringIndex
	USHORT LangID
)
{...}

PFN_WDFUSBTARGETDEVICEFORMATREQUESTFORSTRING 


```

## -parameters

### -param DriverGlobals: 
### -param UsbDevice: 
### -param Request: 
### -param Memory: 
### -param Offset: 
### -param StringIndex: 
### -param LangID: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also