---
UID: NC.d3d10umddi.PFND3D11DDI_SETUNORDEREDACCESSVIEWS
title: PFND3D11DDI_SETUNORDEREDACCESSVIEWS
author: windows-driver-content
description: The CsSetUnorderedAccessViews function sets unordered access view (UAV) objects for a compute shader.
old-location: display\cssetunorderedaccessviews.htm
ms.assetid: ab8c529b-19e2-4a2a-af68-0e3998829788
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: callback
ms.prod: windows-hardware
ms.technology: display
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Desktop
req.target-min-winverclnt: CsSetUnorderedAccessViews is supported beginning with the Windows 7 operating system.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: CsSetUnorderedAccessViews
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
ms.keywords: SETRESULT_INFO, SETRESULT_INFO, *PSETRESULT_INFO
req.iface: 
---

# PFND3D11DDI_SETUNORDEREDACCESSVIEWS callback



## -description
<p>The <i>CsSetUnorderedAccessViews</i> function sets unordered access view (UAV) objects for a compute shader.</p>


## -prototype

````
PFND3D11DDI_SETUNORDEREDACCESSVIEWS CsSetUnorderedAccessViews;

VOID APIENTRY CsSetUnorderedAccessViews(
  _In_       D3D10DDI_HDEVICE              hDevice,
  _In_       UINT                          Offset,
  _In_       UINT                          NumViews,
  _In_ const D3D11DDI_HUNORDEREDACCESSVIEW *phUnorderedAccessView,
  _In_ const UINT                          *pUAVInitialCounts
)
{ ... }
````


## -parameters
<dl>

### -param <i>hDevice</i> [in]

<dd>
<p> A handle to the display device (graphics context).</p>
</dd>

### -param <i>Offset</i> [in]

<dd>
<p> The offset to the first view to set. </p>
</dd>

### -param <i>NumViews</i> [in]

<dd>
<p> The total number of views to set. </p>
</dd>

### -param <i>phUnorderedAccessView</i> [in]

<dd>
<p> An array of handles to the driver's private data for unordered access view objects to set. Note that some handle values can be <b>NULL</b>. </p>
</dd>

### -param <i>pUAVInitialCounts</i> [in]

<dd>
<p>An array of append and consume buffer offsets. A value of -1 indicates that the current offset should be kept. Any other values set the hidden counter for that appendable and consumable UAV. <i>pUAVInitialCounts</i> is only relevant for UAVs  of the <i>phUnorderedAccessView</i> array that were created with either <b>D3D11_DDI_BUFFER_UAV_FLAG_APPEND</b>  or <b>D3D11_DDI_BUFFER_UAV_FLAG_COUNTER</b> specified in the <b>Flags</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff542033">D3D11DDIARG_BUFFER_UNORDEREDACCESSVIEW</a> structure when the UAV was created; otherwise, the argument is ignored.</p>
</dd>
</dl>

## -returns
<p>None</p>

<p>The driver can use the <a href="https://msdn.microsoft.com/968b04a7-8869-410c-a6fc-83d57726858f">pfnSetErrorCb</a> callback function to set an error code. For more information about setting error codes, see the following Remarks section.</p>

## -remarks
<p>The driver should not encounter any error, except for D3DDDIERR_DEVICEREMOVED. Therefore, if the driver passes any error, except for D3DDDIERR_DEVICEREMOVED, in a call to the <a href="https://msdn.microsoft.com/968b04a7-8869-410c-a6fc-83d57726858f">pfnSetErrorCb</a> function, the Microsoft Direct3D runtime determines that the error is critical. Even if the device is removed, the driver is not required to return D3DDDIERR_DEVICEREMOVED; however, if device removal interferes with the operation of <i>CsSetUnorderedAccessViews</i> (which typically should not happen), the driver can return D3DDDIERR_DEVICEREMOVED.</p>

<p>The driver should not encounter any error, except for D3DDDIERR_DEVICEREMOVED. Therefore, if the driver passes any error, except for D3DDDIERR_DEVICEREMOVED, in a call to the <a href="https://msdn.microsoft.com/968b04a7-8869-410c-a6fc-83d57726858f">pfnSetErrorCb</a> function, the Microsoft Direct3D runtime determines that the error is critical. Even if the device is removed, the driver is not required to return D3DDDIERR_DEVICEREMOVED; however, if device removal interferes with the operation of <i>CsSetUnorderedAccessViews</i> (which typically should not happen), the driver can return D3DDDIERR_DEVICEREMOVED.</p>

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
<p>CsSetUnorderedAccessViews is supported beginning with the Windows 7 operating system. </p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff542141">D3D11DDI_DEVICEFUNCS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff542033">D3D11DDIARG_BUFFER_UNORDEREDACCESSVIEW</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/968b04a7-8869-410c-a6fc-83d57726858f">pfnSetErrorCb</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFND3D11DDI_SETUNORDEREDACCESSVIEWS callback function%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
