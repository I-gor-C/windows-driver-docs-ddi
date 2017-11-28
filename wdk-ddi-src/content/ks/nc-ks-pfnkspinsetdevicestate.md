---
UID: NC.ks.PFNKSPINSETDEVICESTATE
title: PFNKSPINSETDEVICESTATE
author: windows-driver-content
description: An AVStream minidriver's AVStrMiniPinSetDeviceState routine is called when the state of a KSPIN structure is changed due to the arrival of a connection state property 'set' IOCTL.
old-location: stream\avstrminipinsetdevicestate.htm
old-project: stream
ms.assetid: df68dda0-6128-46c9-bf2b-562c10f9a6f1
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: NpdBrokerUninitialize
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: ks.h
req.include-header: Ks.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Microsoft Windows XP and later operating systems and DirectX 8.0 and later DirectX versions.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: AVStrMiniPinSetDeviceState
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
req.irql: PASSIVE_LEVEL
req.iface: 
---

# PFNKSPINSETDEVICESTATE callback



## -description
<p>An AVStream minidriver's <i>AVStrMiniPinSetDeviceState</i> routine is called when the state of a <a href="https://msdn.microsoft.com/library/windows/hardware/ff563483">KSPIN</a> structure is changed due to the arrival of a connection state property 'set' IOCTL.  Typically, this will be provided by minidrivers that need to change the state of hardware.</p>


## -prototype

````
PFNKSPINSETDEVICESTATE AVStrMiniPinSetDeviceState;

NTSTATUS AVStrMiniPinSetDeviceState(
  _In_ PKSPIN  Pin,
  _In_ KSSTATE ToState,
  _In_ KSSTATE FromState
)
{ ... }
````


## -parameters
<dl>

### -param <i>Pin</i> [in]

<dd>
<p>Pointer to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff563483">KSPIN</a> structure for which state is changing.</p>
</dd>

### -param <i>ToState</i> [in]

<dd>
<p>The target <a href="https://msdn.microsoft.com/library/windows/hardware/ff566856">KSSTATE</a> after receipt of the IOCTL.</p>
</dd>

### -param <i>FromState</i> [in]

<dd>
<p>The previous <a href="https://msdn.microsoft.com/library/windows/hardware/ff566856">KSSTATE</a>.</p>
</dd>
</dl>

## -returns
<p>Return STATUS_SUCCESS or the error code that was returned from the attempt to set the state. Do not return STATUS_PENDING. The filter control mutex is held during this function. See <a href="NULL">Filter Control Mutex in AVStream</a>.</p>

## -remarks
<p>The minidriver specifies this routine's address in the <b>SetDeviceState</b> member of its <a href="https://msdn.microsoft.com/library/windows/hardware/ff563535">KSPIN_DISPATCH</a> structure.</p>

<p>Minidrivers will not receive a stop upon initial connection of the pin.</p>

<p>Pins that use the standard transport mechanism (standard interface/standard medium or an explicit use of KSPIN_FLAG_USE_STANDARD_TRANSPORT in <a href="https://msdn.microsoft.com/library/windows/hardware/ff563534">KSPIN_DESCRIPTOR_EX</a>) receive filtered state changes through the owning pipe through this routine. This means that no transition will be more than a single step. In other words, <b>KSSTATE_STOP</b> transitions to KSSTATE_ACQUIRE, <b>KSSTATE_ACQUIRE</b> transitions to KSSTATE_PAUSE, and so on. In addition, state changes received in this routine represent the state of the pipe as a whole, not the individual state of the pin as reported in the <b>DeviceState</b> member of the KSPIN structure.</p>

<p>Pins that do not use the standard transport mechanism (nonstandard interface, nonstandard medium, or an explicit use of KSPIN_FLAG_DO_NOT_USE_STANDARD_TRANSPORT in <a href="https://msdn.microsoft.com/library/windows/hardware/ff563534">KSPIN_DESCRIPTOR_EX</a>) receive nonfiltered state changes through this routine. As such, nonstandard transport pins must be prepared to deal with state changes that jump more than a single step. As an example, consider a jump from <b>KSSTATE_RUN</b> to <b>KSSTATE_STOP</b> without an intervening KSSTATE_PAUSE. In addition, the state reported to this routine will be identical to the state reported in the <b>DeviceState</b> member of the relevant KSPIN structure.</p>

<p>This routine is optional.</p>

<p>The minidriver specifies this routine's address in the <b>SetDeviceState</b> member of its <a href="https://msdn.microsoft.com/library/windows/hardware/ff563535">KSPIN_DISPATCH</a> structure.</p>

<p>Minidrivers will not receive a stop upon initial connection of the pin.</p>

<p>Pins that use the standard transport mechanism (standard interface/standard medium or an explicit use of KSPIN_FLAG_USE_STANDARD_TRANSPORT in <a href="https://msdn.microsoft.com/library/windows/hardware/ff563534">KSPIN_DESCRIPTOR_EX</a>) receive filtered state changes through the owning pipe through this routine. This means that no transition will be more than a single step. In other words, <b>KSSTATE_STOP</b> transitions to KSSTATE_ACQUIRE, <b>KSSTATE_ACQUIRE</b> transitions to KSSTATE_PAUSE, and so on. In addition, state changes received in this routine represent the state of the pipe as a whole, not the individual state of the pin as reported in the <b>DeviceState</b> member of the KSPIN structure.</p>

<p>Pins that do not use the standard transport mechanism (nonstandard interface, nonstandard medium, or an explicit use of KSPIN_FLAG_DO_NOT_USE_STANDARD_TRANSPORT in <a href="https://msdn.microsoft.com/library/windows/hardware/ff563534">KSPIN_DESCRIPTOR_EX</a>) receive nonfiltered state changes through this routine. As such, nonstandard transport pins must be prepared to deal with state changes that jump more than a single step. As an example, consider a jump from <b>KSSTATE_RUN</b> to <b>KSSTATE_STOP</b> without an intervening KSSTATE_PAUSE. In addition, the state reported to this routine will be identical to the state reported in the <b>DeviceState</b> member of the relevant KSPIN structure.</p>

<p>This routine is optional.</p>

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
<p>Version</p>
</th>
<td width="70%">
<p>Available in Microsoft Windows XP and later operating systems and DirectX 8.0 and later DirectX versions.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ks.h (include Ks.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>PASSIVE_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563535">KSPIN_DISPATCH</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20AVStrMiniPinSetDeviceState routine%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
