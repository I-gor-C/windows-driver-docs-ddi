---
UID: NF.ks.KsGetPinFromIrp
title: KsGetPinFromIrp
author: windows-driver-content
description: The KsGetPinFromIrp function returns the AVStream pin object associated with the given IRP.
old-location: stream\ksgetpinfromirp.htm
old-project: stream
ms.assetid: 96176a33-0721-4a4d-ba1b-131e25fc2306
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: KsGetPinFromIrp
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
req.alt-api: KsGetPinFromIrp
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

# KsGetPinFromIrp function



## -description
<p>The<b> KsGetPinFromIrp</b> function returns the AVStream pin object associated with the given IRP. </p>


## -syntax

````
PKSPIN KsGetPinFromIrp(
  _In_ PIRP Irp
);
````


## -parameters
<dl>

### -param <i>Irp</i> [in]

<dd>
<p>A pointer to an <a href="https://msdn.microsoft.com/library/windows/hardware/ff550694">IRP</a> for which to return the associated pin.</p>
</dd>
</dl>

## -returns
<p><b>KsGetPinFromIrp</b> returns a pointer to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff563483">KSPIN</a> structure associated with the given IRP or <b>NULL</b>. <b>NULL</b> indicates that either the IRP is not associated with an AVStream object or that it is associated with a filter or a topology node.</p>

## -remarks
<p>Currently, IRPs associated with topology nodes cannot be queried for associated pins. This may change in a future revision of AVStream.</p>

<p>Currently, IRPs associated with topology nodes cannot be queried for associated pins. This may change in a future revision of AVStream.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562622">KsGetFilterFromIrp</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562644">KsGetNodeIdFromIrp</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560908">KsAcquireControl</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566780">KsReleaseControl</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562523">KsFilterAcquireControl</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562551">KsFilterReleaseControl</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KsGetPinFromIrp function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
