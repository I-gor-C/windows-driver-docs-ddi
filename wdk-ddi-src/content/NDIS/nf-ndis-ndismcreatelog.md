---
UID: NF.ndis.NdisMCreateLog
title: NdisMCreateLog
author: windows-driver-content
description: NdisMCreateLog allocates and opens a log file in which a miniport driver can write data to be displayed by a driver-dedicated Win32 application.
old-location: netvista\ndismcreatelog.htm
ms.assetid: 804112cf-fc59-4a04-b848-4239b32e35d7
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: netvista
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Universal
req.target-min-winverclnt: Supported for NDIS 6.0 and NDIS 5.1 drivers (see 
   NdisMCreateLog (NDIS 5.1)) in
   Windows Vista. Supported for NDIS 5.1 drivers (see 
   NdisMCreateLog (NDIS 5.1)) in
   Windows XP.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NdisMCreateLog
req.alt-loc: ndis.lib,ndis.dll
req.ddi-compliance: Irql_Miniport_Driver_Function
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ndis.lib
req.dll: 
req.irql: PASSIVE_LEVEL
ms.keywords: NdisMCreateLog
req.iface: 
---

# NdisMCreateLog function



## -description
<p><b>NdisMCreateLog</b> allocates and opens a log file in which a miniport driver can write data to be
  displayed by a driver-dedicated Win32 application.</p>


## -syntax

````
NDIS_STATUS NdisMCreateLog(
  _In_  NDIS_HANDLE  MiniportAdapterHandle,
  _In_  UINT         Size,
  _Out_ PNDIS_HANDLE LogHandle
);
````


## -parameters
<dl>

### -param <i>MiniportAdapterHandle</i> [in]

<dd>
<p>Specifies the handle input to 
     <a href="https://msdn.microsoft.com/b146fa81-005b-4a6c-962d-4cb023ea790e">MiniportInitializeEx</a>.</p>
</dd>

### -param <i>Size</i> [in]

<dd>
<p>Specifies how many bytes to allocate for the log file. NDIS creates a temporary file that is not
     stored on disk.</p>
</dd>

### -param <i>LogHandle</i> [out]

<dd>
<p>Pointer to a caller-supplied variable in which this function returns a handle to the log file.
     This handle is a required parameter to the 
     <b>Ndis</b><i>Xxx</i><b>Log</b> functions that the miniport driver calls subsequently.</p>
</dd>
</dl>

## -returns
<p><b>NdisMCreateLog</b> can return one of the following:</p><dl>
<dt><b>NDIS_STATUS_SUCCESS</b></dt>
</dl><p>The miniport driver can use the handle returned at 
       <i>LogHandle</i> to write data to the NDIS-allocated log file.</p><dl>
<dt><b>NDIS_STATUS_RESOURCES</b></dt>
</dl><p>A log file of the specified size could not be allocated.</p><dl>
<dt><b>NDIS_STATUS_FAILURE</b></dt>
</dl><p>The driver already called 
       <b>NdisMCreateLog</b> successfully.</p>

<p> </p>

## -remarks
<p>A miniport driver can call the 
    <b>NdisM..Log</b> functions to provide any information the driver writer chooses. Whatever the miniport
    driver logs can be displayed by a driver-dedicated Win32 application. Such an application calls the Win32
    function 
    <a href="base.deviceiocontrol">DeviceIoControl</a> with IOCTL_NDIS_GET_LOG_DATA periodically to retrieve whatever the miniport driver
    has written to the log file. For example, an under-development miniport driver might write test data to
    be displayed by its corresponding application.</p>

<p>If 
    <b>NdisMCreateLog</b> returns NDIS_STATUS_RESOURCES, the driver can adjust the original 
    <i>Size</i> down and try calling this function again. However, a miniport driver cannot call 
    <b>NdisMCreateLog</b> to create more than one log file after a call succeeds.</p>

<p>Whatever size of log file is allocated, subsequent calls to 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff563695">NdisMWriteLogData</a> store data in this
    file, which is treated as a circular buffer. That is, a sequence of calls to 
    <b>NdisMWriteLogData</b> eventually overwrites the data originally written to the log file.</p>

<p>A miniport driver can call the 
    <b>NdisM..Log</b> functions to provide any information the driver writer chooses. Whatever the miniport
    driver logs can be displayed by a driver-dedicated Win32 application. Such an application calls the Win32
    function 
    <a href="base.deviceiocontrol">DeviceIoControl</a> with IOCTL_NDIS_GET_LOG_DATA periodically to retrieve whatever the miniport driver
    has written to the log file. For example, an under-development miniport driver might write test data to
    be displayed by its corresponding application.</p>

<p>If 
    <b>NdisMCreateLog</b> returns NDIS_STATUS_RESOURCES, the driver can adjust the original 
    <i>Size</i> down and try calling this function again. However, a miniport driver cannot call 
    <b>NdisMCreateLog</b> to create more than one log file after a call succeeds.</p>

<p>Whatever size of log file is allocated, subsequent calls to 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff563695">NdisMWriteLogData</a> store data in this
    file, which is treated as a circular buffer. That is, a sequence of calls to 
    <b>NdisMWriteLogData</b> eventually overwrites the data originally written to the log file.</p>

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
<p>Supported for NDIS 6.0 and NDIS 5.1 drivers (see 
   <a href="https://msdn.microsoft.com/library/windows/hardware/ff553481">NdisMCreateLog (NDIS 5.1)</a>) in
   Windows Vista. Supported for NDIS 5.1 drivers (see 
   <b>NdisMCreateLog (NDIS 5.1)</b>) in
   Windows XP.</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547979">Irql_Miniport_Driver_Function</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/b146fa81-005b-4a6c-962d-4cb023ea790e">MiniportInitializeEx</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562790">NdisMCloseLog</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563584">NdisMFlushLog</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563695">NdisMWriteLogData</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisMCreateLog function%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
