---
UID: NF:storport.StorPortWriteRegisterUchar
title: StorPortWriteRegisterUchar macro
author: windows-driver-content
description: The StorPortWriteRegisterBufferUshort routine transfers a given number of character values from a buffer to the indicated HBA register address.
old-location: storage\storportwriteregisteruchar.htm
old-project: storage
ms.assetid: 731ae55e-8cfb-4b76-b811-dbdabd8dd067
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: StorPortWriteRegisterUchar, StorPortWriteRegisterUchar routine [Storage Devices], storage.storportwriteregisteruchar, storport/StorPortWriteRegisterUchar, storprt_5c7a4209-e917-4a68-94f7-7b3b3fcc634e.xml
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
-	StorPortWriteRegisterUchar
product:
- Windows
targetos: Windows
req.typenames: STOR_SPINLOCK
req.product: Windows 10 or later.
---


# StorPortWriteRegisterUchar function
The <b>StorPortWriteRegisterBufferUshort</b> routine transfers a given number of character values from a buffer to the indicated HBA register address.

## Syntax

```
void StorPortWriteRegisterUchar(
   h,
   r,
   v
);
```

## Parameters

`h`

TBD

`r`

TBD

`v`

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