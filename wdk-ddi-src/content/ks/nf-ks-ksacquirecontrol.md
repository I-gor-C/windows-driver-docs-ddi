---
UID: NF.ks.KsAcquireControl
title: KsAcquireControl
author: windows-driver-content
description: The KsAcquireControl function acquires the filter control mutex for Object.
old-location: stream\ksacquirecontrol.htm
old-project: stream
ms.assetid: c316382c-8416-43c2-b5fd-2d52d01e1419
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: KsAcquireControl
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ks.h
req.include-header: Ks.h
req.target-type: Universal
req.target-min-winverclnt: Available in Microsoft Windows XP and later operating systems and DirectX 8.0 and later DirectX versions.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KsAcquireControl
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
req.irql: PASSIVE_LEVEL
req.iface: 
---

# KsAcquireControl function



## -description
<p>The <b>KsAcquireControl</b> function acquires the filter control mutex for <i>Object</i>. </p>


## -syntax

````
void KsAcquireControl(
  _In_ PVOID Object
);
````


## -parameters
<dl>

### -param <i>Object</i> [in]

<dd>
<p>A pointer to the object for which to acquire the filter control mutex. This should be a pointer to either a <a href="https://msdn.microsoft.com/library/windows/hardware/ff562522">KSFILTER</a> or a <a href="https://msdn.microsoft.com/library/windows/hardware/ff563483">KSPIN</a>, cast to PVOID.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>Minidrivers typically do not call this function directly, but instead call either <a href="https://msdn.microsoft.com/library/windows/hardware/ff562523">KsFilterAcquireControl</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff563485">KsPinAcquireControl</a>. These functions provide the necessary typecasting to PVOID automatically.</p>

<p>For more information, see <a href="NULL">Mutexes in AVStream</a>. </p>

<p>Minidrivers typically do not call this function directly, but instead call either <a href="https://msdn.microsoft.com/library/windows/hardware/ff562523">KsFilterAcquireControl</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff563485">KsPinAcquireControl</a>. These functions provide the necessary typecasting to PVOID automatically.</p>

<p>For more information, see <a href="NULL">Mutexes in AVStream</a>. </p>

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
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Ks.lib</dt>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566780">KsReleaseControl</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562523">KsFilterAcquireControl</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563485">KsPinAcquireControl</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562522">KSFILTER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563483">KSPIN</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KsAcquireControl function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
