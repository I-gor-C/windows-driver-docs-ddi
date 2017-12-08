---
UID: NF.ksproxy.IKsDataTypeHandler.KsSetMediaType
title: IKsDataTypeHandler::KsSetMediaType
author: windows-driver-content
description: The KsSetMediaType method sets the media type for a data type handler.
old-location: stream\iksdatatypehandler_kssetmediatype.htm
old-project: stream
ms.assetid: b1c97d4f-b305-4c9f-b3fd-06d0ebcb0ed0
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: IKsDataTypeHandler, KsSetMediaType, IKsDataTypeHandler::KsSetMediaType
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
req.alt-api: IKsDataTypeHandler.KsSetMediaType
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
req.iface: IKsDataTypeHandler
---

# IKsDataTypeHandler::KsSetMediaType method



## -description
<p>The <b>KsSetMediaType</b> method sets the media type for a data type handler. </p>


## -syntax

````
HRESULT KsSetMediaType(
  [in] const AM_MEDIA_TYPE *MediaType
);
````


## -parameters
<dl>

### -param MediaType [in]

<dd>
<p>Pointer to a <b>CMediaType</b> object associated with the media type.</p>
</dd>
</dl>

## -returns
<p>Returns NOERROR if successful; otherwise, returns an error code.</p>

## -remarks
<p>Clients can call <b>KsSetMediaType</b> of a single data type handler to initialize this data type handler to a particular media type from a group of many disparate media types.</p>

<p>For more information about <b>CMediaType</b> class, see the Microsoft Windows SDK documentation.</p>

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
</table>

## -see-also
<dl>
<dt>
<a href="..\ksproxy\nn-ksproxy-iksdatatypehandler.md">IKsDataTypeHandler</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20IKsDataTypeHandler::KsSetMediaType method%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
