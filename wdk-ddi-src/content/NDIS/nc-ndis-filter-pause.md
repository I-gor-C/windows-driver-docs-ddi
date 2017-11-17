---
UID: NC.ndis.FILTER_PAUSE
title: FILTER_PAUSE
author: windows-driver-content
description: NDIS calls a filter driver's FilterPause function to initiate a pause operation for the specified filter module.Note  You must declare the function by using the FILTER_PAUSE type.
old-location: netvista\filterpause.htm
ms.assetid: a239889e-ec39-48fc-9e82-c8bc3d7ca51a
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: callback
ms.prod: windows-hardware
ms.technology: netvista
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Windows
req.target-min-winverclnt: Supported in NDIS 6.0 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FilterPause
req.alt-loc: Ndis.h
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
ms.keywords: RxNameCacheInitialize
req.iface: 
---

# FILTER_PAUSE callback



## -description
<p>NDIS calls a filter driver's 
  <i>FilterPause</i> function to initiate a pause operation for the specified filter module.</p>


## -prototype

````
FILTER_PAUSE FilterPause;

NDIS_STATUS FilterPause(
  _In_ NDIS_HANDLE                   FilterModuleContext,
  _In_ PNDIS_FILTER_PAUSE_PARAMETERS FilterPauseParameters
)
{ ... }
````


## -parameters
<dl>

### -param <i>FilterModuleContext</i> [in]

<dd>
<p>A handle to the context area for the filter module that the filter driver should pause. The filter
     driver created and initialized this context area in the 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff540442">FilterAttach</a> function.</p>
</dd>

### -param <i>FilterPauseParameters</i> [in]

<dd>
<p>A pointer to an 
     <a href="https://msdn.microsoft.com/070c6d5d-9942-4bff-8894-9aa69d5e7983">
     NDIS_FILTER_PAUSE_PARAMETERS</a> structure that defines the pause parameters for the filter
     module.</p>
</dd>
</dl>

## -returns
<p>NDIS drivers cannot fail a pause request. The filter driver should call the 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff564672">NdisWriteEventLogEntry</a> function
     together with parameters that specify the reason for any errors that occur.</p><dl>
<dt><b>NDIS_STATUS_SUCCESS</b></dt>
</dl><p><i>FilterPause</i> successfully paused the specified filter module.</p><dl>
<dt><b>NDIS_STATUS_PENDING</b></dt>
</dl><p>The filter driver will complete the request asynchronously with a call to the 
       <a href="https://msdn.microsoft.com/library/windows/hardware/ff561839">NdisFPauseComplete</a> function.</p>

<p> </p>

## -remarks
<p><i>FilterPause</i> is a required function. NDIS can call 
    <i>FilterPause</i> when the filter module is in the 
    <i>Running</i> state. The filter module enters the 
    <i>Pausing</i> state at the start of execution in the 
    <i>FilterPause</i> function.</p>

<p>A filter driver performs the following operations when NDIS calls 
    <i>FilterPause</i>:</p>

<p>Must call the 
      <a href="https://msdn.microsoft.com/5a9008eb-86ad-4e3c-85a2-c8fd1b8fb4cb">
      NdisFSendNetBufferListsComplete</a> function for any queued send buffers that an overlying driver
      created.</p>

<p>Must call the 
      <a href="https://msdn.microsoft.com/083cf25d-7436-4c4e-b29a-c9a2702b136d">
      NdisFReturnNetBufferLists</a> function for any queued receive buffers that an underlying driver
      created.</p>

<p>Must wait for NDIS to return all outstanding send requests that the driver originated to the 
      <a href="https://msdn.microsoft.com/1a3a1e80-29f1-4f19-b3c7-9a8b189f18c4">
      FilterSendNetBufferListsComplete</a> function.</p>

<p>Must wait for NDIS to return all outstanding receive indications that the driver originated to the 
      <a href="https://msdn.microsoft.com/8d7e362f-62da-4ce7-9497-1cfaff2b678e">
      FilterReturnNetBufferLists</a> function.</p>

<p>After the filter driver returns NDIS_STATUS_SUCCESS from 
    <i>FilterPause</i> or calls the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff561839">NdisFPauseComplete</a> function, the pause
    operation is complete. The filter module is in the 
    <i>Paused</i> state.</p>

<p>In the 
    <i>Pausing</i> or 
    <i>Paused</i> states, a filter driver should continue to handle OID requests or status indications. The
    driver should reject calls to its 
    <a href="https://msdn.microsoft.com/1b3fc0c8-95da-47e5-8ff1-b7967f5148e7">
    FilterSendNetBufferLists</a> function. The driver can pass on calls to its 
    <a href="https://msdn.microsoft.com/6359c2a7-1208-41ea-bbf9-015c91b6e8f6">
    FilterReceiveNetBufferLists</a> function. However, the driver cannot pass any buffers that it created.
    The driver must not originate any receive indications or send requests.</p>

<p>In the 
    <i>Paused</i> state, the filter module must not generate send requests or receive indications.</p>

<p>NDIS calls the 
    <a href="https://msdn.microsoft.com/4a917824-eef1-4945-b45e-1c940bc8a50d">FilterRestart</a> function to initiate a
    restart request for a filter module that is in the 
    <i>Paused</i> state.</p>

<p>NDIS calls 
    <i>FilterPause</i> at IRQL = PASSIVE_LEVEL.</p>

<p>To define a <i>FilterPause</i> function, you must first provide a function declaration that identifies the type of function you're defining. Windows provides a set of function types for drivers. Declaring a function using the function types helps <a href="NULL">Code Analysis for Drivers</a>, <a href="NULL">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it's a requirement for writing drivers for the Windows operating system.</p>

