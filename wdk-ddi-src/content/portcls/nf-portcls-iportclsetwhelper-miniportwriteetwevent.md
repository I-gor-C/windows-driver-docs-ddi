---
UID: NF:portcls.IPortClsEtwHelper.MiniportWriteEtwEvent
title: IPortClsEtwHelper::MiniportWriteEtwEvent method
author: windows-driver-content
description: The MiniportWriteEtwEvent method is used by an audio miniport driver for providing the information about an Event Tracing for Windows (ETW) event.
old-location: audio\iportclsetwhelper_miniportwriteetwevent.htm
old-project: audio
ms.assetid: 7E0C1140-35AA-424F-8229-21B4F4E1EBDF
ms.author: windowsdriverdev
ms.date: 3/19/2018
ms.keywords: IPortClsEtwHelper, IPortClsEtwHelper interface [Audio Devices], MiniportWriteEtwEvent method, IPortClsEtwHelper::MiniportWriteEtwEvent, MiniportWriteEtwEvent method [Audio Devices], MiniportWriteEtwEvent method [Audio Devices], IPortClsEtwHelper interface, MiniportWriteEtwEvent,IPortClsEtwHelper.MiniportWriteEtwEvent, audio.iportclsetwhelper_miniportwriteetwevent, portcls/IPortClsEtwHelper::MiniportWriteEtwEvent
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: method
req.header: portcls.h
req.include-header: 
req.target-type: Universal
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
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
-	COM
api_location:
-	Portcls.h
api_name:
-	IPortClsEtwHelper.MiniportWriteEtwEvent
product: Windows
targetos: Windows
req.typenames: PC_EXIT_LATENCY, *PPC_EXIT_LATENCY
---


# IPortClsEtwHelper::MiniportWriteEtwEvent method
The <code>MiniportWriteEtwEvent</code> method is used by an audio miniport driver for providing the information about an Event Tracing for Windows (ETW) event.

## Syntax

```
NTSTATUS MiniportWriteEtwEvent(
  EPcMiniportEngineEvent miniportEventType,
  ULONGLONG              pvData1,
  ULONGLONG              pvData2,
  ULONGLONG              ulData3,
  ULONGLONG              ulData4
);
```

## Parameters

`miniportEventType`

An <a href="https://msdn.microsoft.com/library/windows/hardware/dn302036">EPcMiniportEngineEvent</a> enumerated value that provides additional error information for reporting glitching errors.

`pvData1`

Data parameter.

`pvData2`

Data parameter.

`ulData3`

Data parameter.

`ulData4`

Data parameter.


## Return Value

<b>MiniportWriteEtwEvent</b> returns S_OK, if the call was successful. Otherwise, the method returns an appropriate error code.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8 Windows Server 2012 |
| **Target Platform** | Universal |
| **Header** | portcls.h |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/dn302036">EPcMiniportEngineEvent</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/dn265123">IPortClsEtwHelper</a>