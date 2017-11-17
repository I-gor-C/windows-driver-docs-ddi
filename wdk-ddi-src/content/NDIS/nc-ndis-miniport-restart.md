---
UID: NC.ndis.MINIPORT_RESTART
title: MINIPORT_RESTART
author: windows-driver-content
description: The MiniportRestart function initiates a restart request for a miniport adapter that is paused.
old-location: netvista\miniportrestart.htm
ms.assetid: 31a18040-2c66-4074-9ace-dd604b4bfe22
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
req.alt-api: MiniportRestart
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

# MINIPORT_RESTART callback



## -description
<p>The 
   <i>MiniportRestart</i> function initiates a restart request for a miniport adapter that
   is paused.</p>


## -prototype

````
MINIPORT_RESTART MiniportRestart;

NDIS_STATUS MiniportRestart(
  _In_ NDIS_HANDLE                       MiniportAdapterContext,
  _In_ PNDIS_MINIPORT_RESTART_PARAMETERS MiniportRestartParameters
)
{ ... }
````


## -parameters
<dl>

### -param <i>MiniportAdapterContext</i> [in]

<dd>
<p>A handle to a context area that the miniport driver allocated in its 
     <a href="https://msdn.microsoft.com/b146fa81-005b-4a6c-962d-4cb023ea790e">MiniportInitializeEx</a> function.
     The miniport driver uses this context area to maintain state information for a miniport adapter.</p>
</dd>

### -param <i>MiniportRestartParameters</i> [in]

<dd>
<p>A pointer to an 
     <a href="https://msdn.microsoft.com/4e005245-ed98-47fd-aaae-421940edf2dc">
     NDIS_MINIPORT_RESTART_PARAMETERS</a> structure that defines the restart parameters for the miniport
     adapter.</p>
</dd>
</dl>

## -returns
<p><i>MiniportRestart</i> returns one of the following status values:</p><dl>
<dt><b>NDIS_STATUS_SUCCESS</b></dt>
</dl><p>
<a href="https://msdn.microsoft.com/31a18040-2c66-4074-9ace-dd604b4bfe22">MiniportRestart</a> successfully restarted the flow of network data through the
       miniport adapter.</p><dl>
<dt><b>NDIS_STATUS_PENDING</b></dt>
</dl><p><i>MiniportRestart</i> did not complete the restart operation and the operation
       will be completed asynchronously. The miniport driver must call the 
       <a href="https://msdn.microsoft.com/library/windows/hardware/ff563665">NdisMRestartComplete</a> function when
       the operation is complete.</p><dl>
<dt><b>NDIS_STATUS_RESOURCES</b></dt>
</dl><p>
<a href="https://msdn.microsoft.com/31a18040-2c66-4074-9ace-dd604b4bfe22">MiniportRestart</a> failed because of insufficient resources.</p><dl>
<dt><b>NDIS_STATUS_FAILURE</b></dt>
</dl><p>None of the preceding status values applies. In this situation, the driver should call the 
       <a href="https://msdn.microsoft.com/library/windows/hardware/ff564663">NdisWriteErrorLogEntry</a> function
       with parameters that specify the reason for the failure.</p>

<p> </p>

## -remarks
<p>A driver specifies the 
    <i>MiniportRestart</i> entry point when it calls the 
    <a href="https://msdn.microsoft.com/bed68aa8-499d-41fd-997b-a46316913cc8">
    NdisMRegisterMiniportDriver</a> function.</p>

<p>The miniport adapter that is specified by the 
    <i>MiniportAdapterContext</i> parameter enters the 
    <i>Restarting</i> state when NDIS calls 
    <i>MiniportRestart</i>.</p>

<p>When NDIS calls 
    <i>MiniportRestart</i>, a miniport driver:</p>

<p>Must complete any tasks that are required to resume send and receive operations.</p>

<p>Optionally modifies the restart attributes that are specified in the 
      <b>RestartAttributes</b> member of the 
      <a href="https://msdn.microsoft.com/4e005245-ed98-47fd-aaae-421940edf2dc">
      NDIS_MINIPORT_RESTART_PARAMETERS</a> structure. If the pointer in 
      <b>RestartAttributes</b> is <b>NULL</b>, the miniport driver should not modify or add to the restart attributes
      list. If the pointer in 
      <b>RestartAttributes</b> is non-<b>NULL</b>, it points to an 
      <a href="https://msdn.microsoft.com/library/windows/hardware/ff567255">NDIS_RESTART_ATTRIBUTES</a> structure.
      If a miniport driver does not restart, it should not modify any attributes.</p>

