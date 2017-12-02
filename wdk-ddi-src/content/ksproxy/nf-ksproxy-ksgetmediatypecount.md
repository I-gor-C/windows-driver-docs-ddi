---
UID: NF.ksproxy.KsGetMediaTypeCount
title: KsGetMediaTypeCount
author: windows-driver-content
description: The KsGetMediaTypeCount function returns the number of available media types on a pin factory identifier.
old-location: stream\ksgetmediatypecount.htm
old-project: stream
ms.assetid: 157cb12c-1b2d-45b5-8541-e16ee3449064
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: KsGetMediaTypeCount
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ksproxy.h
req.include-header: Ksproxy.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KsGetMediaTypeCount
req.alt-loc: Ksproxy.lib,Ksproxy.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ksproxy.lib
req.dll: 
req.irql: 
req.iface: 
---

# KsGetMediaTypeCount function



## -description
<p>The <b>KsGetMediaTypeCount</b> function returns the number of available media types on a pin factory identifier.</p>


## -syntax

````
HRESULT KsGetMediaTypeCount(
  _In_  HANDLE FilterHandle,
  _In_  ULONG  PinFactoryId,
  _Out_ ULONG  *MediaTypeCount
);
````


## -parameters
<dl>

### -param FilterHandle [in]

<dd>
<p>Handle to the filter that contains the pin factory to query.</p>
</dd>

### -param PinFactoryId [in]

<dd>
<p>Identifier of the pin factory against which the number of media types is being returned.</p>
</dd>

### -param MediaTypeCount [out]

<dd>
<p>Pointer to a variable to receive the number of media types.</p>
</dd>
</dl>

## -returns
<p>Returns NOERROR if successful; otherwise, returns an error code.</p>

## -remarks
<p>The number of available media types that <b>KsGetMediaTypeCount</b> returns is equal to the number of available data ranges. </p>

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
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ksproxy.h (include Ksproxy.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Ksproxy.lib</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ksproxy\nn-ksproxy-ikspinfactory.md">IKsPinFactory</a>
</dt>
<dt>
<a href="stream.ksdatarange">KSDATARANGE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KsGetMediaTypeCount function%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
