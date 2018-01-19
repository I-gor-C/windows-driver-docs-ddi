---
UID : NC:d3dkmddi.DXGKDDI_MONITORDESCRIPTORSET_RELEASEDESCRIPTORINFO
title : DXGKDDI_MONITORDESCRIPTORSET_RELEASEDESCRIPTORINFO
author : windows-driver-content
description : The pfnReleaseDescriptorInfo function releases a D3DKMDT_MONITOR_DESCRIPTOR structure that the VidPN manager previously provided to the display miniport driver.
old-location : display\dxgk_monitordescriptorset_interface_pfnreleasedescriptorinfo.htm
old-project : display
ms.assetid : 8debdd01-c4e4-4b7c-b4cd-c1143ea7ebaa
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
req.alt-api : pfnReleaseDescriptorInfo
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


# DXGKDDI_MONITORDESCRIPTORSET_RELEASEDESCRIPTORINFO callback function
The <b>pfnReleaseDescriptorInfo</b> function releases a <a href="..\d3dkmdt\ns-d3dkmdt-_d3dkmdt_monitor_descriptor.md">D3DKMDT_MONITOR_DESCRIPTOR</a> structure that the VidPN manager previously provided to the display miniport driver.

## Syntax

```
DXGKDDI_MONITORDESCRIPTORSET_RELEASEDESCRIPTORINFO DxgkddiMonitordescriptorsetReleasedescriptorinfo;

NTSTATUS DxgkddiMonitordescriptorsetReleasedescriptorinfo(
  IN_CONST_D3DKMDT_HMONITORDESCRIPTORSET hMonitorDescriptorSet,
  IN_CONST_PD3DKMDT_MONITOR_DESCRIPTOR_CONST pMonitorDescriptorInfo
)
{...}
```

## Parameters

`hMonitorDescriptorSet`

A handle to a monitor descriptor set object. The display miniport driver previously obtained this handle by calling the <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi_monitor_getmonitordescriptorset.md">pfnGetMonitorDescriptorSet</a> function of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff568433">Monitor interface</a>.

`pMonitorDescriptorInfo`

A pointer to the D3DKMDT_MONITOR_DESCRIPTOR structure to be released.


## Return Value

The <b>pfnReleaseDescriptorInfo</b> function returns one of the following values.
<dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl>The function succeeded.
<dl>
<dt><b>STATUS_INVALID_MONITOR_DESCRIPTOR</b></dt>
</dl>The descriptor supplied in <i>pMonitorDescriptorInfo</i> was invalid.
<dl>
<dt><b>STATUS_GRAPHICS_INVALID_MONITOR_DESCRIPTORSET</b></dt>
</dl>The handle supplied in <i>hMonitorDescriptorSet</i> was invalid.

## Remarks

When you have finished using a D3DKMDT_MONITOR_DESCRIPTOR structure that you obtained by calling <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi_monitordescriptorset_acquirefirstdescriptorinfo.md">pfnAcquireFirstDescriptorInfo</a> or <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi_monitordescriptorset_acquirenextdescriptorinfo.md">pfnAcquireNextDescriptorInfo</a>, you must release it by calling <b>pfnReleaseDescriptorInfo</b>.</p>

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