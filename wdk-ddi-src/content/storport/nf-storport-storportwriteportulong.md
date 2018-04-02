---
UID: NF:storport.StorPortWritePortUlong
title: StorPortWritePortUlong macro
author: windows-driver-content
description: The StorPortWritePortUlong routine writes a value to a specified register address.
old-location: storage\storportwriteportulong.htm
old-project: storage
ms.assetid: 7c6d61c6-40e5-46fd-8c18-1f9d89c58515
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: StorPortWritePortUlong, StorPortWritePortUlong routine [Storage Devices], storage.storportwriteportulong, storport/StorPortWritePortUlong, storprt_4f568f62-adb7-4176-9229-e2af5d4453cb.xml
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
-	StorPortWritePortUlong
product:
- Windows
targetos: Windows
req.typenames: STOR_SPINLOCK
req.product: Windows 10 or later.
---


# StorPortWritePortUlong function
The <b>StorPortWritePortUlong</b> routine writes a value to a specified register address.

## Syntax

```
void StorPortWritePortUlong(
   h,
   p,
   v
);
```

## Parameters

`h`

TBD

`p`

TBD

`v`

TBD


## Return Value

None

## Remarks

For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff564837">ScsiPortWritePortUlong</a>. For a buffered equivalent of this routine, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff567517">StorPortWritePortBufferUlong</a>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Universal |
| **Header** | storport.h (include Storport.h) |
| **Library** | Storport.lib |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff564837">ScsiPortWritePortUlong</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff567517">StorPortWritePortBufferUlong</a>