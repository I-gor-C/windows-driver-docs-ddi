---
UID: NC.d3d10umddi.PFND3D11_1DDI_RESOURCEUPDATESUBRESOURCEUP
title: PFND3D11_1DDI_RESOURCEUPDATESUBRESOURCEUP
author: windows-driver-content
description: Updates a destination subresource region that stores constant buffers from a source system-memory region. Implemented by Windows Display Driver Model (WDDM) 1.2 and later user-mode display drivers.
old-location: display\defaultconstantbufferupdatesubresourceup_d3d11_1_.htm
old-project: display
ms.assetid: 67FCC9A4-B3C5-46FC-83ED-CFFB8186328F
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: SETRESULT_INFO, SETRESULT_INFO, *PSETRESULT_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Desktop
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DefaultConstantBufferUpdateSubresourceUP(D3D11_1)
req.alt-loc: D3d10umddi.h
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

# PFND3D11_1DDI_RESOURCEUPDATESUBRESOURCEUP callback



## -description
<p>updates a destination subresource region that stores constant buffers from a source system-memory region. Implemented by Windows Display Driver Model (WDDM) 1.2 and later user-mode display drivers.</p>


## -prototype

````
PFND3D11_1DDI_RESOURCEUPDATESUBRESOURCEUP DefaultConstantBufferUpdateSubresourceUP(D3D11_1);

VOID APIENTRY* DefaultConstantBufferUpdateSubresourceUP(D3D11_1)(
                 D3D10DDI_HDEVICE   hDevice,
                 D3D10DDI_HRESOURCE hDstResource,
                 UINT               DstSubresource,
  _In_opt_ const D3D10_DDI_BOX      *pDstBox,
  _In_     const VOID               *pSysMemUP,
                 UINT               RowPitch,
                 UINT               DepthPitch,
                 UINT               CopyFlags
)
{ ... }
````


## -parameters
<dl>

### -param <i>hDevice</i> 

<dd>
<p> A handle to the display device (graphics context).</p>
</dd>

### -param <i>hDstResource</i> 

<dd>
<p> A handle to the destination resource to copy to.</p>
</dd>

### -param <i>DstSubresource</i> 

<dd>
<p> An index that indicates the destination subresource to copy to.</p>
</dd>

### -param <i>pDstBox</i> [in, optional]

<dd>
<p> A pointer to a <a href="..\d3d10umddi\ns-d3d10umddi-d3d10-ddi-box.md">D3D10_DDI_BOX</a> structure that specifies the region of the destination subresource to copy data to. If <i>pDstBox</i> is <b>NULL</b>, the driver should copy to the entire destination subresouce. </p>
</dd>

### -param <i>pSysMemUP</i> [in]

<dd>
<p> A pointer to the beginning address of the source data that <b>DefaultConstantBufferUpdateSubresourceUP(D3D11_1)</b> uses to update the destination subresouce. </p>
</dd>

### -param <i>RowPitch</i> 

<dd>
<p> The offset, in bytes, to move to the next row of source data.</p>
</dd>

### -param <i>DepthPitch</i> 

<dd>
<p> The offset, in bytes, to move to the next depth slice of source data.</p>
</dd>

### -param <i>CopyFlags</i> 

<dd>
<p>A value that specifies characteristics of copy operation as a bitwise <b>OR</b> of the values in the <a href="..\d3d10umddi\ne-d3d10umddi-d3d11-1-ddi-copy-flags.md">D3D11_1_DDI_COPY_FLAGS</a> enumeration type.</p>
</dd>
</dl>

## -returns
<p>None.</p>

<p>The driver can use the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-seterror-cb.md">pfnSetErrorCb</a> callback function to set an error code. For more information about setting error codes, see the following Remarks section.</p>

## -remarks
<p>The driver should not encounter any error, except for <b>D3DDDIERR_DEVICEREMOVED</b>. Therefore, if the driver passes any error, except for <b>D3DDDIERR_DEVICEREMOVED</b>, in a call to the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-seterror-cb.md">pfnSetErrorCb</a> function, the Direct3D runtime will determine that the error is critical. Even if the device was removed, the driver is not required to return <b>D3DDDIERR_DEVICEREMOVED</b>; however, if device removal interfered with the operation of <b>DefaultConstantBufferUpdateSubresourceUP(D3D11_1)</b> (which typically should not happen), the driver can return <b>D3DDDIERR_DEVICEREMOVED</b>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 8</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2012</p>
</td>
</tr>
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
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3d10umddi.h (include D3d10umddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\d3d10umddi\ne-d3d10umddi-d3d11-1-ddi-copy-flags.md">D3D11_1_DDI_COPY_FLAGS</a>
</dt>
<dt>
<a href="..\d3d10umddi\ns-d3d10umddi-d3d11-1ddi-devicefuncs~r1.md">D3D11_1DDI_DEVICEFUNCS</a>
</dt>
<dt>
<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-seterror-cb.md">pfnSetErrorCb</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFND3D11_1DDI_RESOURCEUPDATESUBRESOURCEUP callback function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
