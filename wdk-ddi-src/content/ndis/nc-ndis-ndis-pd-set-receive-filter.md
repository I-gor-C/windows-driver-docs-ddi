---
UID: NC.ndis.NDIS_PD_SET_RECEIVE_FILTER
title: NDIS_PD_SET_RECEIVE_FILTER
author: windows-driver-content
description: The PacketDirect (PD) platform calls a PD-capable miniport driver's NdisPDSetReceiveFilter function to direct specific flows of packets to a specific PD receive queue.
old-location: netvista\ndispdsetreceivefilter.htm
old-project: netvista
ms.assetid: 49587142-9C84-4F73-BE0C-D256A8E6BF4B
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: RxNameCacheInitialize
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: ndis.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NdisPDSetReceiveFilter
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

# NDIS_PD_SET_RECEIVE_FILTER callback



## -description
<p>The PacketDirect (PD) platform calls a PD-capable miniport driver's 
   <i>NdisPDSetReceiveFilter</i> function to direct specific flows of packets to a specific PD receive queue.<div class="alert"><b>Note</b>  You must declare the function by using the <b>NDIS_PD_SET_RECEIVE_FILTER</b> type. For more
   information, see the following Examples section.</div>
<div> </div>
</p>


## -prototype

````
NDIS_PD_SET_RECEIVE_FILTER NdisPDSetReceiveFilter;

NTSTATUS NdisPDSetReceiveFilter(
  _In_        NDIS_PD_PROVIDER_HANDLE   ProviderHandle,
  _In_  const NDIS_PD_FILTER_PARAMETERS *FilterParameters,
  _Out_       NDIS_PD_FILTER_HANDLE     *FilterHandle
)
{ ... }
````


## -parameters
<dl>

### -param <i>ProviderHandle</i> [in]

<dd>
<p>A provider handle that identifies the PD-capable miniport driver's provider object.</p>
</dd>

### -param <i>FilterParameters</i> [in]

<dd>
<p>Parameters that identify any necessary information for the filter. For more information, see the <a href="https://msdn.microsoft.com/library/windows/hardware/dn931840">NDIS_PD_FILTER_PARAMETERS</a> structure.</p>
</dd>

### -param <i>FilterHandle</i> [out]

<dd>
<p>A handle to the filter.</p>
</dd>
</dl>

## -returns
<p>This function returns STATUS_SUCCESS when it completes successful, otherwise it returns the appropriate error code.</p>

## -remarks
<p>PD filters are applied before any spreading takes place this is why packet matching a PD filter can be placed into their dedicated PD queue, and the rest of the packets can be spread by RSS as usual. The PD client is responsible for plumbing non-overlapping ambiguous filters. However, some PD provides may allow overlapping ambiguous filters as long as the PD client can pass a priority value that indicates which filter must be applied first. The PD provider may fail filter set requests with STATUS_NOT_SUPPORTED if the client attempts to set filters with conflicting profiles or overlapping match conditions. The <a href="https://msdn.microsoft.com/library/windows/hardware/dn931833">NDIS_PD_CAPABILITIES</a> structure does not allow the provider to advertise all valid combinations of profiles that the PD client can use simultaneously, this is why some of the capabilities are discovered by the PD client at runtime when and if the PD provider fails the filter set request with STATUS_NOT_SUPPORTED</p>

<p>To define a <i>NdisPDSetReceiveFilter</i> function, you must first provide a function declaration that identifies the type of function you're defining. Windows provides a set of function types for drivers. Declaring a function using the function types helps <a href="NULL">Code Analysis for Drivers</a>, <a href="NULL">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it's a requirement for writing drivers for the Windows operating system.</p>

<p>For example, to define a <i>NdisPDSetReceiveFilter</i> function that is named "MyPDSetReceiveFilter", use the <b>NDIS_PD_SET_RECEIVE_FILTER</b> type as shown in this code example:</p>

<p>Then, implement your function as follows:</p>

<p>The <b>NDIS_PD_SET_RECEIVE_FILTER</b> function type is defined in the Ntddndis.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition.  The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the <b>NDIS_PD_SET_RECEIVE_FILTER</b> function type in the header file are used.  For more information about the requirements for function declarations, see <a href="NULL">Declaring Functions by Using Function Role Types for NDIS Drivers</a>.

For information about  _Use_decl_annotations_, see <a href="http://go.microsoft.com/fwlink/p/?linkid=286697">Annotating Function Behavior</a>. </p>

<p>PD filters are applied before any spreading takes place this is why packet matching a PD filter can be placed into their dedicated PD queue, and the rest of the packets can be spread by RSS as usual. The PD client is responsible for plumbing non-overlapping ambiguous filters. However, some PD provides may allow overlapping ambiguous filters as long as the PD client can pass a priority value that indicates which filter must be applied first. The PD provider may fail filter set requests with STATUS_NOT_SUPPORTED if the client attempts to set filters with conflicting profiles or overlapping match conditions. The <a href="https://msdn.microsoft.com/library/windows/hardware/dn931833">NDIS_PD_CAPABILITIES</a> structure does not allow the provider to advertise all valid combinations of profiles that the PD client can use simultaneously, this is why some of the capabilities are discovered by the PD client at runtime when and if the PD provider fails the filter set request with STATUS_NOT_SUPPORTED</p>

<p>To define a <i>NdisPDSetReceiveFilter</i> function, you must first provide a function declaration that identifies the type of function you're defining. Windows provides a set of function types for drivers. Declaring a function using the function types helps <a href="NULL">Code Analysis for Drivers</a>, <a href="NULL">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it's a requirement for writing drivers for the Windows operating system.</p>

<p>For example, to define a <i>NdisPDSetReceiveFilter</i> function that is named "MyPDSetReceiveFilter", use the <b>NDIS_PD_SET_RECEIVE_FILTER</b> type as shown in this code example:</p>

<p>Then, implement your function as follows:</p>

<p>The <b>NDIS_PD_SET_RECEIVE_FILTER</b> function type is defined in the Ntddndis.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition.  The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the <b>NDIS_PD_SET_RECEIVE_FILTER</b> function type in the header file are used.  For more information about the requirements for function declarations, see <a href="NULL">Declaring Functions by Using Function Role Types for NDIS Drivers</a>.

For information about  _Use_decl_annotations_, see <a href="http://go.microsoft.com/fwlink/p/?linkid=286697">Annotating Function Behavior</a>. </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 10</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2016</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ndis.h</dt>
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