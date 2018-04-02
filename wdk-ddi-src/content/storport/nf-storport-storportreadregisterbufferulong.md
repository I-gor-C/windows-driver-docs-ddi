---
UID: NF:storport.StorPortReadRegisterBufferUlong
title: StorPortReadRegisterBufferUlong macro
author: windows-driver-content
description: The StorPortReadRegisterBufferUlong routine reads a value from a specified register address.
old-location: storage\storportreadregisterbufferulong.htm
old-project: storage
ms.assetid: 069defee-6295-4492-b0bb-135c476c79aa
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: StorPortReadRegisterBufferUlong, StorPortReadRegisterBufferUlong routine [Storage Devices], storage.storportreadregisterbufferulong, storport/StorPortReadRegisterBufferUlong, storprt_18f8816c-5e0f-4139-829d-d9de65d63529.xml
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
-	StorPortReadRegisterBufferUlong
product: Windows
targetos: Windows
req.typenames: STOR_SPINLOCK
req.product: Windows 10 or later.
---


# StorPortReadRegisterBufferUlong function
The <b>StorPortReadRegisterBufferUlong</b> routine reads a value from a specified register address.

## Syntax

```
void StorPortReadRegisterBufferUlong(
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

For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff564735">ScsiPortReadRegisterBufferUlong</a>. For a nonbuffered version of this routine, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff567485">StorPortReadRegisterUlong</a>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Universal |
| **Header** | storport.h (include Storport.h) |
| **Library** | Storport.lib |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff564735">ScsiPortReadRegisterBufferUlong</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff567485">StorPortReadRegisterUlong</a>