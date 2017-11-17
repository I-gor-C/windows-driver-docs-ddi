---
UID: NC.wdfiotarget.PFN_WDFIOTARGETFORMATREQUESTFORINTERNALIOCTLOTHERS
title: PFN_WDFIOTARGETFORMATREQUESTFORINTERNALIOCTLOTHERS
author: windows-driver-content
description: 
ms.assetid: 70b5c676-89d6-48a4-b51a-8190ba3d1f69
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdfiotarget.h
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

# PFN_WDFIOTARGETFORMATREQUESTFORINTERNALIOCTLOTHERS callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFIOTARGETFORMATREQUESTFORINTERNALIOCTLOTHERS PfnWdfiotargetformatrequestforinternalioctlothers; 

// Definition

WDFAPI PfnWdfiotargetformatrequestforinternalioctlothers 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFIOTARGET IoTarget
	WDFREQUEST Request
	ULONG IoctlCode
	WDFMEMORY OtherArg1
	PWDFMEMORY_OFFSET OtherArg1Offset
	WDFMEMORY OtherArg2
	PWDFMEMORY_OFFSET OtherArg2Offset
	WDFMEMORY OtherArg4
	PWDFMEMORY_OFFSET OtherArg4Offset
)
{...}

PFN_WDFIOTARGETFORMATREQUESTFORINTERNALIOCTLOTHERS 


```

## -parameters

### -param DriverGlobals: 
### -param IoTarget: 
### -param Request: 
### -param IoctlCode: 
### -param OtherArg1: 
### -param OtherArg1Offset: 
### -param OtherArg2: 
### -param OtherArg2Offset: 
### -param OtherArg4: 
### -param OtherArg4Offset: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also