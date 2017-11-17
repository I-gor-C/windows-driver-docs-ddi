---
UID: NF.ks.KsGetDefaultClockTime
title: KsGetDefaultClockTime
author: windows-driver-content
description: The KsGetDefaultClockTime function gets the current time of the clock.The function can be called at DISPATCH_LEVEL.
old-location: stream\ksgetdefaultclocktime.htm
ms.assetid: 9689b9f8-e5ae-4689-90b1-6d029408f876
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: stream
req.header: ks.h
req.include-header: Ks.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KsGetDefaultClockTime
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
ms.keywords: KsGetDefaultClockTime
req.iface: 
---

# KsGetDefaultClockTime function



## -description
<p>The <b>KsGetDefaultClockTime</b> function gets the current time of the clock.</p>
<p>The function can be called at DISPATCH_LEVEL.</p>


## -syntax

````
LONGLONG KsGetDefaultClockTime(
  _In_ PKSDEFAULTCLOCK DefaultClock
);
````


## -parameters
<dl>

### -param <i>DefaultClock</i> [in]

<dd>
<p>Specifies an initialize default clock structure that is shared among any instance of the default clock for the parent. </p>
</dd>
</dl>

## -returns
<p>The <b>KsGetDefaultClockTime</b> function returns the current clock time.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566827">KsSetDefaultClockTime</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KsGetDefaultClockTime function%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
