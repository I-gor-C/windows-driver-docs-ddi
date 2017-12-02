---
UID: NF.ks.KsSetDefaultClockTime
title: KsSetDefaultClockTime
author: windows-driver-content
description: The KsSetDefaultClockTime function sets the current time of the clock.
old-location: stream\kssetdefaultclocktime.htm
old-project: stream
ms.assetid: c8b4fef4-cfbb-4cdd-b762-062b8ae4a423
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: KsSetDefaultClockTime
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ks.h
req.include-header: Ks.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KsSetDefaultClockTime
req.alt-loc: Ks.lib,Ks.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ks.lib
req.dll: 
req.irql: 
req.iface: 
---

# KsSetDefaultClockTime function



## -description
<p>The <b>KsSetDefaultClockTime</b> function sets the current time of the clock. It modifies the current time returned by the clock. The owner of the default clock is expected to serialize access to this function and to the <a href="..\ks\nf-ks-kssetdefaultclockstate.md">KsSetDefaultClockState</a> function.</p>
<p>The function can be called at DISPATCH_LEVEL.</p>


## -syntax

````
VOID KsSetDefaultClockTime(
  _In_ PKSDEFAULTCLOCK DefaultClock,
  _In_ LONGLONG        Time
);
````


## -parameters
<dl>

### -param DefaultClock [in]

<dd>
<p>Specifies an initialize default clock structure that is shared among instances of the default clock for the parent. </p>
</dd>

### -param Time [in]

<dd>
<p>Specifies the new time to set the clock. </p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
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
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Ks.lib</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ks\nf-ks-ksgetdefaultclocktime.md">KsGetDefaultClockTime</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KsSetDefaultClockTime function%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
