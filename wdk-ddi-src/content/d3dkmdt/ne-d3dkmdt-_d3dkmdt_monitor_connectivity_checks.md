---
UID: NE:d3dkmdt._D3DKMDT_MONITOR_CONNECTIVITY_CHECKS
title: "_D3DKMDT_MONITOR_CONNECTIVITY_CHECKS"
author: windows-driver-content
description: The D3DKMDT_MONITOR_CONNECTIVITY_CHECKS enumerated type indicates whether the DxgkDdiCommitVidPn function should verify that certain video outputs have connected monitors.
old-location: display\d3dkmdt_monitor_connectivity_checks.htm
old-project: display
ms.assetid: 8a32fef1-e404-478d-8b99-064ed456e37c
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: D3DKMDT_MCC_ENFORCE, D3DKMDT_MCC_IGNORE, D3DKMDT_MCC_UNINITIALIZED, D3DKMDT_MONITOR_CONNECTIVITY_CHECKS, D3DKMDT_MONITOR_CONNECTIVITY_CHECKS enumeration [Display Devices], DmEnums_ac54453d-cc4d-4ea7-ad10-943389a837d7.xml, _D3DKMDT_MONITOR_CONNECTIVITY_CHECKS, d3dkmdt/D3DKMDT_MCC_ENFORCE, d3dkmdt/D3DKMDT_MCC_IGNORE, d3dkmdt/D3DKMDT_MCC_UNINITIALIZED, d3dkmdt/D3DKMDT_MONITOR_CONNECTIVITY_CHECKS, display.d3dkmdt_monitor_connectivity_checks
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: d3dkmdt.h
req.include-header: D3dkmdt.h
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
-	d3dkmdt.h
api_name:
-	D3DKMDT_MONITOR_CONNECTIVITY_CHECKS
product:
- Windows
targetos: Windows
req.typenames: D3DKMDT_MONITOR_CONNECTIVITY_CHECKS
---

# _D3DKMDT_MONITOR_CONNECTIVITY_CHECKS Enumeration
The D3DKMDT_MONITOR_CONNECTIVITY_CHECKS enumerated type indicates whether the <a href="https://msdn.microsoft.com/979b86e9-f3ff-4022-8c00-b6afc2b1f747">DxgkDdiCommitVidPn</a> function should verify that certain video outputs have connected monitors.

## Syntax
```
typedef enum _D3DKMDT_MONITOR_CONNECTIVITY_CHECKS {
  D3DKMDT_MCC_UNINITIALIZED  ,
  D3DKMDT_MCC_IGNORE         ,
  D3DKMDT_MCC_ENFORCE
} D3DKMDT_MONITOR_CONNECTIVITY_CHECKS;
```

## Constants

<table>
            
                <tr>
                    <td>D3DKMDT_MCC_UNINITIALIZED</td>
                    <td>Indicates that a variable of type D3DKMDT_MONITOR_CONNECTIVITY_CHECKS has not yet been assigned a meaningful value.</td>
                </tr>
            
                <tr>
                    <td>D3DKMDT_MCC_IGNORE</td>
                    <td>Indicates that <b>DxgkDdiCommitVidPn</b> does not need to verify that monitors are connected.</td>
                </tr>
            
                <tr>
                    <td>D3DKMDT_MCC_ENFORCE</td>
                    <td>Indicates that <b>DxgkDdiCommitVidPn</b> must verify that monitors are connected.</td>
                </tr>
</table>

## Remarks

The <b>MonitorConnectivityChecks</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff557552">DXGKARG_COMMITVIDPN</a> structure is a D3DKMDT_MONITOR_CONNECTIVITY_CHECKS value.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems. Available in Windows Vista and later versions of the Windows operating systems. |
| **Header** | d3dkmdt.h (include D3dkmdt.h) |

## See Also

<a href="https://msdn.microsoft.com/979b86e9-f3ff-4022-8c00-b6afc2b1f747">DxgkDdiCommitVidPn</a>