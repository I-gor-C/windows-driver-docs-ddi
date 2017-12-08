---
UID: NF.ks.KsFilterGetOuterUnknown
title: KsFilterGetOuterUnknown function
author: windows-driver-content
description: The KsFilterGetOuterUnknown function returns the outer IUnknown interface of the filter specified by Filter.
old-location: stream\ksfiltergetouterunknown.htm
old-project: stream
ms.assetid: 599a6583-dcf2-4fe3-949a-5072bff9915c
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: KsFilterGetOuterUnknown
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
req.alt-api: KsFilterGetOuterUnknown
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
req.irql: PASSIVE_LEVEL
---

# KsFilterGetOuterUnknown function



## -description
The<b> KsFilterGetOuterUnknown </b>function returns the outer <b>IUnknown</b> interface of the filter specified by <i>Filter</i>.


## -syntax

````
PUNKNOWN __inline KsFilterGetOuterUnknown(
  _In_ PKSFILTER Filter
);
````


## -parameters

### -param Filter [in]

A pointer to the <a href="stream.ksfilter">KSFILTER</a> structure for which to return the outer <b>IUnknown</b>.

## -returns
<b>KsFilterGetOuterUnknown </b>returns a pointer to the outer <b>IUknown</b> interface of <i>Filter</i>. The interface can then be used to query for other interfaces, or it can be used in conjunction with a <b>Ks</b><i>Xxx</i><b>RegisterAggregatedClientUnknown</b> call to cause <i>Filter</i> to aggregate a minidriver supplied COM object.

## -remarks
This call is an inline function call to <a href="stream.ksgetouterunknown">KsGetOuterUnknown</a>.

## -requirements
<table>
<tr>
<th width="30%">
Target platform
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
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
<a href="stream.ksgetouterunknown">KsGetOuterUnknown</a>
</dt>
<dt>
<a href="stream.ksregisteraggregatedclientunknown">KsRegisterAggregatedClientUnknown</a>
</dt>
<dt>
<a href="stream.kspinregisteraggregatedclientunknown">KsPinRegisterAggregatedClientUnknown</a>
</dt>
<dt><b>KsRegisterAggregatedClientUnknown</b></dt>
<dt>
<a href="https://msdn.microsoft.com/305039fe-0a00-4f3e-ae1a-61c50a2f2fb3">AVStream Overview</a>
</dt>
<dt>
<a href="stream.ksfilterregisteraggregatedclientunknown">KsFilterRegisterAggregatedClientUnknown</a>
</dt>
<dt>
<a href="stream.kspingetouterunknown">KsPinGetOuterUnknown</a>
</dt>
<dt>
<a href="..\ks\nn-ks-ikscontrol~r1.md">IKsControl</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KsFilterGetOuterUnknown function%20 RELEASE:%20(12/6/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
