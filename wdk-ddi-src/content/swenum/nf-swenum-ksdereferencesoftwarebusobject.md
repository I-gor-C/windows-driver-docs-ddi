---
UID: NF:swenum.KsDereferenceSoftwareBusObject
title: KsDereferenceSoftwareBusObject function
author: windows-driver-content
description: The KsDereferenceSoftwareBusObject function decrements the reference count of the demand-load bus enumerator object's PDO.
old-location: stream\ksdereferencesoftwarebusobject.htm
old-project: stream
ms.assetid: 11203a5d-1484-4a49-aedc-e11baf22cac9
ms.author: windowsdriverdev
ms.date: 2/23/2018
ms.keywords: KsDereferenceSoftwareBusObject, KsDereferenceSoftwareBusObject function [Streaming Media Devices], ksfunc_e9066001-173a-40e1-a933-2f646a21afad.xml, stream.ksdereferencesoftwarebusobject, swenum/KsDereferenceSoftwareBusObject
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: swenum.h
req.include-header: Swenum.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ks.lib
req.dll: 
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	LibDef
api_location:
-	Ks.lib
-	Ks.dll
api_name:
-	KsDereferenceSoftwareBusObject
product: Windows
targetos: Windows
req.typenames: STREAM_TIME_REFERENCE, *PSTREAM_TIME_REFERENCE
req.product: Windows 10 or later.
---


# KsDereferenceSoftwareBusObject function
<i>This function is intended for internal use only.</i>

The <b>KsDereferenceSoftwareBusObject</b> function decrements the reference count of the demand-load bus enumerator object's PDO.

## Syntax

```
KSDDKAPI VOID KsDereferenceSoftwareBusObject(
  KSDEVICE_HEADER Header
);
```

## Parameters

`Header`

Pointer to the device header (extension) of the demand-load bus enumerator.


## Return Value

None

## Remarks

A minidriver can access this function through the <b>DereferenceDeviceObject</b> member of the BUS_INTERFACE_SWENUM structure.

When the demand-load bus enumerator object's PDO reference count is 0, it becomes eligible for removal. Note that this condition does not guarantee removal.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Universal |
| **Header** | swenum.h (include Swenum.h) |
| **Library** | Ks.lib |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff557589">BUS_INTERFACE_SWENUM</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff566749">KsQuerySoftwareBusInterface</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff566763">KsReferenceSoftwareBusObject</a>