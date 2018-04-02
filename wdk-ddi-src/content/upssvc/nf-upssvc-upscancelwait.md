---
UID: NF:upssvc.UPSCancelWait
title: UPSCancelWait function
author: windows-driver-content
description: The UPSCancelWait function cancels all waits initiated by calls to UPSWaitForStateChange.
old-location: battery\upscancelwait.htm
old-project: battery
ms.assetid: 8ac611fc-5634-4857-8533-6e170fe884b2
ms.author: windowsdriverdev
ms.date: 2/15/2018
ms.keywords: UPSCancelWait, UPSCancelWait function [Battery Devices], UPS_fns_79aba7aa-4204-4532-873a-8566ed6168f8.xml, battery.upscancelwait, upssvc/UPSCancelWait
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: upssvc.h
req.include-header: Upssvc.h
req.target-type: Desktop
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
req.lib: 
req.dll: 
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	Upssvc.h
api_name:
-	UPSCancelWait
product: Windows
targetos: Windows
req.typenames: UMDETW_ALLOCATION_USAGE
req.product: Windows 10 or later.
---


# UPSCancelWait function
The <b>UPSCancelWait</b> function cancels all waits initiated by calls to <a href="https://msdn.microsoft.com/library/windows/hardware/ff536316">UPSWaitForStateChange</a>.

## Syntax

```
void UPSCancelWait(

);
```

## Parameters

This function has no parameters.

## Return Value

None

## Remarks

The call returns immediately.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Desktop |
| **Header** | upssvc.h (include Upssvc.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff536316">UPSWaitForStateChange</a>