---
UID : NC:d3d10umddi.PFND3DWDDM1_3DDI_SETMARKER
title : PFND3DWDDM1_3DDI_SETMARKER
author : windows-driver-content
description : Notifies the user-mode display driver that it must generate a new time stamp if any GPU work has completed since the last call to SetMarker.
old-location : display\setmarker.htm
old-project : display
ms.assetid : BE618B0C-18E7-4B2B-87EB-172DAD9BCE15
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : _SETRESULT_INFO, *PSETRESULT_INFO, SETRESULT_INFO
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : callback
req.header : d3d10umddi.h
req.include-header : D3d10umddi.h
req.target-type : Desktop
req.target-min-winverclnt : Windows 8.1,WDDM 1.3 and later
req.target-min-winversvr : Windows Server 2012 R2
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : SetMarker
req.alt-loc : D3d10umddi.h
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


# PFND3DWDDM1_3DDI_SETMARKER callback function
Notifies the user-mode display driver that it must generate a new time stamp if any GPU work has completed since the last call to <i>SetMarker</i>.

## Syntax

```
PFND3DWDDM1_3DDI_SETMARKER Pfnd3dwddm13DdiSetmarker;

void Pfnd3dwddm13DdiSetmarker(
  D3D10DDI_HDEVICE hDevice
)
{...}
```

## Parameters

`hDevice`

A handle to the display device (graphics context).


## Return Value

Returns <b>S_OK</b> or an appropriate error result if the function does not complete successfully.

## Remarks

If the marker event type from the  <i>Type</i> parameter of the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3dwddm1_3ddi_setmarkermode.md">SetMarkerMode</a> function is not <b>D3DWDDM1_3DDI_MARKER_TYPE_NONE</b>, the user-mode display driver must perform this procedure with each call to <i>SetMarker</i>:

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
<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3dwddm1_3ddi_setmarkermode.md">SetMarkerMode</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFND3DWDDM1_3DDI_SETMARKER callback function%20 RELEASE:%20(12/29/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>