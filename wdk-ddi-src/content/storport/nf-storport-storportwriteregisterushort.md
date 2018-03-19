---
UID: NF:storport.StorPortWriteRegisterUshort
title: StorPortWriteRegisterUshort macro
author: windows-driver-content
description: The StorPortWriteRegisterUshort routine transfers a ULONG value to the indicated HBA register address.
old-location: storage\storportwriteregisterushort.htm
old-project: storage
ms.assetid: f4beff75-6177-40c7-a62c-6e24bc54ea58
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: StorPortWriteRegisterUshort, StorPortWriteRegisterUshort routine [Storage Devices], storage.storportwriteregisterushort, storport/StorPortWriteRegisterUshort, storprt_f4cd6932-3fd0-435f-87f3-7241a5778073.xml
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
-	StorPortWriteRegisterUshort
product: Windows
targetos: Windows
req.typenames: STOR_SPINLOCK
req.product: Windows 10 or later.
---


# StorPortWriteRegisterUshort function
The <b>StorPortWriteRegisterUshort</b> routine transfers a ULONG value to the indicated HBA register address.

## Syntax

````
STORPORT_API VOID StorPortWriteRegisterUshort(
  _In_ PVOID   HwDeviceExtension,
  _In_ PUSHORT Register,
  _In_ USHORT  Value
);
````

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

<a href="..\storport\nf-storport-scsiportwriteregisterushort.md">ScsiPortWriteRegisterUshort</a>