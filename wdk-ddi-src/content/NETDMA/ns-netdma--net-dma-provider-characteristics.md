---
UID: NS.netdma._NET_DMA_PROVIDER_CHARACTERISTICS
title: NET_DMA_PROVIDER_CHARACTERISTICS
author: windows-driver-content
description: The NET_DMA_PROVIDER_CHARACTERISTICS structure specifies the characteristics for a NetDMA provider, including the entry points for the ProviderXxx functions.
old-location: netvista\net_dma_provider_characteristics.htm
ms.assetid: 7ec6d449-fdc2-44d8-976b-5a1d23c76e7b
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: netvista
req.header: netdma.h
req.include-header: Netdma.h
req.target-type: Windows
req.target-min-winverclnt: Supported for NetDMA 2.0 drivers in Windows Server 2008. (Added FriendlyName
   member.) Supported for NetDMA 1.1 drivers in Windows Server 2008. Supported for NetDMA 1.0 drivers in
   Windows Server 2008 and Windows Vista.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NET_DMA_PROVIDER_CHARACTERISTICS
req.alt-loc: netdma.h
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
ms.keywords: NET_DMA_PROVIDER_CHARACTERISTICS, NET_DMA_PROVIDER_CHARACTERISTICS, *PNET_DMA_PROVIDER_CHARACTERISTICS
req.iface: 
---

# NET_DMA_PROVIDER_CHARACTERISTICS structure



## -description

## -syntax

````
typedef struct _NET_DMA_PROVIDER_CHARACTERISTICS {
  UCHAR                             MajorVersion;
  UCHAR                             MinorVersion;
  USHORT                            Size;
  ULONG                             Flags;
  PDEVICE_OBJECT                    PhysicalDeviceObject;
  ULONG                             MaxDmaChannelCount;
  DMA_CHANNELS_CPU_AFFINITY_HANDLER SetDmaChannelCpuAffinity;
  DMA_CHANNEL_ALLOCATE_HANDLER      AllocateDmaChannel;
  DMA_CHANNEL_FREE_HANDLER          FreeDmaChannel;
  DMA_START_HANDLER                 StartDma;
  DMA_SUSPEND_HANDLER               SuspendDma;
  DMA_RESUME_HANDLER                ResumeDma;
  DMA_ABORT_HANDLER                 AbortDma;
  DMA_APPEND_HANDLER                AppendDma;
  DMA_RESET_HANDLER                 ResetChannel;
  UNICODE_STRING                    FriendlyName;
} NET_DMA_PROVIDER_CHARACTERISTICS, *PNET_DMA_PROVIDER_CHARACTERISTICS;
````


## -struct-fields
<dl>

### -field <b>MajorVersion</b>

<dd>
<p>The major version number of the DMA provider driver.</p>
</dd>

### -field <b>MinorVersion</b>

<dd>
<p>The minor version number of the DMA provider driver.</p>
</dd>

### -field <b>Size</b>

<dd>
<p>The size, in bytes, of this NET_DMA_PROVIDER_CHARACTERISTICS structure. Set this member to 
     sizeof(NET_DMA_PROVIDER_CHARACTERISTICS).</p>
</dd>

### -field <b>Flags</b>

<dd>
<p>DMA provider characteristics flags. NetDMA 1.0 and 1.1 drivers set this member to zero.
     </p>
<p>NetDMA 2.0 and later drivers can use the following flags.</p>
<p></p>
<dl>

### -field <a id="NET_DMA_PROVIDER_CHARACTERISTICS_DCA_SUPPORTED"></a><a id="net_dma_provider_characteristics_dca_supported"></a>NET_DMA_PROVIDER_CHARACTERISTICS_DCA_SUPPORTED

<dd>
<p>The NetDMA provider supports 
       <a href="NULL">Direct Cache Access (DCA)</a>.</p>
</dd>
</dl>
</dd>

### -field <b>PhysicalDeviceObject</b>

<dd>
<p>The physical device object (PDO) that is associated with the DMA provider. The Plug and Play (PnP)
     manager supplies a pointer to the PDO at the 
     <i>PhysicalDeviceObject</i> parameter to the 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff540521">AddDevice</a> routine.</p>
</dd>

### -field <b>MaxDmaChannelCount</b>

<dd>
<p>The maximum number of DMA channels that the DMA provider can support.</p>
</dd>

### -field <b>SetDmaChannelCpuAffinity</b>

