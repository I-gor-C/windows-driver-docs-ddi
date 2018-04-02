---
UID: NE:d3d10umddi.D3D11_1DDI_AUTHENTICATED_PROCESS_IDENTIFIER_TYPE
title: D3D11_1DDI_AUTHENTICATED_PROCESS_IDENTIFIER_TYPE
author: windows-driver-content
description: Specifies the type of process that is identified in the D3D11_1DDI_AUTHENTICATED_QUERY_RESTRICTED_SHARED_RESOURCE_PROCESS_OUTPUT structure.
old-location: display\d3d11_1ddi_authenticated_process_identifier_type.htm
old-project: display
ms.assetid: 7a8e7641-c946-4feb-b6d7-54ef63de9e76
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: D3D11_1DDI_AUTHENTICATED_PROCESS_IDENTIFIER_TYPE, D3D11_1DDI_AUTHENTICATED_PROCESS_IDENTIFIER_TYPE enumeration [Display Devices], D3D11_1DDI_PROCESSIDTYPE_DWM, D3D11_1DDI_PROCESSIDTYPE_HANDLE, D3D11_1DDI_PROCESSIDTYPE_UNKNOWN, d3d10umddi/D3D11_1DDI_AUTHENTICATED_PROCESS_IDENTIFIER_TYPE, d3d10umddi/D3D11_1DDI_PROCESSIDTYPE_DWM, d3d10umddi/D3D11_1DDI_PROCESSIDTYPE_HANDLE, d3d10umddi/D3D11_1DDI_PROCESSIDTYPE_UNKNOWN, display.d3d11_1ddi_authenticated_process_identifier_type
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
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
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	D3d10umddi.h
api_name:
-	D3D11_1DDI_AUTHENTICATED_PROCESS_IDENTIFIER_TYPE
product: Windows
targetos: Windows
req.typenames: D3D11_1DDI_AUTHENTICATED_PROCESS_IDENTIFIER_TYPE
---

# D3D11_1DDI_AUTHENTICATED_PROCESS_IDENTIFIER_TYPE Enumeration
Specifies the type of process that is identified in the <a href="https://msdn.microsoft.com/library/windows/hardware/hh406429">D3D11_1DDI_AUTHENTICATED_QUERY_RESTRICTED_SHARED_RESOURCE_PROCESS_OUTPUT</a>  structure.

## Syntax
```
typedef enum D3D11_1DDI_AUTHENTICATED_PROCESS_IDENTIFIER_TYPE {
  D3D11_1DDI_PROCESSIDTYPE_UNKNOWN  ,
  D3D11_1DDI_PROCESSIDTYPE_DWM      ,
  D3D11_1DDI_PROCESSIDTYPE_HANDLE
} ;
```

## Constants

<table>
            
                <tr>
                    <td>D3D11_1DDI_PROCESSIDTYPE_UNKNOWN</td>
                    <td>Unknown process type.</td>
                </tr>
            
                <tr>
                    <td>D3D11_1DDI_PROCESSIDTYPE_DWM</td>
                    <td>DWM process.</td>
                </tr>
            
                <tr>
                    <td>D3D11_1DDI_PROCESSIDTYPE_HANDLE</td>
                    <td>Handle to a process.</td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8 Windows 8 |
| **Header** | d3d10umddi.h (include D3d10umddi.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/hh406429">D3D11_1DDI_AUTHENTICATED_QUERY_RESTRICTED_SHARED_RESOURCE_PROCESS_OUTPUT</a>