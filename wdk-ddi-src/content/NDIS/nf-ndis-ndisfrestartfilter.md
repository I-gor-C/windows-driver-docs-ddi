---
UID: NF.ndis.NdisFRestartFilter
title: NdisFRestartFilter
author: windows-driver-content
description: A filter driver calls the NdisFRestartFilter function to request NDIS to initiate a restart operation for a filter module.
old-location: netvista\ndisfrestartfilter.htm
ms.assetid: 8b0fc032-3ec0-4e18-a5f5-6409db8ae42d
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: netvista
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Desktop
req.target-min-winverclnt: Supported in NDIS 6.0 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NdisFRestartFilter
req.alt-loc: ndis.lib,ndis.dll
req.ddi-compliance: Irql_Filter_Driver_Function
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ndis.lib
req.dll: 
req.irql: <= DISPATCH_LEVEL
ms.keywords: NdisFRestartFilter
req.iface: 
---

# NdisFRestartFilter function



## -description
<p>A filter driver calls the
  <b>NdisFRestartFilter</b> function to request NDIS to initiate a restart operation for a filter
  module.</p>


## -syntax

````
NDIS_STATUS NdisFRestartFilter(
  _In_ NDIS_HANDLE NdisFilterHandle
);
````


## -parameters
<dl>

### -param <i>NdisFilterHandle</i> [in]

<dd>
<p>The NDIS handle that identifies this filter module. NDIS passed the handle to the filter driver in
     a call to the 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff540442">FilterAttach</a> function.</p>
</dd>
</dl>

## -returns
<p><b>NdisFRestartFilter</b> returns one of the following status values:</p><dl>
<dt><b>NDIS_STATUS_SUCCESS</b></dt>
</dl><p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562611">NdisFRestartFilter</a> returns NDIS_STATUS_SUCCESS if it started the restart operation.</p><dl>
<dt><b>NDIS_STATUS_RESOURCES</b></dt>
</dl><p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562611">NdisFRestartFilter</a> failed because of insufficient resources.</p><dl>
<dt><b>NDIS_STATUS_FAILURE</b></dt>
</dl><p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562611">NdisFRestartFilter</a> returns NDIS_STATUS_FAILURE if none of the preceding values applies.</p>

<p> </p>

## -remarks
<p>The filter driver can change the filter module attributes at run time by calling the 
    <b>NdisFRestartFilter</b> function. 
    <b>NdisFRestartFilter</b> schedules a pause and then a restart operation for the specified filter
    module.</p>

<p>Before NDIS restarts the filter module, it calls the 
    <a href="https://msdn.microsoft.com/04b7ac32-8996-4648-8c88-aa9f630b1bc4">FilterSetModuleOptions</a> function for the filter module. From 
    its <i>FilterSetModuleOptions</i> function, the filter driver can change the data handlers for that filter module by
    calling the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff564550">NdisSetOptionalHandlers</a> function
    and specifying a new set of handlers.</p>

<p>The filter driver can change the filter module attributes at run time by calling the 
    <b>NdisFRestartFilter</b> function. 
    <b>NdisFRestartFilter</b> schedules a pause and then a restart operation for the specified filter
    module.</p>

<p>Before NDIS restarts the filter module, it calls the 
    <a href="https://msdn.microsoft.com/04b7ac32-8996-4648-8c88-aa9f630b1bc4">FilterSetModuleOptions</a> function for the filter module. From 
    its <i>FilterSetModuleOptions</i> function, the filter driver can change the data handlers for that filter module by
    calling the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff564550">NdisSetOptionalHandlers</a> function
    and specifying a new set of handlers.</p>

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
<p>Supported in NDIS 6.0 and later.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ndis.h (include Ndis.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Ndis.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;= DISPATCH_LEVEL</p>
</td>
</tr>
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547930">Irql_Filter_Driver_Function</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff540442">FilterAttach</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/04b7ac32-8996-4648-8c88-aa9f630b1bc4">FilterSetModuleOptions</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564550">NdisSetOptionalHandlers</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisFRestartFilter function%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
