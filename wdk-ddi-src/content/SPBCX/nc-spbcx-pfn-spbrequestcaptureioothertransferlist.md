---
UID: NC.spbcx.PFN_SPBREQUESTCAPTUREIOOTHERTRANSFERLIST
title: PFN_SPBREQUESTCAPTUREIOOTHERTRANSFERLIST
author: windows-driver-content
description: 
ms.assetid: e3aac882-aa0c-460f-b5c3-cda33c35ba31
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: spbcx.h
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

# PFN_SPBREQUESTCAPTUREIOOTHERTRANSFERLIST callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_SPBREQUESTCAPTUREIOOTHERTRANSFERLIST PfnSpbrequestcaptureioothertransferlist; 

// Definition

WDFAPI PfnSpbrequestcaptureioothertransferlist 
(
	PSPB_DRIVER_GLOBALS DriverGlobals
	SPBREQUEST Request
)
{...}

PFN_SPBREQUESTCAPTUREIOOTHERTRANSFERLIST 


```

## -parameters

### -param DriverGlobals: 
### -param Request: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also