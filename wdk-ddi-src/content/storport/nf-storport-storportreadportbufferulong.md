---
UID: NF:storport.StorPortReadPortBufferUlong
title: StorPortReadPortBufferUlong macro
author: windows-driver-content
description: The StorPortReadPortBufferUlong routine reads a value from a specified port address.
old-location: storage\storportreadportbufferulong.htm
old-project: storage
ms.assetid: 0b7366db-e80f-41f0-9a51-d1c139e948d8
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: StorPortReadPortBufferUlong, StorPortReadPortBufferUlong routine [Storage Devices], storage.storportreadportbufferulong, storport/StorPortReadPortBufferUlong, storprt_175251c9-5c08-4f49-9b3d-a7376c04a0a7.xml
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
-	StorPortReadPortBufferUlong
product: Windows
targetos: Windows
req.typenames: STOR_SPINLOCK
req.product: Windows 10 or later.
---


# StorPortReadPortBufferUlong function
The <b>StorPortReadPortBufferUlong</b> routine reads a value from a specified port address.

## Syntax

````
STORPORT_API VOID StorPortReadPortBufferUlong(
  _In_ PVOID  HwDeviceExtension,
  _In_ PULONG Port,
  _In_ PULONG Buffer,
  _In_ ULONG  Count
);
````

## Parameters

`h`

TBD

`p`

TBD

`b`

TBD

`c`

TBD


## Return Value

None

## Remarks

For more information, see the <a href="..\storport\nf-storport-scsiportreadportbufferulong.md">ScsiPortReadPortBufferUlong</a> routine. For a nonbuffered version of this routine, see <a href="..\storport\nf-storport-storportreadportulong.md">StorPortReadPortUlong</a>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Universal |
| **Header** | storport.h (include Storport.h) |
| **Library** | Storport.lib |

## See Also

<a href="..\storport\nf-storport-scsiportreadportbufferulong.md">ScsiPortReadPortBufferUlong</a>



<a href="..\storport\nf-storport-storportreadportulong.md">StorPortReadPortUlong</a>