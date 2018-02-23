---
UID: NF:wiautil.wiauDbgInit
title: wiauDbgInit macro
author: windows-driver-content
description: The wiauDbgInit function initializes WIA debugging.
old-location: image\wiaudbginit.htm
old-project: Image
ms.assetid: a9308d66-c8b0-4e0e-8203-e2b3f91b7e27
ms.author: windowsdriverdev
ms.date: 2/15/2018
ms.keywords: wiautil/wiauDbgInit, wiauFncs_0f18edab-cbf7-4012-85ea-93f101343ecb.xml, wiauDbgInit function [Imaging Devices], image.wiaudbginit, wiauDbgInit
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
req.lib: wiautil.h
req.dll: 
req.irql: 
topictype:
-	APIRef
-	kbSyntax
apitype:
-	HeaderDef
apilocation:
-	wiautil.h
apiname:
-	wiauDbgInit
product: Windows
targetos: Windows
req.typenames: SKIP_AMOUNT
req.product: Windows 10 or later.
---


# wiauDbgInit function
The <b>wiauDbgInit</b> function initializes WIA debugging.

## Syntax

````
void __stdcall wiauDbgInit(
  _In_opt_ HINSTANCE hInstance
);
````

## Parameters

`hInstance`




## Return Value

None

## Remarks

If the <b>wiauDbgInit</b> function not called, all DLLs loaded by a process inherit the debug flags of that process.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows XP and later.  |
| **Target Platform** | Desktop |
| **Header** | wiautil.h (include Wiautil.h) |
| **Library** | wiautil.h |