<p>For example, to define a <i>FilterPause</i> function that is named "MyPause", use the <b>FILTER_PAUSE</b> type as shown in this code example:</p>

<p>Then, implement your function as follows:</p>

<p>The <b>FILTER_PAUSE</b> function type is defined in the Ndis.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition.  The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the <b>FILTER_PAUSE</b> function type in the header file are used.  For more information about the requirements for function declarations, see <a href="NULL">Declaring Functions by Using Function Role Types for NDIS Drivers</a>.

For information about  _Use_decl_annotations_, see <a href="http://go.microsoft.com/fwlink/p/?linkid=286697">Annotating Function Behavior</a>. </p>

<p><i>FilterPause</i> is a required function. NDIS can call 
    <i>FilterPause</i> when the filter module is in the 
    <i>Running</i> state. The filter module enters the 
    <i>Pausing</i> state at the start of execution in the 
    <i>FilterPause</i> function.</p>

<p>A filter driver performs the following operations when NDIS calls 
    <i>FilterPause</i>:</p>

<p>Must call the 
      <a href="https://msdn.microsoft.com/5a9008eb-86ad-4e3c-85a2-c8fd1b8fb4cb">
      NdisFSendNetBufferListsComplete</a> function for any queued send buffers that an overlying driver
      created.</p>

<p>Must call the 
      <a href="https://msdn.microsoft.com/083cf25d-7436-4c4e-b29a-c9a2702b136d">
      NdisFReturnNetBufferLists</a> function for any queued receive buffers that an underlying driver
      created.</p>

<p>Must wait for NDIS to return all outstanding send requests that the driver originated to the 
      <a href="https://msdn.microsoft.com/1a3a1e80-29f1-4f19-b3c7-9a8b189f18c4">
      FilterSendNetBufferListsComplete</a> function.</p>

<p>Must wait for NDIS to return all outstanding receive indications that the driver originated to the 
      <a href="https://msdn.microsoft.com/8d7e362f-62da-4ce7-9497-1cfaff2b678e">
      FilterReturnNetBufferLists</a> function.</p>

<p>After the filter driver returns NDIS_STATUS_SUCCESS from 
    <i>FilterPause</i> or calls the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff561839">NdisFPauseComplete</a> function, the pause
    operation is complete. The filter module is in the 
    <i>Paused</i> state.</p>

<p>In the 
    <i>Pausing</i> or 
    <i>Paused</i> states, a filter driver should continue to handle OID requests or status indications. The
    driver should reject calls to its 
    <a href="https://msdn.microsoft.com/1b3fc0c8-95da-47e5-8ff1-b7967f5148e7">
    FilterSendNetBufferLists</a> function. The driver can pass on calls to its 
    <a href="https://msdn.microsoft.com/6359c2a7-1208-41ea-bbf9-015c91b6e8f6">
    FilterReceiveNetBufferLists</a> function. However, the driver cannot pass any buffers that it created.
    The driver must not originate any receive indications or send requests.</p>

<p>In the 
    <i>Paused</i> state, the filter module must not generate send requests or receive indications.</p>

<p>NDIS calls the 
    <a href="https://msdn.microsoft.com/4a917824-eef1-4945-b45e-1c940bc8a50d">FilterRestart</a> function to initiate a
    restart request for a filter module that is in the 
    <i>Paused</i> state.</p>

<p>NDIS calls 
    <i>FilterPause</i> at IRQL = PASSIVE_LEVEL.</p>

<p>To define a <i>FilterPause</i> function, you must first provide a function declaration that identifies the type of function you're defining. Windows provides a set of function types for drivers. Declaring a function using the function types helps <a href="NULL">Code Analysis for Drivers</a>, <a href="NULL">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it's a requirement for writing drivers for the Windows operating system.</p>

<p>For example, to define a <i>FilterPause</i> function that is named "MyPause", use the <b>FILTER_PAUSE</b> type as shown in this code example:</p>

<p>Then, implement your function as follows:</p>

<p>The <b>FILTER_PAUSE</b> function type is defined in the Ndis.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition.  The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the <b>FILTER_PAUSE</b> function type in the header file are used.  For more information about the requirements for function declarations, see <a href="NULL">Declaring Functions by Using Function Role Types for NDIS Drivers</a>.

For information about  _Use_decl_annotations_, see <a href="http://go.microsoft.com/fwlink/p/?linkid=286697">Annotating Function Behavior</a>. </p>

## -requirements
<table>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff540442">FilterAttach</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/6359c2a7-1208-41ea-bbf9-015c91b6e8f6">FilterReceiveNetBufferLists</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/4a917824-eef1-4945-b45e-1c940bc8a50d">FilterRestart</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/8d7e362f-62da-4ce7-9497-1cfaff2b678e">FilterReturnNetBufferLists</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/1b3fc0c8-95da-47e5-8ff1-b7967f5148e7">FilterSendNetBufferLists</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/1a3a1e80-29f1-4f19-b3c7-9a8b189f18c4">
   FilterSendNetBufferListsComplete</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff565547">NDIS_FILTER_PAUSE_PARAMETERS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566588">NDIS_OBJECT_HEADER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561839">NdisFPauseComplete</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562613">NdisFReturnNetBufferLists</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/5a9008eb-86ad-4e3c-85a2-c8fd1b8fb4cb">
   NdisFSendNetBufferListsComplete</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564672">NdisWriteEventLogEntry</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20FILTER_PAUSE callback function%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
