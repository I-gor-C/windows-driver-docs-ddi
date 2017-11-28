---
UID: NF.ksproxy.IKsPin.KsQueryMediums
title: IKsPin::KsQueryMediums
author: windows-driver-content
description: The KsQueryMediums method retrieves mediums that a pin supports.
old-location: stream\ikspin_ksquerymediums.htm
old-project: stream
ms.assetid: de6efd10-7f97-422a-abd4-c21c4cbc1dd7
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: IKsPin, KsQueryMediums, IKsPin::KsQueryMediums
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
req.alt-api: IKsPin.KsQueryMediums
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
req.iface: IKsPin
---

# IKsPin::KsQueryMediums method



## -description
<p>The <b>KsQueryMediums</b> method retrieves mediums that a pin supports. </p>


## -syntax

````
HRESULT KsQueryMediums(
  [out] PKSMULTIPLE_ITEM *MediumList
);
````


## -parameters
<dl>

### -param <i>MediumList</i> [out]

<dd>
<p>Pointer to a buffer that receives a pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff563441">KSMULTIPLE_ITEM</a> structure, followed by a sequence of <a href="https://msdn.microsoft.com/library/windows/hardware/ff563538">KSPIN_MEDIUM</a> structures that describe medium types. The KSMULTIPLE_ITEM structure is a header that describes the size of the buffer and the number of entries in the list that follows the header.</p>
</dd>
</dl>

## -returns
<p>Returns NOERROR if successful; otherwise, returns an error code.</p>

## -remarks
<p>The returned mediums are ordered by preference. </p>

<p>Applications call <b>KsQueryMediums</b> to retrieve mediums that pins support in order to build a filter graph.</p>

<p>The returned mediums are ordered by preference. </p>

<p>Applications call <b>KsQueryMediums</b> to retrieve mediums that pins support in order to build a filter graph.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563441">KSMULTIPLE_ITEM</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563538">KSPIN_MEDIUM</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20IKsPin::KsQueryMediums method%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
