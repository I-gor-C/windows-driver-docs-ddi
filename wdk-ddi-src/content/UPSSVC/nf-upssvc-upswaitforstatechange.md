---
UID: NF.upssvc.UPSWaitForStateChange
title: UPSWaitForStateChange
author: windows-driver-content
description: The UPSWaitForStateChange function waits until a specified UPS state changes, or until a time-out interval elapses.
old-location: battery\upswaitforstatechange.htm
ms.assetid: ac78dda4-6d14-441b-8e79-3245f7253875
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: battery
req.header: upssvc.h
req.include-header: Upssvc.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: UPSWaitForStateChange
req.alt-loc: upssvc.h
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
ms.keywords: UPSWaitForStateChange
req.iface: 
req.product: Windows 10 or later.
---

# UPSWaitForStateChange function



## -description
<p>The <b>UPSWaitForStateChange</b> function waits until a specified UPS state changes, or until a time-out interval elapses.</p>


## -syntax

````
void UPSWaitForStateChange(
  _In_ DWORD aCurrentState,
  _In_ DWORD anInterval
);
````


## -parameters
<dl>

### -param <i>aCurrentState</i> [in]

<dd>
<p>Specifies the UPS state on which to wait. When the state of the UPS system changes from the specified state to any other state, the function returns. The specified value can be one of the following:</p>
<p></p>
<dl>

### -param <a id="UPS_ONLINE_"></a><a id="ups_online_"></a>UPS_ONLINE 

<dd>
<p>Utility-supplied power is normal.</p>
</dd>

### -param <a id="UPS_ONBATTERY"></a><a id="ups_onbattery"></a>UPS_ONBATTERY

<dd>
<p>Utility-supplied power is inadequate, and the UPS batteries are discharging.</p>
</dd>

### -param <a id="UPS_LOWBATTERY"></a><a id="ups_lowbattery"></a>UPS_LOWBATTERY

<dd>
<p>Utility-supplied power is inadequate, and the UPS batteries are critically low.</p>
</dd>

### -param <a id="UPS_NOCOMM"></a><a id="ups_nocomm"></a>UPS_NOCOMM

<dd>
<p>Communication with the UPS is not currently established.</p>
</dd>
</dl>
</dd>

### -param <i>anInterval</i> [in]

<dd>
<p>Specifies a time-out interval, in milliseconds, for the function. If the UPS state has not changed from the specified state when the interval elapses, the function returns. A value of INFINITE means the interval never elapses.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>The <b>UPSWaitForStateChange</b> function must wait until either the state of the UPS changes from the value specified by <i>aCurrentState</i>, or until the time specified by <i>anInterval</i> has elapsed, whichever occurs first. </p>

<p>A call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff536311">UPSCancelWait</a> interrupts <b>UPSWaitForStateChange</b> and causes it to return. </p>

<p>The <b>UPSWaitForStateChange</b> function must wait until either the state of the UPS changes from the value specified by <i>aCurrentState</i>, or until the time specified by <i>anInterval</i> has elapsed, whichever occurs first. </p>

<p>A call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff536311">UPSCancelWait</a> interrupts <b>UPSWaitForStateChange</b> and causes it to return. </p>

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
<dt>Upssvc.h (include Upssvc.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536311">UPSCancelWait</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [battery\battery]:%20UPSWaitForStateChange function%20 RELEASE:%20(10/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
