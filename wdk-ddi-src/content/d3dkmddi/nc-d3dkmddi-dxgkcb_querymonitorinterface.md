---
UID : NC:d3dkmddi.DXGKCB_QUERYMONITORINTERFACE
title : DXGKCB_QUERYMONITORINTERFACE
author : windows-driver-content
description : The DxgkCbQueryMonitorInterface function returns a pointer to a DXGK_MONITOR_INTERFACE structure.
old-location : display\dxgkcbquerymonitorinterface.htm
old-project : display
ms.assetid : 0c23e72d-3eb9-4511-a386-1dcc2f4910b7
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : _DD_MULTISAMPLEQUALITYLEVELSDATA, DD_MULTISAMPLEQUALITYLEVELSDATA
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : callback
req.header : d3dkmddi.h
req.include-header : Dispmprt.h
req.target-type : Desktop
req.target-min-winverclnt : Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : DxgkCbQueryMonitorInterface
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
req.irql : <= APC_LEVEL
req.typenames : DD_MULTISAMPLEQUALITYLEVELSDATA
---


# DXGKCB_QUERYMONITORINTERFACE callback function
The <b>DxgkCbQueryMonitorInterface</b> function returns a pointer to a <a href="..\d3dkmddi\ns-d3dkmddi-_dxgk_monitor_interface.md">DXGK_MONITOR_INTERFACE</a> structure. The structure contains pointers to functions that the display miniport driver can call to obtain other interfaces that provide access to monitor descriptors, modes, and frequency ranges.

## Syntax

```
DXGKCB_QUERYMONITORINTERFACE DxgkcbQuerymonitorinterface;

NTSTATUS DxgkcbQuerymonitorinterface(
  IN_CONST_HANDLE hAdapter,
  IN_CONST_DXGK_MONITOR_INTERFACE_VERSION MonitorInterfaceVersion,
  DEREF_OUT_CONST_PPDXGK_MONITOR_INTERFACE ppMonitorInterface
)
{...}
```

## Parameters

`hAdapter`

[in] A handle that represents a display adapter. The VidPN manager provided this handle to the display miniport driver in a call to <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi_recommendfunctionalvidpn.md">DxgkDdiRecommendFunctionalVidPn</a>, <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi_issupportedvidpn.md">DxgkDdiIsSupportedVidPn</a>, <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi_enumvidpncofuncmodality.md">DxgkDdiEnumVidPnCofuncModality</a>, or <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi_commitvidpn.md">DxgkDdiCommitVidPn</a>.

`MonitorInterfaceVersion`

[in] A value from the <a href="..\d3dkmddi\ne-d3dkmddi-_dxgk_monitor_interface_version.md">DXGK_MONITOR_INTERFACE_VERSION</a> enumeration that specifies the version of the monitor interface being requested.

`ppMonitorInterface`

[out] A pointer to a variable that receives a pointer to the <a href="..\d3dkmddi\ns-d3dkmddi-_dxgk_monitor_interface.md">DXGK_MONITOR_INTERFACE</a> structure.


## Return Value

<b>DxgkCbQueryMonitorInterface</b> returns STATUS_SUCCESS if it succeeds. Otherwise, it returns one of the error codes defined in <i>Ntstatus.</i>h. 

The following code example shows how to acquire the monitor-management interface from the Microsoft DirectX graphics kernel subsystem (<i>Dxgkrnl.sys</i>) and use the monitor-management interface to retrieve the monitor-frequency-range-set object.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Desktop |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | d3dkmddi.h (include Dispmprt.h) |
| **Library** |  |
| **IRQL** | <= APC_LEVEL |
| **DDI compliance rules** |  |

## See Also

<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff568433">Monitor Interface</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGKCB_QUERYMONITORINTERFACE callback function%20 RELEASE:%20(12/29/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>