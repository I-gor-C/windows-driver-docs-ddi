---
UID: NC.wdm.POWER_SETTING_CALLBACK
title: POWER_SETTING_CALLBACK
author: windows-driver-content
description: 
ms.assetid: 88210e49-238b-4c85-968b-efaa477d6770
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

# POWER_SETTING_CALLBACK callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

POWER_SETTING_CALLBACK PowerSettingCallback; 

// Definition

_IRQL_requires_same_ NTSTATUS PowerSettingCallback 
(
	LPCGUID SettingGuid
	PVOID Value
	ULONG ValueLength
	PVOID Context
)
{...}

POWER_SETTING_CALLBACK PPOWER_SETTING_CALLBACK


```

## -parameters

### -param SettingGuid: 
### -param Value: 
### -param ValueLength: 
### -param Context: 



## -returns

Returns _IRQL_requires_same_ NTSTATUS that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also