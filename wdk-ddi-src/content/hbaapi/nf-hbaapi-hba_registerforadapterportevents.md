---
UID: NF:hbaapi.HBA_RegisterForAdapterPortEvents
title: HBA_RegisterForAdapterPortEvents function
author: windows-driver-content
description: The HBA_RegisterForAdapterPortEvents routine registers the indicated user callback routine to call when a port event occurs.
old-location: storage\hba_registerforadapterportevents.htm
old-project: storage
ms.assetid: 596bfba5-7025-4cdc-b1f9-c8df546f6dac
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: HBA_RegisterForAdapterPortEvents, HBA_RegisterForAdapterPortEvents routine [Storage Devices], fibreHBA_rtns_147e7408-58e4-47bc-8d3f-185c8ee68b83.xml, hbaapi/HBA_RegisterForAdapterPortEvents, storage.hba_registerforadapterportevents
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
-	HBA_RegisterForAdapterPortEvents
product: Windows
targetos: Windows
req.typenames: HBA_WWNTYPE
---


# HBA_RegisterForAdapterPortEvents function
The <b>HBA_RegisterForAdapterPortEvents</b> routine registers the indicated user callback routine to call when a port event occurs.

## Syntax

```
HBA_STATUS HBA_API HBA_RegisterForAdapterPortEvents(
  IN void(* )(void *pData,HBA_WWN PortWWN,HBA_UINT32 eventType,HBA_UINT32 fabricPortID) callback,
  IN void                                                                               *UserData,
  IN HBA_HANDLE                                                                         Handle,
  IN HBA_WWN                                                                            PortWWN,
  OUT HBA_CALLBACKHANDLE                                                                *pCallbackHandle
);
```

## Parameters

`callback`

Pointer to a callback routine of type <a href="https://msdn.microsoft.com/library/windows/hardware/ff557123">HBA_PORT_CALLBACK</a> that is called when an adapter is added to the system.

`UserData`

TBD

`Handle`

TBD

`PortWWN`

Contains a 64-bit worldwide name (WWN) that uniquely identifies the HBA port from which port events are reported. For a discussion of worldwide names, see the T11 committee's <i>Fibre Channel HBA API</i> specification.

`pCallbackHandle`

TBD


## Return Value

The <b>HBA_RegisterForAdapterPortEvents</b> routine returns a value of type <a href="https://msdn.microsoft.com/library/windows/hardware/ff557233">HBA_STATUS</a> that indicates the status of the HBA. In particular, this member should have one of the following values.

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
Returned if the callback routine was successfully registered. 

</td>
</tr>
<tr>
<td width="40%">
<dl>
<dt><b>HBA_STATUS_ERROR_ILLEGAL_WWN</b></dt>
</dl>
</td>
<td width="60%">
Returned if the HBA referenced by <i>handle</i> does not have a port with a name that matches the value in <i>PortWWN</i>.

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

For a list of port events, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff557123">HBA_PORT_CALLBACK</a>.

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