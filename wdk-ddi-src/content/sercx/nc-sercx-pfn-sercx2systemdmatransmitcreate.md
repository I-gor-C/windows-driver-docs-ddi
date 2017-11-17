---
UID: NC.sercx.PFN_SERCX2SYSTEMDMATRANSMITCREATE
title: PFN_SERCX2SYSTEMDMATRANSMITCREATE
author: windows-driver-content
description: 
ms.assetid: 26b689a0-47a3-42d1-9a73-6617ea998748
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: sercx.h
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

# PFN_SERCX2SYSTEMDMATRANSMITCREATE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_SERCX2SYSTEMDMATRANSMITCREATE PfnSercx2systemdmatransmitcreate; 

// Definition

WDFAPI PfnSercx2systemdmatransmitcreate 
(
	PSERCX_DRIVER_GLOBALS DriverGlobals
	WDFDEVICE Device
	PSERCX2_SYSTEM_DMA_TRANSMIT_CONFIG SystemDmaTransmitConfig
	PWDF_OBJECT_ATTRIBUTES Attributes
	SERCX2SYSTEMDMATRANSMIT *SystemDmaTransmit
)
{...}

PFN_SERCX2SYSTEMDMATRANSMITCREATE 


```

## -parameters

### -param DriverGlobals: 
### -param Device: 
### -param SystemDmaTransmitConfig: 
### -param Attributes: 
### -param *SystemDmaTransmit: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also