---
UID: NF.ks.KsGetParent
title: KsGetParent
author: windows-driver-content
description: The KsGetParent function acquires the parent of the given object.
old-location: stream\ksgetparent.htm
ms.assetid: d7804745-295f-491a-80f4-84441598bbf4
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: stream
req.header: ks.h
req.include-header: Ks.h
req.target-type: Universal
req.target-min-winverclnt: Available in Microsoft Windows XP and later operating systems and DirectX 8.0 and later DirectX versions.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KsGetParent
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
ms.keywords: KsGetParent
req.iface: 
---

# KsGetParent function



## -description
<p>The<b> KsGetParent</b> function acquires the parent of the given object.</p>


## -syntax

````
PVOID KsGetParent(
  _In_ PVOID Object
);
````


## -parameters
<dl>

### -param <i>Object</i> [in]

<dd>
<p>A pointer to the AVStream object for which to find the parent. Must be a pointer to one of the following types: <a href="https://msdn.microsoft.com/library/windows/hardware/ff561681">KSDEVICE</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff562530">KSFILTERFACTORY</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff562522">KSFILTER</a>, or <a href="https://msdn.microsoft.com/library/windows/hardware/ff563483">KSPIN</a>. Callers must manually typecast the object to a PVOID.</p>
</dd>
</dl>

## -returns
<p><b>KsGetParent</b> returns the parent of <i>Object</i> as a PVOID. Callers must manually cast this return value to whatever the type of the parent of <i>Object</i> is.</p>

## -remarks
<p>For a graphical representation of AVStream parent/child relationships, see the diagram in <a href="NULL">AVStream Object Hierarchy</a>.</p>

<p>The object hierarchy is only guaranteed stable while the appropriate mutex is held, in this case the device mutex. For more information, see <a href="NULL">Mutexes in AVStream</a>.</p>

<p>Minidrivers rarely use this function directly. Callers of <b>KsGetParent</b> must manually perform typecasts to and from PVOID. There are a number of inline versions that do the casting for you: <a href="https://msdn.microsoft.com/library/windows/hardware/ff562536">KsFilterFactoryGetParentDevice</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff562548">KsFilterGetParentFilterFactory</a>, and <a href="https://msdn.microsoft.com/library/windows/hardware/ff563516">KsPinGetParentFilter</a>.</p>

<p>For a graphical representation of AVStream parent/child relationships, see the diagram in <a href="NULL">AVStream Object Hierarchy</a>.</p>

<p>The object hierarchy is only guaranteed stable while the appropriate mutex is held, in this case the device mutex. For more information, see <a href="NULL">Mutexes in AVStream</a>.</p>

<p>Minidrivers rarely use this function directly. Callers of <b>KsGetParent</b> must manually perform typecasts to and from PVOID. There are a number of inline versions that do the casting for you: <a href="https://msdn.microsoft.com/library/windows/hardware/ff562536">KsFilterFactoryGetParentDevice</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff562548">KsFilterGetParentFilterFactory</a>, and <a href="https://msdn.microsoft.com/library/windows/hardware/ff563516">KsPinGetParentFilter</a>.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561681">KSDEVICE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562530">KSFILTERFACTORY</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562522">KSFILTER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563483">KSPIN</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562536">KsFilterFactoryGetParentDevice</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562548">KsFilterGetParentFilterFactory</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563516">KsPinGetParentFilter</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KsGetParent function%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
