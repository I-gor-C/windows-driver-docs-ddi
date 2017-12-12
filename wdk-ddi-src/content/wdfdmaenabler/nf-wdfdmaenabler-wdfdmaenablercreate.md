---
UID: NF.wdfdmaenabler.WdfDmaEnablerCreate
title: WdfDmaEnablerCreate function
author: windows-driver-content
description: The WdfDmaEnablerCreate method creates a DMA enabler object.
old-location: wdf\wdfdmaenablercreate.htm
old-project: wdf
ms.assetid: 750c9293-7662-41e0-9a2a-5c19e49ad20e
ms.author: windowsdriverdev
ms.date: 12/7/2017
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
req.product: Windows 10 or later.
---

# WdfDmaEnablerCreate function



## -description
<p class="CCE_Message">[Applies to KMDF only]

The <b>WdfDmaEnablerCreate</b> method creates a DMA enabler object. 



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

### -param Device [in]

A handle to a framework device object.


### -param Config [in]

A pointer to a <a href="wdf.wdf_dma_enabler_config">WDF_DMA_ENABLER_CONFIG</a> structure. Drivers must initialize this structure by calling <a href="wdf.wdf_dma_enabler_config_init">WDF_DMA_ENABLER_CONFIG_INIT</a>.


### -param Attributes [in, optional]

A pointer to a <a href="wdf.wdf_object_attributes">WDF_OBJECT_ATTRIBUTES</a> structure that specifies object attributes for the new DMA enabler object. This parameter is optional and can be WDF_NO_OBJECT_ATTRIBUTES. 


### -param DmaEnablerHandle [out]

A handle to a new DMA enabler object.  


## -returns
<b>WdfDmaEnablerCreate</b> returns STATUS_SUCCESS if the operation succeeds. Otherwise, the method might return one of the following values.
<dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl>An invalid parameter was detected.
<dl>
<dt><b>STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl>
        There was insufficient memory to construct a new DMA enabler object.
       
<dl>
<dt><b>STATUS_INFO_LENGTH_MISMATCH</b></dt>
</dl>The size of the <a href="wdf.wdf_dma_enabler_config">WDF_DMA_ENABLER_CONFIG</a> structure is incorrect.
<dl>
<dt><b>STATUS_NOT_SUPPORTED</b></dt>
</dl>The driver requested DMA version 3 on an operating system earlier than Windows 8.

 

For a list of other return values that the <b>WdfDmaEnablerCreate</b> method might return, see <a href="wdf.framework_object_creation_errors">Framework Object Creation Errors</a>.



This method also might return other <a href="https://msdn.microsoft.com/library/windows/hardware/ff557697">NTSTATUS values</a>.

A bug check occurs if the driver supplies an invalid object handle.




## -remarks
Framework-based drivers must call <b>WdfDmaEnablerCreate</b> before creating DMA transactions for a device.

Before a driver calls <b>WdfDmaEnablerCreate</b>, it must call <a href="wdf.wdfdevicesetalignmentrequirement">WdfDeviceSetAlignmentRequirement</a>.

The framework device object that the <i>Device</i> parameter of <b>WdfDmaEnablerCreate</b> specifies always becomes the parent object for the new DMA enabler object. If the driver specifies a different parent in the <b>ParentObject</b> member of the <a href="wdf.wdf_object_attributes">WDF_OBJECT_ATTRIBUTES</a> structure, the framework ignores this value. The framework deletes the DMA enabler object when it deletes the parent object.

When called with a  <i>Config</i> parameter that requests a system-mode DMA profile, <b>WdfDmaEnablerCreate</b> creates a partially initialized DMA enabler.  The driver must subsequently call <a href="wdf.wdfdmaenablerconfiguresystemprofile">WdfDmaEnablerConfigureSystemProfile</a> to set up the DMA settings for the underlying channels.

For more information about DMA enabler objects and <b>WdfDmaEnablerCreate</b>, see <a href="wdf.enabling_dma_transactions">Enabling DMA Transactions</a>.

The following code example is from the <a href="wdf.sample_kmdf_drivers">PLX9x5x</a> sample driver. This example sets a device's requirement for buffer alignment, initializes a WDF_DMA_ENABLER_CONFIG structure, and calls <b>WdfDmaEnablerCreate</b>.


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
Minimum KMDF version

</th>
<td width="70%">
1.0

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
<tr>
<th width="30%">
Library

</th>
<td width="70%">
<dl>
<dt>Wdf01000.sys (see <a href="wdf.framework_library_versioning">Framework Library Versioning</a>.)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL

</th>
<td width="70%">
PASSIVE_LEVEL

</td>
</tr>
<tr>
<th width="30%">
DDI compliance rules

</th>
<td width="70%">
<a href="devtest.kmdf_drivercreate">DriverCreate</a>, <a href="devtest.kmdf_kmdfirql">KmdfIrql</a>, <a href="devtest.kmdf_kmdfirql2">KmdfIrql2</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="wdf.wdf_dma_enabler_config">WDF_DMA_ENABLER_CONFIG</a>
</dt>
<dt>
<a href="wdf.wdf_dma_enabler_config_init">WDF_DMA_ENABLER_CONFIG_INIT</a>
</dt>
<dt>
<a href="wdf.wdf_object_attributes">WDF_OBJECT_ATTRIBUTES</a>
</dt>
<dt>
<a href="wdf.wdfdevicesetalignmentrequirement">WdfDeviceSetAlignmentRequirement</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfDmaEnablerCreate method%20 RELEASE:%20(12/7/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

