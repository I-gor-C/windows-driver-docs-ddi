---
UID: NE:d3dkmdt._DXGKMDT_OPM_STATUS
title: "_DXGKMDT_OPM_STATUS"
author: windows-driver-content
description: The DXGKMDT_OPM_STATUS enumeration identifies the status of a protected output.
old-location: display\dxgkmdt_opm_status.htm
old-project: display
ms.assetid: e3bfde85-e8a0-41df-9248-f48ceb8b5304
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: DXGKMDT_OPM_STATUS, DXGKMDT_OPM_STATUS enumeration [Display Devices], DXGKMDT_OPM_STATUS_LINK_LOST, DXGKMDT_OPM_STATUS_NORMAL, DXGKMDT_OPM_STATUS_RENEGOTIATION_REQUIRED, DXGKMDT_OPM_STATUS_REVOKED_HDCP_DEVICE_ATTACHED, DXGKMDT_OPM_STATUS_TAMPERING_DETECTED, DmEnums_77faebe8-d3a4-461f-9f03-daa2d81da828.xml, _DXGKMDT_OPM_STATUS, d3dkmdt/DXGKMDT_OPM_STATUS, d3dkmdt/DXGKMDT_OPM_STATUS_LINK_LOST, d3dkmdt/DXGKMDT_OPM_STATUS_NORMAL, d3dkmdt/DXGKMDT_OPM_STATUS_RENEGOTIATION_REQUIRED, d3dkmdt/DXGKMDT_OPM_STATUS_REVOKED_HDCP_DEVICE_ATTACHED, d3dkmdt/DXGKMDT_OPM_STATUS_TAMPERING_DETECTED, display.dxgkmdt_opm_status
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
-	DXGKMDT_OPM_STATUS
product: Windows
targetos: Windows
req.typenames: DXGKMDT_OPM_STATUS
---

# _DXGKMDT_OPM_STATUS Enumeration
The DXGKMDT_OPM_STATUS enumeration identifies the status of a protected output.

## Syntax
```
typedef enum _DXGKMDT_OPM_STATUS {
  DXGKMDT_OPM_STATUS_NORMAL                        ,
  DXGKMDT_OPM_STATUS_LINK_LOST                     ,
  DXGKMDT_OPM_STATUS_RENEGOTIATION_REQUIRED        ,
  DXGKMDT_OPM_STATUS_TAMPERING_DETECTED            ,
  DXGKMDT_OPM_STATUS_REVOKED_HDCP_DEVICE_ATTACHED
} DXGKMDT_OPM_STATUS;
```

## Constants

<table>
            
                <tr>
                    <td>DXGKMDT_OPM_STATUS_NORMAL</td>
                    <td>Indicates that the protected output is working correctly.</td>
                </tr>
            
                <tr>
                    <td>DXGKMDT_OPM_STATUS_LINK_LOST</td>
                    <td>Indicates that although the protected output detected no tampering, an output protection technology unexpectedly stopped working. 

This status bit must be set if DXGKMDT_OPM_STATUS_REVOKED_HDCP_DEVICE_ATTACHED is also set.</td>
                </tr>
            
                <tr>
                    <td>DXGKMDT_OPM_STATUS_RENEGOTIATION_REQUIRED</td>
                    <td>Indicates that the end user caused the configuration of the physical connector to change. Therefore, a renegotiation is required.</td>
                </tr>
            
                <tr>
                    <td>DXGKMDT_OPM_STATUS_TAMPERING_DETECTED</td>
                    <td>Indicates that tampering with the graphics adapter or the adapter's display miniport driver has occurred.</td>
                </tr>
            
                <tr>
                    <td>DXGKMDT_OPM_STATUS_REVOKED_HDCP_DEVICE_ATTACHED</td>
                    <td>Indicates that a revoked High-bandwidth Digital Content Protection (HDCP) device is directly or indirectly attached to a protected output. If HDCP is not enabled, the protected output is not required to detect revoked devices. If HDCP is enabled, the protected output must detect revoked devices. The driver sets this status value only from a call to its <a href="https://msdn.microsoft.com/3d6559e5-776e-4fc0-b99a-8818cbcc289d">DxgkDdiOPMGetInformation</a> function to determine if HDCP is enabled.</td>
                </tr>
</table>

## Remarks

The display miniport driver returns status about a protected output whenever the driver's <a href="https://msdn.microsoft.com/3d6559e5-776e-4fc0-b99a-8818cbcc289d">DxgkDdiOPMGetInformation</a> and <a href="https://msdn.microsoft.com/9f15df1e-bdf5-4634-97f1-78515664b594">DxgkDdiOPMGetCOPPCompatibleInformation</a> functions are called to retrieve information about the protected output. For more information about returning a protected output's status, see <a href="https://msdn.microsoft.com/9945ae9c-1c11-4266-8a5c-d0ffe5ba4b5f">Reporting Status about a Protected Output</a>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems. Available in Windows Vista and later versions of the Windows operating systems. |
| **Header** | d3dkmdt.h (include D3dkmdt.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff560830">DXGKMDT_OPM_ACP_AND_CGMSA_SIGNALING</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff560840">DXGKMDT_OPM_ACTUAL_OUTPUT_FORMAT</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff560854">DXGKMDT_OPM_CONNECTED_HDCP_DEVICE_INFORMATION</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff560925">DXGKMDT_OPM_STANDARD_INFORMATION</a>



<a href="https://msdn.microsoft.com/9f15df1e-bdf5-4634-97f1-78515664b594">DxgkDdiOPMGetCOPPCompatibleInformation</a>



<a href="https://msdn.microsoft.com/3d6559e5-776e-4fc0-b99a-8818cbcc289d">DxgkDdiOPMGetInformation</a>