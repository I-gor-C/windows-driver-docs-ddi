---
UID: NF:storport.StorPortReadRegisterBufferUshort
title: StorPortReadRegisterBufferUshort macro
author: windows-driver-content
description: The StorPortReadRegisterBufferUshort routine reads a value from a specified register address.
old-location: storage\storportreadregisterbufferushort.htm
old-project: storage
ms.assetid: 169f1089-ac17-4d4c-b989-018ff087aa39
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: StorPortReadRegisterBufferUshort, StorPortReadRegisterBufferUshort routine [Storage Devices], storage.storportreadregisterbufferushort, storport/StorPortReadRegisterBufferUshort, storprt_9ba740e5-78b0-464d-903c-6bb4c22788fd.xml
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
-	StorPortReadRegisterBufferUshort
product: Windows
targetos: Windows
req.typenames: STOR_SPINLOCK
req.product: Windows 10 or later.
---


# StorPortReadRegisterBufferUshort function
The <b>StorPortReadRegisterBufferUshort</b> routine reads a value from a specified register address.

## Syntax

```
void StorPortReadRegisterBufferUshort(
   h,
   r,
   b,
   c
);
```

## Parameters

`h`

TBD

`r`

TBD

`b`

TBD

`c`

TBD


## Return Value

None

## Remarks

For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff564737">ScsiPortReadRegisterBufferUshort</a>. For a nonbuffered version of this routine, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff567488">StorPortReadRegisterUshort</a>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Universal |
| **Header** | storport.h (include Storport.h) |
| **Library** | Storport.lib |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff564737">ScsiPortReadRegisterBufferUshort</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff567488">StorPortReadRegisterUshort</a>