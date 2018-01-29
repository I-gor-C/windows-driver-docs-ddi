---
UID : NC:d3dumddi.PFND3DDDI_CREATEDECODEDEVICE
title : PFND3DDDI_CREATEDECODEDEVICE
author : windows-driver-content
description : The CreateDecodeDevice function creates a Microsoft DirectX Video Acceleration (DirectX VA) decode device that is used to decode video.
old-location : display\createdecodedevice.htm
old-project : display
ms.assetid : 4d9a062a-2fdf-4e55-a335-c03c5d5665ff
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : display.createdecodedevice, CreateDecodeDevice callback function [Display Devices], CreateDecodeDevice, PFND3DDDI_CREATEDECODEDEVICE, PFND3DDDI_CREATEDECODEDEVICE, d3dumddi/CreateDecodeDevice, UserModeDisplayDriver_Functions_a6618d5f-ea60-467f-bc0b-e1fe3ee268fe.xml
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : callback
req.header : d3dumddi.h
req.include-header : D3dumddi.h
req.target-type : Desktop
req.target-min-winverclnt : Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
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
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : DXGK_PTE
---


# PFND3DDDI_CREATEDECODEDEVICE callback function
The <b>CreateDecodeDevice</b> function creates a Microsoft DirectX Video Acceleration (DirectX VA) decode device that is used to decode video.

## Syntax

```
PFND3DDDI_CREATEDECODEDEVICE Pfnd3dddiCreatedecodedevice;

HRESULT Pfnd3dddiCreatedecodedevice(
  HANDLE hDevice,
  D3DDDIARG_CREATEDECODEDEVICE *
)
{...}
```

## Parameters

`hDevice`

A handle to the display device (graphics context).

`*`




## Return Value

<b>CreateDecodeDevice</b> returns one of the following values:
<table>
<tr>
<th>Return code</th>
<th>Description</th>
</tr>
<tr>
<td width="40%">
<dl>
<dt><b>S_OK</b></dt>
</dl>
</td>
<td width="60%">
The DirectX VA decode device is successfully created.

</td>
</tr>
<tr>
<td width="40%">
<dl>
<dt><b>E_OUTOFMEMORY</b></dt>
</dl>
</td>
<td width="60%">

<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi_createdecodedevice.md">CreateDecodeDevice</a> could not allocate the required memory for it to complete.

</td>
</tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Desktop |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | d3dumddi.h (include D3dumddi.h) |
| **Library** |  |
| **IRQL** |  |
| **DDI compliance rules** |  |

## See Also

<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi_destroydecodedevice.md">DestroyDecodeDevice</a>

<a href="..\d3dumddi\ns-d3dumddi-_d3dddiarg_createdecodedevice.md">D3DDDIARG_CREATEDECODEDEVICE</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFND3DDDI_CREATEDECODEDEVICE callback function%20 RELEASE:%20(12/29/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>