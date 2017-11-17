---
UID: NF.ks.KsFilterFactoryUpdateCacheData
title: KsFilterFactoryUpdateCacheData
author: windows-driver-content
description: The KsFilterFactoryUpdateCacheData function updates the FilterData registry key and the Medium cache (a set of registry keys) for a given filter factory.
old-location: stream\ksfilterfactoryupdatecachedata.htm
ms.assetid: a5c868a5-0e79-482b-9694-02cae2de99ca
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: stream
req.header: ks.h
req.include-header: Ks.h
req.target-type: Universal
req.target-min-winverclnt: Available in Microsoft Windows XP and later operating systems and DirectX 9.0 and later DirectX versions.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KsFilterFactoryUpdateCacheData
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
req.irql: 
ms.keywords: KsFilterFactoryUpdateCacheData
req.iface: 
---

# KsFilterFactoryUpdateCacheData function



## -description
<p>The <b>KsFilterFactoryUpdateCacheData</b> function updates the FilterData registry key and the Medium cache (a set of registry keys) for a given filter factory.</p>


## -syntax

````
NTSTATUS KsFilterFactoryUpdateCacheData(
  _In_           PKSFILTERFACTORY    FilterFactory,
  _In_opt_ const KSFILTER_DESCRIPTOR *FilterDescriptor
);
````


## -parameters
<dl>

### -param <i>FilterFactory</i> [in]

<dd>
<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/ff562530">KSFILTERFACTORY</a> for which to update FilterData and Medium cache in the registry.</p>
</dd>

### -param <i>FilterDescriptor</i> [in, optional]

<dd>
<p>An optional <a href="https://msdn.microsoft.com/library/windows/hardware/ff562553">KSFILTER_DESCRIPTOR</a> for which the FilterData key and Medium cache will be updated. If <b>NULL</b>, <i>FilterFactory</i>'s descriptor is used instead. Provide if the filter factory uses dynamic pins and needs to update information for pins that have not yet been instantiated.</p>
</dd>
</dl>

## -returns
<p><b>
             KsFilterFactoryUpdateCacheData</b> returns STATUS_SUCCESS or a failure code, indicating whether the relevant registry information was successfully updated. It returns STATUS_INVALID_PARAMETER if no device interface is found that corresponds to the categories passed in the filter descriptor.</p>

## -remarks
<p>This function updates the FilterData key and Medium cache for all categories specified in <i>FilterDescriptor</i>. If <i>FilterDescriptor</i> is <b>NULL</b>, the FilterData and Medium cache are updated for all categories specified in <i>FilterFactory</i>'s <a href="https://msdn.microsoft.com/library/windows/hardware/ff562553">KSFILTER_DESCRIPTOR</a> member.</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566773">KsRegisterFilterWithNoKSPins</a> provides similar functionality, but should not be used if two instances of <a href="https://msdn.microsoft.com/library/windows/hardware/ff562553">KSFILTER_DESCRIPTOR</a> under the same <a href="https://msdn.microsoft.com/library/windows/hardware/ff561681">KSDEVICE</a> are registered in the same category, and differ only in reference GUID. In this case, <b>KsRegisterFilterWithNoKSPins</b> updates data only for the first, even though the second may have been specified.</p>

<p>Do not use this routine in place of <b>KsRegisterFilterWithNoKSPins</b> for filters with no KS pins, such as analog style crossbars. Use this routine only for a specific filter for which the minidriver is passing the corresponding filter factory.</p>

<p>In addition, <b>KsRegisterFilterWithNoKSPins</b> only allows one medium per registered pin. This may not be sufficient for a BDA minidriver.</p>

<p>For more information, see <a href="NULL">AVStream Object Hierarchy</a>.</p>

<p>This function updates the FilterData key and Medium cache for all categories specified in <i>FilterDescriptor</i>. If <i>FilterDescriptor</i> is <b>NULL</b>, the FilterData and Medium cache are updated for all categories specified in <i>FilterFactory</i>'s <a href="https://msdn.microsoft.com/library/windows/hardware/ff562553">KSFILTER_DESCRIPTOR</a> member.</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566773">KsRegisterFilterWithNoKSPins</a> provides similar functionality, but should not be used if two instances of <a href="https://msdn.microsoft.com/library/windows/hardware/ff562553">KSFILTER_DESCRIPTOR</a> under the same <a href="https://msdn.microsoft.com/library/windows/hardware/ff561681">KSDEVICE</a> are registered in the same category, and differ only in reference GUID. In this case, <b>KsRegisterFilterWithNoKSPins</b> updates data only for the first, even though the second may have been specified.</p>

<p>Do not use this routine in place of <b>KsRegisterFilterWithNoKSPins</b> for filters with no KS pins, such as analog style crossbars. Use this routine only for a specific filter for which the minidriver is passing the corresponding filter factory.</p>

<p>In addition, <b>KsRegisterFilterWithNoKSPins</b> only allows one medium per registered pin. This may not be sufficient for a BDA minidriver.</p>

<p>For more information, see <a href="NULL">AVStream Object Hierarchy</a>.</p>

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
<p>Available in Microsoft Windows XP and later operating systems and DirectX 9.0 and later DirectX versions.</p>
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
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566773">KsRegisterFilterWithNoKSPins</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562553">KSFILTER_DESCRIPTOR</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562530">KSFILTERFACTORY</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KsFilterFactoryUpdateCacheData function%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
