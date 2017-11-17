---
UID: NC.wdm.PFN_RTL_IS_NTDDI_VERSION_AVAILABLE
title: PFN_RTL_IS_NTDDI_VERSION_AVAILABLE
author: windows-driver-content
description: 
ms.assetid: fee74316-0fdb-4950-a43d-23d06f6e96fe
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

# PFN_RTL_IS_NTDDI_VERSION_AVAILABLE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_RTL_IS_NTDDI_VERSION_AVAILABLE PfnRtlIsNtddiVersionAvailable; 

// Definition

BOOLEAN PfnRtlIsNtddiVersionAvailable 
(
	ULONG Version
)
{...}

PFN_RTL_IS_NTDDI_VERSION_AVAILABLE 


```

## -parameters

### -param Version: 



## -returns

Returns BOOLEAN that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also