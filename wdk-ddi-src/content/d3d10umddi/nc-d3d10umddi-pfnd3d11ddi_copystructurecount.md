---
UID: NC:d3d10umddi.PFND3D11DDI_COPYSTRUCTURECOUNT
title: PFND3D11DDI_COPYSTRUCTURECOUNT
author: windows-driver-content
description: The CopyStructureCount function copies the number of items in the filled portion (that is, the filled-size value) of an append buffer unordered access view (UAV) to an offset into a destination buffer.
old-location: display\copystructurecount.htm
old-project: display
ms.assetid: 39f20ff3-859f-4933-8be0-e2bb7c05e7e1
ms.author: windowsdriverdev
ms.date: 2/20/2018
ms.keywords: display.copystructurecount, CopyStructureCount callback function [Display Devices], CopyStructureCount, PFND3D11DDI_COPYSTRUCTURECOUNT, PFND3D11DDI_COPYSTRUCTURECOUNT, d3d10umddi/CopyStructureCount, UserModeDisplayDriverDx11_Functions_b6bad9fd-b0b2-40fa-aa4a-664554984dcd.xml
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Desktop
req.target-min-winverclnt: CopyStructureCount is supported beginning with the Windows 7 operating system.
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
-	CopyStructureCount
product: Windows
targetos: Windows
req.typenames: "*PSETRESULT_INFO, SETRESULT_INFO"
---


# PFND3D11DDI_COPYSTRUCTURECOUNT callback function
The <b>CopyStructureCount</b> function copies the number of items in the filled portion (that is, the filled-size value) of an append buffer unordered access view (UAV) to an offset into a destination buffer.

## Syntax

```
PFND3D11DDI_COPYSTRUCTURECOUNT Pfnd3d11ddiCopystructurecount;

void Pfnd3d11ddiCopystructurecount(
   D3D10DDI_HDEVICE,
   D3D10DDI_HRESOURCE,
   UINT,
   D3D11DDI_HUNORDEREDACCESSVIEW
)
{...}
```

## Parameters

`D3D10DDI_HDEVICE`



`D3D10DDI_HRESOURCE`



`UINT`



`D3D11DDI_HUNORDEREDACCESSVIEW`




## Return Value

None

The driver can use the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi_seterror_cb.md">pfnSetErrorCb</a> callback function to set an error code. For more information about setting error codes, see the following Remarks section.

## Remarks

The driver should not encounter any error, except for D3DDDIERR_DEVICEREMOVED. Therefore, if the driver passes any error, except for D3DDDIERR_DEVICEREMOVED, in a call to the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi_seterror_cb.md">pfnSetErrorCb</a> function, the Direct3D runtime determines that the error is critical. Even if the device is removed, the driver is not required to return D3DDDIERR_DEVICEREMOVED; however, if the device removal interferes with the operation of <b>CopyStructureCount</b> (which typically should not happen), the driver can return D3DDDIERR_DEVICEREMOVED.

<b>CopyStructureCount</b> takes the filled-size value of the append buffer UAV (a UAV that supports push and pop-up operations on structures like on a stack) and copies this value to an offset into the destination buffer. The graphics hardware uses a 4-byte filled-size value to keep track of how much data is filled in the append buffer UAV.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | CopyStructureCount is supported beginning with the Windows 7 operating system.  |
| **Target Platform** | Desktop |
| **Header** | d3d10umddi.h (include D3d10umddi.h) |

## See Also

<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11ddi_createunorderedaccessview.md">CreateUnorderedAccessView</a>



<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi_seterror_cb.md">pfnSetErrorCb</a>



<a href="..\d3d10umddi\ns-d3d10umddi-d3d11ddi_devicefuncs.md">D3D11DDI_DEVICEFUNCS</a>



<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11ddi_createresource.md">CreateResource(D3D11)</a>



 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFND3D11DDI_COPYSTRUCTURECOUNT callback function%20 RELEASE:%20(2/20/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>