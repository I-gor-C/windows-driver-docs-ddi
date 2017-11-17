---
UID: NC.d3dumddi.PFND3DDDI_ESCAPECB
title: PFND3DDDI_ESCAPECB
author: windows-driver-content
description: The pfnEscapeCb callback function shares information with the display miniport driver.
old-location: display\pfnescapecb.htm
ms.assetid: 66c0347f-2cf3-42fc-8641-47c731e958c9
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: callback
ms.prod: windows-hardware
ms.technology: display
req.header: d3dumddi.h
req.include-header: D3dumddi.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: pfnEscapeCb
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
ms.keywords: DXGK_MIRACAST_CHUNK_INFO, DXGK_MIRACAST_CHUNK_INFO
req.iface: 
---

# PFND3DDDI_ESCAPECB callback



## -description
<p>The <b>pfnEscapeCb</b> callback function shares information with the display miniport driver.</p>


## -prototype

````
PFND3DDDI_ESCAPECB pfnEscapeCb;

__checkReturn HRESULT APIENTRY CALLBACK pfnEscapeCb(
  _In_          HANDLE          hAdapter,
  _Inout_ const D3DDDICB_ESCAPE *pData
)
{ ... }
````


## -parameters
<dl>

### -param <i>hAdapter</i> [in]

<dd>
<p>A handle to the graphics adapter object.</p>
</dd>

### -param <i>pData</i> [in, out]

<dd>
<p>A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff544190">D3DDDICB_ESCAPE</a> structure that describes the shared information.</p>
</dd>
</dl>

## -returns
<p><b>pfnEscapeCb</b> returns one of the following values:</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>Information was successfully shared.</p><dl>
<dt><b>E_OUTOFMEMORY</b></dt>
</dl><p><b>pfnEscapeCb</b> could not complete because of insufficient memory.</p><dl>
<dt><b>E_INVALIDARG</b></dt>
</dl><p>
        Parameters were validated and determined to be incorrect.
       </p><dl>
<dt><b>D3DDDIERR_DEVICEREMOVED</b></dt>
</dl><p><b>pfnEscapeCb</b> could not initiate a call to the display miniport driver's <a href="https://msdn.microsoft.com/79a524cd-dec1-4ea8-a660-d9d9c644e162">DxgkDdiEscape</a> function because a Plug and Play (PnP) stop or a Timeout Detection and Recovery (TDR) event occurred. The user-mode display driver function that called <b>pfnEscapeCb</b> must return this error code back to the Direct3D runtime. </p>

<p><b>Direct3D Version 9 Note:  </b>For more information about returning error codes, see <a href="https://msdn.microsoft.com/4a2384e8-407f-4248-8b31-7c4e836b15dc">Returning Error Codes Received from Runtime Functions</a>.</p>

<p><b>Direct3D Versions 10 and 11 Note:  </b>If the driver function does not return a value (that is, has VOID for a return parameter type), the driver function calls the <a href="https://msdn.microsoft.com/968b04a7-8869-410c-a6fc-83d57726858f">pfnSetErrorCb</a> function to send an error code back to the runtime. For more information about handling error codes, see <a href="https://msdn.microsoft.com/ac4e056e-3304-4934-887a-5cc2b87989bd">Handling Errors</a>.</p>

<p> </p>

<p>This function might also return other HRESULT values.</p>

## -remarks
<p>A user-mode display driver calls <b>pfnEscapeCb</b> to share miscellaneous information with the display miniport driver in a way that is not supported by any other driver communication. The user-mode display driver can send miscellaneous information to the display miniport driver or can retrieve information from the display miniport driver. </p>

<p><b>Direct3D Version 11 Note:  </b>For more information about how the driver calls <b>pfnEscapeCb</b>, see <a href="https://msdn.microsoft.com/014a5e44-f8c4-45c0-96e8-d82f37b8b28d">Changes from Direct3D 10</a>.</p>

<p>A user-mode display driver calls <b>pfnEscapeCb</b> to share miscellaneous information with the display miniport driver in a way that is not supported by any other driver communication. The user-mode display driver can send miscellaneous information to the display miniport driver or can retrieve information from the display miniport driver. </p>

<p><b>Direct3D Version 11 Note:  </b>For more information about how the driver calls <b>pfnEscapeCb</b>, see <a href="https://msdn.microsoft.com/014a5e44-f8c4-45c0-96e8-d82f37b8b28d">Changes from Direct3D 10</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows Vista and later versions of the Windows operating systems.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544512">D3DDDI_DEVICECALLBACKS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544190">D3DDDICB_ESCAPE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/79a524cd-dec1-4ea8-a660-d9d9c644e162">DxgkDdiEscape</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFND3DDDI_ESCAPECB callback function%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
