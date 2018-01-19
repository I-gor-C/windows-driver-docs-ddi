---
UID : NC:wdm.PBUILD_MDL_FROM_SCATTER_GATHER_LIST
title : PBUILD_MDL_FROM_SCATTER_GATHER_LIST
author : windows-driver-content
description : The BuildMdlFromScatterGatherList routine builds an MDL from a scatter/gather list allocated by the system.Note  This routine is reserved for system use.
old-location : kernel\buildmdlfromscattergatherlist.htm
old-project : kernel
ms.assetid : 2bf190a3-cc42-42b4-b687-cd66021e66c2
ms.author : windowsdriverdev
ms.date : 1/4/2018
ms.keywords : _WDI_TYPE_PMK_NAME, WDI_TYPE_PMK_NAME, *PWDI_TYPE_PMK_NAME
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : callback
req.header : wdm.h
req.include-header : Wdm.h
req.target-type : Desktop
req.target-min-winverclnt : Available in Windows XP and later versions of Windows.
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : BuildMdlFromScatterGatherList
req.alt-loc : wdm.h
req.ddi-compliance : IrqlDispatch
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : <= DISPATCH_LEVEL
req.typenames : WDI_TYPE_PMK_NAME, *PWDI_TYPE_PMK_NAME
req.product : Windows 10 or later.
---


# PBUILD_MDL_FROM_SCATTER_GATHER_LIST callback function
The <b>BuildMdlFromScatterGatherList</b> routine builds an MDL from a scatter/gather list allocated by the system.

## Syntax

```
PBUILD_MDL_FROM_SCATTER_GATHER_LIST PbuildMdlFromScatterGatherList;

NTSTATUS PbuildMdlFromScatterGatherList(
  PDMA_ADAPTER DmaAdapter,
  PSCATTER_GATHER_LIST ScatterGather,
  PMDL OriginalMdl,
  PMDL *TargetMdl
)
{...}
```

## Parameters

`DmaAdapter`

Pointer to the <a href="..\wdm\ns-wdm-_dma_adapter.md">DMA_ADAPTER</a> structure returned by <a href="https://msdn.microsoft.com/library/windows/hardware/ff549220">IoGetDmaAdapter</a> that represents the bus-master adapter or DMA controller.

`ScatterGather`

Pointer to the <a href="..\wdm\ns-wdm-_scatter_gather_list.md">SCATTER_GATHER_LIST</a> structure passed to the driver's <a href="..\wdm\nc-wdm-driver_list_control.md">AdapterListControl</a> routine.

`OriginalMdl`

Pointer to the original MDL that the driver used to build the scatter/gather list.

`*TargetMdl`




## Return Value

<b>BuildMdlFromScatterGatherList</b> returns one of the following status codes:
<dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl>The operation succeeded.
<dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl>The <i>OriginalMdl</i> parameter is <b>NULL</b>.
<dl>
<dt><b>STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl>There is not enough memory available to allocate a new MDL.
<dl>
<dt><b>STATUS_NONE_MAPPED</b></dt>
</dl>The system has already created a new MDL for the memory locations in the scatter/gather list. (This only happens if the routine is called twice on the same scatter/gather list.)

## Remarks

<b>BuildMdlFromScatterGatherList</b>
           is not a system routine that can be called directly by name. This routine can be called only by pointer from the address returned in a 
          <a href="..\wdm\ns-wdm-_dma_operations.md">DMA_OPERATIONS</a>
           structure. Drivers obtain the address of this routine by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff549220">IoGetDmaAdapter</a> with the <b>Version</b> member of the <i>DeviceDescription</i> parameter set to DEVICE_DESCRIPTION_VERSION2. If <b>IoGetDmaAdapter</b> returns <b>NULL</b>, the routine is not available on your platform.

When a driver creates a scatter/gather list to write to a device, the system can make a copy of the data to be written, and use that copy to perform the DMA operation. Use this routine to access the memory locations in the scatter/gather list, regardless of whether those locations are a copy.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Desktop |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | wdm.h (include Wdm.h) |
| **Library** |  |
| **IRQL** | <= DISPATCH_LEVEL |
| **DDI compliance rules** | IrqlDispatch |

## See Also

<dl>
<dt>
<a href="..\wdm\ns-wdm-_device_description.md">DEVICE_DESCRIPTION</a>
</dt>
<dt>
<a href="..\wdm\ns-wdm-_dma_adapter.md">DMA_ADAPTER</a>
</dt>
<dt>
<a href="..\wdm\ns-wdm-_dma_operations.md">DMA_OPERATIONS</a>
</dt>
<dt>
<a href="..\wdm\ns-wdm-_scatter_gather_list.md">SCATTER_GATHER_LIST</a>
</dt>
<dt>
<a href="..\wdm\nc-wdm-pbuild_scatter_gather_list.md">BuildScatterGatherList</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549220">IoGetDmaAdapter</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20PBUILD_MDL_FROM_SCATTER_GATHER_LIST callback function%20 RELEASE:%20(1/4/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>