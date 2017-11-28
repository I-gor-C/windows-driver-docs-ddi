---
UID: NF.ks.KsProcessPinUpdate
title: KsProcessPinUpdate
author: windows-driver-content
description: The KsProcessPinUpdate function is called from within a filter-centric filter's AVStrMiniFilterProcess dispatch to update a process pin.
old-location: stream\ksprocesspinupdate.htm
old-project: stream
ms.assetid: 9f6c28ad-d3dd-4be4-a637-10958a9cbd20
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: KsProcessPinUpdate
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ks.h
req.include-header: Ks.h
req.target-type: Universal
req.target-min-winverclnt: Available in Microsoft Windows XP and later operating systems and DirectX 8.0 and later DirectX versions.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KsProcessPinUpdate
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
req.iface: 
---

# KsProcessPinUpdate function



## -description
<p>The <b>KsProcessPinUpdate</b> function is called from within a filter-centric filter's <a href="https://msdn.microsoft.com/library/windows/hardware/ff556315">AVStrMiniFilterProcess</a> dispatch to update a process pin.</p>


## -syntax

````
BOOLEAN KsProcessPinUpdate(
  _In_ PKSPROCESSPIN ProcessPin
);
````


## -parameters
<dl>

### -param <i>ProcessPin</i> [in]

<dd>
<p>A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff564256">KSPROCESSPIN</a> structure that represents the process pin to update.</p>
</dd>
</dl>

## -returns
<p><b>KsProcessPinUpdate</b> returns <b>TRUE</b> if <i>ProcessPin</i>'s conditions for processing are met; otherwise, it returns <b>FALSE</b>. (These conditions are set in the pin descriptor within the <b>Pin</b> member of <i>ProcessPin</i>.) If the minidriver's dispatch calls this routine while the filter is in the STOP state, <b>KsProcessPinUpdate</b> returns <b>FALSE</b> since no pipe exists.</p>

## -remarks
<p>For more information, see <a href="NULL">Filter-Centric Processing</a>.</p>

<p>For more information, see <a href="NULL">Filter-Centric Processing</a>.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564256">KSPROCESSPIN</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564260">KSPROCESSPIN_INDEXENTRY</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KsProcessPinUpdate function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
