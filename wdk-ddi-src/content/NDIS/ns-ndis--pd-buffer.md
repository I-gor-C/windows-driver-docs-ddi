---
UID: NS.ndis._PD_BUFFER
title: PD_BUFFER
author: windows-driver-content
description: This structure represents a PacketDirect (PD) packet, or a portion of a PD packet in a queue.
old-location: netvista\pd_buffer.htm
ms.assetid: 91555FBA-30F5-4CED-BA0D-2F0BE40BFF9E
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: netvista
req.header: ndis.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PD_BUFFER
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
req.irql: See Remarks section
ms.keywords: PD_BUFFER, PD_BUFFER
req.iface: 
---

# PD_BUFFER structure



## -description
<p>This structure represents a PacketDirect (PD) packet, or a portion of a PD packet in a queue.</p>


## -syntax

````
typedef struct _PD_BUFFER {
  PD_BUFFER                                                       *NextPDBuffer;
  PD_BUFFER                                                       *NextPartialPDBuffer;
  PVOID                                                           PDClientReserved;
  _Field_size_bytes_(PDClientContextSize)  PVOID                  PDClientContext;
  _Field_size_bytes_(DataBufferSize)  
 PUCHAR                    DataBufferVirtualAddress;
   _Field_size_bytes_(DataBufferSize)  
      DMA_LOGICAL_ADDRESS DataBufferDmaLogicalAddress;
  ULONG                                                           DataBufferSize;
  USHORT                                                          PDClientContextSize;
  USHORT                                                          Attributes;
  USHORT                                                          Flags;
  USHORT                                                          DataStart;
  ULONG                                                           DataLength;
  union {
    struct {
      union {
        ULONG64 RxFilterContext;
        ULONG64 GftFlowEntryId;
      };
      ULONG                         RxHashValue;
      union {
        struct {
          ULONG RxIPHeaderChecksumSucceeded  :1;
          ULONG RxTCPChecksumSucceeded  :1;
          ULONG RxUDPChecksumSucceeded  :1;
          ULONG RxIPHeaderChecksumFailed  :1;
          ULONG RxTCPChecksumFailed  :1;
          ULONG RxUDPChecksumFailed  :1;
          ULONG RxHashComputed  :1;
          ULONG RxHashWithL4PortNumbers  :1;
          ULONG RxGftExceptionPacket  :1;
          ULONG RxGftCopyPacket  :1;
          ULONG RxGftSamplePacket  :1;
          ULONG RxReserved1  :5;
          ULONG RxCoalescedSegCount  :16;
          ULONG RxRscTcpTimestampDelta  :1;
        };
        ULONG  RxOffloads[2];
      };
      union {
        struct {
          ULONG TxIsIPv4  :1;
          ULONG TxIsIPv6  :1;
          ULONG TxTransportHeaderOffset  :10;
          ULONG TxMSS  :20;
          ULONG TxComputeIPHeaderChecksum  :1;
          ULONG TxComputeTCPChecksum  :1;
          ULONG TxComputeUDPChecksum  :1;
          ULONG TxIsEncapsulatedPacket  :1;
          ULONG TxInnerPacketOffsetsValid  :1;
          ULONG TxReserved1  :11;
          ULONG TxInnerFrameOffset  :8;
          ULONG TxInnerIpHeaderRelativeOffset  :6;
          ULONG TxInnerIsIPv6  :1;
          ULONG TxInnerTcpOptionsPresent  :1;
        };
        ULONG  TxOffloads[2];
      };
      PD_BUFFER_VIRTUAL_SUBNET_INFO VirtualSubnetInfo;
      PD_BUFFER_8021Q_INFO          Ieee8021qInfo;
      USHORT                        GftSourceVPortId;
      ULONG                         Reserved;
      UINT64                        ProviderScratch;
    } MetaDataV0;
  };
} PD_BUFFER, *PPD_BUFFER;
````


## -struct-fields
<dl>

### -field <b>NextPDBuffer</b>

<dd>
<p>A pointer to the next <b>PD_BUFFER</b> structure in the queue.</p>
</dd>

### -field <b>NextPartialPDBuffer</b>

<dd>
<p>A pointer to the next partial <b>PD_BUFFER</b> structure in the queue.</p>
</dd>

### -field <b>PDClientReserved</b>

<dd>
<p>Reserved for system use. Do not use.</p>
</dd>

### -field <b>PDClientContext</b>

<dd>
<p>The client and the provider are not allowed to modify this field.      If a client has allocated the <b>PD_BUFFER</b> with a non-zero value for      ClientContextSize, then the PDClientContext refers to a buffer size      of ClientContextSize. Otherwise, this field is NULL.</p>
</dd>

### -field <b>DataBufferVirtualAddress</b>

<dd>
<p>This field represents the address that hosts and software can use to access/modify the packet contents. The actual packet data is always at  DataBufferVirtualAddress+DataStart. The provider and the      platform never modify the value of this field after the <b>PD_BUFFER</b>      initialization.</p>
</dd>

### -field <b>DataBufferDmaLogicalAddress</b>

