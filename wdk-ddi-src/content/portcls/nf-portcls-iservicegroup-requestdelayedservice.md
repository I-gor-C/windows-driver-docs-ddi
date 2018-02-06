---
UID: NF:portcls.IServiceGroup.RequestDelayedService
title: IServiceGroup::RequestDelayedService method
author: windows-driver-content
description: The RequestDelayedService method requests service after the specified delay.
old-location: audio\iservicegroup_requestdelayedservice.htm
old-project: audio
ms.assetid: 045a6c20-2e4e-4669-953d-f8648bf2d718
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: RequestDelayedService, RequestDelayedService method [Audio Devices], IServiceGroup interface [Audio Devices], RequestDelayedService method, IServiceGroup, audmp-routines_2f9be34c-bff3-46d4-a490-595c8f4311b9.xml, RequestDelayedService method [Audio Devices], IServiceGroup interface, portcls/IServiceGroup::RequestDelayedService, audio.iservicegroup_requestdelayedservice, IServiceGroup::RequestDelayedService
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
req.lib: portcls.h
req.dll: 
req.irql: PASSIVE_LEVEL
topictype:
-	APIRef
-	kbSyntax
apitype:
-	COM
apilocation:
-	portcls.h
apiname:
-	IServiceGroup.RequestDelayedService
product: Windows
targetos: Windows
req.typenames: "*PPC_EXIT_LATENCY, PC_EXIT_LATENCY"
---


# RequestDelayedService method
The <code>RequestDelayedService</code> method requests service after the specified delay.

## Syntax

````
void RequestDelayedService(
  [in] ULONGLONG ulDelay
);
````

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
| **Library** | portcls.h |
| **IRQL** | PASSIVE_LEVEL |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff537004">IServiceGroup::SupportDelayedService</a>

<a href="..\portcls\nn-portcls-iservicegroup.md">IServiceGroup</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [audio\audio]:%20IServiceGroup::RequestDelayedService method%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>