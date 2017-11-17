---
UID: NE.wdfdmaenabler._WDF_DMA_PROFILE
title: WDF_DMA_PROFILE
author: windows-driver-content
description: The WDF_DMA_PROFILE enumeration identifies the types of bus-master or system-mode DMA operations that devices can support.
old-location: wdf\wdf_dma_profile.htm
ms.assetid: a2672bca-5c2e-423d-9ba0-fad610170e88
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: wdf
req.header: wdfdmaenabler.h
req.include-header: Wdf.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 
req.alt-api: WDF_DMA_PROFILE
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
req.irql: PASSIVE_LEVEL
ms.keywords: WDF_REMOVE_LOCK_OPTIONS, WDF_REMOVE_LOCK_OPTIONS, *PWDF_REMOVE_LOCK_OPTIONS
req.iface: 
req.product: Windows 10 or later.
---

# WDF_DMA_PROFILE enumeration



## -description
<p class="CCE_Message">[Applies to KMDF only]</p>
<p>The <b>WDF_DMA_PROFILE</b> enumeration identifies the types of bus-master or system-mode DMA operations that devices can support.</p>


## -syntax

````
typedef enum _WDF_DMA_PROFILE { 
  WdfDmaProfileInvalid                = 0,
  WdfDmaProfilePacket                 = 1,
  WdfDmaProfileScatterGather          = 2,
  WdfDmaProfilePacket64               = 3,
  WdfDmaProfileScatterGather64        = 4,
  WdfDmaProfileScatterGatherDuplex    = 5,
  WdfDmaProfileScatterGather64Duplex  = 6,
  WdfDmaProfileSystem                 = 7,
  WdfDmaProfileSystemDuplex           = 8
} WDF_DMA_PROFILE;
````


## -enum-fields
<dl>

### -field <a id="WdfDmaProfileInvalid"></a><a id="wdfdmaprofileinvalid"></a><a id="WDFDMAPROFILEINVALID"></a><b>WdfDmaProfileInvalid</b>

<dd>
<p>For internal use only.</p>
</dd>

### -field <a id="WdfDmaProfilePacket"></a><a id="wdfdmaprofilepacket"></a><a id="WDFDMAPROFILEPACKET"></a><b>WdfDmaProfilePacket</b>

<dd>
<p>The device supports single-packet DMA operations, using 32-bit addressing.</p>
</dd>

### -field <a id="WdfDmaProfileScatterGather"></a><a id="wdfdmaprofilescattergather"></a><a id="WDFDMAPROFILESCATTERGATHER"></a><b>WdfDmaProfileScatterGather</b>

<dd>
<p>The device supports packet-based, scatter/gather DMA operations, using 32-bit addressing.</p>
</dd>

### -field <a id="WdfDmaProfilePacket64"></a><a id="wdfdmaprofilepacket64"></a><a id="WDFDMAPROFILEPACKET64"></a><b>WdfDmaProfilePacket64</b>

<dd>
<p>The device supports single-packet DMA operations, using 64-bit addressing.</p>
</dd>

### -field <a id="WdfDmaProfileScatterGather64"></a><a id="wdfdmaprofilescattergather64"></a><a id="WDFDMAPROFILESCATTERGATHER64"></a><b>WdfDmaProfileScatterGather64</b>

<dd>
<p>The device supports packet-based, scatter/gather DMA operations, using 64-bit addressing.</p>
</dd>

### -field <a id="WdfDmaProfileScatterGatherDuplex"></a><a id="wdfdmaprofilescattergatherduplex"></a><a id="WDFDMAPROFILESCATTERGATHERDUPLEX"></a><b>WdfDmaProfileScatterGatherDuplex</b>

<dd>
<p>The device supports packet-based, scatter/gather DMA operations, using 32-bit addressing. The device also supports duplex operation.</p>
</dd>

### -field <a id="WdfDmaProfileScatterGather64Duplex"></a><a id="wdfdmaprofilescattergather64duplex"></a><a id="WDFDMAPROFILESCATTERGATHER64DUPLEX"></a><b>WdfDmaProfileScatterGather64Duplex</b>

