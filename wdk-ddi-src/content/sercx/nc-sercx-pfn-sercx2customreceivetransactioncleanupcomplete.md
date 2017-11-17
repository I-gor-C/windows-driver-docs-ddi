---
UID: NC.sercx.PFN_SERCX2CUSTOMRECEIVETRANSACTIONCLEANUPCOMPLETE
title: PFN_SERCX2CUSTOMRECEIVETRANSACTIONCLEANUPCOMPLETE
author: windows-driver-content
description: 
ms.assetid: 24b38198-e452-40bb-bd66-c8211590382d
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

# PFN_SERCX2CUSTOMRECEIVETRANSACTIONCLEANUPCOMPLETE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_SERCX2CUSTOMRECEIVETRANSACTIONCLEANUPCOMPLETE PfnSercx2customreceivetransactioncleanupcomplete; 

// Definition

WDFAPI PfnSercx2customreceivetransactioncleanupcomplete 
(
	PSERCX_DRIVER_GLOBALS DriverGlobals
	SERCX2CUSTOMRECEIVETRANSACTION CustomReceiveTransaction
)
{...}

PFN_SERCX2CUSTOMRECEIVETRANSACTIONCLEANUPCOMPLETE 


```

## -parameters

### -param DriverGlobals: 
### -param CustomReceiveTransaction: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also