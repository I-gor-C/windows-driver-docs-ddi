---
UID: NF.fwpsk.FwpsGetPacketListSecurityInformation0
title: FwpsGetPacketListSecurityInformation0
author: windows-driver-content
description: The FwpsGetPacketListSecurityInformation0 function retrieves information associated with a packet list.Note  FwpsGetPacketListSecurityInformation0 is a specific version of FwpsGetPacketListSecurityInformation.
old-location: netvista\fwpsgetpacketlistsecurityinformation0.htm
old-project: netvista
ms.assetid: c3391615-963b-4916-9280-ce782269692c
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: FwpsGetPacketListSecurityInformation0
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: fwpsk.h
req.include-header: Fwpsk.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows Vista.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FwpsGetPacketListSecurityInformation0
req.alt-loc: fwpkclnt.lib,fwpkclnt.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Fwpkclnt.lib
req.dll: 
req.irql: <= DISPATCH_LEVEL
req.iface: 
---

# FwpsGetPacketListSecurityInformation0 function



## -description
<p>The 
  <b>FwpsGetPacketListSecurityInformation0</b> function retrieves information associated with a packet
  list.</p>


## -syntax

````
NTSTATUS NTAPI FwpsGetPacketListSecurityInformation0(
  _In_    NET_BUFFER_LIST               *packetList,
  _In_    UINT32                        queryFlags,
  _Inout_ FWPS_PACKET_LIST_INFORMATION0 *packetInformation
);
````


## -parameters
<dl>

### -param <i>packetList</i> [in]

<dd>
<p>A pointer to the 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structure for which the
     associated information is being retrieved.</p>
</dd>

### -param <i>queryFlags</i> [in]

<dd>
<p>A UINT32 value that contains a bitwise OR of a combination of the following flags that specify the
     information to be retrieved:
     </p>
<p></p>
<dl>

### -param <a id="FWPS_PACKET_LIST_INFORMATION_QUERY_INBOUND"></a><a id="fwps_packet_list_information_query_inbound"></a>FWPS_PACKET_LIST_INFORMATION_QUERY_INBOUND

<dd>
<p>Retrieve information for an inbound packet list.</p>
</dd>

### -param <a id="FWPS_PACKET_LIST_INFORMATION_QUERY_OUTBOUND"></a><a id="fwps_packet_list_information_query_outbound"></a>FWPS_PACKET_LIST_INFORMATION_QUERY_OUTBOUND

<dd>
<p>Retrieve information for an outbound packet list.</p>
</dd>

### -param <a id="FWPS_PACKET_LIST_INFORMATION_QUERY_IPSEC"></a><a id="fwps_packet_list_information_query_ipsec"></a>FWPS_PACKET_LIST_INFORMATION_QUERY_IPSEC

<dd>
<p>Retrieve the IPsec information associated with the packet list. This flag must be used in
       combination with either the FWPS_PACKET_LIST_INFORMATION_QUERY_INBOUND flag or the
       FWPS_PACKET_LIST_INFORMATION_QUERY_OUTBOUND flag.</p>
</dd>

### -param <a id="FWPS_PACKET_LIST_INFORMATION_QUERY_FWP"></a><a id="fwps_packet_list_information_query_fwp"></a>FWPS_PACKET_LIST_INFORMATION_QUERY_FWP

<dd>
<p>Retrieve the Windows Filtering Platform information associated with the packet list.</p>
</dd>

### -param <a id="FWPS_PACKET_LIST_INFORMATION_QUERY_ALL_INBOUND"></a><a id="fwps_packet_list_information_query_all_inbound"></a>FWPS_PACKET_LIST_INFORMATION_QUERY_ALL_INBOUND

<dd>
<p>Retrieve all information associated with an inbound packet list.</p>
</dd>

### -param <a id="FWPS_PACKET_LIST_INFORMATION_QUERY_ALL_OUTBOUND"></a><a id="fwps_packet_list_information_query_all_outbound"></a>FWPS_PACKET_LIST_INFORMATION_QUERY_ALL_OUTBOUND

<dd>
<p>Retrieve all information associated with an outbound packet list.</p>
</dd>
</dl>
</dd>

### -param <i>packetInformation</i> [in, out]

<dd>
<p>A pointer to an 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff552412">FWPS_PACKET_LIST_INFORMATION0</a> structure that receives the information associated with the packet
     list.</p>
</dd>
</dl>

## -returns
<p>The 
     <b>FwpsGetPacketListSecurityInformation0</b> function returns one of the following NTSTATUS codes.</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The information associated with the packet list was successfully retrieved.</p><dl>
<dt><b>Other status codes</b></dt>
</dl><p>An error occurred.</p>

<p> </p>

## -remarks
<p>A callout driver calls the 
    <b>FwpsGetPacketListSecurityInformation0</b> function from within its 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff544887">classifyFn</a> callout function to retrieve
    information associated with the packet list. This information can be used to determine the action to be
    taken on the data.</p>

<p>A callout driver calls the 
    <b>FwpsGetPacketListSecurityInformation0</b> function from within its 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff544887">classifyFn</a> callout function to retrieve
    information associated with the packet list. This information can be used to determine the action to be
    taken on the data.</p>

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
<p>Available starting with Windows Vista.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Fwpsk.h (include Fwpsk.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Fwpkclnt.lib</dt>
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
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544887">classifyFn</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552412">FWPS_PACKET_LIST_INFORMATION0</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20FwpsGetPacketListSecurityInformation0 function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
