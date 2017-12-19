---
UID: NC.d3dumddi.PFND3DDDI_SETSTREAMSOURCE
title: PFND3DDDI_SETSTREAMSOURCE
author: windows-driver-content
description: The SetStreamSource function binds a portion of a vertex stream source to a vertex buffer.
old-location: display\setstreamsource.htm
old-project: display
ms.assetid: 669dbabc-91fb-40f9-a034-11c3c2e70436
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: _DXGK_PTE, DXGK_PTE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: d3dumddi.h
req.include-header: D3dumddi.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: SetStreamSource
req.alt-loc: d3dumddi.h
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
---

# PFND3DDDI_SETSTREAMSOURCE callback



## -description
The <i>SetStreamSource</i> function binds a portion of a vertex stream source to a vertex buffer. 



## -prototype

````
PFND3DDDI_SETSTREAMSOURCE SetStreamSource;

__checkReturn HRESULT APIENTRY SetStreamSource(
  _In_       HANDLE                    hDevice,
  _In_ const D3DDDIARG_SETSTREAMSOURCE *pData
)
{ ... }
````


## -parameters

### -param hDevice [in]

 A handle to the display device (graphics context).


### -param pData [in]

 A pointer to a <a href="display.d3dddiarg_setstreamsource">D3DDDIARG_SETSTREAMSOURCE</a> structure that specifies the portion of the vertex stream source to bind.


## -returns
<i>SetStreamSource</i> returns S_OK or an appropriate error result if the portion of the vertex stream source is not successfully bound.


## -remarks
The Microsoft Direct3D runtime calls the user-mode display driver's <i>SetStreamSource</i> function to store vertex data of multiple vertex formats in a single vertex data stream. The runtime notifies the driver of where vertex data of a particular format is located in the vertex data stream by supplying the stream offset, in bytes, to the beginning of that vertex data. 


## -requirements
<table>
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
Available in Windows Vista and later versions of the Windows operating systems.

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>D3dumddi.h (include D3dumddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="display.d3dddiarg_setstreamsource">D3DDDIARG_SETSTREAMSOURCE</a>
</dt>
<dt>
<a href="display.d3dddi_devicefuncs">D3DDDI_DEVICEFUNCS</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFND3DDDI_SETSTREAMSOURCE callback function%20 RELEASE:%20(12/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

