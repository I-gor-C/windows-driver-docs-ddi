---
UID : NS:fwpsk.FWPS_INCOMING_METADATA_VALUES0_
title : FWPS_INCOMING_METADATA_VALUES0_
author : windows-driver-content
description : The FWPS_INCOMING_METADATA_VALUES0 structure defines metadata values that the filter engine passes to a callout's classifyFn callout function.Note  FWPS_INCOMING_METADATA_VALUES0 is a specific version of FWPS_INCOMING_METADATA_VALUES.
old-location : netvista\fwps_incoming_metadata_values0.htm
old-project : netvista
ms.assetid : fba7eb60-0d19-4bfd-b484-2e615d3e9237
ms.author : windowsdriverdev
ms.date : 1/11/2018
ms.keywords : FWPS_INCOMING_METADATA_VALUES0_, FWPS_INCOMING_METADATA_VALUES0
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : fwpsk.h
req.include-header : Fwpsk.h
req.target-type : Windows
req.target-min-winverclnt : Available starting with  Windows Vista.
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : FWPS_INCOMING_METADATA_VALUES0
req.alt-loc : fwpsk.h
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : <= DISPATCH_LEVEL
req.typenames : FWPS_INCOMING_METADATA_VALUES0
---

# FWPS_INCOMING_METADATA_VALUES0_ structure
The <b>FWPS_INCOMING_METADATA_VALUES0</b> structure defines metadata values that the filter engine passes to
  a callout's 
  <a href="..\fwpsk\nc-fwpsk-fwps_callout_classify_fn0.md">classifyFn</a> callout function.

## Syntax
````
typedef struct FWPS_INCOMING_METADATA_VALUES0_ {
  UINT32                          currentMetadataValues;
  UINT32                          flags;
  UINT64                          reserved;
  FWPS_DISCARD_METADATA0          discardMetadata;
  UINT64                          flowHandle;
  UINT32                          ipHeaderSize;
  UINT32                          transportHeaderSize;
  FWP_BYTE_BLOB                   *processPath;
  UINT64                          token;
  UINT64                          processId;
  UINT32                          sourceInterfaceIndex;
  UINT32                          destinationInterfaceIndex;
  ULONG                           compartmentId;
  FWPS_INBOUND_FRAGMENT_METADATA0 fragmentMetadata;
  ULONG                           pathMtu;
  HANDLE                          completionHandle;
  UINT64                          transportEndpointHandle;
  SCOPE_ID                        remoteScopeId;
  WSACMSGHDR                      *controlData;
  ULONG                           controlDataLength;
  FWP_DIRECTION                   packetDirection;
#if (NTDDI_VERSION >= NTDDI_WIN6SP1)
  PVOID                           headerIncludeHeader;
  ULONG                           headerIncludeHeaderLength;
#if (NTDDI_VERSION >= NTDDI_WIN7)
  IP_ADDRESS_PREFIX               destinationPrefix;
  UINT16                          frameLength;
  UINT64                          parentEndpointHandle;
  UINT32                          icmpIdAndSequence;
  DWORD                           localRedirectTargetPID;
  SOCKADDR                        *originalDestination;
#if (NTDDI_VERSION >= NTDDI_WIN8)
  HANDLE                          redirectRecords;
  UINT32                          currentL2MetadataValues;
  UINT32                          l2Flags;
  UINT32                          ethernetMacHeaderSize;
  UINT32                          wiFiOperationMode;
#if (NDIS_SUPPORT_NDIS630)
  NDIS_SWITCH_PORT_ID             vSwitchSourcePortId;
  NDIS_SWITCH_NIC_INDEX           vSwitchSourceNicIndex;
  NDIS_SWITCH_PORT_ID             vSwitchDestinationPortId;
#else 
  UINT32                          padding0;
  USHORT                          padding1;
  UINT32                          padding2;
#endif 
  HANDLE                          vSwitchPacketContext;
  UINT32                          l2ConnectionProfileIndex;
#endif 
#endif 
#endif 
#if (NTDDI_VERSION >= NTDDI_WIN8)
  PVOID                           subProcessTag;
  UINT64                          Reserved1;
#endif 
} FWPS_INCOMING_METADATA_VALUES0;
````

## Members

        
            `compartmentId`

            The identifier of the routing compartment in which the packet either was received or is being
     sent. Any modified packets should be injected back into the same routing compartment that is indicated
     for the original packet. This member contains valid data only if the FWPS_METADATA_FIELD_COMPARTMENT_ID
     flag is set in the 
     <b>currentMetadataValues</b> member.
        
            `completionHandle`

            A completion handle that is required to pend the current filtering operation. This member contains
     valid data only if the FWPS_METADATA_FIELD_COMPLETION_HANDLE flag is set in the 
     <b>currentMetadataValues</b> member.
        
            `controlData`

            An optional socket control data object. This member contains valid data only if the
     FWPS_METADATA_FIELD_TRANSPORT_CONTROL_DATA flag is set in the 
     <b>currentMetadataValues</b> member. For information about the WSACMSGHDR type,
     see 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff544964">CMSGHDR</a>.
        
            `controlDataLength`

            The length, in bytes, of the 
     <b>controlData</b> member.
        
            `currentL2MetadataValues`

            A bitmask that contains flags  that specify which layer 2 values are set. One or more values can be combined with a bitwise OR.

