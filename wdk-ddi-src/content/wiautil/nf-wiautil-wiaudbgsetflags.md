---
UID: NF:wiautil.wiauDbgSetFlags
title: wiauDbgSetFlags macro
author: windows-driver-content
description: The wiauDbgSetFlags function sets debugging flags.
old-location: image\wiaudbgsetflags.htm
old-project: image
ms.assetid: e3b944ef-daa5-412c-ac11-7b08d2b9333b
ms.author: windowsdriverdev
ms.date: 2/27/2018
ms.keywords: image.wiaudbgsetflags, wiauDbgSetFlags, wiauDbgSetFlags function [Imaging Devices], wiauFncs_d0f9a6a3-6958-44cb-9467-7f6413f95ca7.xml, wiautil/wiauDbgSetFlags
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: macro
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
-	wiautil.h
api_name:
-	wiauDbgSetFlags
product: Windows
targetos: Windows
req.typenames: SKIP_AMOUNT
req.product: Windows 10 or later.
---


# wiauDbgSetFlags function
The <b>wiauDbgSetFlags</b> function sets debugging flags.

## Syntax

````
inline DWORD __stdcall wiauDbgSetFlags(
   DWORD flags
);
````

## Parameters

`a`

TBD


## Return Value

None


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows XP and later.  |
| **Target Platform** | Desktop |
| **Header** | wiautil.h (include Wiautil.h) |

## See Also

<a href="..\wiautil\nf-wiautil-wiaudbgflags.md">wiauDbgFlags</a>