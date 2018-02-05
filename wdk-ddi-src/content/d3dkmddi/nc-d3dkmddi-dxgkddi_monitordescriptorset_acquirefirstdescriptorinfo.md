---
UID : NC:d3dkmddi.DXGKDDI_MONITORDESCRIPTORSET_ACQUIREFIRSTDESCRIPTORINFO
title : DXGKDDI_MONITORDESCRIPTORSET_ACQUIREFIRSTDESCRIPTORINFO
author : windows-driver-content
description : The pfnAcquireFirstDescriptorInfo function returns the first descriptor in a monitor descriptor set object.
old-location : display\dxgk_monitordescriptorset_interface_pfnacquirefirstdescriptorinfo.htm
old-project : display
ms.assetid : 228f6947-a7e5-4b76-8224-fac6889fc77a
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : display.dxgk_monitordescriptorset_interface_pfnacquirefirstdescriptorinfo, pfnAcquireFirstDescriptorInfo callback function [Display Devices], pfnAcquireFirstDescriptorInfo, DXGKDDI_MONITORDESCRIPTORSET_ACQUIREFIRSTDESCRIPTORINFO, DXGKDDI_MONITORDESCRIPTORSET_ACQUIREFIRSTDESCRIPTORINFO, d3dkmddi/pfnAcquireFirstDescriptorInfo, VidPnFunctions_fae7b938-60d5-41c0-92a8-9381e67aa411.xml
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
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : DD_MULTISAMPLEQUALITYLEVELSDATA
---


# DXGKDDI_MONITORDESCRIPTORSET_ACQUIREFIRSTDESCRIPTORINFO callback function
The <b>pfnAcquireFirstDescriptorInfo</b> function returns the first descriptor in a monitor descriptor set object.

## Syntax

```
DXGKDDI_MONITORDESCRIPTORSET_ACQUIREFIRSTDESCRIPTORINFO DxgkddiMonitordescriptorsetAcquirefirstdescriptorinfo;

NTSTATUS DxgkddiMonitordescriptorsetAcquirefirstdescriptorinfo(
  IN_CONST_D3DKMDT_HMONITORDESCRIPTORSET hMonitorDescriptorSet,
  DEREF_OUT_CONST_PPD3DKMDT_MONITOR_DESCRIPTOR ppFirstMonitorDescriptorInfo
)
{...}
```

## Parameters

`hMonitorDescriptorSet`

[in] A handle to a monitor descriptor set object. The display miniport driver previously obtained this handle by calling the <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi_monitor_getmonitordescriptorset.md">pfnGetMonitorDescriptorSet</a> function of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff568433">Monitor interface</a>.

`ppFirstMonitorDescriptorInfo`

[out] A pointer to a variable that receives a pointer to a <a href="..\d3dkmdt\ns-d3dkmdt-_d3dkmdt_monitor_descriptor.md">D3DKMDT_MONITOR_DESCRIPTOR</a> structure. The structure is the first descriptor in the set.


## Return Value

The <b>pfnAcquireFirstDescriptorInfo</b> function returns one of the following values.
<table>
<tr>
<th>Return code</th>
<th>Description</th>
</tr>
<tr>
<td width="40%">
<dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl>
</td>
<td width="60%">
The function successfully returned the first descriptor in the set.

</td>
</tr>
<tr>
<td width="40%">
<dl>
<dt><b>STATUS_GRAPHICS_DATASET_IS_EMPTY</b></dt>
</dl>
</td>
<td width="60%">
The function succeeded, but there were no descriptors in the set.

</td>
</tr>
<tr>
<td width="40%">
<dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl>
</td>
<td width="60%">
An invalid parameter was supplied.

</td>
</tr>
<tr>
<td width="40%">
<dl>
<dt><b>STATUS_GRAPHICS_INVALID_MONITOR_DESCRIPTORSET</b></dt>
</dl>
</td>
<td width="60%">
The handle supplied in <i>hMonitorDescriptorSet</i> was invalid.

</td>
</tr>
</table>

## Remarks

When you have finished using the D3DKMDT_MONITOR_DESCRIPTOR structure, you must release the structure by calling <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi_monitordescriptorset_releasedescriptorinfo.md">pfnReleaseDescriptorInfo</a>.

You can obtain all the descriptors in a monitor descriptor set by calling <b>pfnAcquireFirstDescriptorInfo</b> and then making a sequence of calls to <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi_monitordescriptorset_acquirenextdescriptorinfo.md">pfnAcquireNextDescriptorInfo</a>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems. Available in Windows Vista and later versions of the Windows operating systems. |
| **Target Platform** | Desktop |
| **Header** | d3dkmddi.h (include D3dkmddi.h) |
| **IRQL** | PASSIVE_LEVEL |