<dd>
<p>The device supports packet-based, scatter/gather DMA operations, using 64-bit addressing. The device also supports duplex operation.</p>
</dd>

### -field <a id="WdfDmaProfileSystem"></a><a id="wdfdmaprofilesystem"></a><a id="WDFDMAPROFILESYSTEM"></a><b>WdfDmaProfileSystem</b>

<dd>
<p>The device supports system-mode DMA operations. This value is available in version 1.11 and later versions of KMDF running on Windows 8 or later versions of Windows.</p>
</dd>

### -field <a id="WdfDmaProfileSystemDuplex"></a><a id="wdfdmaprofilesystemduplex"></a><a id="WDFDMAPROFILESYSTEMDUPLEX"></a><b>WdfDmaProfileSystemDuplex</b>

<dd>
<p>The device supports system-mode DMA operations. The device also supports duplex operation. This value is available in version 1.11 and later versions of KMDF running on Windows 8 or later versions of Windows.</p>
</dd>
</dl>

## -remarks
<p><b>WDF_DMA_PROFILE</b>-typed values are used within the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/ff551290">WDF_DMA_ENABLER_CONFIG</a> structure. The driver supplies <b>WDF_DMA_ENABLER_CONFIG</b> when it calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff546983">WdfDmaEnablerCreate</a>.</p>

<p>If the driver selects one of the system-mode DMA profiles, the framework requests the DMA version 3 interface from WDM.  System-mode DMA is available starting in Windows 8. For more information about system-mode DMA, see <a href="wdf.supporting_system-mode_dma">Supporting System-Mode DMA</a>.</p>

<p>Kernel-Mode Driver Framework (KMDF) miniport drivers such as NDIS miniport drivers can request the system-mode DMA profiles. For information about how to write a framework-based miniport driver, see <a href="wdf.creating_kmdf_miniport_drivers">Creating Framework-based Miniport Drivers</a>. </p>

<p><b>WDF_DMA_PROFILE</b>-typed values are used within the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/ff551290">WDF_DMA_ENABLER_CONFIG</a> structure. The driver supplies <b>WDF_DMA_ENABLER_CONFIG</b> when it calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff546983">WdfDmaEnablerCreate</a>.</p>

<p>If the driver selects one of the system-mode DMA profiles, the framework requests the DMA version 3 interface from WDM.  System-mode DMA is available starting in Windows 8. For more information about system-mode DMA, see <a href="wdf.supporting_system-mode_dma">Supporting System-Mode DMA</a>.</p>

<p>Kernel-Mode Driver Framework (KMDF) miniport drivers such as NDIS miniport drivers can request the system-mode DMA profiles. For information about how to write a framework-based miniport driver, see <a href="wdf.creating_kmdf_miniport_drivers">Creating Framework-based Miniport Drivers</a>. </p>

<p><b>WDF_DMA_PROFILE</b>-typed values are used within the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/ff551290">WDF_DMA_ENABLER_CONFIG</a> structure. The driver supplies <b>WDF_DMA_ENABLER_CONFIG</b> when it calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff546983">WdfDmaEnablerCreate</a>.</p>

<p>If the driver selects one of the system-mode DMA profiles, the framework requests the DMA version 3 interface from WDM.  System-mode DMA is available starting in Windows 8. For more information about system-mode DMA, see <a href="wdf.supporting_system-mode_dma">Supporting System-Mode DMA</a>.</p>

<p>Kernel-Mode Driver Framework (KMDF) miniport drivers such as NDIS miniport drivers can request the system-mode DMA profiles. For information about how to write a framework-based miniport driver, see <a href="wdf.creating_kmdf_miniport_drivers">Creating Framework-based Miniport Drivers</a>. </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum KMDF version</p>
</th>
<td width="70%">
<p>1.0</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551290">WDF_DMA_ENABLER_CONFIG</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WDF_DMA_PROFILE enumeration%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
