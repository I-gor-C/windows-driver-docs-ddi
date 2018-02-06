---
UID: NC:d3d10umddi.PFND3D10DDI_IA_SETVERTEXBUFFERS
title: PFND3D10DDI_IA_SETVERTEXBUFFERS
author: windows-driver-content
description: The IaSetVertexBuffers function sets vertex buffers for an input assembler.
old-location: display\iasetvertexbuffers.htm
old-project: display
ms.assetid: 3d5a7ea1-08c2-4594-93bc-97b985cd16dc
ms.author: windowsdriverdev
ms.date: 12/29/2017
ms.keywords: display.iasetvertexbuffers, IaSetVertexBuffers callback function [Display Devices], IaSetVertexBuffers, PFND3D10DDI_IA_SETVERTEXBUFFERS, PFND3D10DDI_IA_SETVERTEXBUFFERS, d3d10umddi/IaSetVertexBuffers, UserModeDisplayDriverDx10_Functions_12104a04-1497-42c6-a5e1-6573b33a43d3.xml
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Desktop
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
req.irql: 
topictype:
-	APIRef
-	kbSyntax
apitype:
-	UserDefined
apilocation:
-	d3d10umddi.h
apiname:
-	IaSetVertexBuffers
product: Windows
targetos: Windows
req.typenames: SETRESULT_INFO, *PSETRESULT_INFO
---


# PFND3D10DDI_IA_SETVERTEXBUFFERS callback function
The <i>IaSetVertexBuffers</i> function sets vertex buffers for an input assembler.

## Syntax

```
PFND3D10DDI_IA_SETVERTEXBUFFERS Pfnd3d10ddiIaSetvertexbuffers;

void Pfnd3d10ddiIaSetvertexbuffers(
   D3D10DDI_HDEVICE,
  UINT StartSlot,
  UINT NumBuffers,
  CONST D3D10DDI_HRESOURCE *,
  CONST UINT *,
  CONST UINT *
)
{...}
```

## Parameters

`D3D10DDI_HDEVICE`



`StartSlot`



`NumBuffers`

The total number of buffers to set.

`*`



`*`



`*`




## Return Value

None

The driver can use the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi_seterror_cb.md">pfnSetErrorCb</a> callback function to set an error code. For more information about setting error codes, see the following Remarks section.

## Remarks

The driver should not encounter any error, except for D3DDDIERR_DEVICEREMOVED. Therefore, if the driver passes any error, except for D3DDDIERR_DEVICEREMOVED, in a call to the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi_seterror_cb.md">pfnSetErrorCb</a> function, the Direct3D runtime will determine that the error is critical. Even if the device was removed, the driver is not required to return D3DDDIERR_DEVICEREMOVED; however, if device removal interfered with the operation of <i>IaSetVertexBuffers</i> (which typically should not happen), the driver can return D3DDDIERR_DEVICEREMOVED.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems. Available in Windows Vista and later versions of the Windows operating systems. |
| **Target Platform** | Desktop |
| **Header** | d3d10umddi.h (include D3d10umddi.h) |

## See Also

<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi_seterror_cb.md">pfnSetErrorCb</a>

<a href="..\d3d10umddi\ns-d3d10umddi-d3d10ddi_devicefuncs.md">D3D10DDI_DEVICEFUNCS</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFND3D10DDI_IA_SETVERTEXBUFFERS callback function%20 RELEASE:%20(12/29/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>