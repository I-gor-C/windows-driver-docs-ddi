---
UID: NF:storport.StorPortWriteRegisterUlong
title: StorPortWriteRegisterUlong macro
author: windows-driver-content
description: The StorPortWriteRegisterUlong routine transfers a ULONG value to the indicated HBA register address.
old-location: storage\storportwriteregisterulong.htm
old-project: storage
ms.assetid: 12ed5f88-26af-43a4-82c7-5f36d9388cc8
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: StorPortWriteRegisterUlong, StorPortWriteRegisterUlong routine [Storage Devices], storage.storportwriteregisterulong, storport/StorPortWriteRegisterUlong, storprt_64890de0-32e7-4e07-bcbc-35a11acd6896.xml
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
-	StorPortWriteRegisterUlong
product: Windows
targetos: Windows
req.typenames: STOR_SPINLOCK
req.product: Windows 10 or later.
---


# StorPortWriteRegisterUlong function
The <b>StorPortWriteRegisterUlong</b> routine transfers a ULONG value to the indicated HBA register address.

## Syntax

```
void StorPortWriteRegisterUlong(
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

<a href="https://msdn.microsoft.com/library/windows/hardware/ff564870">ScsiPortWriteRegisterUlong</a>