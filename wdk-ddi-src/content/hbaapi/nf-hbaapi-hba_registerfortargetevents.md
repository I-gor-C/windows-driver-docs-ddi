---
UID: NF:hbaapi.HBA_RegisterForTargetEvents
title: HBA_RegisterForTargetEvents function
author: windows-driver-content
description: The HBA_RegisterForTargetEvents routine registers for target events with a specified target or with all targets associated with an adapter.
old-location: storage\hba_registerfortargetevents.htm
old-project: storage
ms.assetid: a06f6757-e125-4f80-9594-a60fa1fef6e4
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: HBA_RegisterForTargetEvents, HBA_RegisterForTargetEvents routine [Storage Devices], fibreHBA_rtns_511fff45-f98b-4dbe-a74c-d577497f4e8c.xml, hbaapi/HBA_RegisterForTargetEvents, storage.hba_registerfortargetevents
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: hbaapi.h
req.include-header: Hbaapi.h
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
req.lib: Hbaapi.lib
req.dll: Hbaapi.dll
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	DllExport
api_location:
-	Hbaapi.dll
api_name:
-	HBA_RegisterForTargetEvents
product: Windows
targetos: Windows
req.typenames: HBA_WWNTYPE
---


# HBA_RegisterForTargetEvents function
The <b>HBA_RegisterForTargetEvents</b> routine registers for target events with a specified target or with all targets associated with an adapter.

## Syntax

```
HBA_STATUS HBA_API HBA_RegisterForTargetEvents(
  IN void(* )(void *pData,HBA_WWN hbaPortWWN,HBA_WWN discoveredPortWWN,HBA_UINT32 eventType) callback,
  IN void                                                                                    *pUserData,
  IN HBA_HANDLE                                                                              Handle,
  IN HBA_WWN                                                                                 HbaPortWWN,
  IN HBA_WWN                                                                                 DiscoveredPortWWN,
  OUT HBA_CALLBACKHANDLE                                                                     *pCallbackHandle,
  IN HBA_UINT32                                                                              AllTargets
);
```

## Parameters

`callback`

Pointer to a callback routine of type <a href="https://msdn.microsoft.com/library/windows/hardware/ff557123">HBA_PORT_CALLBACK</a> that is called when an adapter is added to the system.

`pUserData`

TBD

`Handle`

TBD

`HbaPortWWN`

TBD

`DiscoveredPortWWN`

TBD

`pCallbackHandle`

TBD

`AllTargets`

TBD


## Return Value

The <b>HBA_RegisterForTargetEvents</b> routine returns a value of type <a href="https://msdn.microsoft.com/library/windows/hardware/ff557233">HBA_STATUS</a> that indicates the status of the HBA. In particular, <b>HBA_RegisterForTargetEvents</b> returns one of the following values.

<table>
<tr>
<th>Return code</th>
<th>Description</th>
</tr>
<tr>
<td width="40%">
<dl>
<dt><b>HBA_STATUS_OK</b></dt>
</dl>
</td>
<td width="60%">
Returned if the callback registration was successful. 

</td>
</tr>
<tr>
<td width="40%">
<dl>
<dt><b>HBA_STATUS_ERROR_ILLEGAL_WWN</b></dt>
</dl>
</td>
<td width="60%">
Returned if the HBA referenced by <i>handle</i> does not contain a port with a name that matches <i>discoveredPortWWN</i>. 

</td>
</tr>
<tr>
<td width="40%">
<dl>
<dt><b>HBA_STATUS_ERROR</b></dt>
</dl>
</td>
<td width="60%">
Returned if an unspecified error occurred that prevented the registration of the callback routine. 

</td>
</tr>
</table>

## Remarks

To stop event delivery, call <b>HBA_RemoveCallback</b>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Desktop |
| **Header** | hbaapi.h (include Hbaapi.h) |
| **Library** | Hbaapi.lib |
| **DLL** | Hbaapi.dll |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff557097">HBA_OpenAdapter</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff557123">HBA_PORT_CALLBACK</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff557175">HBA_RemoveCallback</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff557233">HBA_STATUS</a>