<div class="alert"><b>Note</b>  Available only in <i>Windows 8</i> and later versions of Windows.</div>
<div> </div>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
        
            `currentMetadataValues`

            A UINT32 value that contains a bitwise OR of a combination of 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff559186">Metadata Field Identifiers</a> that
     specify which metadata values are set in the structure.
        
            `destinationInterfaceIndex`

            The index of the network interface where an outgoing packet is to be sent. This member contains
     valid data only if the FWPS_METADATA_FIELD_DESTINATION_INTERFACE_INDEX flag is set in the 
     <b>currentMetadataValues</b> member.
        
            `destinationPrefix`

            The destination prefix.
     

<div class="alert"><b>Note</b>  Available only in Windows 7 and later versions of Windows.</div>
<div> </div>
        
            `discardMetadata`

            An 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff551235">FWPS_DISCARD_METADATA0</a> structure
     that describes the reason why the data was discarded. This member contains valid data only if the
     FWPS_METADATA_FIELD_DISCARD_REASON flag is set in the 
     <b>currentMetadataValues</b> member.
        
            `ethernetMacHeaderSize`

            The size, in bytes,  of the MAC header if the FWPS_L2_METADATA_FIELD_802_3_MAC_HEADER_SIZE flag is set. This flag is set for the inbound 802.3 layer only.
     

<div class="alert"><b>Note</b>  Available only in <i>Windows 8</i> and later versions of Windows.</div>
<div> </div>
        
            `flags`

            Used internally by the filter engine. Callout drivers should ignore this member.
        
            `flowHandle`

            A handle for the data flow. This member contains valid data only if the
     FWPS_METADATA_FIELD_FLOW_HANDLE flag is set in the 
     <b>currentMetadataValues</b> member.
        
            `fragmentMetadata`

            An 
     <a href="https://msdn.microsoft.com/9bead001-7ea7-4a51-8a7c-82fe01017dd7">
     FWPS_INBOUND_FRAGMENT_METADATA0</a> structure that describes the fragment data for a received packet
     fragment. This member contains valid data only if the FWPS_METADATA_FIELD_FRAGMENT_DATA flag is set in
     the 
     <b>currentMetadataValues</b> member.
        
            `frameLength`

            The frame length.
     

<div class="alert"><b>Note</b>  Available only in Windows 7 and later versions of Windows.</div>
<div> </div>
        
            `headerIncludeHeader`

            A pointer to the IP header if the packet is sent from a raw socket.
     

<div class="alert"><b>Note</b>  Available only in Windows Server 2008, Windows Vista SP1, and later versions of
     Windows.</div>
<div> </div>
        
            `headerIncludeHeaderLength`

            The length, in bytes, of the IP header that is pointed to by 
     <b>headerIncludeHeader</b>.
     

<div class="alert"><b>Note</b>  Available only in Windows Server 2008, Windows Vista SP1, and later versions of
     Windows.</div>
<div> </div>
        
            `icmpIdAndSequence`

            The ICMP identifier and sequence.
     

<div class="alert"><b>Note</b>  Available only in Windows 7 and later versions of Windows.</div>
<div> </div>
        
            `ipHeaderSize`

            The offset, in bytes, of the IP header.
     

On inbound paths, 
     <b>ipHeaderSize</b>, when used in conjunction with the 
     <b>transportHeaderSize</b> member, specifies the number of bytes to retreat from
     the data offset location to the beginning of the IP header.

On the following inbound ICMP error layers, 
     <b>ipHeaderSize</b> alone specifies the total number of bytes to retreat from the
     data offset to the beginning of the IP header:

<dl>
<dd>
FWPS_LAYER_INBOUND_ICMP_ERROR_V4

</dd>
<dd>
FWPS_LAYER_INBOUND_ICMP_ERROR_V6

</dd>
<dd>
FWPS_LAYER_INBOUND_ICMP_ERROR_V4_DISCARD

</dd>
<dd>
FWPS_LAYER_INBOUND_ICMP_ERROR_V6_DISCARD

</dd>
</dl>
On outbound paths, if 
     <b>ipHeaderSize</b> is greater than zero, it specifies the number of bytes to
     advance from the data offset location to the end of the IP header.

This member is not applicable to the outbound path at the following layers:

<dl>
<dd>
FWPS_LAYER_DATAGRAM_DATA_V4

