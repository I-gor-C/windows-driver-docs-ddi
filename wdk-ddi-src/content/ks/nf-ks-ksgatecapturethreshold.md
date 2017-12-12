---
UID: NF.ks.KsGateCaptureThreshold
title: KsGateCaptureThreshold function
author: windows-driver-content
description: The KsGateCaptureThreshold function is used to capture an ON input of an AND gate specified by Gate.
old-location: stream\ksgatecapturethreshold.htm
old-project: stream
ms.assetid: 24a7745d-28f8-4f5a-9f51-37ad2d0ffa0b
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: KsGateCaptureThreshold
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ks.h
req.include-header: Ks.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Microsoft Windows XP and later operating systems and DirectX 8.0 and later DirectX versions.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KsGateCaptureThreshold
req.alt-loc: ks.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: Any level
---

# KsGateCaptureThreshold function



## -description
The<b> KsGateCaptureThreshold</b> function is used to capture an ON input of an AND gate specified by <i>Gate</i>.



## -syntax

````
BOOLEAN __inline KsGateCaptureThreshold(
  _In_ PKSGATE Gate
);
````


## -parameters

### -param Gate [in]

A pointer to a <a href="stream.ksgate">KSGATE</a> structure representing the AND gate for which to capture an ON input synchronously.


## -returns
<b>KsGateCaptureThreshold</b> returns <b>TRUE</b> if the AND gate was originally open. Note that returning <b>TRUE</b> implies that the gate was closed so that no other thread could simultaneously capture the gate and commence processing.


## -remarks
<b>KsGateCaptureThreshold</b> checks the state of the given AND gate. If the gate is open, it turns off an input to the gate, thereby transitioning the gate to a closed state. If the gate is closed, the function does nothing. Unlike <b>KsGateGetStateUnsafe</b>, this call is done synchronously with respect to other gate state changes. It is the primary synchronization mechanism for processing based on gate control.

Despite its name, this function is only a valid call for AND gates, not gates in general. AVStream, however, does not verify whether <i>Gate</i> is an AND gate or an OR gate. It is the caller's responsibility to ensure that the call is only made on AND gates.

The call is made using interlocked functions and is thus synchronous with respect to any of the other gate state change functions; it is also a very efficient method of process control. 


## -requirements
<table>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Version

</th>
<td width="70%">
Available in Microsoft Windows XP and later operating systems and DirectX 8.0 and later DirectX versions.

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Ks.h (include Ks.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL

</th>
<td width="70%">
Any level

</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="stream.ksgateinitializeand">KsGateInitializeAnd</a>
</dt>
<dt>
<a href="stream.ksgateinitializeor">KsGateInitializeOr</a>
</dt>
<dt>
<a href="stream.ksgategetstateunsafe">KsGateGetStateUnsafe</a>
</dt>
<dt>
<a href="stream.ksgateaddoninputtoand">KsGateAddOnInputToAnd</a>
</dt>
<dt>
<a href="stream.ksgateaddoninputtoor">KsGateAddOnInputToOr</a>
</dt>
<dt>
<a href="stream.ksgateaddoffinputtoand">KsGateAddOffInputToAnd</a>
</dt>
<dt>
<a href="stream.ksgateaddoffinputtoor">KsGateAddOffInputToOr</a>
</dt>
<dt>
<a href="stream.ksgateremoveoninputfromand">KsGateRemoveOnInputFromAnd</a>
</dt>
<dt>
<a href="stream.ksgateremoveoninputfromor">KsGateRemoveOnInputFromOr</a>
</dt>
<dt>
<a href="stream.ksgateremoveoffinputfromand">KsGateRemoveOffInputFromAnd</a>
</dt>
<dt>
<a href="stream.ksgateremoveoffinputfromor">KsGateRemoveOffInputFromOr</a>
</dt>
<dt>
<a href="stream.ksgateturninputon">KsGateTurnInputOn</a>
</dt>
<dt>
<a href="stream.ksgateturninputoff">KsGateTurnInputOff</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KsGateCaptureThreshold function%20 RELEASE:%20(12/6/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

