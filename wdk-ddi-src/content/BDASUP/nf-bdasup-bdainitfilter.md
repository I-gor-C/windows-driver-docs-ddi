---
UID: NF.bdasup.BdaInitFilter
title: BdaInitFilter
author: windows-driver-content
description: The BdaInitFilter function initializes the BDA filter context associated with a filter instance.
old-location: stream\bdainitfilter.htm
ms.assetid: d6f5c6e5-d944-42a6-bfc2-decc7606cba1
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: stream
req.header: bdasup.h
req.include-header: Bdasup.h
req.target-type: Desktop
req.target-min-winverclnt: Available on Microsoft Windows XP and later operating systems. This routine is available on the Windows 2000 platform only if Microsoft DirectX 9.0 and later is installed on that platform.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: BdaInitFilter
req.alt-loc: Bdasup.lib,Bdasup.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Bdasup.lib
req.dll: 
req.irql: PASSIVE_LEVEL
ms.keywords: BdaInitFilter
req.iface: 
---

# BdaInitFilter function



## -description
<p>The <b>BdaInitFilter</b> function initializes the BDA filter context associated with a filter instance. </p>


## -syntax

````
NTSTATUS BdaInitFilter(
  _In_       PKSFILTER           pKSFilter,
  _In_ const BDA_FILTER_TEMPLATE *pBdaFilterTemplate
);
````


## -parameters
<dl>

### -param <i>pKSFilter</i> [in]

<dd>
<p>Points to the filter in which to initialize the BDA filter context.</p>
</dd>

### -param <i>pBdaFilterTemplate</i> [in]

<dd>
<p>Points to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff556523">BDA_FILTER_TEMPLATE</a> structure that describes the filter template for the BDA device. To determine topology for and configure the initialized filter, the network provider uses information referenced in this BDA_FILTER_TEMPLATE structure. </p>
</dd>
</dl>

## -returns
<p>Returns STATUS_SUCCESS or an appropriate error code. </p>

## -remarks
<p>A BDA minidriver calls the <b>BdaInitFilter</b> function to initialize an instance of a filter using a specific BDA filter template and a filter factory that was previously created through a call to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff556438">BdaCreateFilterFactory</a> function. The BDA minidriver can subsequently use this filter instance in calls to other BDA support functions, such as, <a href="https://msdn.microsoft.com/library/windows/hardware/ff556445">BdaCreatePin</a>. </p>

<p>When a BDA minidriver calls <b>BdaInitFilter</b>, the BDA support driver (<i>Bdasup.sys</i>) creates its own BDA filter context. This BDA filter context is hidden from the BDA minidriver. However, when required, the BDA support driver can access this BDA filter context. The BDA support driver adds a pointer to this BDA filter context to the object bag for the associated <a href="https://msdn.microsoft.com/library/windows/hardware/ff562522">KSFILTER</a> object. When the associated KSFILTER object is destroyed, AVStream requests that the BDA support driver delete this BDA filter context from the object bag. In this way, the BDA support driver can destroy this BDA filter context without requiring intervention by the BDA minidriver. </p>

<p>A BDA minidriver calls the <b>BdaInitFilter</b> function to initialize an instance of a filter using a specific BDA filter template and a filter factory that was previously created through a call to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff556438">BdaCreateFilterFactory</a> function. The BDA minidriver can subsequently use this filter instance in calls to other BDA support functions, such as, <a href="https://msdn.microsoft.com/library/windows/hardware/ff556445">BdaCreatePin</a>. </p>

<p>When a BDA minidriver calls <b>BdaInitFilter</b>, the BDA support driver (<i>Bdasup.sys</i>) creates its own BDA filter context. This BDA filter context is hidden from the BDA minidriver. However, when required, the BDA support driver can access this BDA filter context. The BDA support driver adds a pointer to this BDA filter context to the object bag for the associated <a href="https://msdn.microsoft.com/library/windows/hardware/ff562522">KSFILTER</a> object. When the associated KSFILTER object is destroyed, AVStream requests that the BDA support driver delete this BDA filter context from the object bag. In this way, the BDA support driver can destroy this BDA filter context without requiring intervention by the BDA minidriver. </p>

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
<p>Available on Microsoft Windows XP and later operating systems. This routine is available on the Windows 2000 platform only if Microsoft DirectX 9.0 and later is installed on that platform.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Bdasup.h (include Bdasup.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Bdasup.lib</dt>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556438">BdaCreateFilterFactory</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556445">BdaCreatePin</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556523">BDA_FILTER_TEMPLATE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562522">KSFILTER</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20BdaInitFilter function%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