</dd>
<dd>
FWPS_LAYER_DATAGRAM_DATA_V6

</dd>
<dd>
FWPS_LAYER_DATAGRAM_DATA_V4_DISCARD

</dd>
<dd>
FWPS_LAYER_DATAGRAM_DATA_V6_DISCARD

</dd>
</dl>
This member contains valid data only if the FWPS_METADATA_FIELD_IP_HEADER_SIZE flag is set in the 
     <b>currentMetadataValues</b> member.
        
            `l2Flags`

            A bitmask containing layer 2 flags that can be combined with a bitwise OR.
     

<div class="alert"><b>Note</b>  Available only in <i>Windows 8</i> and later versions of Windows.</div>
<div> </div>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
        
            `localRedirectTargetPID`

            The PID of the process that is responsible for a redirected connection.
     

<div class="alert"><b>Note</b>  Available only in Windows 7 and later versions of Windows.</div>
<div> </div>
        
            `originalDestination`

            The original destination of a redirected connection.
     

<div class="alert"><b>Note</b>  Available only in Windows 7 and later versions of Windows.</div>
<div> </div>
        
            `packetDirection`

            The direction of network traffic (inbound or outbound) as specified by one of the constant values of
      
      <a href="https://msdn.microsoft.com/library/windows/hardware/ff552433">FWP_DIRECTION</a>. This member is set at the
      application layer enforcement (ALE) connect or receive/accept layers during a reauthorization classify
      operation. For more information, see the Remarks section.

<div class="alert"><b>Note</b>  This member contains valid data only if the FWPS_METADATA_FIELD_PACKET_DIRECTION
      flag is set in the 
      <b>currentMetadataValues</b> member.</div>
<div> </div>
        
            `padding0`

            Reserved. 

<div class="alert"><b>Note</b>  Available only in <i>Windows 8</i> and later versions of Windows.</div>
<div> </div>
        
            `padding1`

            Reserved. 

<div class="alert"><b>Note</b>  Available only in <i>Windows 8</i> and later versions of Windows.</div>
<div> </div>
        
            `padding2`

            Reserved. 

<div class="alert"><b>Note</b>  Available only in <i>Windows 8</i> and later versions of Windows.</div>
<div> </div>
        
            `parentEndpointHandle`

            The handle of the endpoint's parent.
     

<div class="alert"><b>Note</b>  Available only in Windows 7 and later versions of Windows.</div>
<div> </div>
        
            `pathMtu`

            The path maximum transmission unit (path MTU) for an outbound packet. This value indicates the
     largest physical packet size, in bytes, that a network can transmit without fragmentation, This member
     contains valid data only if the FWPS_METADATA_FIELD_PATH_MTU flag is set in the 
     <b>currentMetadataValues</b> member.
        
            `processId`

            The process ID for the process that owns the endpoint. This member contains valid data only if the
     FWPS_METADATA_FIELD_PROCESS_ID flag is set in the 
     <b>currentMetadataValues</b> member.
        
            `processPath`

            A pointer to an 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff552427">FWP_BYTE_BLOB</a> structure that contains the
     full path to the process that owns the endpoint. This member contains valid data only if the
     FWPS_METADATA_FIELD_PROCESS_PATH flag is set in the 
     <b>currentMetadataValues</b> member.
        
            `redirectRecords`

            A redirect records handle that can be passed to the <a href="..\fwpsk\nf-fwpsk-fwpsqueryconnectionredirectstate0.md">FwpsQueryConnectionRedirectState0</a> function to get the redirect state. 

<div class="alert"><b>Note</b>  Available only in <i>Windows 8</i> and later versions of Windows.</div>
<div> </div>
        
            `remoteScopeId`

            The remote scope identifier to be used in outbound transport layer injection. This member contains
     valid data only if the FWPS_METADATA_FIELD_REMOTE_SCOPE_ID flag is set in the 
     <b>currentMetadataValues</b> member.
        
            `reserved`

            Reserved for system use. Callout drivers should ignore this member.
        
            `sourceInterfaceIndex`

            The index of the network interface where an incoming packet was received. This member contains
     valid data only if the FWPS_METADATA_FIELD_SOURCE_INTERFACE_INDEX flag is set in the 
     <b>currentMetadataValues</b> member.
        
            `subProcessTag`

            Reserved. 

<div class="alert"><b>Note</b>  Available only in <i>Windows 8</i> and later versions of Windows.</div>
<div> </div>
        
            `token`

            A handle for the token used to validate the permissions for the user. This member contains valid
     data only if the FWPS_METADATA_FIELD_TOKEN flag is set in the 
     <b>currentMetadataValues</b> member.
        
            `transportEndpointHandle`

            An endpoint handle that indicates the end of the packet to be injected into the outbound transport
     layer. This member contains valid data only if the FWPS_METADATA_FIELD_TRANSPORT_ENDPOINT_HANDLE flag is
     set in the 
     <b>currentMetadataValues</b> member.
        
            `transportHeaderSize`

            The offset or size, in bytes, of the transport header.
     

