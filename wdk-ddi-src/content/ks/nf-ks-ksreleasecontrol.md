---
UID: NF.ks.KsReleaseControl
title: KsReleaseControl
author: windows-driver-content
description: The KsReleaseControl function releases the control mutex for Object.
old-location: stream\ksreleasecontrol.htm
old-project: stream
ms.assetid: f585f1ad-7ed0-49b1-ab35-a6b879118b38
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: KsReleaseControl
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
req.alt-api: KsReleaseControl
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

# KsReleaseControl function



## -description
<p>The<b> KsReleaseControl </b>function releases the control mutex for <i>Object</i>.</p>


## -syntax

````
void KsReleaseControl(
  _In_ PVOID Object
);
````


## -parameters
<dl>

### -param <i>Object</i> [in]

<dd>
<p>The object for which to release the control mutex.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p><i>Object</i> should be either a filter or a pin cast to PVOID.</p>

<p>Minidrivers typically do not call <b>KsReleaseControl</b> directly, but instead call <a href="https://msdn.microsoft.com/library/windows/hardware/ff562551">KsFilterReleaseControl</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff563526">KsPinReleaseControl</a>. These versions automatically provide the necessary typecasting to PVOID.</p>

<p>For more information, see <a href="NULL">Mutexes in AVStream</a>. </p>

<p><i>Object</i> should be either a filter or a pin cast to PVOID.</p>

<p>Minidrivers typically do not call <b>KsReleaseControl</b> directly, but instead call <a href="https://msdn.microsoft.com/library/windows/hardware/ff562551">KsFilterReleaseControl</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff563526">KsPinReleaseControl</a>. These versions automatically provide the necessary typecasting to PVOID.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560908">KsAcquireControl</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562523">KsFilterAcquireControl</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563485">KsPinAcquireControl</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562551">KsFilterReleaseControl</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563526">KsPinReleaseControl</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KsReleaseControl function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
