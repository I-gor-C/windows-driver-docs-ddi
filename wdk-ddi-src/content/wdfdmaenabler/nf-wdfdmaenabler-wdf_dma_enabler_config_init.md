---
UID: NF.wdfdmaenabler.WDF_DMA_ENABLER_CONFIG_INIT
title: WDF_DMA_ENABLER_CONFIG_INIT function
author: windows-driver-content
description: The WDF_DMA_ENABLER_CONFIG_INIT function initializes a driver's WDF_DMA_ENABLER_CONFIG structure.
old-location: wdf\wdf_dma_enabler_config_init.htm
old-project: wdf
ms.assetid: b01efb50-a3b2-4ffd-83e6-daa0ebbc6484
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: WDF_DMA_ENABLER_CONFIG_INIT
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
req.alt-api: WDF_DMA_ENABLER_CONFIG_INIT
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
req.product: Windows 10 or later.
---

# WDF_DMA_ENABLER_CONFIG_INIT function



## -description
<p class="CCE_Message">[Applies to KMDF only]

The <b>WDF_DMA_ENABLER_CONFIG_INIT</b> function initializes a driver's <a href="wdf.wdf_dma_enabler_config">WDF_DMA_ENABLER_CONFIG</a> structure.



## -syntax

````
VOID WDF_DMA_ENABLER_CONFIG_INIT(
  _Out_ PWDF_DMA_ENABLER_CONFIG Config,
  _In_  WDF_DMA_PROFILE         Profile,
  _In_  size_t                  MaximumLength
);
````


## -parameters

### -param Config [out]

A pointer to a driver-allocated <a href="wdf.wdf_dma_enabler_config">WDF_DMA_ENABLER_CONFIG</a> structure.


### -param Profile [in]

A value for the <b>Profile</b> member of the <a href="wdf.wdf_dma_enabler_config">WDF_DMA_ENABLER_CONFIG</a> structure.


### -param MaximumLength [in]

A value for the <b>MaximumLength</b> member of the <a href="wdf.wdf_dma_enabler_config">WDF_DMA_ENABLER_CONFIG</a> structure.


## -returns
None


## -remarks
Drivers must call the <b>WDF_DMA_ENABLER_CONFIG_INIT</b> function before calling <a href="wdf.wdfdmaenablercreate">WdfDmaEnablerCreate</a>. 

For a code example that uses <b>WDF_DMA_ENABLER_CONFIG_INIT</b>, see <a href="wdf.wdfdmaenablercreate">WdfDmaEnablerCreate</a>.


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
IRQL

</th>
<td width="70%">
PASSIVE_LEVEL

</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="wdf.wdf_dma_enabler_config">WDF_DMA_ENABLER_CONFIG</a>
</dt>
<dt>
<a href="wdf.wdfdmaenablercreate">WdfDmaEnablerCreate</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WDF_DMA_ENABLER_CONFIG_INIT function%20 RELEASE:%20(12/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

