---
UID: NF.ksproxy.IKsControl.KsProperty
title: IKsControl::KsProperty
author: windows-driver-content
description: The KsProperty method sets a property or retrieves property information, along with any other defined support operations available on a property set.
old-location: stream\ikscontrol_ksproperty.htm
ms.assetid: cc43f704-e1f8-4d62-8cdf-11575ec0b473
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: stream
req.header: ksproxy.h
req.include-header: Ksproxy.h
req.target-type: Desktop
Mobile
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IKsControl.KsProperty
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
ms.keywords: IKsControl, KsProperty, IKsControl::KsProperty
req.iface: IKsControl
---

# IKsControl::KsProperty method



## -description
<p>The <b>KsProperty</b> method sets a property or retrieves property information, along with any other defined support operations available on a property set. </p>


## -syntax

````
HRESULT KsProperty(
  [in]      PKSPROPERTY Property,
  [in]      ULONG       PropertyLength,
  [in, out] LPVOID      PropertyData,
  [in]      ULONG       DataLength,
  [in, out] ULONG       *BytesReturned
);
````


## -parameters
<dl>

### -param <i>Property</i> [in]

<dd>
<p>Pointer to a structure that describes a property and the request type of the property request. This structure must be either a <a href="https://msdn.microsoft.com/library/windows/hardware/ff564262">KSPROPERTY</a> or a structure that contains a <b>KSPROPERTY</b> structure as its first member. An example of a structure that can be pointed to by this member is the <a href="https://msdn.microsoft.com/library/windows/hardware/ff566089">KSPROPERTY_VIDEOPROCAMP_S</a> structure.</p>
</dd>

### -param <i>PropertyLength</i> [in]

<dd>
<p>Size, in bytes, of the buffer at <i>Property</i>.</p>
</dd>

### -param <i>PropertyData</i> [in, out]

<dd>
<p>Pointer to a buffer that contains data for a KSPROPERTY_TYPE_SET, KSPROPERTY_TYPE_UNSERIALIZESET, or KSPROPERTY_TYPE_UNSERIALIZERAW operation, or buffer space that receives data for all other operations.</p>
</dd>

### -param <i>DataLength</i> [in]

<dd>
<p>Size, in bytes, of the buffer at <i>PropertyData</i>.</p>
</dd>

### -param <i>BytesReturned</i> [in, out]

<dd>
<p>Pointer to a variable that receives the size, in bytes, of the data that <b>KsProperty</b> stores in the buffer at <i>PropertyData</i>. If no data is stored, the size is zero.</p>
</dd>
</dl>

## -returns
<p>Returns NOERROR if successful; otherwise, returns an error code.</p>

## -remarks
<p>To determine the buffer size that is required for a specific property request, you can call this method with <i>PropertyData</i> set to <b>NULL</b> and <i>DataLength</i> equal to zero. The method returns HRESULT_FROM_WIN32(ERROR_MORE_DATA), and <i>BytesReturned</i> contains the size of the required buffer.</p>

<p>To determine the buffer size that is required for a specific property request, you can call this method with <i>PropertyData</i> set to <b>NULL</b> and <i>DataLength</i> equal to zero. The method returns HRESULT_FROM_WIN32(ERROR_MORE_DATA), and <i>BytesReturned</i> contains the size of the required buffer.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564262">KSPROPERTY</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566089">KSPROPERTY_VIDEOPROCAMP_S</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20IKsControl::KsProperty method%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
