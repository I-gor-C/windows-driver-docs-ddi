---
UID: NF.wdfdmaenabler.WdfDmaEnablerWdmGetDmaAdapter
title: WdfDmaEnablerWdmGetDmaAdapter function
author: windows-driver-content
description: The WdfDmaEnablerWdmGetDmaAdapter method returns a pointer to a WDM DMA_ADAPTER structure that is associated with a DMA enabler object.
old-location: wdf\wdfdmaenablerwdmgetdmaadapter.htm
old-project: wdf
ms.assetid: 2546303a-53c3-4c6b-a230-eb1ebd74cb76
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: WdfDmaEnablerWdmGetDmaAdapter
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdfdmaenabler.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.5
req.umdf-ver: 
req.alt-api: WdfDmaEnablerWdmGetDmaAdapter
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
req.irql: <=DISPATCH_LEVEL
req.product: Windows 10 or later.
---

# WdfDmaEnablerWdmGetDmaAdapter function



## -description
<p class="CCE_Message">[Applies to KMDF only]
The <b>WdfDmaEnablerWdmGetDmaAdapter</b> method returns a pointer to a WDM <a href="kernel.dma_adapter">DMA_ADAPTER</a> structure that is associated with a DMA enabler object.


## -syntax

````
PDMA_ADAPTER WdfDmaEnablerWdmGetDmaAdapter(
  _In_ WDFDMAENABLER     DmaEnabler,
  _In_ WDF_DMA_DIRECTION DmaDirection
);
````


## -parameters

### -param DmaEnabler [in]

A handle to a DMA enabler object that the driver obtained from a previous call to <a href="wdf.wdfdmaenablercreate">WdfDmaEnablerCreate</a>. 

### -param DmaDirection [in]

A <a href="wdf.wdf_dma_direction">WDF_DMA_DIRECTION</a>-typed value that specifies the direction of the DMA transfer operation. For more information, see the following Remarks section.

## -returns
<b>WdfDmaEnablerWdmGetDmaAdapter</b> returns a pointer to a <a href="kernel.dma_adapter">DMA_ADAPTER</a> structure, or <b>NULL</b> if the <i>DmaDirection</i> parameter's value is invalid.

A bug check occurs if the driver supplies an invalid object handle.



## -remarks
When your driver calls <a href="wdf.wdfdmaenablercreate">WdfDmaEnablerCreate</a>, the framework creates a separate <a href="https://msdn.microsoft.com/8bc672b4-0f4d-4e0c-9904-c8d0a3f3639c">adapter object</a> for each direction if the driver specifies a duplex profile, and it creates a single adapter object if the driver does not specify a duplex profile.

If your driver specified a duplex profile when it called <a href="wdf.wdfdmaenablercreate">WdfDmaEnablerCreate</a>, the <b>WdfDmaEnablerWdmGetDmaAdapter</b> method's <i>DmaDirection</i> parameter's value must be <b>WdfDmaDirectionReadFromDevice</b> to obtain the <a href="kernel.dma_adapter">DMA_ADAPTER</a> structure for read operations and <b>WdfDmaDirectionWriteToDevice</b> to obtain the <b>DMA_ADAPTER</b> structure for write operations.  If your driver did not specify a duplex profile, the driver can specify either <b>WdfDmaDirectionReadFromDevice</b> or <b>WdfDmaDirectionWriteToDevice</b>.

The pointer that <b>WdfDmaEnablerWdmGetDmaAdapter</b> returns is valid until the DMA enabler object is deleted. If the driver provides an <a href="..\wdfobject\nc-wdfobject-evt_wdf_object_context_cleanup.md">EvtCleanupCallback</a> function for the DMA enabler object, the pointer is valid until the callback function returns.

The following code example creates a DMA enabler object and then obtains pointers to the WDM <a href="kernel.dma_adapter">DMA_ADAPTER</a> structures that the framework creates for read and write operations.

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
1.5
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
&lt;=DISPATCH_LEVEL
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
<a href="kernel.dma_adapter">DMA_ADAPTER</a>
</dt>
<dt>
<a href="wdf.wdf_dma_direction">WDF_DMA_DIRECTION</a>
</dt>
<dt>
<a href="wdf.wdfdmaenablercreate">WdfDmaEnablerCreate</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfDmaEnablerWdmGetDmaAdapter method%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
