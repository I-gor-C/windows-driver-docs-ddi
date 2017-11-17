---
UID: NC.wdm.POB_PRE_OPERATION_CALLBACK
title: POB_PRE_OPERATION_CALLBACK
author: windows-driver-content
description: 
ms.assetid: 65c1319c-15bd-4410-bfea-e048e08f56cb
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdm.h
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

# POB_PRE_OPERATION_CALLBACK callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

POB_PRE_OPERATION_CALLBACK PobPreOperationCallback; 

// Definition

OB_PREOP_CALLBACK_STATUS PobPreOperationCallback 
(
	PVOID RegistrationContext
	POB_PRE_OPERATION_INFORMATION OperationInformation
)
{...}

POB_PRE_OPERATION_CALLBACK 


```

## -parameters

### -param RegistrationContext: 
### -param OperationInformation: 



## -returns

Returns OB_PREOP_CALLBACK_STATUS that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also