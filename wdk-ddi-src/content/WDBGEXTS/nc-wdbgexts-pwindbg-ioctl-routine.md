---
UID: NC.wdbgexts.PWINDBG_IOCTL_ROUTINE
title: PWINDBG_IOCTL_ROUTINE
author: windows-driver-content
description: 
ms.assetid: 3a73f425-6dc3-433e-95d5-ef883b831f1c
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdbgexts.h
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

# PWINDBG_IOCTL_ROUTINE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PWINDBG_IOCTL_ROUTINE PwindbgIoctlRoutine; 

// Definition

ULONG PwindbgIoctlRoutine 
(
	USHORT IoctlType
	PVOID lpvData
	ULONG cbSize
)
{...}

PWINDBG_IOCTL_ROUTINE 


```

## -parameters

### -param IoctlType: 
### -param lpvData: 
### -param cbSize: 



## -returns

Returns ULONG that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also