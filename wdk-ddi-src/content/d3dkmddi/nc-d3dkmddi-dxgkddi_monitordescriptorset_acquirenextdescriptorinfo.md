---
UID : NC:d3dkmddi.DXGKDDI_MONITORDESCRIPTORSET_ACQUIRENEXTDESCRIPTORINFO
title : DXGKDDI_MONITORDESCRIPTORSET_ACQUIRENEXTDESCRIPTORINFO
author : windows-driver-content
description : The pfnAcquireNextDescriptorInfo function returns the next descriptor in a monitor descriptor set, given the current descriptor.
old-location : display\dxgk_monitordescriptorset_interface_pfnacquirenextdescriptorinfo.htm
old-project : display
ms.assetid : 34d048df-d4a1-4ef5-b917-791f35de9e3a
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : _DD_MULTISAMPLEQUALITYLEVELSDATA, DD_MULTISAMPLEQUALITYLEVELSDATA
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : callback
req.header : d3dkmddi.h
req.include-header : D3dkmddi.h
req.target-type : Desktop
req.target-min-winverclnt : Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : pfnAcquireNextDescriptorInfo
req.alt-loc : d3dkmddi.h
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : PASSIVE_LEVEL
req.typenames : DD_MULTISAMPLEQUALITYLEVELSDATA
---


# DXGKDDI_MONITORDESCRIPTORSET_ACQUIRENEXTDESCRIPTORINFO callback function
The <b>pfnAcquireNextDescriptorInfo</b> function returns the next descriptor in a monitor descriptor set, given the current descriptor.

## Syntax

```
DXGKDDI_MONITORDESCRIPTORSET_ACQUIRENEXTDESCRIPTORINFO DxgkddiMonitordescriptorsetAcquirenextdescriptorinfo;

NTSTATUS DxgkddiMonitordescriptorsetAcquirenextdescriptorinfo(
  IN_CONST_D3DKMDT_HMONITORDESCRIPTORSET hMonitorDescriptorSet,
  IN_CONST_PD3DKMDT_MONITOR_DESCRIPTOR_CONST pMonitorDescriptorInfo,
  DEREF_OUT_CONST_PPD3DKMDT_MONITOR_DESCRIPTOR ppNextMonitorDescriptorInfo
)
{...}
```

## Parameters

`hMonitorDescriptorSet`

[in] A handle to a monitor descriptor set object. The display miniport driver previously obtained this handle by calling the <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi_monitor_getmonitordescriptorset.md">pfnGetMonitorDescriptorSet</a> function of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff568433">Monitor interface</a>.

`pMonitorDescriptorInfo`

[in] A pointer to a <a href="..\d3dkmdt\ns-d3dkmdt-_d3dkmdt_monitor_descriptor.md">D3DKMDT_MONITOR_DESCRIPTOR</a> structure that is the current descriptor. The display miniport driver previously obtained this pointer by calling <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi_monitordescriptorset_acquirefirstdescriptorinfo.md">pfnAcquireFirstDescriptorInfo</a> or <b>pfnAcquireNextDescriptorInfo</b>.

`ppNextMonitorDescriptorInfo`

[out] A pointer to a variable that receives a pointer to a <a href="..\d3dkmdt\ns-d3dkmdt-_d3dkmdt_monitor_descriptor.md">D3DKMDT_MONITOR_DESCRIPTOR</a> structure. The structure is the next descriptor in the set.


## Return Value

The <b>pfnAcquireNextDescriptorInfo</b> function returns one of the following values.
<dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl>The function successfully returned the next descriptor in the set.
<dl>
<dt><b>STATUS_GRAPHICS_NO_MORE_ELEMENTS_IN_DATASET</b></dt>
</dl>The function succeeded, but there were no more descriptors in the set.
<dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl>An invalid parameter was supplied.
<dl>
<dt><b>STATUS_INVALID_MONITOR_DESCRIPTOR</b></dt>
</dl>The descriptor supplied in <i>pMonitorDescriptorInfo</i> was invalid.
<dl>
<dt><b>STATUS_GRAPHICS_INVALID_MONITOR_DESCRIPTORSET</b></dt>
</dl>The handle supplied in <i>hMonitorDescriptorSet</i> was invalid.

## Remarks

When you have finished using the D3DKMDT_MONITOR_DESCRIPTOR structure, you must release the structure by calling <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi_monitordescriptorset_releasedescriptorinfo.md">pfnReleaseDescriptorInfo</a>.

You can obtain all the descriptors in a monitor descriptor set by calling <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi_monitordescriptorset_acquirefirstdescriptorinfo.md">pfnAcquireFirstDescriptorInfo</a> and then making a sequence of calls to <b>pfnAcquireNextDescriptorInfo</b>.</p>

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Desktop |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | d3dkmddi.h (include D3dkmddi.h) |
| **Library** |  |
| **IRQL** | PASSIVE_LEVEL |
| **DDI compliance rules** |  |