<p>Can provide status indications with the 
      <a href="https://msdn.microsoft.com/df857349-4ae1-470b-b41a-ff014f40b79b">
      NdisMIndicateStatusEx</a> function.</p>

<p>Should handle status requests in the 
      <a href="https://msdn.microsoft.com/733d84f5-c1d4-42a0-a59b-4ba50247f165">MiniportOidRequest</a> function.</p>

<p>If a miniport driver modifies the list of restart attributes, the miniport driver:</p>

<p>Can add new media-specific attributes to the list of restart attributes. In this situation, the
      miniport driver must allocate a new 
      <a href="https://msdn.microsoft.com/1f9f4b91-bd1f-4daa-ac98-6372bf55c2ab">
      NDIS_RESTART_ATTRIBUTES</a> structure--for example, with the 
      <a href="https://msdn.microsoft.com/aac4049c-a876-4bbb-ba3b-fa36c299e1c7">
      NdisAllocateMemoryWithTagPriority</a> function--and provide memory space for the new attributes.
      After propagating the restart attributes to overlying drivers, NDIS frees the attributes memory for the
      miniport drivers.</p>

<p>Can modify the media-specific attributes in the list of restart attributes. If the miniport driver
      requires more memory space, it can free an NDIS_RESTART_ATTRIBUTES structure with the 
      <a href="https://msdn.microsoft.com/library/windows/hardware/ff562577">NdisFreeMemory</a> function and allocate a
      new structure to contain the modified information. After propagating the restart attributes to
      overlying drivers, NDIS frees the attributes memory for the miniport drivers.</p>

<p>Can modify any field in the 
      <a href="https://msdn.microsoft.com/f67bd2fe-4553-4b1a-8d39-26777bcc60e0">
      NDIS_RESTART_GENERAL_ATTRIBUTES</a> structure. When NDIS provides a non-<b>NULL</b> pointer in the 
      <b>RestartAttributes</b> member of the 
      <a href="https://msdn.microsoft.com/4e005245-ed98-47fd-aaae-421940edf2dc">
      NDIS_MINIPORT_RESTART_PARAMETERS</a> structure, the attributes list contains one entry in which the 
      <b>Oid</b> member in the 
      <a href="https://msdn.microsoft.com/library/windows/hardware/ff567255">NDIS_RESTART_ATTRIBUTES</a> structure
      is 
      <a href="netvista.oid_gen_miniport_restart_attributes">
      OID_GEN_MINIPORT_RESTART_ATTRIBUTES</a> and the 
      <b>Data</b> member contains an NDIS_RESTART_GENERAL_ATTRIBUTES structure.</p>

<p>Should make sure that the 
      <a href="https://msdn.microsoft.com/f67bd2fe-4553-4b1a-8d39-26777bcc60e0">
      NDIS_RESTART_GENERAL_ATTRIBUTES</a> structure contains the correct information. To make sure that the
      NDIS_RESTART_GENERAL_ATTRIBUTES structure contains the required information, you should first determine
      the version of the structure by checking the 
      <b>Revision</b> member in the 
      <a href="https://msdn.microsoft.com/library/windows/hardware/ff566588">NDIS_OBJECT_HEADER</a> structure that is
      specified in the 
      <b>Header</b> member of the NDIS_RESTART_GENERAL_ATTRIBUTES structure.</p>

<p>NDIS does not initiate other Plug and Play (PnP) operations for the miniport adapter, such as halt,
    initialize, power change, or a pause request, until the restart operation is complete.</p>

<p>After the miniport driver successfully restarts the send and receive operations, it must complete the
    restart operation. If the driver returns NDIS_STATUS_SUCCESS from 
    <i>MiniportRestart</i>, the restart operation is complete. If the driver returns
    NDIS_STATUS_PENDING, it can continue restart operations. The restart operation is complete after the
    driver calls the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff563665">NdisMRestartComplete</a> function. After
    the restart operation is complete, the miniport adapter is in the 
    <i>Running</i> state.</p>

<p>The miniport driver can resume indicating received packets for the miniport adapter immediately after
    NDIS calls 
    <i>MiniportRestart</i> and before the driver calls 
    <b>NdisMRestartComplete</b>. The miniport driver should be ready to accept send requests after the driver
    completes the restart request.</p>

<p>If the miniport driver does not restart the send and receive operations, the driver must return an
    appropriate failure status from 
    <i>MiniportRestart</i>. In this situation, the driver must stop any send or receive
    operations that were started and then return to the 
    <i>Paused</i> state.</p>

<p>NDIS calls 
    <i>MiniportRestart</i> at IRQL = PASSIVE_LEVEL.</p>

