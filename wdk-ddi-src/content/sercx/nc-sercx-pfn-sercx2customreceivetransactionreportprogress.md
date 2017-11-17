---
UID: NC.sercx.PFN_SERCX2CUSTOMRECEIVETRANSACTIONREPORTPROGRESS
title: PFN_SERCX2CUSTOMRECEIVETRANSACTIONREPORTPROGRESS
author: windows-driver-content
description: 
ms.assetid: 064861cf-63b6-431d-9b72-ca5d092936c3
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

# PFN_SERCX2CUSTOMRECEIVETRANSACTIONREPORTPROGRESS callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_SERCX2CUSTOMRECEIVETRANSACTIONREPORTPROGRESS PfnSercx2customreceivetransactionreportprogress; 

// Definition

WDFAPI PfnSercx2customreceivetransactionreportprogress 
(
	PSERCX_DRIVER_GLOBALS DriverGlobals
	SERCX2CUSTOMRECEIVETRANSACTION CustomReceiveTransaction
	SERCX2_CUSTOM_RECEIVE_TRANSACTION_PROGRESS Progress
)
{...}

PFN_SERCX2CUSTOMRECEIVETRANSACTIONREPORTPROGRESS 


```

## -parameters

### -param DriverGlobals: 
### -param CustomReceiveTransaction: 
### -param Progress: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also