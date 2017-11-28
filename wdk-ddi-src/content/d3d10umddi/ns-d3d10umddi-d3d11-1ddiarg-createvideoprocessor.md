---
UID: NS.d3d10umddi.D3D11_1DDIARG_CREATEVIDEOPROCESSOR
title: D3D11_1DDIARG_CREATEVIDEOPROCESSOR
author: windows-driver-content
description: Specifies the attributes of a video processor object.
old-location: display\d3d11_1ddiarg_createvideoprocessor.htm
old-project: display
ms.assetid: 957cfebe-4cd9-4a35-822e-ebde4cd9e84c
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3D11_1DDIARG_CREATEVIDEOPROCESSOR, D3D11_1DDIARG_CREATEVIDEOPROCESSOR
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3D11_1DDIARG_CREATEVIDEOPROCESSOR
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

# D3D11_1DDIARG_CREATEVIDEOPROCESSOR structure



## -description
<p>Specifies the attributes of a video processor object.</p>


## -syntax

````
typedef struct D3D11_1DDIARG_CREATEVIDEOPROCESSOR {
  D3D11_1DDI_HVIDEOPROCESSORENUM hVideoProcessorEnum;
  UINT                           RateConversionCapsIndex;
} D3D11_1DDIARG_CREATEVIDEOPROCESSOR;
````


## -struct-fields
<dl>

### -field <b>hVideoProcessorEnum</b>

<dd>
<p>A handle to a video processor enumeration object that was created through a call to the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11-1ddi-createvideoprocessorenum.md">CreateVideoProcessorEnum</a> function. </p>
</dd>

### -field <b>RateConversionCapsIndex</b>

<dd>
<p>Specifies the frame-rate conversion capabilities for the video processor. The value is a zero-based index that corresponds to the <i>RateConversionIndex</i> parameter of the <a href="https://msdn.microsoft.com/library/windows/hardware/hh451690">GetVideoProcessorRateConversionCaps</a> method. </p>
</dd>
</dl>

## -remarks


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
<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11-1ddi-createvideoprocessorenum.md">CreateVideoProcessorEnum</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh451690">GetVideoProcessorRateConversionCaps</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3D11_1DDIARG_CREATEVIDEOPROCESSOR structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
