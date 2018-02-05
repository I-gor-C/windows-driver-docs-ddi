---
UID : NC:d3dkmddi.DXGKCB_GETCAPTUREADDRESS
title : DXGKCB_GETCAPTUREADDRESS
author : windows-driver-content
description : The DxgkCbGetCaptureAddress function retrieves the physical address and segment identifier of a capture buffer that is associated with the given allocation handle.
old-location : display\dxgkcbgetcaptureaddress.htm
old-project : display
ms.assetid : f87a5a5f-20d3-48cb-93f0-114eafe7238b
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : display.dxgkcbgetcaptureaddress, DxgkCbGetCaptureAddress callback function [Display Devices], DxgkCbGetCaptureAddress, DXGKCB_GETCAPTUREADDRESS, DXGKCB_GETCAPTUREADDRESS, d3dkmddi/DxgkCbGetCaptureAddress, DpFunctions_a8e4882c-a196-4cdf-826f-fa4cf44ba8f8.xml
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : callback
req.header : d3dkmddi.h
req.include-header : D3dkmddi.h
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
req.irql : "< DISPATCH_LEVEL"
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : DD_MULTISAMPLEQUALITYLEVELSDATA
---


# DXGKCB_GETCAPTUREADDRESS callback function
The <b>DxgkCbGetCaptureAddress</b> function retrieves the physical address and segment identifier of a capture buffer that is associated with the given allocation handle.

## Syntax

```
DXGKCB_GETCAPTUREADDRESS DxgkcbGetcaptureaddress;

NTSTATUS DxgkcbGetcaptureaddress(

)
{...}
```

## Parameters

This function has no parameters.

## Return Value

<b>DxgkCbGetCaptureAddress</b> returns one of the following values:
<table>
<tr>
<th>Return code</th>
<th>Description</th>
</tr>
<tr>
<td width="40%">
<dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl>
</td>
<td width="60%">
<b>DxgkCbGetCaptureAddress</b> successfully retrieved the capture buffer information.

</td>
</tr>
<tr>
<td width="40%">
<dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl>
</td>
<td width="60%">
The allocation handle that is specified in the <b>hAllocation</b> member of the <a href="..\d3dkmddi\ns-d3dkmddi-_dxgkargcb_getcaptureaddress.md">DXGKARGCB_GETCAPTUREADDRESS</a> structure that the <i>pData</i> parameter pointed to was either invalid or did not represent a capture buffer. 

</td>
</tr>
</table> 

<i>DxgkCbGetCaptureAddress</i> might also return other error codes that are defined in Ntstatus.h.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems. Available in Windows Vista and later versions of the Windows operating systems. |
| **Target Platform** | Desktop |
| **Header** | d3dkmddi.h (include D3dkmddi.h) |
| **IRQL** | "< DISPATCH_LEVEL" |

## See Also

<a href="..\d3dkmddi\ns-d3dkmddi-_dxgkargcb_getcaptureaddress.md">DXGKARGCB_GETCAPTUREADDRESS</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGKCB_GETCAPTUREADDRESS callback function%20 RELEASE:%20(12/29/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>