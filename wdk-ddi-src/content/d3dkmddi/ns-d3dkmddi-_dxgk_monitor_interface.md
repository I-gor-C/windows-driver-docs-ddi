---
UID: NS:d3dkmddi._DXGK_MONITOR_INTERFACE
title: "_DXGK_MONITOR_INTERFACE"
author: windows-driver-content
description: The DXGK_MONITOR_INTERFACE structure contains pointers to functions that belong to the Monitor Interface, which is implemented by the video present network (VidPN) manager.
old-location: display\dxgk_monitor_interface.htm
old-project: display
ms.assetid: edb6df63-7354-4da3-b641-2ce7f28ca7e8
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: DXGK_MONITOR_INTERFACE, DXGK_MONITOR_INTERFACE structure [Display Devices], DmStructs_23906e50-4f65-4483-a54c-915f9fd3c433.xml, _DXGK_MONITOR_INTERFACE, d3dkmddi/DXGK_MONITOR_INTERFACE, display.dxgk_monitor_interface
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmddi.h
req.include-header: D3dkmddi.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
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
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	d3dkmddi.h
api_name:
-	DXGK_MONITOR_INTERFACE
product: Windows
targetos: Windows
req.typenames: DXGK_MONITOR_INTERFACE
---

# _DXGK_MONITOR_INTERFACE structure
The DXGK_MONITOR_INTERFACE structure contains pointers to functions that belong to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff568433">Monitor Interface</a>, which is implemented by the video present network (VidPN) manager.

## Syntax
````
typedef struct _DXGK_MONITOR_INTERFACE {
  DXGK_MONITOR_INTERFACE_VERSION              Version;
  DXGKDDI_MONITOR_ACQUIREMONITORSOURCEMODESET pfnAcquireMonitorSourceModeSet;
  DXGKDDI_MONITOR_RELEASEMONITORSOURCEMODESET pfnReleaseMonitorSourceModeSet;
  DXGKDDI_MONITOR_GETMONITORFREQUENCYRANGESET pfnGetMonitorFrequencyRangeSet;
  DXGKDDI_MONITOR_GETMONITORDESCRIPTORSET     pfnGetMonitorDescriptorSet;
} DXGK_MONITOR_INTERFACE;
````

## Members


`Version`

A value from the <a href="..\d3dkmddi\ne-d3dkmddi-_dxgk_monitor_interface_version.md">DXGK_MONITOR_INTERFACE_VERSION</a> enumeration that indicates the monitor interface version. Must be set to 1.

`pfnAcquireMonitorSourceModeSet`

A pointer to the <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi_monitor_acquiremonitorsourcemodeset.md">pfnAcquireMonitorSourceModeSet</a> function.

`pfnReleaseMonitorSourceModeSet`

A pointer to the <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi_monitor_releasemonitorsourcemodeset.md">pfnReleaseMonitorSourceModeSet</a> function.

`pfnGetMonitorFrequencyRangeSet`

A pointer to the <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi_monitor_getmonitorfrequencyrangeset.md">pfnGetMonitorFrequencyRangeSet</a> function.

`pfnGetMonitorDescriptorSet`

A pointer to the <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi_monitor_getmonitordescriptorset.md">pfnGetMonitorDescriptorSet</a> function.

## Remarks
<div class="alert"><b>Note</b>    A display miniport driver must verify the interface version specified in the <b>Version</b> member before using <p class="note">this structure.

</div>
<div> </div>

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems. Available in Windows Vista and later versions of the Windows operating systems. |
| **Header** | d3dkmddi.h (include D3dkmddi.h) |

## See Also

<a href="..\d3dkmddi\ns-d3dkmddi-_dxgk_monitor_interface_v2.md">DXGK_MONITOR_INTERFACE_V2</a>



<a href="..\d3dkmddi\ne-d3dkmddi-_dxgk_monitor_interface_version.md">DXGK_MONITOR_INTERFACE_VERSION</a>