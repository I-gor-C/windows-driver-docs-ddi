---
UID: NF.ks.KsStreamPointerGetMdl
title: KsStreamPointerGetMdl
author: windows-driver-content
description: The KsStreamPointerGetMdl function returns the MDL associated with the frame referenced by StreamPointer.
old-location: stream\ksstreampointergetmdl.htm
old-project: stream
ms.assetid: 05d37fbd-9bdc-478a-8772-6f63d1363c1c
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: KsStreamPointerGetMdl
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
req.alt-api: KsStreamPointerGetMdl
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
req.irql: <=DISPATCH_LEVEL
req.iface: 
---

# KsStreamPointerGetMdl function



## -description
<p>The<b> KsStreamPointerGetMdl </b>function returns the MDL associated with the frame referenced by <i>StreamPointer</i>.</p>


## -syntax

````
PMDL KsStreamPointerGetMdl(
  _In_ PKSSTREAM_POINTER StreamPointer
);
````


## -parameters
<dl>

### -param StreamPointer [in]

<dd>
<p>A pointer to the <a href="..\ks\ns-ks--ksstream-pointer.md">KSSTREAM_POINTER</a> structure that references the frame for which to return the associated MDL.</p>
</dd>
</dl>

## -returns
<p>Returns either a pointer to the <a href="wdkgloss.m#wdkgloss.memory_descriptor_list__mdl_#wdkgloss.memory_descriptor_list__mdl_"><i>memory descriptor list (MDL)</i></a> describing the frame referenced by <i>StreamPointer</i> or returns <b>NULL</b>. A <b>NULL</b> return value usually indicates that the given stream pointer was not locked at call-time.</p>

## -remarks
<p>The stream pointer <b>must</b> be locked in order for <b>KsStreamPointerGetMdl </b>to execute successfully.</p>

<p>Also see <a href="https://msdn.microsoft.com/4bac68a0-34d2-431a-9ed9-8a42751a736f">Stream Pointers</a>.</p>

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
<p>&lt;=DISPATCH_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ks\nf-ks-ksstreampointergetirp.md">KsStreamPointerGetIrp</a>
</dt>
<dt>
<a href="..\ks\nf-ks-ksstreampointerlock.md">KsStreamPointerLock</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KsStreamPointerGetMdl function%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