On inbound paths, 
     <b>transportHeaderSize</b> specifies the number of bytes to retreat from the data
     offset location to the end of the transport header.

On the following inbound ICMP error layers, 
     <b>transportHeaderSize</b> specifies the size of the ICMP header:

<dl>
<dd>
FWPS_LAYER_INBOUND_ICMP_ERROR_V4

</dd>
<dd>
FWPS_LAYER_INBOUND_ICMP_ERROR_V6

</dd>
<dd>
FWPS_LAYER_INBOUND_ICMP_ERROR_V4_DISCARD

</dd>
<dd>
FWPS_LAYER_INBOUND_ICMP_ERROR_V6_DISCARD

</dd>
</dl>
On outbound paths, 
     <b>transportHeaderSize</b> specifies the number of bytes to advance from the data
     offset location to the end of the transport header.

This member contains valid data only if the FWPS_METADATA_FIELD_TRANSPORT_HEADER_SIZE flag is set in
     the 
     <b>currentMetadataValues</b> member.
        
            `vSwitchDestinationPortId`

            A unique identifier for the destination port on the   virtual switch. 

<div class="alert"><b>Note</b>  Available only in <i>Windows 8</i> and later versions of Windows.</div>
<div> </div>
        
            `vSwitchPacketContext`

            A handle to the virtual switch packet context. 

<div class="alert"><b>Note</b>  Available only in <i>Windows 8</i> and later versions of Windows.</div>
<div> </div>
        
            `vSwitchSourceNicIndex`

            A index for the source NIC on the   virtual switch. 

<div class="alert"><b>Note</b>  Available only in <i>Windows 8</i> and later versions of Windows.</div>
<div> </div>
        
            `vSwitchSourcePortId`

            A unique identifier for the source port on the   virtual switch. 

<div class="alert"><b>Note</b>  Available only in <i>Windows 8</i> and later versions of Windows.</div>
<div> </div>
        
            `wiFiOperationMode`

            The  current Native 802.11  operation mode  if the FWPS_L2_METADATA_FIELD_802_11_OPERATION_MODE flag is set. For more information, see <a href="..\windot11\ns-windot11-_dot11_current_operation_mode.md">DOT11_CURRENT_OPERATION_MODE</a>.
     

<div class="alert"><b>Note</b>  Available only in <i>Windows 8</i> and later versions of Windows.</div>
<div> </div>

    ## Remarks
        The filter engine passes a pointer to an FWPS_INCOMING_METADATA_VALUES0 structure to a callout's 
    <a href="..\fwpsk\nc-fwpsk-fwps_callout_classify_fn0.md">classifyFn</a> callout function. The metadata
    values contained in the structure are not processed by the filter engine but are supplied to a callout's 
    <i>classifyFn</i> callout function to provide
    additional information.

A callout driver can use the following macro to test if a specific metadata value is present in an
    FWPS_INCOMING_METADATA_VALUES0 structure:



A pointer to an FWPS_INCOMING_METADATA_VALUES0 structure.

The metadata field identifier for the metadata value being tested. See 
      <a href="https://msdn.microsoft.com/library/windows/hardware/ff559186">Metadata Field Identifiers</a> for a
      list of the metadata field identifiers.

If the FWPS_METADATA_FIELD_PACKET_DIRECTION metadata value is present in an
    FWPS_INCOMING_METADATA_VALUES0 structure, the 
    <b>packetDirection</b> member specifies whether the packet was inbound or outbound
    during a reauthorization classify operation. Otherwise, the FWPS_METADATA_FIELD_PACKET_DIRECTION metadata
    value is not present.

The callout driver must follow these guidelines when it inspects the packet:

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | fwpsk.h (include Fwpsk.h) |

    ## See Also

        <dl>
<dt>
<a href="..\fwpsk\nc-fwpsk-fwps_callout_classify_fn0.md">classifyFn</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544964">CMSGHDR</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552427">FWP_BYTE_BLOB</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552433">FWP_DIRECTION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551235">FWPS_DISCARD_METADATA0</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/9bead001-7ea7-4a51-8a7c-82fe01017dd7">
   FWPS_INBOUND_FRAGMENT_METADATA0</a>
</dt>
<dt>
<a href="..\fwpsk\nf-fwpsk-fwpsqueryconnectionredirectstate0.md">FwpsQueryConnectionRedirectState0</a>
</dt>
<dt>
<a href="..\ndis\ns-ndis-_net_buffer_list.md">NET_BUFFER_LIST</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20FWPS_INCOMING_METADATA_VALUES0 structure%20 RELEASE:%20(1/11/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>