---
UID: NC.ndis.FILTER_RESTART
title: FILTER_RESTART
author: windows-driver-content
description: The FilterRestart function initiates a restart operation for the specified filter module.Note  You must declare the function by using the FILTER_RESTART type.
old-location: netvista\filterrestart.htm
old-project: netvista
ms.assetid: 4a917824-eef1-4945-b45e-1c940bc8a50d
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: RxNameCacheInitialize
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Windows
req.target-min-winverclnt: Supported in NDIS 6.0 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FilterRestart
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
req.iface: 
---

# FILTER_RESTART callback



## -description
<p>The 
  <i>FilterRestart</i> function initiates a restart operation for the specified filter module.</p>


## -prototype

````
FILTER_RESTART FilterRestart;

NDIS_STATUS FilterRestart(
  _In_ NDIS_HANDLE                     FilterModuleContext,
  _In_ PNDIS_FILTER_RESTART_PARAMETERS FilterRestartParameters
)
{ ... }
````


## -parameters
<dl>

### -param <i>FilterModuleContext</i> [in]

<dd>
<p>A handle to the context area for the filter module that the filter driver should restart. The
     filter driver created and initialized this context area in the 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff540442">FilterAttach</a> function.</p>
</dd>

### -param <i>FilterRestartParameters</i> [in]

<dd>
<p>A pointer to an 
     <a href="..\ndis\ns-ndis--ndis-filter-restart-parameters.md">
     NDIS_FILTER_RESTART_PARAMETERS</a> structure that defines the restart parameters for the filter
     module.</p>
</dd>
</dl>

## -returns
<p><i>FilterRestart</i> returns one of the following status values:</p><dl>
<dt><b>NDIS_STATUS_SUCCESS</b></dt>
</dl><p><i>FilterRestart</i> successfully restarted the specified filter module.</p><dl>
<dt><b>NDIS_STATUS_PENDING</b></dt>
</dl><p>The filter driver will complete the request asynchronously with a call to the 
       <a href="https://msdn.microsoft.com/library/windows/hardware/ff562610">NdisFRestartComplete</a> function
       after it completes the restart operation.</p><dl>
<dt><b>NDIS_STATUS_RESOURCES</b></dt>
</dl><p><i>FilterRestart</i> failed because of insufficient resources.</p><dl>
<dt><b>NDIS_STATUS_FAILURE</b></dt>
</dl><p>None of the preceding status values applies. The filter driver should call the 
       <a href="https://msdn.microsoft.com/library/windows/hardware/ff564672">NdisWriteEventLogEntry</a> function
       together with parameters that specify the reason for the failure.</p>

<p> </p>

## -remarks
<p><i>FilterRestart</i> is a required function for filter drivers. NDIS can call 
    <i>FilterRestart</i> when a filter module is in the 
    <i>Paused</i> state. The filter module enters the 
    <i>Restarting</i> state at the start of the execution of 
    <i>FilterRestart</i>.</p>

<p>When NDIS calls 
    <i>FilterRestart</i>, a filter driver:</p>

<p>Must complete the operations that are required to restart normal send and receive operations.</p>

<p>Optionally reads or writes configuration parameters.</p>

<p>Optionally reallocates buffer pools.</p>

<p>Optionally modifies the restart attributes that are specified in the 
      <b>RestartAttributes</b> member of the 
      <a href="..\ndis\ns-ndis--ndis-filter-restart-parameters.md">
      NDIS_FILTER_RESTART_PARAMETERS</a> structure. If the pointer in 
      <b>RestartAttributes</b> is <b>NULL</b>, the filter driver should not modify or add to the restart attributes
      list. If the pointer in 
      <b>RestartAttributes</b> is non-<b>NULL</b>, it points to the first 
      <a href="https://msdn.microsoft.com/library/windows/hardware/ff567255">NDIS_RESTART_ATTRIBUTES</a> structure
      in the list of restart attributes. If a filter driver does not restart, it should not modify any
      attributes.</p>

<p>Optionally uses OID requests to query or set information in the underlying drivers. Filter drivers
      should not issue OID requests for information that is already provided in the list of restart
      attributes.</p>

<p>Returns NDIS_STATUS_SUCCESS or a failure status.</p>

<p>If a filter driver modifies the list of restart attributes, the filter driver:</p>

<p>Should not modify any media-specific attributes if it does not recognize the OID in the 
      <b>Oid</b> member of the 
      <a href="..\ndis\ns-ndis--ndis-restart-attributes.md">
      NDIS_RESTART_ATTRIBUTES</a> structure.</p>

<p>Can add new media-specific attributes to the list of restart attributes. In this situation, the
      filter driver must allocate a new NDIS_RESTART_ATTRIBUTES structure--for example, with the 
      <a href="..\ndis\nf-ndis-ndisallocatememorywithtagpriority.md">
      NdisAllocateMemoryWithTagPriority</a> function--and provide memory space for the new attributes.
      After propagating the restart attributes to overlying drivers, NDIS frees the attributes memory for
      filter drivers.</p>

