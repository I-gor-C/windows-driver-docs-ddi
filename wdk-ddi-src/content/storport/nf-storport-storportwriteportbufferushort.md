---
UID: NF:storport.StorPortWritePortBufferUshort
title: StorPortWritePortBufferUshort macro
author: windows-driver-content
description: The StorPortWritePortBufferUshort routine writes a value to a specified register address.
old-location: storage\storportwriteportbufferushort.htm
old-project: storage
ms.assetid: e7b7718b-0c03-4114-8402-9657c49230ad
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: StorPortWritePortBufferUshort, StorPortWritePortBufferUshort routine [Storage Devices], storage.storportwriteportbufferushort, storport/StorPortWritePortBufferUshort, storprt_831acb6e-3529-4e20-897d-e2765b6f7f53.xml
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
-	StorPortWritePortBufferUshort
product:
- Windows
targetos: Windows
req.typenames: STOR_SPINLOCK
req.product: Windows 10 or later.
---


# StorPortWritePortBufferUshort function
The <b>StorPortWritePortBufferUshort</b> routine writes a value to a specified register address.

## Syntax

```
void StorPortWritePortBufferUshort(
   h,
   p,
   b,
   c
);
```

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

For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff564826">ScsiPortWritePortBufferUshort</a>. For a non-buffered equivalent of this routine, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff567527">StorPortWritePortUshort</a>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Universal |
| **Header** | storport.h (include Storport.h) |
| **Library** | Storport.lib |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff564826">ScsiPortWritePortBufferUshort</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff567527">StorPortWritePortUshort</a>