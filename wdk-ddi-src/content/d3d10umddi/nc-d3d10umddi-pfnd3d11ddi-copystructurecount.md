---
UID: NC.d3d10umddi.PFND3D11DDI_COPYSTRUCTURECOUNT
title: PFND3D11DDI_COPYSTRUCTURECOUNT
author: windows-driver-content
description: The CopyStructureCount function copies the number of items in the filled portion (that is, the filled-size value) of an append buffer unordered access view (UAV) to an offset into a destination buffer.
old-location: display\copystructurecount.htm
old-project: display
ms.assetid: 39f20ff3-859f-4933-8be0-e2bb7c05e7e1
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: SETRESULT_INFO, SETRESULT_INFO, *PSETRESULT_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Desktop
req.target-min-winverclnt: CopyStructureCount is supported beginning with the Windows 7 operating system.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: CopyStructureCount
req.alt-loc: d3d10umddi.h
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

# PFND3D11DDI_COPYSTRUCTURECOUNT callback



## -description
<p>The <b>CopyStructureCount</b> function copies the number of items in the filled portion (that is, the filled-size value) of an append buffer unordered access view (UAV) to an offset into a destination buffer. </p>


## -prototype

````
PFND3D11DDI_COPYSTRUCTURECOUNT CopyStructureCount;

VOID APIENTRY CopyStructureCount(
  _In_ D3D10DDI_HDEVICE              hDevice,
  _In_ D3D10DDI_HRESOURCE            hDstBuffer,
  _In_ UINT                          DstAlignedByteOffset,
  _In_ D3D11DDI_HUNORDEREDACCESSVIEW hSrcView
)
{ ... }
````


## -parameters
<dl>

### -param hDevice [in]

<dd>
<p> A handle to the display device (graphics context).</p>
</dd>

### -param hDstBuffer [in]

<dd>
<p> A handle to a destination buffer to copy the filled-size value of an UAV to. To create this destination buffer, the runtime must have previously called the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11ddi-createresource.md">CreateResource(D3D11)</a> function with the <b>ResourceDimension</b> member of the <a href="..\d3d10umddi\ns-d3d10umddi-d3d11ddiarg-createresource.md">D3D11DDIARG_CREATERESOURCE</a> structure set to the D3D10DDIRESOURCE_BUFFER value. </p>
</dd>

### -param DstAlignedByteOffset [in]

<dd>
<p> The 4-byte aligned offset, in bytes, into the destination buffer that the <i>hDstBuffer</i> parameter specifies. <b>CopyStructureCount</b> copies the filled-size value of the append buffer view that the <i>hSrcView</i> parameter specifies to this offset in <b>hDstBuffer</b>. <b>DstAlignedByteOffset</b> must be a multiple of four. </p>
</dd>

### -param hSrcView [in]

<dd>
<p> A handle to the source append UAV, which must be an append buffer view. <b>CopyStructureCount</b> copies the filled-size value of this view to the destination buffer that the <b>hDstBuffer</b> parameter specifies. To create this append buffer view, the runtime must have previously called the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11ddi-createunorderedaccessview.md">CreateUnorderedAccessView</a> function with the D3D11_DDI_BUFFER_UAV_FLAG_APPEND flag set. </p>
</dd>
</dl>

## -returns
<p>None</p>

<p>The driver can use the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-seterror-cb.md">pfnSetErrorCb</a> callback function to set an error code. For more information about setting error codes, see the following Remarks section.</p>

## -remarks
<p>The driver should not encounter any error, except for D3DDDIERR_DEVICEREMOVED. Therefore, if the driver passes any error, except for D3DDDIERR_DEVICEREMOVED, in a call to the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-seterror-cb.md">pfnSetErrorCb</a> function, the Direct3D runtime determines that the error is critical. Even if the device is removed, the driver is not required to return D3DDDIERR_DEVICEREMOVED; however, if the device removal interferes with the operation of <b>CopyStructureCount</b> (which typically should not happen), the driver can return D3DDDIERR_DEVICEREMOVED.</p>

<p><b>CopyStructureCount</b> takes the filled-size value of the append buffer UAV (a UAV that supports push and pop-up operations on structures like on a stack) and copies this value to an offset into the destination buffer. The graphics hardware uses a 4-byte filled-size value to keep track of how much data is filled in the append buffer UAV. </p>

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
<p>CopyStructureCount is supported beginning with the Windows 7 operating system. </p>
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
<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11ddi-createresource.md">CreateResource(D3D11)</a>
</dt>
<dt>
<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11ddi-createunorderedaccessview.md">CreateUnorderedAccessView</a>
</dt>
<dt>
<a href="..\d3d10umddi\ns-d3d10umddi-d3d11ddi-devicefuncs~r1.md">D3D11DDI_DEVICEFUNCS</a>
</dt>
<dt>
<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-seterror-cb.md">pfnSetErrorCb</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFND3D11DDI_COPYSTRUCTURECOUNT callback function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
