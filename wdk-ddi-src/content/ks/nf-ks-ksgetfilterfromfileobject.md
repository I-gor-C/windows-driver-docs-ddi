---
UID: NF.ks.KsGetFilterFromFileObject
title: KsGetFilterFromFileObject
author: windows-driver-content
description: The KsGetFilterFromFileObject function returns the AVStream filter object associated with FileObject.
old-location: stream\ksgetfilterfromfileobject.htm
old-project: stream
ms.assetid: eb4ca943-43cb-4eac-8a73-484a7b8acafe
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: KsGetFilterFromFileObject
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
req.alt-api: KsGetFilterFromFileObject
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
req.irql: Any level
req.iface: 
---

# KsGetFilterFromFileObject function



## -description
<p>The<b> KsGetFilterFromFileObject </b>function returns the AVStream filter object associated with <i>FileObject</i>.</p>


## -syntax

````
PKSFILTER __inline KsGetFilterFromFileObject(
  _In_ PFILE_OBJECT FileObject
);
````


## -parameters
<dl>

### -param <i>FileObject</i> [in]

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff545834">FILE_OBJECT</a> for which to return the associated AVStream filter object.</p>
</dd>
</dl>

## -returns
<p><b>KsGetFilterFromFileObject</b> returns a pointer to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff562522">KSFILTER</a> structure associated with <i>FileObject</i>.</p>

## -remarks
<p>It is the responsibility of the minidriver to verify that <i>FileObject</i> is a file object associated with an AVStream filter. Do this by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff562651">KsGetObjectTypeFromFileObject</a> before calling <b>KsGetFilterFromFileObject</b>.</p>

<p><b>KsGetFilterFromFileObject</b> is an inline call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff562648">KsGetObjectFromFileObject</a>. The difference is that <b>KsGetFilterFromFileObject</b> typecasts the return as type pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff562522">KSFILTER</a> structure. </p>

<p>It is the responsibility of the minidriver to verify that <i>FileObject</i> is a file object associated with an AVStream filter. Do this by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff562651">KsGetObjectTypeFromFileObject</a> before calling <b>KsGetFilterFromFileObject</b>.</p>

<p><b>KsGetFilterFromFileObject</b> is an inline call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff562648">KsGetObjectFromFileObject</a>. The difference is that <b>KsGetFilterFromFileObject</b> typecasts the return as type pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff562522">KSFILTER</a> structure. </p>

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
<p>Any level</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562648">KsGetObjectFromFileObject</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562651">KsGetObjectTypeFromFileObject</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562617">KsGetDeviceForDeviceObject</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KsGetFilterFromFileObject function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
