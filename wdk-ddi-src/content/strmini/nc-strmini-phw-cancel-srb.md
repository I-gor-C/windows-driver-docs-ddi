---
UID: NC.strmini.PHW_CANCEL_SRB
title: PHW_CANCEL_SRB
author: windows-driver-content
description: The class driver calls the minidriver's StrMiniCancelPacket routine to signal that a stream request has been canceled.
old-location: stream\strminicancelpacket.htm
old-project: stream
ms.assetid: e64c00dd-4eef-4e1e-abb0-8263088f6dc6
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: PST_PARAMETER_DATA, ST_PARAMETER_DATA, *PST_PARAMETER_DATA
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: strmini.h
req.include-header: Strmini.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: StrMiniCancelPacket
req.alt-loc: strmini.h
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
req.iface: 
req.product: Windows 10 or later.
---

# PHW_CANCEL_SRB callback



## -description
<p>The class driver calls the minidriver's <i>StrMiniCancelPacket</i> routine to signal that a stream request has been canceled.</p>


## -prototype

````
PHW_CANCEL_SRB StrMiniCancelPacket;

VOID StrMiniCancelPacket(
  _In_ PHW_STREAM_REQUEST_BLOCK pSrb
)
{ ... }
````


## -parameters
<dl>

### -param <i>pSrb</i> [in]

<dd>
<p>Pointer to the stream request that had been canceled.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>The minidriver specifies this routine in the <b>HwCancelPacket</b> member of its <a href="https://msdn.microsoft.com/library/windows/hardware/ff559682">HW_INITIALIZATION_DATA</a> structure. The minidriver passes this structure to the class driver when it registers itself by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff568263">StreamClassRegisterMinidriver</a>.</p>

<p>Minidrivers that rely on the class driver to handle synchronization should, once they have successfully canceled a request, signal to the class driver that they are ready for another request by using <a href="https://msdn.microsoft.com/library/windows/hardware/ff568266">StreamClassStreamNotification</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff568239">StreamClassDeviceNotification</a> with the appropriate <b>ReadyForNext</b><i>Xxx</i><b>Request</b>.</p>

<p>The minidriver specifies this routine in the <b>HwCancelPacket</b> member of its <a href="https://msdn.microsoft.com/library/windows/hardware/ff559682">HW_INITIALIZATION_DATA</a> structure. The minidriver passes this structure to the class driver when it registers itself by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff568263">StreamClassRegisterMinidriver</a>.</p>

<p>Minidrivers that rely on the class driver to handle synchronization should, once they have successfully canceled a request, signal to the class driver that they are ready for another request by using <a href="https://msdn.microsoft.com/library/windows/hardware/ff568266">StreamClassStreamNotification</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff568239">StreamClassDeviceNotification</a> with the appropriate <b>ReadyForNext</b><i>Xxx</i><b>Request</b>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Strmini.h (include Strmini.h)</dt>
</dl>
</td>
</tr>
</table>