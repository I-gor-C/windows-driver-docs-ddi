---
UID: NF.ks.KsPinGetAndGate
title: KsPinGetAndGate
author: windows-driver-content
description: The KsPinGetAndGate function returns the processing control gate for Pin.
old-location: stream\kspingetandgate.htm
old-project: stream
ms.assetid: abd4da69-c0c3-442f-af58-e77362c637da
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: KsPinGetAndGate
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
req.alt-api: KsPinGetAndGate
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
req.irql: Any level
req.iface: 
---

# KsPinGetAndGate function



## -description
<p>The<b> KsPinGetAndGate</b> function returns the processing control gate for <i>Pin</i>.</p>


## -syntax

````
PKSGATE KsPinGetAndGate(
  _In_ PKSPIN Pin
);
````


## -parameters
<dl>

### -param <i>Pin</i> [in]

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff563483">KSPIN</a> for which to return the processing control gate.</p>
</dd>
</dl>

## -returns
<p>Returns a pointer to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff562566">KSGATE</a> representing the processing control gate for <i>Pin</i>.</p>

## -remarks
<p>For more information, see <a href="NULL">Flow Control Gates in AVStream</a>.</p>

<p>For more information, see <a href="NULL">Flow Control Gates in AVStream</a>.</p>

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
<p>Any level</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562542">KsFilterGetAndGate</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562566">KSGATE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KsPinGetAndGate function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
