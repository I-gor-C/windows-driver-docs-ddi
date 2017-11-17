---
UID: NC.d3d10umddi.PFND3D10DDI_SETTEXTFILTERSIZE
title: PFND3D10DDI_SETTEXTFILTERSIZE
author: windows-driver-content
description: The SetTextFilterSize function sets the width and height of the monochrome convolution filter.
old-location: display\settextfiltersize.htm
ms.assetid: 663fd3c3-7a8f-446d-b45a-392716116407
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: callback
ms.prod: windows-hardware
ms.technology: display
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: SetTextFilterSize
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

# PFND3D10DDI_SETTEXTFILTERSIZE callback



## -description
<p>The <i>SetTextFilterSize</i> function sets the width and height of the monochrome convolution filter.</p>


## -prototype

````
PFND3D10DDI_SETTEXTFILTERSIZE SetTextFilterSize;

VOID APIENTRY SetTextFilterSize(
  _In_ D3D10DDI_HDEVICE hDevice,
  _In_ UINT             Width,
  _In_ UINT             Height
)
{ ... }
````


## -parameters
<dl>

### -param <i>hDevice</i> [in]

<dd>
<p> A handle to the display device (graphics context).</p>
</dd>

### -param <i>Width</i> [in]

<dd>
<p> The width of the monochrome convolution filter. The width can be from 1 to 7 texels.</p>
</dd>

### -param <i>Height</i> [in]

<dd>
<p> The height of the monochrome convolution filter. The height can be from 1 to 7 texels.</p>
</dd>
</dl>

## -returns
<p>None</p>

<p>The driver can use the <a href="https://msdn.microsoft.com/968b04a7-8869-410c-a6fc-83d57726858f">pfnSetErrorCb</a> callback function to set an error code. For more information about setting error codes, see the following Remarks section.</p>

## -remarks
<p>The number of samples that are required from a kernel's dimensions is actually (<i>Width</i> + 1) x (<i>Height</i> + 1), which can come out to from 4 to 64 samples. These settings apply across all samplers that are configured to use the D3D10_DDI_FILTER_TEXT_1BIT filter from the <a href="https://msdn.microsoft.com/library/windows/hardware/ff541952">D3D10_DDI_FILTER</a> enumeration.</p>

<p><i>SetTextFilterSize</i> ensures that values that are supplied in the <i>Width</i> and <i>Height</i> parameters are in range. The default vaules for <i>Width</i> and <i>Height</i> are both 1, initially. The driver must set these default values during device creation.</p>

<p>The driver should not encounter any error, except for D3DDDIERR_DEVICEREMOVED. Therefore, if the driver passes any error, except for D3DDDIERR_DEVICEREMOVED, in a call to the <a href="https://msdn.microsoft.com/968b04a7-8869-410c-a6fc-83d57726858f">pfnSetErrorCb</a> function, the Direct3D runtime will determine that the error is critical. Even if the device was removed, the driver is not required to return D3DDDIERR_DEVICEREMOVED. However, if device removal interfered with the operation of <i>SetTextFilterSize</i> (which typically should not happen), the driver can return D3DDDIERR_DEVICEREMOVED.</p>

<p>The number of samples that are required from a kernel's dimensions is actually (<i>Width</i> + 1) x (<i>Height</i> + 1), which can come out to from 4 to 64 samples. These settings apply across all samplers that are configured to use the D3D10_DDI_FILTER_TEXT_1BIT filter from the <a href="https://msdn.microsoft.com/library/windows/hardware/ff541952">D3D10_DDI_FILTER</a> enumeration.</p>

<p><i>SetTextFilterSize</i> ensures that values that are supplied in the <i>Width</i> and <i>Height</i> parameters are in range. The default vaules for <i>Width</i> and <i>Height</i> are both 1, initially. The driver must set these default values during device creation.</p>

<p>The driver should not encounter any error, except for D3DDDIERR_DEVICEREMOVED. Therefore, if the driver passes any error, except for D3DDDIERR_DEVICEREMOVED, in a call to the <a href="https://msdn.microsoft.com/968b04a7-8869-410c-a6fc-83d57726858f">pfnSetErrorCb</a> function, the Direct3D runtime will determine that the error is critical. Even if the device was removed, the driver is not required to return D3DDDIERR_DEVICEREMOVED. However, if device removal interfered with the operation of <i>SetTextFilterSize</i> (which typically should not happen), the driver can return D3DDDIERR_DEVICEREMOVED.</p>

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
<dt>D3d10umddi.h (include D3d10umddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541952">D3D10_DDI_FILTER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541833">D3D10DDI_DEVICEFUNCS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/968b04a7-8869-410c-a6fc-83d57726858f">pfnSetErrorCb</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFND3D10DDI_SETTEXTFILTERSIZE callback function%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
