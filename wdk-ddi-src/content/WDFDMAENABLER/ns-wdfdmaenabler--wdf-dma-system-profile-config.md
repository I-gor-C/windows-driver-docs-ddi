---
UID: NS.wdfdmaenabler._WDF_DMA_SYSTEM_PROFILE_CONFIG
title: WDF_DMA_SYSTEM_PROFILE_CONFIG
author: windows-driver-content
description: The WDF_DMA_SYSTEM_PROFILE_CONFIG structure describes the hardware-specific settings related to a system-mode DMA enabler.
old-location: wdf\wdf_dma_system_profile_config.htm
ms.assetid: 80131AB6-4A2B-4D99-9289-CE9FE26E0695
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: wdf
req.header: wdfdmaenabler.h
req.include-header: Wdf.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: 
req.kmdf-ver: 1.11
req.umdf-ver: 
req.alt-api: WDF_DMA_SYSTEM_PROFILE_CONFIG
req.alt-loc: wdfdmaenabler.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <=DISPATCH_LEVEL
ms.keywords: WDF_DMA_SYSTEM_PROFILE_CONFIG, WDF_DMA_SYSTEM_PROFILE_CONFIG, *PWDF_DMA_SYSTEM_PROFILE_CONFIG
req.iface: 
req.product: Windows 10 or later.
---

# WDF_DMA_SYSTEM_PROFILE_CONFIG structure



## -description
<p class="CCE_Message">[Applies to KMDF only]</p>
<p>The <b>WDF_DMA_SYSTEM_PROFILE_CONFIG</b> structure describes the hardware-specific settings related to a system-mode DMA enabler.</p>


## -syntax

````
typedef struct _WDF_DMA_SYSTEM_PROFILE_CONFIG {
  ULONG                           Size;
  BOOLEAN                         DemandMode;
  BOOLEAN                         LoopedTransfer;
  DMA_WIDTH                       DmaWidth;
  PHYSICAL_ADDRESS                DeviceAddress;
  PCM_PARTIAL_RESOURCE_DESCRIPTOR DmaDescriptor;
} WDF_DMA_SYSTEM_PROFILE_CONFIG, *PWDF_DMA_SYSTEM_PROFILE_CONFIG;
````


## -struct-fields
<dl>

### -field <b>Size</b>

<dd>
<p>The size of this structure in bytes.</p>
</dd>

### -field <b>DemandMode</b>

<dd>
<p>Specifies that the transfer is controlled by the device's DMA  
      request line specified in the <b>DmaDescriptor</b> member of this structure. See more information in Remarks.</p>
</dd>

### -field <b>LoopedTransfer</b>

<dd>
<p>Specifies that the DMA adapter should loop around the specified transfer if the length is greater than the size of the buffer.</p>
</dd>

### -field <b>DmaWidth</b>

<dd>
<p>The width of the register specified by <b>DeviceAddress</b>. Possible values are Width8Bits, Width16Bits, Width32Bits, and Width64Bits.</p>
</dd>

### -field <b>DeviceAddress</b>

<dd>
<p>The translated address to or from which the DMA controller transfers. The driver can specify an offset from this base address on each transaction by calling <a href="https://msdn.microsoft.com/library/windows/hardware/hh451188">WdfDmaTransactionSetDeviceAddressOffset</a>.</p>
</dd>

### -field <b>DmaDescriptor</b>

<dd>
<p>The translated resource descriptor for the DMA channel assigned 
      the device during <a href="https://msdn.microsoft.com/a3d4a983-8a75-44be-bd72-8673d89f9f87">EvtDevicePrepareHardware</a>. This provides the DMA request line for the adapter.</p>
</dd>
</dl>

## -remarks
<p>The driver provides this structure to <a href="https://msdn.microsoft.com/library/windows/hardware/hh451108">WdfDmaEnablerConfigureSystemProfile</a> after creating a system-profile DMA enabler.</p>

<p>Typically, drivers set <b>DemandMode</b> to TRUE.   The driver's <a href="https://msdn.microsoft.com/c01b94b2-aabf-47dd-952a-06e481579614">EvtProgramDma</a> callback function then programs the device to assert its DMA request line and initiate the transfer.  In this case, the transfer might begin while <i>EvtProgramDma</i> is still running.</p>

<p>The driver must ensure that the device's DMA request line is not asserted before the driver's <a href="https://msdn.microsoft.com/c01b94b2-aabf-47dd-952a-06e481579614">EvtProgramDma</a> callback function begins execution. Otherwise, it is possible for the DMA transfer to begin before the framework calls <i>EvtProgramDma</i>.
</p>

<p>If <b>DemandMode</b> is set to FALSE, the DMA transfer may begin before the framework calls the driver’s <a href="https://msdn.microsoft.com/c01b94b2-aabf-47dd-952a-06e481579614">EvtProgramDma</a> function. </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum support</p>
</th>
<td width="70%">
<p>Windows 8</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum KMDF version</p>
</th>
<td width="70%">
<p>1.11</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdfdmaenabler.h (include Wdf.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439499">WDF_DMA_SYSTEM_PROFILE_CONFIG_INIT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh451108">WdfDmaEnablerConfigureSystemProfile</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WDF_DMA_SYSTEM_PROFILE_CONFIG structure%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
