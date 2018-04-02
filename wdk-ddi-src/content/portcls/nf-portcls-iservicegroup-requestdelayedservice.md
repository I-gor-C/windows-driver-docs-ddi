---
UID: NF:portcls.IServiceGroup.RequestDelayedService
title: IServiceGroup::RequestDelayedService method
author: windows-driver-content
description: The RequestDelayedService method requests service after the specified delay.
old-location: audio\iservicegroup_requestdelayedservice.htm
old-project: audio
ms.assetid: 045a6c20-2e4e-4669-953d-f8648bf2d718
ms.author: windowsdriverdev
ms.date: 3/19/2018
ms.keywords: IServiceGroup, IServiceGroup interface [Audio Devices], RequestDelayedService method, IServiceGroup::RequestDelayedService, RequestDelayedService method [Audio Devices], RequestDelayedService method [Audio Devices], IServiceGroup interface, RequestDelayedService,IServiceGroup.RequestDelayedService, audio.iservicegroup_requestdelayedservice, audmp-routines_2f9be34c-bff3-46d4-a490-595c8f4311b9.xml, portcls/IServiceGroup::RequestDelayedService
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: method
req.header: portcls.h
req.include-header: Portcls.h
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
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	COM
api_location:
-	portcls.h
api_name:
-	IServiceGroup.RequestDelayedService
product:
- Windows
targetos: Windows
req.typenames: PC_EXIT_LATENCY, *PPC_EXIT_LATENCY
---


# IServiceGroup::RequestDelayedService method
The <code>RequestDelayedService</code> method requests service after the specified delay.

## Syntax

```
void RequestDelayedService(
  ULONGLONG ullDelay
);
```

## Parameters

`ullDelay`




## Return Value

None

## Remarks

Before calling <code>RequestDelayedService</code> to request a timer delay, initialize the timer by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff537004">IServiceGroup::SupportDelayedService</a>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Universal |
| **Header** | portcls.h (include Portcls.h) |
| **IRQL** | PASSIVE_LEVEL |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff536994">IServiceGroup</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff537004">IServiceGroup::SupportDelayedService</a>