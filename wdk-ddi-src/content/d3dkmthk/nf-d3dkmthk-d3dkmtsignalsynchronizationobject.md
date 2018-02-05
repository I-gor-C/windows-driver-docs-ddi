---
UID : NF:d3dkmthk.D3DKMTSignalSynchronizationObject
title : D3DKMTSignalSynchronizationObject function
author : windows-driver-content
description : The D3DKMTSignalSynchronizationObject function inserts a signal for the specified synchronization objects in the specified context stream.
old-location : display\d3dkmtsignalsynchronizationobject.htm
old-project : display
ms.assetid : 1b8fc764-023f-4aa0-b610-2394a48efc02
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : OpenGL_Functions_183a6489-8a99-4dd3-a697-04db44b229c9.xml, d3dkmthk/D3DKMTSignalSynchronizationObject, display.d3dkmtsignalsynchronizationobject, D3DKMTSignalSynchronizationObject, D3DKMTSignalSynchronizationObject function [Display Devices]
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : function
req.header : d3dkmthk.h
req.include-header : D3dkmthk.h
req.target-type : Universal
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
req.lib : Gdi32.lib
req.dll : Gdi32.dll
req.irql : 
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : D3DKMT_DRIVERVERSION
---


# D3DKMTSignalSynchronizationObject function
The <b>D3DKMTSignalSynchronizationObject</b> function inserts a signal for the specified synchronization objects in the specified context stream.

## Syntax

````
NTSTATUS APIENTRY D3DKMTSignalSynchronizationObject(
  _In_ const D3DKMT_SIGNALSYNCHRONIZATIONOBJECT *pData
);
````

## Parameters

`D3DKMT_SIGNALSYNCHRONIZATIONOBJECT`

TBD


## Return Value

<b>D3DKMTSignalSynchronizationObject</b> returns one of the following values:
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
The signaling was successfully set up.

</td>
</tr>
<tr>
<td width="40%">
<dl>
<dt><b>STATUS_DEVICE_REMOVED</b></dt>
</dl>
</td>
<td width="60%">
The graphics adapter was stopped or the display context was reset.

</td>
</tr>
<tr>
<td width="40%">
<dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl>
</td>
<td width="60%">
Parameters were validated and determined to be incorrect.

</td>
</tr>
</table> 

This function might also return other NTSTATUS values.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems. Available in Windows Vista and later versions of the Windows operating systems. |
| **Target Platform** | Universal |
| **Header** | d3dkmthk.h (include D3dkmthk.h) |
| **Library** | Gdi32.lib |
| **DLL** | Gdi32.dll |

## See Also

<a href="..\d3dkmthk\ns-d3dkmthk-_d3dkmt_signalsynchronizationobject.md">D3DKMT_SIGNALSYNCHRONIZATIONOBJECT</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DKMTSignalSynchronizationObject function%20 RELEASE:%20(12/29/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>