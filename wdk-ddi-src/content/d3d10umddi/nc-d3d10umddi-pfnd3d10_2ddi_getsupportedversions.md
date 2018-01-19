---
UID : NC:d3d10umddi.PFND3D10_2DDI_GETSUPPORTEDVERSIONS
title : PFND3D10_2DDI_GETSUPPORTEDVERSIONS
author : windows-driver-content
description : The GetSupportedVersions function queries for the Direct3D interface versions that the driver supports.
old-location : display\getsupportedversions.htm
old-project : display
ms.assetid : b38683f3-42f2-4f5e-9482-f72e9f2e0a34
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : _SETRESULT_INFO, *PSETRESULT_INFO, SETRESULT_INFO
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : callback
req.header : d3d10umddi.h
req.include-header : D3d10umddi.h
req.target-type : Desktop
req.target-min-winverclnt : GetSupportedVersions is supported beginning with the Windows 7 operating system.
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : GetSupportedVersions
req.alt-loc : d3d10umddi.h
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : 
req.typenames : "*PSETRESULT_INFO, SETRESULT_INFO"
---


# PFND3D10_2DDI_GETSUPPORTEDVERSIONS callback function
The <i>GetSupportedVersions</i> function queries for the Direct3D interface versions that the driver supports.

## Syntax

```
PFND3D10_2DDI_GETSUPPORTEDVERSIONS Pfnd3d102DdiGetsupportedversions;

HRESULT Pfnd3d102DdiGetsupportedversions(
   D3D10DDI_HADAPTER,
  UINT32 *puEntries,
  UINT64 *pSupportedDDIInterfaceVersions
)
{...}
```

## Parameters

`D3D10DDI_HADAPTER`



`*puEntries`



`*pSupportedDDIInterfaceVersions`




## Return Value

<i>GetSupportedVersions</i> returns one of the following values:
<dl>
<dt><b>S_OK</b></dt>
</dl>The capabilities are successfully retrieved.
<dl>
<dt><b>E_OUTOFMEMORY</b></dt>
</dl><i>GetSupportedVersions</i> could not allocate memory that is required for it to complete.

## Remarks

When the Direct3D runtime calls the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi_openadapter.md">OpenAdapter10_2</a> function, the <b>Interface</b> and <b>Version</b> members of the <a href="..\d3d10umddi\ns-d3d10umddi-d3d10ddiarg_openadapter.md">D3D10DDIARG_OPENADAPTER</a> structure contain the DDI version that the runtime uses to instantiate the driver. The driver can completely ignore these members. The driver can instead return capabilities and version information out through its <i>GetSupportedVersions</i> function.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Desktop |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | d3d10umddi.h (include D3d10umddi.h) |
| **Library** |  |
| **IRQL** |  |
| **DDI compliance rules** |  |

## See Also

<dl>
<dt>
<a href="..\d3d10umddi\ns-d3d10umddi-d3d10_2ddi_adapterfuncs.md">D3D10_2DDI_ADAPTERFUNCS</a>
</dt>
<dt>
<a href="..\d3d10umddi\ns-d3d10umddi-d3d10ddiarg_openadapter.md">D3D10DDIARG_OPENADAPTER</a>
</dt>
<dt>
<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi_openadapter.md">OpenAdapter10_2</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFND3D10_2DDI_GETSUPPORTEDVERSIONS callback function%20 RELEASE:%20(12/29/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>