<p>To define a <i>MiniportRestart</i> function, you must first provide a function declaration that identifies the type of function you're defining. Windows provides a set of function types for drivers. Declaring a function using the function types helps <a href="NULL">Code Analysis for Drivers</a>, <a href="NULL">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it's a requirement for writing drivers for the Windows operating system.</p>

<p>For example, to define a <i>MiniportRestart</i> function that is named "MyRestart", use the <b>MINIPORT_RESTART</b> type as shown in this code example:</p>

<p>Then, implement your function as follows:</p>

<p>The <b>MINIPORT_RESTART</b> function type is defined in the Ndis.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition.  The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the <b>MINIPORT_RESTART</b> function type in the header file are used.  For more information about the requirements for function declarations, see <a href="NULL">Declaring Functions by Using Function Role Types for NDIS Drivers</a>.

For information about  _Use_decl_annotations_, see <a href="http://go.microsoft.com/fwlink/p/?linkid=286697">Annotating Function Behavior</a>. </p>

<p>A driver specifies the 
    <i>MiniportRestart</i> entry point when it calls the 
    <a href="https://msdn.microsoft.com/bed68aa8-499d-41fd-997b-a46316913cc8">
    NdisMRegisterMiniportDriver</a> function.</p>

<p>The miniport adapter that is specified by the 
    <i>MiniportAdapterContext</i> parameter enters the 
    <i>Restarting</i> state when NDIS calls 
    <i>MiniportRestart</i>.</p>

<p>When NDIS calls 
    <i>MiniportRestart</i>, a miniport driver:</p>

<p>Must complete any tasks that are required to resume send and receive operations.</p>

<p>Optionally modifies the restart attributes that are specified in the 
      <b>RestartAttributes</b> member of the 
      <a href="https://msdn.microsoft.com/4e005245-ed98-47fd-aaae-421940edf2dc">
      NDIS_MINIPORT_RESTART_PARAMETERS</a> structure. If the pointer in 
      <b>RestartAttributes</b> is <b>NULL</b>, the miniport driver should not modify or add to the restart attributes
      list. If the pointer in 
      <b>RestartAttributes</b> is non-<b>NULL</b>, it points to an 
      <a href="https://msdn.microsoft.com/library/windows/hardware/ff567255">NDIS_RESTART_ATTRIBUTES</a> structure.
      If a miniport driver does not restart, it should not modify any attributes.</p>

<p>Can provide status indications with the 
      <a href="https://msdn.microsoft.com/df857349-4ae1-470b-b41a-ff014f40b79b">
      NdisMIndicateStatusEx</a> function.</p>

<p>Should handle status requests in the 
      <a href="https://msdn.microsoft.com/733d84f5-c1d4-42a0-a59b-4ba50247f165">MiniportOidRequest</a> function.</p>

<p>If a miniport driver modifies the list of restart attributes, the miniport driver:</p>

<p>Can add new media-specific attributes to the list of restart attributes. In this situation, the
      miniport driver must allocate a new 
      <a href="https://msdn.microsoft.com/1f9f4b91-bd1f-4daa-ac98-6372bf55c2ab">
      NDIS_RESTART_ATTRIBUTES</a> structure--for example, with the 
      <a href="https://msdn.microsoft.com/aac4049c-a876-4bbb-ba3b-fa36c299e1c7">
      NdisAllocateMemoryWithTagPriority</a> function--and provide memory space for the new attributes.
      After propagating the restart attributes to overlying drivers, NDIS frees the attributes memory for the
      miniport drivers.</p>

<p>Can modify the media-specific attributes in the list of restart attributes. If the miniport driver
      requires more memory space, it can free an NDIS_RESTART_ATTRIBUTES structure with the 
      <a href="https://msdn.microsoft.com/library/windows/hardware/ff562577">NdisFreeMemory</a> function and allocate a
      new structure to contain the modified information. After propagating the restart attributes to
      overlying drivers, NDIS frees the attributes memory for the miniport drivers.</p>

<p>Can modify any field in the 
      <a href="https://msdn.microsoft.com/f67bd2fe-4553-4b1a-8d39-26777bcc60e0">
      NDIS_RESTART_GENERAL_ATTRIBUTES</a> structure. When NDIS provides a non-<b>NULL</b> pointer in the 
      <b>RestartAttributes</b> member of the 
      <a href="https://msdn.microsoft.com/4e005245-ed98-47fd-aaae-421940edf2dc">
      NDIS_MINIPORT_RESTART_PARAMETERS</a> structure, the attributes list contains one entry in which the 
      <b>Oid</b> member in the 
      <a href="https://msdn.microsoft.com/library/windows/hardware/ff567255">NDIS_RESTART_ATTRIBUTES</a> structure
      is 
      <a href="netvista.oid_gen_miniport_restart_attributes">
      OID_GEN_MINIPORT_RESTART_ATTRIBUTES</a> and the 
      <b>Data</b> member contains an NDIS_RESTART_GENERAL_ATTRIBUTES structure.</p>

