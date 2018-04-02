---
UID: NF:wdfdriver.WdfGetDriver
title: WdfGetDriver function
author: windows-driver-content
description: The WdfGetDriver method returns a handle to the framework driver object that represents the calling driver.
old-location: wdf\wdfgetdriver.htm
old-project: wdf
ms.assetid: 423d4407-9e30-4625-bbe8-5465af29cfaa
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: DFDriverObjectRef_7419a365-e5ee-49cd-8d85-4db65cd27645.xml, WdfGetDriver, WdfGetDriver method, kmdf.wdfgetdriver, wdf.wdfgetdriver, wdfdriver/WdfGetDriver
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdfdriver.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 2.0
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Wdf01000.sys (KMDF); WUDFx02000.dll (UMDF)
req.dll: 
req.irql: Any level
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	LibDef
api_location:
-	Wdf01000.sys
-	Wdf01000.sys.dll
-	WUDFx02000.dll
-	WUDFx02000.dll.dll
api_name:
-	WdfGetDriver
product:
- Windows
targetos: Windows
req.typenames: WDF_DRIVER_INIT_FLAGS
req.product: Windows 10 or later.
---


# WdfGetDriver function
<p class="CCE_Message">[Applies to KMDF and UMDF]

The <b>WdfGetDriver</b> method returns a handle to the framework driver object that represents the calling driver.

## Syntax

```
WDFDRIVER WdfGetDriver(

);
```

## Parameters

This function has no parameters.

## Return Value

<b>WdfGetDriver</b> returns a handle to a framework driver object, or <b>NULL</b> if the driver has not called <a href="https://msdn.microsoft.com/library/windows/hardware/ff547175">WdfDriverCreate</a>.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Universal |
| **Minimum KMDF version** | 1.0 |
| **Minimum UMDF version** | 2.0 |
| **Header** | wdfdriver.h (include Wdf.h) |
| **Library** | Wdf01000.sys (KMDF); WUDFx02000.dll (UMDF) |
| **IRQL** | Any level |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff547175">WdfDriverCreate</a>