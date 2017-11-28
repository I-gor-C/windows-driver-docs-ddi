---
UID: NF.ks.KsPinAcquireControl
title: KsPinAcquireControl
author: windows-driver-content
description: The KsPinAcquireControl function acquires the control mutex for the AVStream pin specified by Pin.
old-location: stream\kspinacquirecontrol.htm
old-project: stream
ms.assetid: 05ff1829-8305-4bc4-be22-233d391a5dc0
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: KsPinAcquireControl
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
req.alt-api: KsPinAcquireControl
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

# KsPinAcquireControl function



## -description
<p>The<b> KsPinAcquireControl</b> function acquires the control mutex for the AVStream pin specified by <i>Pin</i>.</p>


## -syntax

````
void __inline KsPinAcquireControl(
  _In_ PKSPIN Pin
);
````


## -parameters
<dl>

### -param <i>Pin</i> [in]

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff563483">KSPIN</a> for which to acquire the control mutex.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>The pin control mutex is the same mutex that is used by <i>Pin</i>'s parent. This means that the mutex for <i>Pin</i> is also a filter control mutex. For more information, see <a href="NULL">Mutexes in AVStream</a>.</p>

<p><b>KsPinAcquireControl</b> is an inline call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff560908">KsAcquireControl</a> with the appropriate typecasting. Minidrivers manipulating pins should call <b>KsPinAcquireControl</b> instead of calling <b>KsAcquireControl</b> directly.</p>

<p>The pin control mutex is the same mutex that is used by <i>Pin</i>'s parent. This means that the mutex for <i>Pin</i> is also a filter control mutex. For more information, see <a href="NULL">Mutexes in AVStream</a>.</p>

<p><b>KsPinAcquireControl</b> is an inline call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff560908">KsAcquireControl</a> with the appropriate typecasting. Minidrivers manipulating pins should call <b>KsPinAcquireControl</b> instead of calling <b>KsAcquireControl</b> directly.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560908">KsAcquireControl</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563526">KsPinReleaseControl</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566780">KsReleaseControl</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563483">KSPIN</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KsPinAcquireControl function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