<dd>
<p>This field represents the logical memory location used for storing the packet data. The provider
must use for DMA. The actual packet data is always at
    DataBufferDmaLogicalAddress+DataStart. The provider and the
    platform must never modify the value of this field after the <b>PD_BUFFER</b>
    initialization.</p>
</dd>

### -field <b>DataBufferSize</b>

<dd>
<p>This is the total size of the allocated data buffer. The provider and the platform must never modify the value of this field
    after the <b>PD_BUFFER</b> initialization. This data type is <b>ULONG</b> instead of
    <b>USHORT</b> because of large send offload.</p>
</dd>

### -field <b>PDClientContextSize</b>

<dd>
<p>When this value is non-zero, it is the size of the buffer pointed to by PDClientContext.
    The value of this field must only be modified by the platform. The platform does not change the value of this field after the <b>PD_BUFFER</b> allocation.</p>
</dd>

### -field <b>Attributes</b>

<dd>
<p>The attributes must never be modified by the provider. The table below lists attributes that this <b>PD_BUFFER</b> structure can have.</p>
<table>
<tr>
<th>Attribute</th>
<th>Description</th>
</tr>
<tr>
<td>PD_BUFFER_ATTR_BUILT_IN_DATA_BUFFER</td>
<td>A <b>PD_BUFFER</b> allocated with its own accompanying data buffer will have
this attribute set. The <b>PD_BUFFER</b> attributes must never be modified by clients
or providers.</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>Flags</b>

<dd>
<p>The following table lists flags that this <b>PD_BUFFER</b> structure can have.</p>
<table>
<tr>
<th>Flag</th>
<th>Description</th>
</tr>
<tr>
<td>PD_BUFFER_FLAG_PARTIAL_PACKET_HEAD</td>
<td>Indicates that this buffer is the head of partial packets.</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>DataStart</b>

<dd>
<p>This field denotes where the packet starts relative to the original starting address of the allocated data buffer. The provider must never modify this field. The provider adds this value to the
    DataBufferDmaLogicalAddress value to derive the actual
    target DMA address for packet reception/transmission. For example, the
    target DMA address value in the hardware receive/transmit descriptor
    must be set to DataBufferDmaLogicalAddress+DataStart when a <b>PD_BUFFER</b>
    is posted to a receive/transmit queue.</p>
</dd>

### -field <b>DataLength</b>

<dd>
<p>The length of the this packet or partial packet data.</p>
</dd>

### -field <b>MetaDataV0</b>

<dd>
<dl>

### -field <b>RxFilterContext</b>

<dd>
<p>The provider sets this to the filter context value obtained
                from the matched filter that steered the packet to the receive
                queue. Filter context values are specified by the clients
                when configuring filters.</p>
</dd>

### -field <b>GftFlowEntryId</b>

<dd>
<p>If one of the RxGftExceptionPacket or RxGftCopyPacket or RxGftSamplePacket bits are set, the RxFilterContext value is
                overwritten with a GFT flow entry Id value.</p>
</dd>

### -field <b>RxHashValue</b>

<dd>
<p>The hash value computed for the incoming packet
            that is steered to the receive queue using RSS.</p>
</dd>

### -field <b>RxIPHeaderChecksumSucceeded</b>

<dd>
<p>A common RX offload field that indicates if the IP header checksum succeeded.</p>
</dd>

### -field <b>RxTCPChecksumSucceeded</b>

<dd>
<p>A common RX offload field that indicates if the TCP checksum succeeded.</p>
</dd>

### -field <b>RxUDPChecksumSucceeded</b>

<dd>
<p>A common RX offload field that indicates if the UDP checksum succeeded.</p>
</dd>

### -field <b>RxIPHeaderChecksumFailed</b>

<dd>
<p>A common RX offload field that indicates if the IP header checksum failed.</p>
</dd>

### -field <b>RxTCPChecksumFailed</b>

<dd>
<p>A common RX offload field that indicates if the TCP checksum failed.</p>
</dd>

### -field <b>RxUDPChecksumFailed</b>

<dd>
<p>A common RX offload field that indicates if the UDP checksum failed.</p>
</dd>

### -field <b>RxHashComputed</b>

<dd>
<p>A common RX offload field that indicates if the hash is computed.</p>
</dd>

### -field <b>RxHashWithL4PortNumbers</b>

<dd>
<p>A common RX offload field that indicates the hash is computed with L4 port numbers.</p>
</dd>

### -field <b>RxGftExceptionPacket</b>

<dd>
<p>A common RX offload field that indicates this is a GFT exception packet.</p>
</dd>

### -field <b>RxGftCopyPacket</b>

<dd>
<p>A common RX offload field that indicates this is a GFT copy packet.</p>
</dd>

### -field <b>RxGftSamplePacket</b>

<dd>
<p>A common RX offload field that indicates this is a GFT sample packet.</p>
</dd>

### -field <b>RxReserved1</b>

<dd>
<p>Reserved.</p>
</dd>

### -field <b>RxCoalescedSegCount</b>

<dd>
<p>A common RX offload field that contains the amount of coalesced segments.</p>
</dd>

### -field <b>RxRscTcpTimestampDelta</b>

