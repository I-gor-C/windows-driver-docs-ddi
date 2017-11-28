---
UID: NF.ksproxy.KsGetMediaType
title: KsGetMediaType
author: windows-driver-content
description: The KsGetMediaType function retrieves information about a media type on a pin factory identifier.
old-location: stream\ksgetmediatype.htm
old-project: stream
ms.assetid: 4b7aac38-ab29-4cac-a7f0-896423b17400
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: KsGetMediaType
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
req.alt-api: KsGetMediaType
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

# KsGetMediaType function



## -description
<p>The <b>KsGetMediaType</b> function retrieves information about a media type on a pin factory identifier. </p>


## -syntax

````
HRESULT KsGetMediaType(
  _In_  int           Position,
  _Out_ AM_MEDIA_TYPE *AmMediaType,
  _In_  HANDLE        FilterHandle,
  _In_  ULONG         PinFactoryId
);
````


## -parameters
<dl>

### -param <i>Position</i> [in]

<dd>
<p>Offset into the data range item that <b>KsGetMediaType</b> fills. Note that the data type of <i>Position</i> is <b>int</b> to conform to underlying calls.</p>
</dd>

### -param <i>AmMediaType</i> [out]

<dd>
<p>Pointer to a variable that receives information in a AM_MEDIA_TYPE structure.</p>
</dd>

### -param <i>FilterHandle</i> [in]

<dd>
<p>Handle to the filter that contains the pin factory to query.</p>
</dd>

### -param <i>PinFactoryId</i> [in]

<dd>
<p>Identifier of the pin factory against which the information for a media type is being returned.</p>
</dd>
</dl>

## -returns
<p>Returns NOERROR if successful; otherwise, returns an error code.</p>

## -remarks
<p>The <b>KsGetMediaType</b> function queries the list of data ranges and performs a data intersection on the specified data range, thus producing a data format. It then converts that data format to a media type.</p>

<p>For more information about AM_MEDIA_TYPE, see the Microsoft Windows SDK documentation.</p>

<p>The <b>KsGetMediaType</b> function queries the list of data ranges and performs a data intersection on the specified data range, thus producing a data format. It then converts that data format to a media type.</p>

<p>For more information about AM_MEDIA_TYPE, see the Microsoft Windows SDK documentation.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559910">IKsPinFactory</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KsGetMediaType function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
