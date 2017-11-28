---
UID: NF.ksproxy.IKsObject.KsGetObjectHandle
title: IKsObject::KsGetObjectHandle
author: windows-driver-content
description: The KsGetObjectHandle method retrieves a file handle to a KS object.
old-location: stream\iksobject_ksgetobjecthandle.htm
old-project: stream
ms.assetid: 55c4f362-eb3c-4c4f-a048-7abdd270f67f
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: IKsObject, KsGetObjectHandle, IKsObject::KsGetObjectHandle
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ksproxy.h
req.include-header: Ksproxy.h
req.target-type: Desktop
Mobile
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IKsObject.KsGetObjectHandle
req.alt-loc: ksproxy.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
req.iface: IKsObject
---

# IKsObject::KsGetObjectHandle method



## -description
<p>The <b>KsGetObjectHandle</b> method retrieves a file handle to a KS object. </p>


## -syntax

````
HANDLE KsGetObjectHandle();
````


## -parameters


## -returns
<p>Returns a file handle to a KS object if successful; otherwise, returns null. </p>

<p>Returns a file handle to a KS object if successful; otherwise, returns null. </p>

<p>Returns a file handle to a KS object if successful; otherwise, returns null. </p>

## -remarks
<p>Applications can use the handle that <b>KsGetObjectHandle</b> returns to send control-code requests to the driver that handles the KS object. </p>

<p>Applications can use the handle that <b>KsGetObjectHandle</b> returns to send control-code requests to the driver that handles the KS object. </p>

<p>Applications can use the handle that <b>KsGetObjectHandle</b> returns to send control-code requests to the driver that handles the KS object. </p>

<p>Applications can use the handle that <b>KsGetObjectHandle</b> returns to send control-code requests to the driver that handles the KS object. </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
<dt>Mobile</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ksproxy.h (include Ksproxy.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567142">KsSynchronousDeviceControl</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20IKsObject::KsGetObjectHandle method%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