<dd>
<p>The entry point for the 
     <a href="https://msdn.microsoft.com/a53d8798-63fa-4b16-bda2-880ca3521d03">
     ProviderSetDmaChannelCpuAffinity</a> function.</p>
</dd>

### -field <b>AllocateDmaChannel</b>

<dd>
<p>The entry point for the 
     <a href="https://msdn.microsoft.com/42bc0e08-3d85-424f-aaa4-4df788d3706a">
     ProviderAllocateDmaChannel</a> function.</p>
</dd>

### -field <b>FreeDmaChannel</b>

<dd>
<p>The entry point for the 
     <a href="https://msdn.microsoft.com/5bbe432d-f236-46ec-8e78-788bd676b852">
     ProviderFreeDmaChannel</a> function.</p>
</dd>

### -field <b>StartDma</b>

<dd>
<p>The entry point for the 
     <a href="https://msdn.microsoft.com/0926e8c4-f2ca-401f-abe8-76aec359a1e2">ProviderStartDma</a> function.</p>
</dd>

### -field <b>SuspendDma</b>

<dd>
<p>The entry point for the 
     <a href="https://msdn.microsoft.com/b020b0c6-eb69-44d0-a374-b39eb2f536f1">ProviderSuspendDma</a> function. If this
     function is not supported, set this member to <b>NULL</b>.</p>
</dd>

### -field <b>ResumeDma</b>

<dd>
<p>The entry point for the 
     <a href="https://msdn.microsoft.com/06609603-eeed-4fb0-a878-87cad2e72b46">ProviderResumeDma</a> function. If this
     function is not supported, set this member to <b>NULL</b>.</p>
</dd>

### -field <b>AbortDma</b>

<dd>
<p>The entry point for the 
     <a href="https://msdn.microsoft.com/b9c23f36-0885-49fd-b92e-dac38d5f363f">ProviderAbortDma</a> function. If this
     function is not supported, set this member to <b>NULL</b>.</p>
</dd>

### -field <b>AppendDma</b>

<dd>
<p>The entry point for the 
     <a href="https://msdn.microsoft.com/51de8ddf-cbfc-4e49-b44a-207307a937e7">ProviderAppendDma</a> function.</p>
</dd>

### -field <b>ResetChannel</b>

<dd>
<p>The entry point for the 
     <a href="https://msdn.microsoft.com/ee882897-fbc6-4017-8c30-2a54f6c49491">ProviderResetChannel</a> function. If
     this function is not supported, set this member to <b>NULL</b>.</p>
</dd>

### -field <b>FriendlyName</b>

<dd>
<p>A Unicode string that represents the user-readable description of the NetDMA provider
     driver.</p>
</dd>
</dl>

## -remarks
<p>To register a DMA provider, a DMA provider driver calls the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff568336">NetDmaRegisterProvider</a> function
    from its 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff540521">AddDevice</a> routine.</p>

<p>The DMA provider driver supplies a NET_DMA_PROVIDER_CHARACTERISTICS structure at the 
    <i>ProviderCharacteristics</i> parameter of 
    <b>NetDmaRegisterProvider</b>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Supported for NetDMA 2.0 drivers in Windows Server 2008. (Added FriendlyName
   member.) Supported for NetDMA 1.1 drivers in Windows Server 2008. Supported for NetDMA 1.0 drivers in
   Windows Server 2008 and Windows Vista.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Netdma.h (include Netdma.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff540521">AddDevice</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff568336">NetDmaRegisterProvider</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/b9c23f36-0885-49fd-b92e-dac38d5f363f">ProviderAbortDma</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/42bc0e08-3d85-424f-aaa4-4df788d3706a">ProviderAllocateDmaChannel</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/51de8ddf-cbfc-4e49-b44a-207307a937e7">ProviderAppendDma</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/5bbe432d-f236-46ec-8e78-788bd676b852">ProviderFreeDmaChannel</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/a53d8798-63fa-4b16-bda2-880ca3521d03">
   ProviderSetDmaChannelCpuAffinity</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/0926e8c4-f2ca-401f-abe8-76aec359a1e2">ProviderStartDma</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/b020b0c6-eb69-44d0-a374-b39eb2f536f1">ProviderSuspendDma</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/ee882897-fbc6-4017-8c30-2a54f6c49491">ProviderResetChannel</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/06609603-eeed-4fb0-a878-87cad2e72b46">ProviderResumeDma</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NET_DMA_PROVIDER_CHARACTERISTICS structure%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
