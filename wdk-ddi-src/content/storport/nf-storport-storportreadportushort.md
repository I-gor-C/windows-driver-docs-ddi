---
UID: NF:storport.StorPortReadPortUshort
title: StorPortReadPortUshort macro
author: windows-driver-content
description: The StorPortReadPortUshort routine reads a value from a specified port address.
old-location: storage\storportreadportushort.htm
old-project: storage
ms.assetid: e5c9e91a-96b7-4774-8bb4-7519968ce072
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: StorPortReadPortUshort, StorPortReadPortUshort routine [Storage Devices], storage.storportreadportushort, storport/StorPortReadPortUshort, storprt_fe44d011-ae82-4255-9df9-c1d8f999fd63.xml
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: macro
req.header: storport.h
req.include-header: Storport.h
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
req.lib: Storport.lib
req.dll: 
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	LibDef
api_location:
-	Storport.lib
-	Storport.dll
api_name:
-	StorPortReadPortUshort
product: Windows
targetos: Windows
req.typenames: STOR_SPINLOCK
req.product: Windows 10 or later.
---


# StorPortReadPortUshort function
The <b>StorPortReadPortUshort</b> routine reads a value from a specified port address.

## Syntax

````
STORPORT_API USHORT StorPortReadPortUshort(
  _In_ PVOID   HwDeviceExtension,
  _In_ PUSHORT Port
);
````

## Parameters

`h`

TBD

`p`

TBD


## Return Value

None

## Remarks

For more information, see <a href="..\storport\nf-storport-scsiportreadportbufferushort.md">ScsiPortReadPortBufferUshort</a>. For a buffered version of this routine, see <a href="..\storport\nf-storport-storportreadportbufferushort.md">StorPortReadPortBufferUshort</a>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Universal |
| **Header** | storport.h (include Storport.h) |
| **Library** | Storport.lib |

## See Also

<a href="..\storport\nf-storport-storportreadportbufferushort.md">StorPortReadPortBufferUshort</a>



<a href="..\storport\nf-storport-scsiportreadportbufferushort.md">ScsiPortReadPortBufferUshort</a>