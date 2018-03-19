---
UID: NF:storport.StorPortWriteRegisterBufferUlong
title: StorPortWriteRegisterBufferUlong macro
author: windows-driver-content
description: The StorPortWriteRegisterBufferUlong routine transfers a given number of ULONG values from a buffer to the HBA.
old-location: storage\storportwriteregisterbufferulong.htm
old-project: storage
ms.assetid: a610f6c5-6627-406e-9b33-f321c6d55a89
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: StorPortWriteRegisterBufferUlong, StorPortWriteRegisterBufferUlong routine [Storage Devices], storage.storportwriteregisterbufferulong, storport/StorPortWriteRegisterBufferUlong, storprt_f43e38af-b5f2-4727-990c-dc0cb79bbc09.xml
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
-	StorPortWriteRegisterBufferUlong
product: Windows
targetos: Windows
req.typenames: STOR_SPINLOCK
req.product: Windows 10 or later.
---


# StorPortWriteRegisterBufferUlong function
The <b>StorPortWriteRegisterBufferUlong</b> routine transfers a given number of ULONG values from a buffer to the HBA.

## Syntax

````
STORPORT_API VOID StorPortWriteRegisterBufferUlong(
  _In_ PVOID  HwDeviceExtension,
  _In_ PULONG Register,
  _In_ PULONG Buffer,
  _In_ ULONG  Count
);
````

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

<a href="..\storport\nf-storport-storportwriteregisterbufferulong.md">StorPortWriteRegisterBufferUlong</a>