---
UID: NF.ks.KsGetObjectFromFileObject
title: KsGetObjectFromFileObject
author: windows-driver-content
description: The KsGetObjectFromFileObject function returns the AVStream object cast to PVOID from FileObject.
old-location: stream\ksgetobjectfromfileobject.htm
old-project: stream
ms.assetid: 6bd4f75b-a332-4e1f-8df7-0d6f51b0737b
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: KsGetObjectFromFileObject
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
req.alt-api: KsGetObjectFromFileObject
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

# KsGetObjectFromFileObject function



## -description
<p>The<b> KsGetObjectFromFileObject</b> function returns the AVStream object cast to PVOID from <i>FileObject</i>.</p>


## -syntax

````
PVOID KsGetObjectFromFileObject(
  _In_ PFILE_OBJECT FileObject
);
````


## -parameters
<dl>

### -param <i>FileObject</i> [in]

<dd>
<p>A pointer to the <a href="..\wdm\ns-wdm--file-object.md">FILE_OBJECT</a> structure for which to determine the associated AVStream object.</p>
</dd>
</dl>

## -returns
<p><b>KsGetObjectFromFileObject</b> returns a pointer to the AVStream object associated with <i>FileObject</i> (cast to PVOID). This pointer may point to a <a href="..\ks\ns-ks--ksfilter.md">KSFILTER</a> or a <a href="..\ks\ns-ks--kspin.md">KSPIN</a>, for example.</p>

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
<a href="..\ks\nf-ks-ksgetobjecttypefromfileobject.md">KsGetObjectTypeFromFileObject</a>
</dt>
<dt>
<a href="..\ks\nf-ks-ksgetfilterfromfileobject.md">KsGetFilterFromFileObject</a>
</dt>
<dt>
<a href="..\ks\nf-ks-ksgetpinfromfileobject.md">KsGetPinFromFileObject</a>
</dt>
<dt>
<a href="..\ks\nf-ks-kspingetconnectedpinfileobject.md">KsPinGetConnectedPinFileObject</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KsGetObjectFromFileObject function%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
