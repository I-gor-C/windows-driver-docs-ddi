---
UID: NF.ks.KsFilterAddTopologyConnections
title: KsFilterAddTopologyConnections
author: windows-driver-content
description: The KsFilterAddTopologyConnections function adds new topology connections to a filter.
old-location: stream\ksfilteraddtopologyconnections.htm
ms.assetid: 32a61103-5f2f-4b73-a299-bf6a14c3bec9
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: stream
req.header: ks.h
req.include-header: Ks.h
req.target-type: Universal
req.target-min-winverclnt: Available in Microsoft Windows XP and later operating systems and DirectX 8.0 and later DirectX versions.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KsFilterAddTopologyConnections
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
req.irql: PASSIVE_LEVEL
ms.keywords: KsFilterAddTopologyConnections
req.iface: 
---

# KsFilterAddTopologyConnections function



## -description
<p>The<b> KsFilterAddTopologyConnections</b> function adds new topology connections to a filter.</p>


## -syntax

````
NTSTATUS KsFilterAddTopologyConnections(
  _In_       PKSFILTER             Filter,
  _In_       ULONG                 NewConnectionsCount,
  _In_ const KSTOPOLOGY_CONNECTION *NewTopologyConnections
);
````


## -parameters
<dl>

### -param <i>Filter</i> [in]

<dd>
<p><i>A pointer</i> to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff562522">KSFILTER</a> to which to add the new connections.</p>
</dd>

### -param <i>NewConnectionsCount</i> [in]

<dd>
<p>The number of connections in <i>NewTopologyConnections</i>.</p>
</dd>

### -param <i>NewTopologyConnections</i> [in]

<dd>
<p>A pointer to an array of <a href="https://msdn.microsoft.com/library/windows/hardware/ff567148">KSTOPOLOGY_CONNECTION</a> structures containing the new topology connections.</p>
</dd>
</dl>

## -returns
<p><b>KsFilterAddTopologyConnections </b>returns STATUS_SUCCESS or an error code indicating failure of the attempt to add topology connections.</p>

## -remarks
<p>Note that the filter control mutex must be held before calling this function.</p>

<p>For more information about mutexes, see <a href="NULL">Mutexes in AVStream</a>.</p>

<p>Note that the filter control mutex must be held before calling this function.</p>

<p>For more information about mutexes, see <a href="NULL">Mutexes in AVStream</a>.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562522">KSFILTER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567148">KSTOPOLOGY_CONNECTION</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KsFilterAddTopologyConnections function%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
