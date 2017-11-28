---
UID: NF.ndis.NdisMRegisterDmaChannel
title: NdisMRegisterDmaChannel
author: windows-driver-content
description: The NdisMRegisterDmaChannel function claims a system DMA controller channel during initialization for DMA operations on a subordinate NIC or on an ISA bus-master NIC.
old-location: netvista\ndismregisterdmachannel.htm
old-project: netvista
ms.assetid: 32e92f77-8f45-408b-a284-c00d3b5bd1b4
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: NdisMRegisterDmaChannel
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Universal
req.target-min-winverclnt: Supported for NDIS 6.0 and NDIS 5.1 drivers (see 
   NdisMRegisterDmaChannel (NDIS
   5.1)) in Windows Vista. Supported for NDIS 5.1 drivers (see 
   NdisMRegisterDmaChannel (NDIS
   5.1)) in Windows XP.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NdisMRegisterDmaChannel
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
req.iface: 
---

# NdisMRegisterDmaChannel function



## -description
<p>The
  <b>NdisMRegisterDmaChannel</b> function claims a system DMA controller channel during initialization for DMA
  operations on a subordinate NIC or on an ISA bus-master NIC.</p>


## -syntax

````
NDIS_STATUS NdisMRegisterDmaChannel(
  _Out_ PNDIS_HANDLE          MiniportDmaHandle,
  _In_  NDIS_HANDLE           MiniportAdapterHandle,
  _In_  UINT                  DmaChannel,
  _In_  BOOLEAN               Dma32BitAddresses,
  _In_  PNDIS_DMA_DESCRIPTION DmaDescription,
  _In_  ULONG                 MaximumLength
);
````


## -parameters
<dl>

### -param <i>MiniportDmaHandle</i> [out]

<dd>
<p>A pointer to a caller-supplied variable in which this function returns a handle the miniport
     driver uses in subsequent calls to the 
     <b>NdisM<i>Xxx</i></b> system DMA functions.</p>
</dd>

### -param <i>MiniportAdapterHandle</i> [in]

<dd>
<p>The miniport adapter handle input to the 
     <a href="..\ndis\nc-ndis-miniport-initialize.md">
     MiniportInitializeEx</a> function.</p>
</dd>

### -param <i>DmaChannel</i> [in]

<dd>
<p>Ignored. Set the DMA channel, if any, at 
     <i>DmaDescription</i> .</p>
</dd>

### -param <i>Dma32BitAddresses</i> [in]

<dd>
<p>A boolean value that is <b>TRUE</b> if the NIC has 32 address lines. Otherwise, it is <b>FALSE</b>.</p>
</dd>

### -param <i>DmaDescription</i> [in]

<dd>
<p>A pointer to an NDIS_DMA_DESCRIPTION structure filled in by the caller. This structure is defined
     as follows: 
     </p>
<div class="code"><span codelanguage=""><table>
<tr>
<th></th>
</tr>
<tr>
<td>
<pre>typedef struct _NDIS_DMA_DESCRIPTION {
    BOOLEAN DemandMode;
    BOOLEAN AutoInitialize;
    BOOLEAN DmaChannelSpecified;
    DMA_WIDTH DmaWidth;
    DMA_SPEED DmaSpeed;
    ULONG DmaPort;
    ULONG DmaChannel;
} NDIS_DMA_DESCRIPTION, *PNDIS_DMA_DESCRIPTION;</pre>
</td>
</tr>
</table></span></div>
<p>The driver should initialize this structure with zeros before filling in the following members:</p>
<p></p>
<dl>

### -param <a id="DemandMode"></a><a id="demandmode"></a><a id="DEMANDMODE"></a><b>DemandMode</b>

<dd>
<p>A boolean value that is <b>TRUE</b> if the subordinate NIC uses the system DMA controller's demand
       mode. Otherwise, it is <b>FALSE</b>.</p>
</dd>

### -param <a id="AutoInitialize"></a><a id="autoinitialize"></a><a id="AUTOINITIALIZE"></a><b>AutoInitialize</b>

<dd>
<p>A boolean value that is <b>TRUE</b> if the subordinate NIC uses the system DMA controller's
       autoinitialize mode. Otherwise, it is <b>FALSE</b>.</p>
</dd>

### -param <a id="DmaChannelSpecified"></a><a id="dmachannelspecified"></a><a id="DMACHANNELSPECIFIED"></a><b>DmaChannelSpecified</b>

<dd>
<p>A boolean value that is <b>TRUE</b> if 
       <b>DmaChannel</b> is set to the bus-relative value of the system DMA controller channel used by the
       NIC. Otherwise, it is <b>FALSE</b>.</p>
</dd>

### -param <a id="DmaWidth"></a><a id="dmawidth"></a><a id="DMAWIDTH"></a><b>DmaWidth</b>

<dd>
<p>The transfer width for DMA operations, one of 
       <b>Width8Bits</b>, 
       <b>Width16Bits</b>, or 
       <b>Width32Bits</b>.</p>
</dd>

### -param <a id="DmaSpeed"></a><a id="dmaspeed"></a><a id="DMASPEED"></a><b>DmaSpeed</b>

<dd>
<p>The DMA speed as one of 
       <b>Compatible</b>, 
       <b>TypeA</b>, 
       <b>TypeB</b>, or 
       <b>TypeC</b>.</p>
</dd>

