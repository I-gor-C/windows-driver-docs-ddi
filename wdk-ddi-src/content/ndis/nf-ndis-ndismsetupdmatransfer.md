---
UID: NF.ndis.NdisMSetupDmaTransfer
title: NdisMSetupDmaTransfer
author: windows-driver-content
description: The NdisMSetupDmaTransfer function sets up the host DMA controller for a DMA transfer.
old-location: netvista\ndismsetupdmatransfer.htm
old-project: netvista
ms.assetid: 2a7ebedd-0042-4624-9c9b-721cccfb0c4f
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: NdisMSetupDmaTransfer
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Universal
req.target-min-winverclnt: Supported for NDIS 6.0 and NDIS 5.1 drivers (see    NdisMSetupDmaTransfer (NDIS   5.1)) in Windows Vista. Supported for NDIS 5.1 drivers (see    NdisMSetupDmaTransfer (NDIS   5.1)) in Windows XP.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NdisMSetupDmaTransfer
req.alt-loc: ndis.h
req.ddi-compliance: Irql_Miniport_Driver_Function
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <= DISPATCH_LEVEL
req.iface: 
---

# NdisMSetupDmaTransfer function



## -description
<p>The 
  <b>NdisMSetupDmaTransfer</b> function sets up the host DMA controller for a DMA transfer.</p>


## -syntax

````
VOID NdisMSetupDmaTransfer(
  _Out_ PNDIS_STATUS Status,
  _In_  NDIS_HANDLE  MiniportDmaHandle,
  _In_  PNDIS_BUFFER Buffer,
  _In_  ULONG        Offset,
  _In_  ULONG        Length,
  _In_  BOOLEAN      WriteToDevice
);
````


## -parameters
<dl>

### -param <i>Status</i> [out]

<dd>
<p>A pointer to a caller-supplied variable in which this function returns the status of the request,
     which can be one of the following:
     </p>
<p></p>
<dl>

### -param <a id="NDIS_STATUS_SUCCESS"></a><a id="ndis_status_success"></a>NDIS_STATUS_SUCCESS

<dd>
<p>The DMA controller has been set up to transfer the specified data, which has been flushed to or
       from the device to maintain data integrity.</p>
</dd>

### -param <a id="NDIS_STATUS_RESOURCES"></a><a id="ndis_status_resources"></a>NDIS_STATUS_RESOURCES

<dd>
<p>An attempt to set up the DMA controller for the transfer has failed, either because the channel
       designated by 
       <i>MiniportDmaHandle</i> is currently in use transferring data or because the given 
       <i>Length</i> is invalid.</p>
</dd>
</dl>
</dd>

### -param <i>MiniportDmaHandle</i> [in]

<dd>
<p>The DMA handle returned by the 
     <a href="..\ndis\nf-ndis-ndismregisterdmachannel.md">NdisMRegisterDmaChannel</a> function
     during initialization.</p>
</dd>

### -param <i>Buffer</i> [in]

<dd>
<p>A pointer to the buffer descriptor mapping the range of host memory from which or into which the
     data will be transferred.</p>
</dd>

### -param <i>Offset</i> [in]

<dd>
<p>The byte offset within the mapped buffer at which the transfer should start. Zero indicates the
     transfer should begin at the initial byte of the range specified at 
     <i>Buffer</i> .</p>
</dd>

### -param <i>Length</i> [in]

<dd>
<p>The number of bytes of data to be transferred. The range specified by 
     <i>Offset</i> and 
     <i>Length</i> must be a proper subrange of that specified at 
     <i>Buffer</i> .</p>
</dd>

### -param <i>WriteToDevice</i> [in]

<dd>
<p>A boolean value that is <b>TRUE</b> for an outbound transfer from the system through the NIC. Otherwise,
     it is <b>FALSE</b>.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>Drivers of subordinate-DMA NICs call 
    <b>NdisMSetupDmaTransfer</b> in response to incoming send requests, for which the driver sets 
    <i>WriteToDevice</i> to <b>TRUE</b>. They set 
    <i>WriteToDevice</i> to <b>FALSE</b> when they transfer received data from the NIC to host memory.</p>

<p>The caller of 
    <b>NdisMSetupDmaTransfer</b> supplies a buffer descriptor mapping the host memory range that is the target
    of the transfer or that contains data for a download operation from the host to the NIC. To specify a
    transfer sized to suit the DMA constraints of the NIC, the caller can set up a subrange to be transferred
    with the 
    <i>Offset</i> and 
    <i>Length</i> parameters if necessary.</p>

<p>The caller must supply a buffer descriptor that specifies the host range into which received data will
    be transferred from the NIC when 
    <i>WriteToDevice</i> is <b>FALSE</b>. Otherwise, the buffer descriptor at 
    <i>Buffer</i> was chained to a packet descriptor input to the miniport driver's 
    <a href="..\ndis\nc-ndis-miniport-send-net-buffer-lists.md">
    MiniportSendNetBufferLists</a> function.</p>

<p>To improve performance for small transmit requests, such as a send request of less than 256 bytes in
    length, a miniport driver can copy the packet data into an internal staging buffer and pass a
    driver-allocated buffer descriptor mapping that buffer to 
    <b>NdisMSetupDmaTransfer</b>.</p>

<p>On return from 
    <b>NdisMSetupDmaTransfer</b>, the host DMA controller has been programmed for the transfer. The miniport
    driver then programs the NIC for the transfer operation.</p>

<p>When the transfer is complete, the miniport driver must call the 
    <a href="..\ndis\nf-ndis-ndismcompletedmatransfer.md">
    NdisMCompleteDmaTransfer</a> function.</p>

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
   <a href="https://msdn.microsoft.com/0e1e487d-d991-4729-bcf0-3c0f76f00bc4">NdisMSetupDmaTransfer (NDIS
   5.1)</a>) in Windows Vista. Supported for NDIS 5.1 drivers (see 
   <b>NdisMSetupDmaTransfer (NDIS
   5.1)</b>) in Windows XP.</p>
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
<p>&lt;= DISPATCH_LEVEL</p>
</td>
</tr>
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="devtest.ndis_irql_miniport_driver_function">Irql_Miniport_Driver_Function</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ndis\nc-ndis-miniport-send-net-buffer-lists.md">MiniportSendNetBufferLists</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndismcompletedmatransfer.md">NdisMCompleteDmaTransfer</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndismregisterdmachannel.md">NdisMRegisterDmaChannel</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisMSetupDmaTransfer function%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
