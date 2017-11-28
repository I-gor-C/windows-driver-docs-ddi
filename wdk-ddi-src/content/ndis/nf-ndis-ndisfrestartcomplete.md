---
UID: NF.ndis.NdisFRestartComplete
title: NdisFRestartComplete
author: windows-driver-content
description: A filter driver must call the NdisFRestartComplete function to complete a restart operation if the driver returned NDIS_STATUS_PENDING from its FilterRestart function.
old-location: netvista\ndisfrestartcomplete.htm
old-project: netvista
ms.assetid: 84685763-e7d8-4184-afa3-83efb4a0d3d7
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: NdisFRestartComplete
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Desktop
req.target-min-winverclnt: Supported in NDIS 6.0 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NdisFRestartComplete
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
req.irql: PASSIVE_LEVEL
req.iface: 
---

# NdisFRestartComplete function



## -description
<p>A filter driver must call the 
  <b>NdisFRestartComplete</b> function to complete a restart operation if the driver returned
  NDIS_STATUS_PENDING from its 
  <a href="..\ndis\nc-ndis-filter-restart.md">FilterRestart</a> function.</p>


## -syntax

````
VOID NdisFRestartComplete(
  _In_ NDIS_HANDLE NdisFilterHandle,
  _In_ NDIS_STATUS Status
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

### -param <i>Status</i> [in]

<dd>
<p>The final status of the restart operation. The following status values are supported:
     </p>
<p></p>
<dl>

### -param <a id="NDIS_STATUS_SUCCESS"></a><a id="ndis_status_success"></a>NDIS_STATUS_SUCCESS

<dd>
<p>The driver successfully restarted the flow of network data.</p>
</dd>

### -param <a id="NDIS_STATUS_RESOURCES"></a><a id="ndis_status_resources"></a>NDIS_STATUS_RESOURCES

<dd>
<p>The restart failed because of insufficient resources.</p>
</dd>

### -param <a id="NDIS_STATUS_FAILURE"></a><a id="ndis_status_failure"></a>NDIS_STATUS_FAILURE

<dd>
<p>The driver indicates NDIS_STATUS_FAILURE if none of the preceding values applies. The driver
       should call the 
       <a href="https://msdn.microsoft.com/library/windows/hardware/ff564672">NdisWriteEventLogEntry</a> function
       together with parameters that specify the reason for the failure.</p>
</dd>
</dl>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>NDIS calls a filter driver's 
    <a href="..\ndis\nc-ndis-filter-restart.md">FilterRestart</a> function to initiate a
    restart request for filter module. The filter module remains in the 
    <i>Restarting</i> state until the restart operation is complete.</p>

<p>A pending restart operation is complete after the driver calls the 
    <b>NdisFRestartComplete</b> function. The filter module is in the 
    <i>Running</i> state after the restart operation is complete.</p>

<p>A filter driver can resume indicating received network data immediately after NDIS calls 
    <i>FilterRestart</i> and before the driver calls 
    <b>NdisFRestartComplete</b>. The driver should be ready to accept send requests after it completes the
    restart operation.</p>

<p>NDIS calls a filter driver's 
    <a href="..\ndis\nc-ndis-filter-restart.md">FilterRestart</a> function to initiate a
    restart request for filter module. The filter module remains in the 
    <i>Restarting</i> state until the restart operation is complete.</p>

<p>A pending restart operation is complete after the driver calls the 
    <b>NdisFRestartComplete</b> function. The filter module is in the 
    <i>Running</i> state after the restart operation is complete.</p>

<p>A filter driver can resume indicating received network data immediately after NDIS calls 
    <i>FilterRestart</i> and before the driver calls 
    <b>NdisFRestartComplete</b>. The driver should be ready to accept send requests after it completes the
    restart operation.</p>

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
<p>PASSIVE_LEVEL</p>
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
<a href="..\ndis\nc-ndis-filter-restart.md">FilterRestart</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564672">NdisWriteEventLogEntry</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisFRestartComplete function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
