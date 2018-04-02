---
UID: NF:storport.StorPortReadRegisterUshort
title: StorPortReadRegisterUshort macro
author: windows-driver-content
description: The StorPortReadRegisterUshort routine reads a value from a specified register address.
old-location: storage\storportreadregisterushort.htm
old-project: storage
ms.assetid: 11659e7d-db54-401c-a179-75cc5d411b55
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: StorPortReadRegisterUshort, StorPortReadRegisterUshort routine [Storage Devices], storage.storportreadregisterushort, storport/StorPortReadRegisterUshort, storprt_f477688d-54cb-4cb6-b713-0e70cfbf2139.xml
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
-	StorPortReadRegisterUshort
product: Windows
targetos: Windows
req.typenames: STOR_SPINLOCK
req.product: Windows 10 or later.
---


# StorPortReadRegisterUshort function
The <b>StorPortReadRegisterUshort</b> routine reads a value from a specified register address.

## Syntax

```
void StorPortReadRegisterUshort(
   h,
   r
);
```

## Parameters

`h`

TBD

`r`

TBD


## Return Value

None

## Remarks

For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff564744">ScsiPortReadRegisterUshort</a>. For a buffered version of this routine, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff567481">StorPortReadRegisterBufferUshort</a>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Universal |
| **Header** | storport.h (include Storport.h) |
| **Library** | Storport.lib |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff564744">ScsiPortReadRegisterUshort</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff567481">StorPortReadRegisterBufferUshort</a>