---
UID: NC.wdfusb.PFN_WDFUSBTARGETDEVICEFORMATREQUESTFORCONTROLTRANSFER
title: PFN_WDFUSBTARGETDEVICEFORMATREQUESTFORCONTROLTRANSFER
author: windows-driver-content
description: 
ms.assetid: 26063047-0161-41b2-bb14-bdb5dc159293
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

# PFN_WDFUSBTARGETDEVICEFORMATREQUESTFORCONTROLTRANSFER callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFUSBTARGETDEVICEFORMATREQUESTFORCONTROLTRANSFER PfnWdfusbtargetdeviceformatrequestforcontroltransfer; 

// Definition

WDFAPI PfnWdfusbtargetdeviceformatrequestforcontroltransfer 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFUSBDEVICE UsbDevice
	WDFREQUEST Request
	PWDF_USB_CONTROL_SETUP_PACKET SetupPacket
	WDFMEMORY TransferMemory
	PWDFMEMORY_OFFSET TransferOffset
)
{...}

PFN_WDFUSBTARGETDEVICEFORMATREQUESTFORCONTROLTRANSFER 


```

## -parameters

### -param DriverGlobals: 
### -param UsbDevice: 
### -param Request: 
### -param SetupPacket: 
### -param TransferMemory: 
### -param TransferOffset: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also