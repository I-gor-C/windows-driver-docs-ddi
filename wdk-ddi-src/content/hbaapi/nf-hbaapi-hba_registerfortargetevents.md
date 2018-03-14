---
UID: NF:hbaapi.HBA_RegisterForTargetEvents
title: HBA_RegisterForTargetEvents function
author: windows-driver-content
description: The HBA_RegisterForTargetEvents routine registers for target events with a specified target or with all targets associated with an adapter.
old-location: storage\hba_registerfortargetevents.htm
old-project: storage
ms.assetid: a06f6757-e125-4f80-9594-a60fa1fef6e4
ms.author: windowsdriverdev
ms.date: 2/26/2018
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

````
HBA_STATUS HBA_API HBA_RegisterForTargetEvents(
   HBA_TARGET_CALLBACK callback,
   void                *userData,
   HBA_HANDLE          handle,
   HBA_WWN             hbaPortWWN,
   HBA_WWN             discoveredPortWWN,
   HBA_CALLBACKHANDLE  *callbackHandle,
   HBA_UINT32          allTargets
);
````

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

<a href="..\hbaapi\nf-hbaapi-hba_openadapter.md">HBA_OpenAdapter</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff557233">HBA_STATUS</a>



<a href="..\hbaapi\nf-hbaapi-hba_removecallback.md">HBA_RemoveCallback</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff557123">HBA_PORT_CALLBACK</a>



 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20HBA_RegisterForTargetEvents routine%20 RELEASE:%20(2/26/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>