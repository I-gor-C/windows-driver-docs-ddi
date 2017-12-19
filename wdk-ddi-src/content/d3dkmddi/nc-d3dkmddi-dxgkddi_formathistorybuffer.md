---
UID: NC.d3dkmddi.DXGKDDI_FORMATHISTORYBUFFER
title: DXGKDDI_FORMATHISTORYBUFFER
author: windows-driver-content
description: Copies unformatted data from the history buffer into a buffer that's properly formatted to be submitted to the Event Tracing for Windows (ETW) facility.
old-location: display\dxgkddiformathistorybuffer.htm
old-project: display
ms.assetid: 84417629-5C12-4CB5-B147-0A558A4F9090
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: _DD_MULTISAMPLEQUALITYLEVELSDATA, DD_MULTISAMPLEQUALITYLEVELSDATA
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: d3dkmddi.h
req.include-header: 
req.target-type: Desktop
req.target-min-winverclnt: Windows 8.1,WDDM 1.3
req.target-min-winversvr: Windows Server 2012 R2
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DxgkDdiFormatHistoryBuffer
req.alt-loc: D3dkmddi.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: DISPATCH_LEVEL
---

# DXGKDDI_FORMATHISTORYBUFFER callback



## -description
 Copies unformatted data from the history buffer into a buffer that's properly formatted to be submitted to the Event Tracing for Windows (ETW) facility.



## -prototype

````
DXGKDDI_FORMATHISTORYBUFFER DxgkDdiFormatHistoryBuffer;

_Check_return NTSTATUS APIENTRY* DxgkDdiFormatHistoryBuffer(
  _In_ const HANDLE                      hContext,
  _In_       DXGKARG_FORMATHISTORYBUFFER *pFormatData
)
{ ... }
````


## -parameters

### -param hContext [in]

A handle to the device context for the DMA buffer that contains the unformatted history buffer.


### -param pFormatData [in]

A pointer to a <a href="display.dxgkarg_formathistorybuffer">DXGKARG_FORMATHISTORYBUFFER</a> structure that contains data about how to format the history buffer.


## -returns
Returns <b>STATUS_SUCCESS</b> if it succeeds; otherwise, it returns one of the error codes defined in Ntstatus.h.


## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Minimum supported client

</th>
<td width="70%">
Windows 8.1

</td>
</tr>
<tr>
<th width="30%">
Minimum supported server

</th>
<td width="70%">
Windows Server 2012 R2

</td>
</tr>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Version

</th>
<td width="70%">
WDDM 1.3

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>D3dkmddi.h</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL

</th>
<td width="70%">
DISPATCH_LEVEL

</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="display.dxgkarg_formathistorybuffer">DXGKARG_FORMATHISTORYBUFFER</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGKDDI_FORMATHISTORYBUFFER callback function%20 RELEASE:%20(12/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

