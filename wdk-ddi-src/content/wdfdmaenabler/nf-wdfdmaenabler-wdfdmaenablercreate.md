---
UID: NF.wdfdmaenabler.WdfDmaEnablerCreate
title: WdfDmaEnablerCreate
author: windows-driver-content
description: The WdfDmaEnablerCreate method creates a DMA enabler object.
old-location: wdf\wdfdmaenablercreate.htm
old-project: wdf
ms.assetid: 750c9293-7662-41e0-9a2a-5c19e49ad20e
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: WdfDmaEnablerCreate
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdfdmaenabler.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 
req.alt-api: WdfDmaEnablerCreate
req.alt-loc: Wdf01000.sys,Wdf01000.sys.dll
req.ddi-compliance: DriverCreate, KmdfIrql, KmdfIrql2
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Wdf01000.sys (see Framework Library Versioning.)
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# WdfDmaEnablerCreate function



## -description
<p class="CCE_Message">[Applies to KMDF only]</p>
<p>The <b>WdfDmaEnablerCreate</b> method creates a DMA enabler object. </p>


## -syntax

````
NTSTATUS WdfDmaEnablerCreate(
  _In_     WDFDEVICE               Device,
  _In_     PWDF_DMA_ENABLER_CONFIG Config,
  _In_opt_ PWDF_OBJECT_ATTRIBUTES  Attributes,
  _Out_    WDFDMAENABLER           *DmaEnablerHandle
);
````


## -parameters
<dl>

### -param <i>Device</i> [in]

<dd>
<p>A handle to a framework device object.</p>
</dd>

### -param <i>Config</i> [in]

<dd>
<p>A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff551290">WDF_DMA_ENABLER_CONFIG</a> structure. Drivers must initialize this structure by calling <a href="..\wdfdmaenabler\nf-wdfdmaenabler-wdf-dma-enabler-config-init.md">WDF_DMA_ENABLER_CONFIG_INIT</a>.</p>
</dd>

### -param <i>Attributes</i> [in, optional]

<dd>
<p>A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff552400">WDF_OBJECT_ATTRIBUTES</a> structure that specifies object attributes for the new DMA enabler object. This parameter is optional and can be WDF_NO_OBJECT_ATTRIBUTES. </p>
</dd>

### -param <i>DmaEnablerHandle</i> [out]

<dd>
<p>A handle to a new DMA enabler object.  </p>
</dd>
</dl>

## -returns
<p><b>WdfDmaEnablerCreate</b> returns STATUS_SUCCESS if the operation succeeds. Otherwise, the method might return one of the following values.</p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>An invalid parameter was detected.</p><dl>
<dt><b>STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl><p>
        There was insufficient memory to construct a new DMA enabler object.
       </p><dl>
<dt><b>STATUS_INFO_LENGTH_MISMATCH</b></dt>
</dl><p>The size of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff551290">WDF_DMA_ENABLER_CONFIG</a> structure is incorrect.</p><dl>
<dt><b>STATUS_NOT_SUPPORTED</b></dt>
</dl><p>The driver requested DMA version 3 on an operating system earlier than Windows 8.</p>

<p> </p>

<p>For a list of other return values that the <b>WdfDmaEnablerCreate</b> method might return, see <a href="wdf.framework_object_creation_errors">Framework Object Creation Errors</a>.

</p>

<p>This method also might return other <a href="https://msdn.microsoft.com/library/windows/hardware/ff557697">NTSTATUS values</a>.</p>

<p>A bug check occurs if the driver supplies an invalid object handle.

</p>

## -remarks
<p>Framework-based drivers must call <b>WdfDmaEnablerCreate</b> before creating DMA transactions for a device.</p>

<p>Before a driver calls <b>WdfDmaEnablerCreate</b>, it must call <a href="https://msdn.microsoft.com/library/windows/hardware/ff546861">WdfDeviceSetAlignmentRequirement</a>.</p>

<p>The framework device object that the <i>Device</i> parameter of <b>WdfDmaEnablerCreate</b> specifies always becomes the parent object for the new DMA enabler object. If the driver specifies a different parent in the <b>ParentObject</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff552400">WDF_OBJECT_ATTRIBUTES</a> structure, the framework ignores this value. The framework deletes the DMA enabler object when it deletes the parent object.</p>

<p>When called with a  <i>Config</i> parameter that requests a system-mode DMA profile, <b>WdfDmaEnablerCreate</b> creates a partially initialized DMA enabler.  The driver must subsequently call <a href="https://msdn.microsoft.com/library/windows/hardware/hh451108">WdfDmaEnablerConfigureSystemProfile</a> to set up the DMA settings for the underlying channels.</p>

<p>For more information about DMA enabler objects and <b>WdfDmaEnablerCreate</b>, see <a href="wdf.enabling_dma_transactions">Enabling DMA Transactions</a>.</p>

<p>The following code example is from the <a href="wdf.sample_kmdf_drivers">PLX9x5x</a> sample driver. This example sets a device's requirement for buffer alignment, initializes a WDF_DMA_ENABLER_CONFIG structure, and calls <b>WdfDmaEnablerCreate</b>.</p>

<p>Framework-based drivers must call <b>WdfDmaEnablerCreate</b> before creating DMA transactions for a device.</p>

<p>Before a driver calls <b>WdfDmaEnablerCreate</b>, it must call <a href="https://msdn.microsoft.com/library/windows/hardware/ff546861">WdfDeviceSetAlignmentRequirement</a>.</p>

<p>The framework device object that the <i>Device</i> parameter of <b>WdfDmaEnablerCreate</b> specifies always becomes the parent object for the new DMA enabler object. If the driver specifies a different parent in the <b>ParentObject</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff552400">WDF_OBJECT_ATTRIBUTES</a> structure, the framework ignores this value. The framework deletes the DMA enabler object when it deletes the parent object.</p>

<p>When called with a  <i>Config</i> parameter that requests a system-mode DMA profile, <b>WdfDmaEnablerCreate</b> creates a partially initialized DMA enabler.  The driver must subsequently call <a href="https://msdn.microsoft.com/library/windows/hardware/hh451108">WdfDmaEnablerConfigureSystemProfile</a> to set up the DMA settings for the underlying channels.</p>

<p>For more information about DMA enabler objects and <b>WdfDmaEnablerCreate</b>, see <a href="wdf.enabling_dma_transactions">Enabling DMA Transactions</a>.</p>

<p>The following code example is from the <a href="wdf.sample_kmdf_drivers">PLX9x5x</a> sample driver. This example sets a device's requirement for buffer alignment, initializes a WDF_DMA_ENABLER_CONFIG structure, and calls <b>WdfDmaEnablerCreate</b>.</p>

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
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Wdf01000.sys (see <a href="wdf.framework_library_versioning">Framework Library Versioning</a>.)</dt>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544957">DriverCreate</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff548167">KmdfIrql</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975091">KmdfIrql2</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551290">WDF_DMA_ENABLER_CONFIG</a>
</dt>
<dt>
<a href="..\wdfdmaenabler\nf-wdfdmaenabler-wdf-dma-enabler-config-init.md">WDF_DMA_ENABLER_CONFIG_INIT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552400">WDF_OBJECT_ATTRIBUTES</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546861">WdfDeviceSetAlignmentRequirement</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfDmaEnablerCreate method%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
