---
UID: NF.ks.KsGetParent
title: KsGetParent function
author: windows-driver-content
description: The KsGetParent function acquires the parent of the given object.
old-location: stream\ksgetparent.htm
old-project: stream
ms.assetid: d7804745-295f-491a-80f4-84441598bbf4
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: KsGetParent
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
---

# KsGetParent function



## -description
The<b> KsGetParent</b> function acquires the parent of the given object.


## -syntax

````
PVOID KsGetParent(
  _In_ PVOID Object
);
````


## -parameters

### -param Object [in]

A pointer to the AVStream object for which to find the parent. Must be a pointer to one of the following types: <a href="stream.ksdevice">KSDEVICE</a>, <a href="stream.ksfilterfactory">KSFILTERFACTORY</a>, <a href="stream.ksfilter">KSFILTER</a>, or <a href="stream.kspin">KSPIN</a>. Callers must manually typecast the object to a PVOID.

## -returns
<b>KsGetParent</b> returns the parent of <i>Object</i> as a PVOID. Callers must manually cast this return value to whatever the type of the parent of <i>Object</i> is.

## -remarks
For a graphical representation of AVStream parent/child relationships, see the diagram in <a href="https://msdn.microsoft.com/b7d6f06d-6c97-414e-a453-d375e2d7ccf5">AVStream Object Hierarchy</a>.

The object hierarchy is only guaranteed stable while the appropriate mutex is held, in this case the device mutex. For more information, see <a href="https://msdn.microsoft.com/011edaaa-7449-41c3-8cfb-0d319901af8b">Mutexes in AVStream</a>.

Minidrivers rarely use this function directly. Callers of <b>KsGetParent</b> must manually perform typecasts to and from PVOID. There are a number of inline versions that do the casting for you: <a href="stream.ksfilterfactorygetparentdevice">KsFilterFactoryGetParentDevice</a>, <a href="stream.ksfiltergetparentfilterfactory">KsFilterGetParentFilterFactory</a>, and <a href="stream.kspingetparentfilter">KsPinGetParentFilter</a>.

## -requirements
<table>
<tr>
<th width="30%">
Target platform
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Version
</th>
<td width="70%">
Available in Microsoft Windows XP and later operating systems and DirectX 8.0 and later DirectX versions.
</td>
</tr>
<tr>
<th width="30%">
Header
</th>
<td width="70%">
<dl>
<dt>Ks.h (include Ks.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library
</th>
<td width="70%">
<dl>
<dt>Ks.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL
</th>
<td width="70%">
PASSIVE_LEVEL
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="stream.ksdevice">KSDEVICE</a>
</dt>
<dt>
<a href="stream.ksfilterfactory">KSFILTERFACTORY</a>
</dt>
<dt>
<a href="stream.ksfilter">KSFILTER</a>
</dt>
<dt>
<a href="stream.kspin">KSPIN</a>
</dt>
<dt>
<a href="stream.ksfilterfactorygetparentdevice">KsFilterFactoryGetParentDevice</a>
</dt>
<dt>
<a href="stream.ksfiltergetparentfilterfactory">KsFilterGetParentFilterFactory</a>
</dt>
<dt>
<a href="stream.kspingetparentfilter">KsPinGetParentFilter</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KsGetParent function%20 RELEASE:%20(12/6/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
