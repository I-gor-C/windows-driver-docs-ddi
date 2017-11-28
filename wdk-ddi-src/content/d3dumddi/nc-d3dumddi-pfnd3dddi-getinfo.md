---
UID: NC.d3dumddi.PFND3DDDI_GETINFO
title: PFND3DDDI_GETINFO
author: windows-driver-content
description: The GetInfo function retrieves information about the specified display device.
old-location: display\getinfo.htm
old-project: display
ms.assetid: dcc0519e-f919-48bc-829f-416648de0b40
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGK_MIRACAST_CHUNK_INFO, DXGK_MIRACAST_CHUNK_INFO
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
req.alt-api: GetInfo
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
req.iface: 
---

# PFND3DDDI_GETINFO callback



## -description
<p>The <i>GetInfo</i> function retrieves information about the specified display device.</p>


## -prototype

````
PFND3DDDI_GETINFO GetInfo;

__checkReturn HRESULT APIENTRY GetInfo(
   __in HANDLE                   hDevice,
   __in UINT                     DevInfoID,
   __out_bcount(DevInfoSize)VOID *pDevInfoStruct,
   __in UINT                     DevInfoSize
)
{ ... }
````


## -parameters
<dl>

### -param <i>hDevice</i> 

<dd>
<p> A handle to the display device (graphics context).</p>
</dd>

### -param <i>DevInfoID</i> 

<dd>
<p> An identifier for the type of device information to retrieve.</p>
</dd>

### -param <i>pDevInfoStruct</i> 

<dd>
<p> A pointer to a buffer of the type that <i>DevInfoID</i> specifies that receives information about the device.</p>
</dd>

### -param <i>DevInfoSize</i> 

<dd>
<p> The size, in bytes, of the buffer that is supplied by <i>pDevInfoStruct</i>.</p>
</dd>
</dl>

## -returns
<p><i>GetInfo</i> returns one of the following values:</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The device information is successfully retrieved.</p><dl>
<dt><b>E_NOTIMPL</b></dt>
</dl><p>The driver does not support the requested type of device information.</p><dl>
<dt><b>E_INVALIDARG</b></dt>
</dl><p>Parameters were validated and determined to be incorrect.</p>

<p> </p>

## -remarks
<p>The Microsoft DirectX 7 and DirectX 8 runtimes call the <i>GetInfo</i> function to query a user-mode display driver for additional device information.</p>

<p>The Direct3D 8 runtime sets the D3DDDIDEVINFOID_VCACHE flag in the <i>DevInfoID</i> parameter and specifies an empty <a href="https://msdn.microsoft.com/library/windows/hardware/ff544294">D3DDDIDEVINFO_VCACHE</a> structure in the <i>pDevInfoStruct</i> parameter to query the user-mode display driver's support for vertex cache.</p>

<p>The Microsoft DirectX 7 and DirectX 8 runtimes call the <i>GetInfo</i> function to query a user-mode display driver for additional device information.</p>

<p>The Direct3D 8 runtime sets the D3DDDIDEVINFOID_VCACHE flag in the <i>DevInfoID</i> parameter and specifies an empty <a href="https://msdn.microsoft.com/library/windows/hardware/ff544294">D3DDDIDEVINFO_VCACHE</a> structure in the <i>pDevInfoStruct</i> parameter to query the user-mode display driver's support for vertex cache.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544519">D3DDDI_DEVICEFUNCS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544294">D3DDDIDEVINFO_VCACHE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFND3DDDI_GETINFO callback function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
