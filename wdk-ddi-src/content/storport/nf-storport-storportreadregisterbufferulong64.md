---
UID: NF:storport.StorPortReadRegisterBufferUlong64
title: StorPortReadRegisterBufferUlong64 macro
author: windows-driver-content
description: This StorPortReadRegisterBufferUlong64 routine reads a number of ULONG64 values from the specified 64-bit register address into a buffer.
old-location: storage\storportreadregisterbufferulong64.htm
old-project: storage
ms.assetid: 585EE323-99EC-4367-8D97-CB554D695C11
ms.author: windowsdriverdev
ms.date: 2/24/2018
ms.keywords: StorPortReadRegisterBufferUlong64, StorPortReadRegisterBufferUlong64 routine [Storage Devices], storage.storportreadregisterbufferulong64, storport/StorPortReadRegisterBufferUlong64
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: macro
req.header: storport.h
req.include-header: Storport.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 8.
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
req.lib: storport.h
req.dll: 
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	storport.h
api_name:
-	StorPortReadRegisterBufferUlong64
product: Windows
targetos: Windows
req.typenames: STOR_SPINLOCK
req.product: Windows 10 or later.
---


# StorPortReadRegisterBufferUlong64 function
This <b>StorPortReadRegisterBufferUlong64</b> routine reads a number of <b>ULONG64</b> values from the specified 64-bit register address into a buffer.

## Syntax

````
 VOID StorPortReadRegisterBufferUlong64(
  _In_  PULONG64  Register,
  _Out_ PULONG64  Buffer,
  _In_  ULONG     Count
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

## Remarks

The <b>StorPortReadRegisterBufferUlong64</b> routine is only available on the 64-bit version of Windows.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available starting with Windows 8.  |
| **Target Platform** | Universal |
| **Header** | storport.h (include Storport.h) |
| **Library** | storport.h |

## See Also

<a href="..\storport\nf-storport-storportwriteregisterbufferulong64.md">StorPortWriteRegisterBufferUlong64</a>



 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20StorPortReadRegisterBufferUlong64 routine%20 RELEASE:%20(2/24/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>