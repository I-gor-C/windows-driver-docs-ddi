---
UID: NC.wdm.PCALCULATE_SCATTER_GATHER_LIST_SIZE
title: PCALCULATE_SCATTER_GATHER_LIST_SIZE
author: windows-driver-content
description: The CalculateScatterGatherList routine calculates the size, in bytes, of scatter/gather list necessary to hold a given buffer.
old-location: kernel\calculatescattergatherlist.htm
old-project: kernel
ms.assetid: d7509502-0965-44b9-8efb-cec4fbe3ac88
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: _WDI_TYPE_PMK_NAME, WDI_TYPE_PMK_NAME, PWDI_TYPE_PMK_NAME, *PWDI_TYPE_PMK_NAME
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: wdm.h
req.include-header: Wdm.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows XP and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: CalculateScatterGatherList
req.alt-loc: wdm.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: Any level
req.product: Windows 10 or later.
---

# PCALCULATE_SCATTER_GATHER_LIST_SIZE callback



## -description
The <b>CalculateScatterGatherList</b> routine calculates the size, in bytes, of scatter/gather list necessary to hold a given buffer.



## -prototype

````
PCALCULATE_SCATTER_GATHER_LIST_SIZE CalculateScatterGatherList;

NTSTATUS CalculateScatterGatherList(
  _In_      PDMA_ADAPTER DmaAdapter,
  _In_opt_  PMDL         Mdl,
  _In_      PVOID        CurrentVa,
  _In_      ULONG        Length,
  _Out_     PULONG       ScatterGatherListSize,
  _Out_opt_ PULONG       NumberOfMapRegisters
)
{ ... }
````


## -parameters

### -param DmaAdapter [in]

Pointer to the <a href="kernel.dma_adapter">DMA_ADAPTER</a> structure returned by <a href="kernel.iogetdmaadapter">IoGetDmaAdapter</a> that represents the bus-master adapter or DMA controller.


### -param Mdl [in, optional]

Either <b>NULL</b> or a pointer to the MDL that contains the buffer. 


### -param CurrentVa [in]

Pointer to the virtual address of the beginning of the buffer. 


### -param Length [in]

Specifies the length of the buffer, in bytes. 


### -param ScatterGatherListSize [out]

Pointer to the variable the routine uses to return the size of the scatter/gather list, in bytes.


### -param NumberOfMapRegisters [out, optional]

Either <b>NULL</b> or pointer to the variable the routine uses to return the number of map registers needed for DMA operations on the buffer. 


## -returns
<b>CalculateScatterGatherList</b> returns one of the following status codes.
<dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl>The values returned in <i>ScatterGatherListSize</i> and <i>NumberOfMapRegisters</i> are valid. 
<dl>
<dt><b>STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl>The number of map registers required exceeds the number of map registers available. 
<dl>
<dt><b>STATUS_BUFFER_TOO_SMALL</b></dt>
</dl>The specified <i>Length</i> is too big to fit within the buffer. 

 


## -remarks
<b>CalculateScatterGatherList</b>
      is not a system routine that can be called directly by name. This routine can be called only by pointer from the address returned in a 
     <a href="kernel.dma_operations">DMA_OPERATIONS</a>
      structure. Drivers obtain the address of this routine by calling <a href="kernel.iogetdmaadapter">IoGetDmaAdapter</a> with the <b>Version</b> member of the <i>DeviceDescription</i> parameter set to DEVICE_DESCRIPTION_VERSION2. If <b>IoGetDmaAdapter</b> returns <b>NULL</b>, the routine is not available on your platform.

If the caller passes <b>NULL</b> for the <i>Mdl</i> parameter, the routine calculates the maximum possible size needed to hold a scatter/gather list for the specified buffer. If the caller specifies the MDL that contains the buffer in the <i>Mdl</i> parameter, the routine computes the actual size needed to hold the scatter/gather list.

A driver uses <b>CalculateScatterGatherList</b> to allocate a scatter/gather list buffer to pass to <a href="..\wdm\nc-wdm-pbuild_scatter_gather_list.md">BuildScatterGatherList</a>.


## -requirements
<table>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Version

</th>
<td width="70%">
Available in Windows XP and later versions of Windows. 

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Wdm.h (include Wdm.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL

</th>
<td width="70%">
Any level

</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="kernel.device_description">DEVICE_DESCRIPTION</a>
</dt>
<dt>
<a href="kernel.dma_adapter">DMA_ADAPTER</a>
</dt>
<dt>
<a href="kernel.dma_operations">DMA_OPERATIONS</a>
</dt>
<dt>
<a href="kernel.scatter_gather_list">SCATTER_GATHER_LIST</a>
</dt>
<dt>
<a href="..\wdm\nc-wdm-pbuild_scatter_gather_list.md">BuildScatterGatherList</a>
</dt>
<dt>
<a href="kernel.iogetdmaadapter">IoGetDmaAdapter</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20PCALCULATE_SCATTER_GATHER_LIST_SIZE callback function%20 RELEASE:%20(12/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