<p>Can modify the media-specific attributes in the list of restart attributes. If the filter driver
      requires more memory space, it can free the 
      <a href="https://msdn.microsoft.com/library/windows/hardware/ff567255">NDIS_RESTART_ATTRIBUTES</a> structure
      with the 
      <a href="https://msdn.microsoft.com/library/windows/hardware/ff562577">NdisFreeMemory</a> function and allocate a
      new structure to contain the modified information. After propagating the restart attributes to
      overlying drivers, NDIS frees the attributes memory for filter drivers.</p>

<p>Should, if the 
      <b>Oid</b> member in the NDIS_RESTART_ATTRIBUTES structure is 
      <a href="netvista.oid_gen_miniport_restart_attributes">
      OID_GEN_MINIPORT_RESTART_ATTRIBUTES</a>, make sure that the 
      <a href="..\ndis\ns-ndis--ndis-restart-general-attributes.md">
      NDIS_RESTART_GENERAL_ATTRIBUTES</a> structure contains the information that the filter driver
      requires. To make sure that the NDIS_RESTART_GENERAL_ATTRIBUTES structure contains the required
      information, you should check the 
      <b>Revision</b> member in the 
      <a href="https://msdn.microsoft.com/library/windows/hardware/ff566588">NDIS_OBJECT_HEADER</a> structure that is
      specified in the 
      <b>Header</b> member of the NDIS_RESTART_GENERAL_ATTRIBUTES structure.</p>

<p>Must, if the filter driver changes restart attributes, provide a 
      <a href="..\ndis\nc-ndis-filter-oid-request.md">FilterOidRequest</a> function. The
      filter driver must make sure that the information that overlying drivers receive in the restart
      attributes is consistent with the information that they receive in response to OID requests.</p>

<p>After the filter driver returns its status or calls the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff562610">NdisFRestartComplete</a> function, the
    restart operation is complete. If the operation completed successfully, the filter module is in the 
    <i>Running</i> state and normal send and receive processing is resumed. If the restart operation failed,
    the filter module returns to the 
    <i>Paused</i> state.</p>

<p>NDIS calls 
    <i>FilterRestart</i> at IRQL = PASSIVE_LEVEL.</p>

<p>To define a <i>FilterRestart</i> function, you must first provide a function declaration that identifies the type of function you're defining. Windows provides a set of function types for drivers. Declaring a function using the function types helps <a href="NULL">Code Analysis for Drivers</a>, <a href="NULL">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it's a requirement for writing drivers for the Windows operating system.</p>

<p>For example, to define a <i>FilterRestart</i> function that is named "MyRestart", use the <b>FILTER_RESTART</b> type as shown in this code example:</p>

<p>Then, implement your function as follows:</p>

<p>The <b>FILTER_RESTART</b> function type is defined in the Ndis.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition.  The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the <b>FILTER_RESTART</b> function type in the header file are used.  For more information about the requirements for function declarations, see <a href="NULL">Declaring Functions by Using Function Role Types for NDIS Drivers</a>.

For information about  _Use_decl_annotations_, see <a href="http://go.microsoft.com/fwlink/p/?linkid=286697">Annotating Function Behavior</a>. </p>

<p><i>FilterRestart</i> is a required function for filter drivers. NDIS can call 
    <i>FilterRestart</i> when a filter module is in the 
    <i>Paused</i> state. The filter module enters the 
    <i>Restarting</i> state at the start of the execution of 
    <i>FilterRestart</i>.</p>

<p>When NDIS calls 
    <i>FilterRestart</i>, a filter driver:</p>

<p>Must complete the operations that are required to restart normal send and receive operations.</p>

<p>Optionally reads or writes configuration parameters.</p>

<p>Optionally reallocates buffer pools.</p>

<p>Optionally modifies the restart attributes that are specified in the 
      <b>RestartAttributes</b> member of the 
      <a href="..\ndis\ns-ndis--ndis-filter-restart-parameters.md">
      NDIS_FILTER_RESTART_PARAMETERS</a> structure. If the pointer in 
      <b>RestartAttributes</b> is <b>NULL</b>, the filter driver should not modify or add to the restart attributes
      list. If the pointer in 
      <b>RestartAttributes</b> is non-<b>NULL</b>, it points to the first 
      <a href="https://msdn.microsoft.com/library/windows/hardware/ff567255">NDIS_RESTART_ATTRIBUTES</a> structure
      in the list of restart attributes. If a filter driver does not restart, it should not modify any
      attributes.</p>

<p>Optionally uses OID requests to query or set information in the underlying drivers. Filter drivers
      should not issue OID requests for information that is already provided in the list of restart
      attributes.</p>

<p>Returns NDIS_STATUS_SUCCESS or a failure status.</p>

<p>If a filter driver modifies the list of restart attributes, the filter driver:</p>

