---
UID: NC.wdfdriver.PFN_WDFWDMDRIVERGETWDFDRIVERHANDLE
title: PFN_WDFWDMDRIVERGETWDFDRIVERHANDLE
author: windows-driver-content
description: 
ms.assetid: d9ae4c4d-dcb4-41e8-84d2-d2021c3b0da9
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdfdriver.h
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

# PFN_WDFWDMDRIVERGETWDFDRIVERHANDLE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFWDMDRIVERGETWDFDRIVERHANDLE PfnWdfwdmdrivergetwdfdriverhandle; 

// Definition

WDFAPI PfnWdfwdmdrivergetwdfdriverhandle 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	PDRIVER_OBJECT DriverObject
)
{...}

PFN_WDFWDMDRIVERGETWDFDRIVERHANDLE 


```

## -parameters

### -param DriverGlobals: 
### -param DriverObject: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also