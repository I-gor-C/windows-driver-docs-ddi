---
UID: NF:storport.StorPortWritePortBufferUchar
title: StorPortWritePortBufferUchar macro
author: windows-driver-content
description: The StorPortWritePortBufferUchar routine writes a value to a specified register address.
old-location: storage\storportwriteportbufferuchar.htm
old-project: storage
ms.assetid: 44b57aa2-37ef-4491-8a88-9e7f880f5c1b
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: StorPortWritePortBufferUchar, StorPortWritePortBufferUchar routine [Storage Devices], storage.storportwriteportbufferuchar, storport/StorPortWritePortBufferUchar, storprt_5bdd38fc-5cb0-483e-a0aa-19179c7ad833.xml
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
-	StorPortWritePortBufferUchar
product: Windows
targetos: Windows
req.typenames: STOR_SPINLOCK
req.product: Windows 10 or later.
---


# StorPortWritePortBufferUchar function
The <b>StorPortWritePortBufferUchar</b> routine writes a value to a specified register address.

## Syntax

```
void StorPortWritePortBufferUchar(
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

For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff564817">ScsiPortWritePortBufferUchar</a>. For a nonbuffered equivalent of this routine, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff567522">StorPortWritePortUchar</a>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Universal |
| **Header** | storport.h (include Storport.h) |
| **Library** | Storport.lib |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff564817">ScsiPortWritePortBufferUchar</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff567522">StorPortWritePortUchar</a>