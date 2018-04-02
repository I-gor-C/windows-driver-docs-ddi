---
UID: NF:storport.StorPortReadRegisterBufferUchar
title: StorPortReadRegisterBufferUchar macro
author: windows-driver-content
description: The StorPortReadRegisterBufferUchar routine reads a value from a specified register address.
old-location: storage\storportreadregisterbufferuchar.htm
old-project: storage
ms.assetid: f633a967-46b5-4532-b372-b9739f2146a2
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: StorPortReadRegisterBufferUchar, StorPortReadRegisterBufferUchar routine [Storage Devices], storage.storportreadregisterbufferuchar, storport/StorPortReadRegisterBufferUchar, storprt_361bfb77-1197-40cb-81ec-fc198e6454e9.xml
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
-	StorPortReadRegisterBufferUchar
product:
- Windows
targetos: Windows
req.typenames: STOR_SPINLOCK
req.product: Windows 10 or later.
---


# StorPortReadRegisterBufferUchar function
The <b>StorPortReadRegisterBufferUchar</b> routine reads a value from a specified register address.

## Syntax

```
void StorPortReadRegisterBufferUchar(
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

For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff564734">ScsiPortReadRegisterBufferUchar</a>. For a nonbuffered version of this routine, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff567483">StorPortReadRegisterUchar</a>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Universal |
| **Header** | storport.h (include Storport.h) |
| **Library** | Storport.lib |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff564734">ScsiPortReadRegisterBufferUchar</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff567483">StorPortReadRegisterUchar</a>