<p>Should not modify any media-specific attributes if it does not recognize the OID in the 
      <b>Oid</b> member of the 
      <a href="..\ndis\ns-ndis--ndis-restart-attributes.md">
      NDIS_RESTART_ATTRIBUTES</a> structure.</p>

<p>Can add new media-specific attributes to the list of restart attributes. In this situation, the
      filter driver must allocate a new NDIS_RESTART_ATTRIBUTES structure--for example, with the 
      <a href="..\ndis\nf-ndis-ndisallocatememorywithtagpriority.md">
      NdisAllocateMemoryWithTagPriority</a> function--and provide memory space for the new attributes.
      After propagating the restart attributes to overlying drivers, NDIS frees the attributes memory for
      filter drivers.</p>

<p>Can modify the media-specific attributes in the list of restart attributes. If the filter driver
      requires more memory space, it can free the 
      <a href="https://msdn.microsoft.com/library/windows/hardware/ff567255">NDIS_RESTART_ATTRIBUTES</a> structure
      with the 
      <a href="https://msdn.microsoft.com/library/windows/hardware/ff562577">NdisFreeMemory</a> function and allocate a
      new structure to contain the modified information. After propagating the restart attributes to
      overlying drivers, NDIS frees the attributes memory for filter drivers.</p>

<p>Should, if the 
      <b>Oid</b> member in the NDIS_RESTART_ATTRIBUTES structure is 
      <a href="netvista.oid_gen_miniport_restart_attributes">
      OID_GEN_MINIPORT_RESTART_ATTRIBUTES</a>, make sure that the 
      <a href="..\ndis\ns-ndis--ndis-restart-general-attributes.md">
      NDIS_RESTART_GENERAL_ATTRIBUTES</a> structure contains the information that the filter driver
      requires. To make sure that the NDIS_RESTART_GENERAL_ATTRIBUTES structure contains the required
      information, you should check the 
      <b>Revision</b> member in the 
      <a href="https://msdn.microsoft.com/library/windows/hardware/ff566588">NDIS_OBJECT_HEADER</a> structure that is
      specified in the 
      <b>Header</b> member of the NDIS_RESTART_GENERAL_ATTRIBUTES structure.</p>

<p>Must, if the filter driver changes restart attributes, provide a 
      <a href="..\ndis\nc-ndis-filter-oid-request.md">FilterOidRequest</a> function. The
      filter driver must make sure that the information that overlying drivers receive in the restart
      attributes is consistent with the information that they receive in response to OID requests.</p>

<p>After the filter driver returns its status or calls the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff562610">NdisFRestartComplete</a> function, the
    restart operation is complete. If the operation completed successfully, the filter module is in the 
    <i>Running</i> state and normal send and receive processing is resumed. If the restart operation failed,
    the filter module returns to the 
    <i>Paused</i> state.</p>

<p>NDIS calls 
    <i>FilterRestart</i> at IRQL = PASSIVE_LEVEL.</p>

<p>To define a <i>FilterRestart</i> function, you must first provide a function declaration that identifies the type of function you're defining. Windows provides a set of function types for drivers. Declaring a function using the function types helps <a href="NULL">Code Analysis for Drivers</a>, <a href="NULL">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it's a requirement for writing drivers for the Windows operating system.</p>

<p>For example, to define a <i>FilterRestart</i> function that is named "MyRestart", use the <b>FILTER_RESTART</b> type as shown in this code example:</p>

<p>Then, implement your function as follows:</p>

<p>The <b>FILTER_RESTART</b> function type is defined in the Ndis.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition.  The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the <b>FILTER_RESTART</b> function type in the header file are used.  For more information about the requirements for function declarations, see <a href="NULL">Declaring Functions by Using Function Role Types for NDIS Drivers</a>.

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
<a href="..\ndis\nc-ndis-filter-oid-request.md">FilterOidRequest</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-filter-status.md">FilterStatus</a>
</dt>
<dt>
<a href="..\ndis\ns-ndis--ndis-filter-restart-parameters.md">
   NDIS_FILTER_RESTART_PARAMETERS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566588">NDIS_OBJECT_HEADER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567255">NDIS_RESTART_ATTRIBUTES</a>
</dt>
<dt>
<a href="..\ndis\ns-ndis--ndis-restart-general-attributes.md">
   NDIS_RESTART_GENERAL_ATTRIBUTES</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567391">NDIS_STATUS_LINK_STATE</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndisallocatememorywithtagpriority.md">
   NdisAllocateMemoryWithTagPriority</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562577">NdisFreeMemory</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562608">NdisFRegisterFilterDriver</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562610">NdisFRestartComplete</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564672">NdisWriteEventLogEntry</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff569595">OID_GEN_LINK_STATE</a>
</dt>
<dt>
<a href="netvista.oid_gen_miniport_restart_attributes">
   OID_GEN_MINIPORT_RESTART_ATTRIBUTES</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20FILTER_RESTART callback function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