### -param <a id="DmaPort"></a><a id="dmaport"></a><a id="DMAPORT"></a><b>DmaPort</b>

<dd>
<p>This member refers to the MCA bus, which is no longer supported. This member must be
       zero.</p>
</dd>

### -param <a id="DmaChannel"></a><a id="dmachannel"></a><a id="DMACHANNEL"></a><b>DmaChannel</b>

<dd>
<p>The bus-relative number of the system DMA controller channel used by the NIC.</p>
</dd>
</dl>
</dd>

### -param <i>MaximumLength</i> [in]

<dd>
<p>The maximum number of bytes that the NIC can transfer in a single DMA operation. If the NIC has
     unlimited transfer capacity, set this parameter to -1.</p>
</dd>
</dl>

## -returns
<p><b>NdisMRegisterDmaChannel</b> can return one of the following status values:</p><dl>
<dt><b>NDIS_STATUS_SUCCESS</b></dt>
</dl><p>NDIS claimed the specified DMA channel in the registry for the caller's NIC and set up necessary
       resources for subsequent DMA operations by the miniport driver.</p><dl>
<dt><b>NDIS_STATUS_RESOURCE_CONFLICT</b></dt>
</dl><p>An attempt to claim the DMA channel in the registry has failed, possibly because another driver
       has already claimed that channel for its device. 
       <b>NdisMRegisterDmaChannel</b> logs an error if this occurs.</p><dl>
<dt><b>NDIS_STATUS_RESOURCES</b></dt>
</dl><p>NDIS could not allocate the system resources it needs to support DMA operations by this miniport
       driver.</p><dl>
<dt><b>NDIS_STATUS_FAILURE</b></dt>
</dl><p>Either the bus type or bus number is out of range or the driver declared the NIC to be a bus
       master on an I/O bus other than ISA.</p>

<p> </p>

## -remarks
<p>A driver of a subordinate-DMA NIC must call 
    <b>NdisMRegisterDmaChannel</b> from its 
    <a href="..\ndis\nc-ndis-miniport-initialize.md">MiniportInitializeEx</a> function to
    reserve system resources for subsequent DMA operations and to claim them in the registry.</p>

<p>The driver of an ISA bus-master NIC also must call 
    <b>NdisMRegisterDmaChannel</b> from 
    <i>MiniportInitializeEx</i> to claim a system DMA controller channel for the NIC in the registry.</p>

<p><i>MiniportInitializeEx</i> must call the 
    <a href="..\ndis\nf-ndis-ndismsetminiportattributes.md">
    NdisMSetMiniportAttributes</a> function before calling 
    <b>NdisMRegisterDmaChannel</b>.</p>

<p><i>MiniportInitializeEx</i> obtained the bus-relative values passed to 
    <b>NdisMRegisterDmaChannel</b> either from the registry or by calling the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff563591">NdisMGetBusData</a> function.</p>

<p>If such a driver cannot allocate the system DMA resources that its device needs, 
    <i>MiniportInitializeEx</i> should release all resources it already allocated for the NIC and, then, fail
    initialization for that NIC.</p>

<p>If the driver successfully registers the DMA channel, it must later call the 
    <a href="..\ndis\nf-ndis-ndismderegisterdmachannel.md">
    NdisMDeregisterDmaChannel</a> function to deregister the DMA channel.</p>

<p>A driver of a subordinate-DMA NIC must call 
    <b>NdisMRegisterDmaChannel</b> from its 
    <a href="..\ndis\nc-ndis-miniport-initialize.md">MiniportInitializeEx</a> function to
    reserve system resources for subsequent DMA operations and to claim them in the registry.</p>

<p>The driver of an ISA bus-master NIC also must call 
    <b>NdisMRegisterDmaChannel</b> from 
    <i>MiniportInitializeEx</i> to claim a system DMA controller channel for the NIC in the registry.</p>

<p><i>MiniportInitializeEx</i> must call the 
    <a href="..\ndis\nf-ndis-ndismsetminiportattributes.md">
    NdisMSetMiniportAttributes</a> function before calling 
    <b>NdisMRegisterDmaChannel</b>.</p>

<p><i>MiniportInitializeEx</i> obtained the bus-relative values passed to 
    <b>NdisMRegisterDmaChannel</b> either from the registry or by calling the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff563591">NdisMGetBusData</a> function.</p>

<p>If such a driver cannot allocate the system DMA resources that its device needs, 
    <i>MiniportInitializeEx</i> should release all resources it already allocated for the NIC and, then, fail
    initialization for that NIC.</p>

<p>If the driver successfully registers the DMA channel, it must later call the 
    <a href="..\ndis\nf-ndis-ndismderegisterdmachannel.md">
    NdisMDeregisterDmaChannel</a> function to deregister the DMA channel.</p>

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
   <a href="https://msdn.microsoft.com/0493063c-305c-4d2d-a3ab-61eae114a8cf">NdisMRegisterDmaChannel (NDIS
   5.1)</a>) in Windows Vista. Supported for NDIS 5.1 drivers (see 
   <b>NdisMRegisterDmaChannel (NDIS
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
<a href="..\ndis\nc-ndis-miniport-initialize.md">MiniportInitializeEx</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563574">NdisMDeregisterDmaChannel</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563591">NdisMGetBusData</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563672">NdisMSetMiniportAttributes</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisMRegisterDmaChannel function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