<p>Should make sure that the 
      <a href="https://msdn.microsoft.com/f67bd2fe-4553-4b1a-8d39-26777bcc60e0">
      NDIS_RESTART_GENERAL_ATTRIBUTES</a> structure contains the correct information. To make sure that the
      NDIS_RESTART_GENERAL_ATTRIBUTES structure contains the required information, you should first determine
      the version of the structure by checking the 
      <b>Revision</b> member in the 
      <a href="https://msdn.microsoft.com/library/windows/hardware/ff566588">NDIS_OBJECT_HEADER</a> structure that is
      specified in the 
      <b>Header</b> member of the NDIS_RESTART_GENERAL_ATTRIBUTES structure.</p>

<p>NDIS does not initiate other Plug and Play (PnP) operations for the miniport adapter, such as halt,
    initialize, power change, or a pause request, until the restart operation is complete.</p>

<p>After the miniport driver successfully restarts the send and receive operations, it must complete the
    restart operation. If the driver returns NDIS_STATUS_SUCCESS from 
    <i>MiniportRestart</i>, the restart operation is complete. If the driver returns
    NDIS_STATUS_PENDING, it can continue restart operations. The restart operation is complete after the
    driver calls the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff563665">NdisMRestartComplete</a> function. After
    the restart operation is complete, the miniport adapter is in the 
    <i>Running</i> state.</p>

<p>The miniport driver can resume indicating received packets for the miniport adapter immediately after
    NDIS calls 
    <i>MiniportRestart</i> and before the driver calls 
    <b>NdisMRestartComplete</b>. The miniport driver should be ready to accept send requests after the driver
    completes the restart request.</p>

<p>If the miniport driver does not restart the send and receive operations, the driver must return an
    appropriate failure status from 
    <i>MiniportRestart</i>. In this situation, the driver must stop any send or receive
    operations that were started and then return to the 
    <i>Paused</i> state.</p>

<p>NDIS calls 
    <i>MiniportRestart</i> at IRQL = PASSIVE_LEVEL.</p>

<p>To define a <i>MiniportRestart</i> function, you must first provide a function declaration that identifies the type of function you're defining. Windows provides a set of function types for drivers. Declaring a function using the function types helps <a href="NULL">Code Analysis for Drivers</a>, <a href="NULL">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it's a requirement for writing drivers for the Windows operating system.</p>

<p>For example, to define a <i>MiniportRestart</i> function that is named "MyRestart", use the <b>MINIPORT_RESTART</b> type as shown in this code example:</p>

<p>Then, implement your function as follows:</p>

<p>The <b>MINIPORT_RESTART</b> function type is defined in the Ndis.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition.  The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the <b>MINIPORT_RESTART</b> function type in the header file are used.  For more information about the requirements for function declarations, see <a href="NULL">Declaring Functions by Using Function Role Types for NDIS Drivers</a>.

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
<a href="https://msdn.microsoft.com/b146fa81-005b-4a6c-962d-4cb023ea790e">MiniportInitializeEx</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/047241a5-6f52-4a82-a334-8508f0de5e1a">MiniportPause</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/733d84f5-c1d4-42a0-a59b-4ba50247f165">MiniportOidRequest</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/4e005245-ed98-47fd-aaae-421940edf2dc">
   NDIS_MINIPORT_RESTART_PARAMETERS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566588">NDIS_OBJECT_HEADER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567255">NDIS_RESTART_ATTRIBUTES</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/f67bd2fe-4553-4b1a-8d39-26777bcc60e0">
   NDIS_RESTART_GENERAL_ATTRIBUTES</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/aac4049c-a876-4bbb-ba3b-fa36c299e1c7">
   NdisAllocateMemoryWithTagPriority</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562577">NdisFreeMemory</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563600">NdisMIndicateStatusEx</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563654">NdisMRegisterMiniportDriver</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563665">NdisMRestartComplete</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564663">NdisWriteErrorLogEntry</a>
</dt>
<dt>
<a href="netvista.oid_gen_miniport_restart_attributes">
   OID_GEN_MINIPORT_RESTART_ATTRIBUTES</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20MINIPORT_RESTART callback function%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
