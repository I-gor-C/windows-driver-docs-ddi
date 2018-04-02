---
UID: NF:storport.StorPortReadPortUchar
title: StorPortReadPortUchar macro
author: windows-driver-content
description: The StorPortReadPortUchar routine reads a value from a specified port address
old-location: storage\storportreadportuchar.htm
old-project: storage
ms.assetid: 6898ca45-e4a2-41ad-a47e-6dfbcc60b00a
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: StorPortReadPortUchar, StorPortReadPortUchar routine [Storage Devices], storage.storportreadportuchar, storport/StorPortReadPortUchar, storprt_de88c383-95ac-4f3e-b02d-aec76132e4c3.xml
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
-	StorPortReadPortUchar
product:
- Windows
targetos: Windows
req.typenames: STOR_SPINLOCK
req.product: Windows 10 or later.
---


# StorPortReadPortUchar function
The <b>StorPortReadPortUchar</b> routine reads a value from a specified port address

## Syntax

```
void StorPortReadPortUchar(
   h,
   p
);
```

## Parameters

`h`

TBD

`p`

TBD


## Return Value

None

## Remarks

For more information, see the <a href="https://msdn.microsoft.com/library/windows/hardware/ff564715">ScsiPortReadPortBufferUchar</a> routine. For a buffered version of this routine, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff567468">StorPortReadPortBufferUchar</a>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Universal |
| **Header** | storport.h (include Storport.h) |
| **Library** | Storport.lib |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff564715">ScsiPortReadPortBufferUchar</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff567468">StorPortReadPortBufferUchar</a>