---
UID: NF.wdfdmaenabler.WDF_DMA_SYSTEM_PROFILE_CONFIG_INIT
title: WDF_DMA_SYSTEM_PROFILE_CONFIG_INIT function
author: windows-driver-content
description: The WDF_DMA_SYSTEM_PROFILE_CONFIG_INIT function initializes a driver's WDF_DMA_SYSTEM_PROFILE_CONFIG structure.
old-location: wdf\wdf_dma_system_profile_config_init.htm
old-project: wdf
ms.assetid: C3E9B4D6-A1BB-425E-A131-D93C3219D28B
ms.author: windowsdriverdev
ms.date: 12/7/2017
ms.keywords: WDF_DMA_SYSTEM_PROFILE_CONFIG_INIT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdfdmaenabler.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: 
req.kmdf-ver: 1.11
req.umdf-ver: 
req.alt-api: WDF_DMA_SYSTEM_PROFILE_CONFIG_INIT
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
req.irql: 
req.product: Windows 10 or later.
---

# WDF_DMA_SYSTEM_PROFILE_CONFIG_INIT function



## -description
<p class="CCE_Message">[Applies to KMDF only]

The <b>WDF_DMA_SYSTEM_PROFILE_CONFIG_INIT</b> function initializes a driver's <a href="wdf.wdf_dma_system_profile_config">WDF_DMA_SYSTEM_PROFILE_CONFIG</a> structure.



## -syntax

````
__inline
void WDF_DMA_SYSTEM_PROFILE_CONFIG_INIT(
  _Out_ PWDF_DMA_SYSTEM_PROFILE_CONFIG  Config,
  _In_  PHYSICAL_ADDRESS                Address,
  _In_  DMA_WIDTH                       DmaWidth,
  _In_  PCM_PARTIAL_RESOURCE_DESCRIPTOR DmaDescriptor
);
````


## -parameters

### -param Config [out]

A pointer to a driver-allocated <a href="wdf.wdf_dma_system_profile_config">WDF_DMA_SYSTEM_PROFILE_CONFIG</a> structure.


### -param Address [in]

The translated address of the register to target for DMA. For more information, see Remarks.


### -param DmaWidth [in]

The width of the register specified by <b>Address</b>.


### -param DmaDescriptor [in]

The translated resource descriptor for the DMA channel assigned 
      the device during <a href="..\wdfdevice\nc-wdfdevice-evt_wdf_device_prepare_hardware.md">EvtDevicePrepareHardware</a>.


## -returns
This function does not return a value.


## -remarks
Typically, a driver calls <b>WDF_DMA_SYSTEM_PROFILE_CONFIG_INIT</b> from within its <a href="..\wdfdevice\nc-wdfdevice-evt_wdf_device_prepare_hardware.md">EvtDevicePrepareHardware</a> callback function. A driver must call the <b>WDF_DMA_SYSTEM_PROFILE_CONFIG_INIT</b> function before calling <a href="wdf.wdfdmaenablerconfiguresystemprofile">WdfDmaEnablerConfigureSystemProfile</a>.

Depending on the System on a Chip (SoC) design, the <i>Address</i> parameter might have a different meaning. For example if DMA uses dedicated transfer ports on the device, <i>Address</i> might indicate the port to which DMA writes occur.

 For more information about creating a system-mode DMA enabler, see <a href="wdf.supporting_system-mode_dma">Supporting System-Mode DMA</a>.

For a code example that uses <b>WDF_DMA_SYSTEM_PROFILE_CONFIG_INIT</b>, see <a href="wdf.wdfdmaenablerconfiguresystemprofile">WdfDmaEnablerConfigureSystemProfile</a>.


## -requirements
<table>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Minimum support

</th>
<td width="70%">
Windows 8

</td>
</tr>
<tr>
<th width="30%">
Minimum KMDF version

</th>
<td width="70%">
1.11

</td>
</tr>
<tr>
<th width="30%">
Header

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
<a href="wdf.wdf_dma_system_profile_config">WDF_DMA_SYSTEM_PROFILE_CONFIG</a>
</dt>
<dt>
<a href="wdf.wdfdmaenablercreate">WdfDmaEnablerCreate</a>
</dt>
<dt>
<a href="wdf.wdfdmaenablerconfiguresystemprofile">WdfDmaEnablerConfigureSystemProfile</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WDF_DMA_SYSTEM_PROFILE_CONFIG_INIT function%20 RELEASE:%20(12/7/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

