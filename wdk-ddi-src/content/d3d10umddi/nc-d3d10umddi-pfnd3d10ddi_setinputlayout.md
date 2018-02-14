---
UID: NC:d3d10umddi.PFND3D10DDI_SETINPUTLAYOUT
title: PFND3D10DDI_SETINPUTLAYOUT
author: windows-driver-content
description: The IaSetInputLayout function sets an input layout for the input assembler.
old-location: display\iasetinputlayout.htm
old-project: display
ms.assetid: 905e4e7f-5bc5-487f-8d82-4ebc2db66135
ms.author: windowsdriverdev
ms.date: 12/29/2017
ms.keywords: display.iasetinputlayout, IaSetInputLayout callback function [Display Devices], IaSetInputLayout, PFND3D10DDI_SETINPUTLAYOUT, PFND3D10DDI_SETINPUTLAYOUT, d3d10umddi/IaSetInputLayout, UserModeDisplayDriverDx10_Functions_fbd365d3-26a5-49a8-b89c-c094d8e873d9.xml
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
-	IaSetInputLayout
product: Windows
targetos: Windows
req.typenames: "*PSETRESULT_INFO, SETRESULT_INFO"
---


# PFND3D10DDI_SETINPUTLAYOUT callback function
The <i>IaSetInputLayout</i> function sets an input layout for the input assembler.

## Syntax

```
PFND3D10DDI_SETINPUTLAYOUT Pfnd3d10ddiSetinputlayout;

void Pfnd3d10ddiSetinputlayout(
   D3D10DDI_HDEVICE,
   D3D10DDI_HELEMENTLAYOUT
)
{...}
```

## Parameters

`D3D10DDI_HDEVICE`



`D3D10DDI_HELEMENTLAYOUT`




## Return Value

None

The driver can use the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi_seterror_cb.md">pfnSetErrorCb</a> callback function to set an error code. For more information about setting error codes, see the following Remarks section.

## Remarks

After the <i>IaSetInputLayout</i> function completes, all subsequent drawing operations use the given layout object until another is selected.

The driver should not encounter any error, except for D3DDDIERR_DEVICEREMOVED. Therefore, if the driver passes any error, except for D3DDDIERR_DEVICEREMOVED, in a call to the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi_seterror_cb.md">pfnSetErrorCb</a> function, the Direct3D runtime will determine that the error is critical. Even if the device was removed, the driver is not required to return D3DDDIERR_DEVICEREMOVED; however, if device removal interfered with the operation of <i>IaSetInputLayout</i> (which typically should not happen), the driver can return D3DDDIERR_DEVICEREMOVED.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems. Available in Windows Vista and later versions of the Windows operating systems. |
| **Target Platform** | Desktop |
| **Header** | d3d10umddi.h (include D3d10umddi.h) |

## See Also

<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi_seterror_cb.md">pfnSetErrorCb</a>



<a href="..\d3d10umddi\ns-d3d10umddi-d3d10ddi_devicefuncs.md">D3D10DDI_DEVICEFUNCS</a>



 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFND3D10DDI_SETINPUTLAYOUT callback function%20 RELEASE:%20(12/29/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>