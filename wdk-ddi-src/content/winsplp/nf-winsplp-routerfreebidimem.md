---
UID: NF:winsplp.RouterFreeBidiMem
title: RouterFreeBidiMem function
author: windows-driver-content
description: RouterFreeBidiMem frees a block of memory that was previously allocated by RouterAllocBidiMem.
old-location: print\routerfreebidimem.htm
old-project: print
ms.assetid: 946b1630-844a-43ac-8c26-fdfa2ee7866a
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: RouterFreeBidiMem, RouterFreeBidiMem function [Print Devices], print.routerfreebidimem, spoolfnc_cc4cfcb8-c020-4112-9774-a2961e8a4ba2.xml, winsplp/RouterFreeBidiMem
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: winsplp.h
req.include-header: Winsplp.h
req.target-type: Desktop
req.target-min-winverclnt: This function is available in Windows XP and later operating systems.
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
req.lib: Spoolss.lib
req.dll: Spoolss.dll
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	DllExport
api_location:
-	Spoolss.dll
api_name:
-	RouterFreeBidiMem
product: Windows
targetos: Windows
req.typenames: NOTIFICATION_CONFIG_FLAGS
req.product: Windows 10 or later.
---


# RouterFreeBidiMem function
<code>RouterFreeBidiMem</code> frees a block of memory that was previously allocated by <a href="..\winsplp\nf-winsplp-routerallocbidimem.md">RouterAllocBidiMem</a>.

## Syntax

````
VOID RouterFreeBidiMem(
  _In_ PVOID pMemPointer
);
````

## Parameters

`pMemPointer`

Pointer to the memory to be freed.


## Return Value

None


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | This function is available in Windows XP and later operating systems.  |
| **Target Platform** | Desktop |
| **Header** | winsplp.h (include Winsplp.h) |
| **Library** | Spoolss.lib |
| **DLL** | Spoolss.dll |

## See Also

<a href="..\winsplp\nf-winsplp-routerallocbidimem.md">RouterAllocBidiMem</a>