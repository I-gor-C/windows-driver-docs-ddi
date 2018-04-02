---
UID: NF:storport.StorPortWriteRegisterBufferUshort
title: StorPortWriteRegisterBufferUshort macro
author: windows-driver-content
description: The StorPortWriteRegisterBufferUshort routine transfers a given number of USHORT values from a buffer to the HBA.
old-location: storage\storportwriteregisterbufferushort.htm
old-project: storage
ms.assetid: 13da18b3-682f-485a-9d74-0bbff4254862
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: StorPortWriteRegisterBufferUshort, StorPortWriteRegisterBufferUshort routine [Storage Devices], storage.storportwriteregisterbufferushort, storport/StorPortWriteRegisterBufferUshort, storprt_8b227304-10e5-46fc-93e1-41b1c91068b1.xml
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
-	StorPortWriteRegisterBufferUshort
product:
- Windows
targetos: Windows
req.typenames: STOR_SPINLOCK
req.product: Windows 10 or later.
---


# StorPortWriteRegisterBufferUshort function
The <b>StorPortWriteRegisterBufferUshort</b> routine transfers a given number of USHORT values from a buffer to the HBA.

## Syntax

```
void StorPortWriteRegisterBufferUshort(
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


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Universal |
| **Header** | storport.h (include Storport.h) |
| **Library** | Storport.lib |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff564855">ScsiPortWriteRegisterBufferUshort</a>