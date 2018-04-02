---
UID: NF:wiautil.wiauDbgLegacyError
title: wiauDbgLegacyError function
author: windows-driver-content
description: The wiauDbgLegacyError function logs an error message.
old-location: image\wiaudbglegacyerror.htm
old-project: image
ms.assetid: c2a9bd35-ce3a-4640-9982-b470e98b4692
ms.author: windowsdriverdev
ms.date: 2/27/2018
ms.keywords: image.wiaudbglegacyerror, wiauDbgLegacyError, wiauDbgLegacyError function [Imaging Devices], wiauFncs_03e81269-0a09-42c4-8d0d-1f808e6ef69e.xml, wiautil/wiauDbgLegacyError
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
-	wiauDbgLegacyError
product:
- Windows
targetos: Windows
req.typenames: SKIP_AMOUNT
req.product: Windows 10 or later.
---


# wiauDbgLegacyError function
The <b>wiauDbgLegacyError</b> function logs an error message.

## Syntax

```
void wiauDbgLegacyError(
  LPCSTR fmt,
  ...    
);
```

## Parameters

`fmt`

TBD

`Arg1`




## Return Value

None

## Remarks

The <b>wiauDbgLegacyError</b> function is identical to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff549633">wiauDbgError</a> function except that the latter function has an additional parameter used to identify the function or method that is active when the function is called.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows XP and later.  |
| **Target Platform** | Desktop |
| **Header** | wiautil.h (include Wiautil.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff549633">wiauDbgError</a>