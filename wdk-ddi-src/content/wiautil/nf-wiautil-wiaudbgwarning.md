---
UID: NF:wiautil.wiauDbgWarning
title: wiauDbgWarning function
author: windows-driver-content
description: The wiauDbgWarning function logs a warning message.
old-location: image\wiaudbgwarning.htm
old-project: image
ms.assetid: f10f1c28-0bfd-44c5-a0aa-9f9227f775d2
ms.author: windowsdriverdev
ms.date: 2/27/2018
ms.keywords: image.wiaudbgwarning, wiauDbgWarning, wiauDbgWarning function [Imaging Devices], wiauFncs_1248626b-0d4f-445c-855c-9ba477cf306c.xml, wiautil/wiauDbgWarning
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wiautil.h
req.include-header: Wiautil.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows XP and later.
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
req.lib: 
req.dll: 
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	Wiautil.h
api_name:
-	wiauDbgWarning
product: Windows
targetos: Windows
req.typenames: SKIP_AMOUNT
req.product: Windows 10 or later.
---


# wiauDbgWarning function
The <b>wiauDbgWarning</b> function logs a warning message.

## Syntax

```
void wiauDbgWarning(
  LPCSTR fname,
  LPCSTR fmt,
  ...    
);
```

## Parameters

`fname`

Pointer to a string containing the name of the function or method into which the call to <b>wiauDbgWarning</b> is inserted.

`fmt`

TBD

`Arg1`




## Return Value

None


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows XP and later.  |
| **Target Platform** | Desktop |
| **Header** | wiautil.h (include Wiautil.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff549627">wiauDbgDump</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff549633">wiauDbgError</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff549637">wiauDbgErrorHr</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff550161">wiauDbgTrace</a>