<dd>
<p>A common RX offload field that contains RSC and TCP timestamp difference.</p>
</dd>

### -field <b>RxOffloads</b>

<dd>
<p>RX offloads for this buffer.</p>
</dd>

### -field <b>TxIsIPv4</b>

<dd>
<p>A common TX offload field that indicates this packet is IPv4.</p>
</dd>

### -field <b>TxIsIPv6</b>

<dd>
<p>A common TX offload field that indicates this packet is IPv6.</p>
</dd>

### -field <b>TxTransportHeaderOffset</b>

<dd>
<p>A common TX offload field that contains the packet's header offset.</p>
</dd>

### -field <b>TxMSS</b>

<dd>
<p>A common TX offload field that contains the maximum segment size of this packet.</p>
</dd>

### -field <b>TxComputeIPHeaderChecksum</b>

<dd>
<p>A common TX offload field that indicates the IP header checksum is computed.</p>
</dd>

### -field <b>TxComputeTCPChecksum</b>

<dd>
<p>A common TX offload field that indicates the TCP checksum is computed.</p>
</dd>

### -field <b>TxComputeUDPChecksum</b>

<dd>
<p>A common TX offload field that indicates the UDP checksum is computed.</p>
</dd>

### -field <b>TxIsEncapsulatedPacket</b>

<dd>
<p>A common TX offload field that indicates the packet is encapsulated.</p>
</dd>

### -field <b>TxInnerPacketOffsetsValid</b>

<dd>
<p>A common TX offload field that indicates the inner packet offsets are valid.</p>
</dd>

### -field <b>TxReserved1</b>

<dd>
<p>Reserved.</p>
</dd>

### -field <b>TxInnerFrameOffset</b>

<dd>
<p>A common TX offload field that contains the inner frame offset.</p>
</dd>

### -field <b>TxInnerIpHeaderRelativeOffset</b>

<dd>
<p>A common TX offload field that contains the inner IP header relative offset.</p>
</dd>

### -field <b>TxInnerIsIPv6</b>

<dd>
<p>A common TX offload field that indicates the inner packet is IPv6.</p>
</dd>

### -field <b>TxInnerTcpOptionsPresent</b>

<dd>
<p>A common TX offload field that indicates the inner TCP options are present.</p>
</dd>

### -field <b>TxOffloads</b>

<dd>
<p>TX offloads for this buffer.</p>
</dd>

### -field <b>VirtualSubnetInfo</b>

<dd>
<p>The virtual subnet information.</p>
</dd>

### -field <b>Ieee8021qInfo</b>

<dd>
<p>The IEEE 802.1Q information.</p>
</dd>

### -field <b>GftSourceVPortId</b>

<dd>
<p>The GFT source virtual port ID.</p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>Reserved for system use.</p>
</dd>

### -field <b>ProviderScratch</b>

<dd>
<p>A scratch field that the PD provider can use for its own purposes while the PD_BUFFER is sitting in the provider queue (in other words, posted by the client but not yet drained back by the client). Once the PD_BUFFER is drained by the client, there is no guarantee that the contents of this field will be preserved.</p>
</dd>
</dl>
</dd>
</dl>

## -remarks
<p>If an L2 packet is represented by multiple <b>PD_BUFFER</b> structures, the first <b>PD_BUFFER</b>
must have the PD_BUFFER_ATTR_BUILT_IN_DATA_BUFFER flag set and the
NextPartialPDBuffer field must point to the partial <b>PD_BUFFER</b> structures that
constitute the whole packet. Each of the partial <b>PD_BUFFER</b> structures must point to the next partial <b>PD_BUFFER</b> by using the NextPartialPDBuffer as opposed to the NextPDBuffer field. The NextPDBuffer field must be NULL in all partial <b>PD_BUFFER</b> structures except
for the head buffer. All partial PD_BUFFER structures except for the head buffer must
have the PD_BUFFER_ATTR_BUILT_IN_DATA_BUFFER flag cleared. The last partial
<b>PD_BUFFER</b> must have it's NextPartialPDBuffer field set to NULL. The total
length of the L2 packet is the sum of DataLength fields from each partial
<b>PD_BUFFER</b>. The head <b>PD_BUFFER</b> must contain up to and including the IP transport (TCP, UDP, SCTP, etc) header. In the case of encapsulation or double-encapsulation,
the inner-most IP transport header must be contained in the head <b>PD_BUFFER</b>.</p>

<p>When posting <b>PD_BUFFER</b> structures to receive queues, DataLength is ignored by
    the provider (For more information see the ReceiveDataLength description in the <a href="https://msdn.microsoft.com/library/windows/hardware/dn931846">NDIS_PD_QUEUE_PARAMETERS</a> structure).
    When draining completed <b>PD_BUFFER</b>  structures from receive queues,
    the provider stores the length of the received packet in the  DataLength field. The length does not include FCS or any stripped 801Q
    headers.
    When posting <b>PD_BUFFER</b> structures to transmit queues, DataLength denotes the length
    of the packet to be sent. When draining completed <b>PD_BUFFER</b> structures from
    transmit queues, the provider leaves the DataLength field unmodified.</p>

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
</table>