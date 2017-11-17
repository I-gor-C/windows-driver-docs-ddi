---
UID: NC.d3dumddi.PFND3DDDI_DESTROYVIDEOPROCESSDEVICE
title: PFND3DDDI_DESTROYVIDEOPROCESSDEVICE
author: windows-driver-content
description: The DestroyVideoProcessDevice function releases resources for a Microsoft DirectX Video Acceleration (VA) video processing device.
old-location: display\destroyvideoprocessdevice.htm
ms.assetid: dc0f8dba-afdd-47f4-ba7f-72c510e80052
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
req.alt-api: DestroyVideoProcessDevice
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

# PFND3DDDI_DESTROYVIDEOPROCESSDEVICE callback



## -description
<p>The <b>DestroyVideoProcessDevice</b> function releases resources for a Microsoft DirectX Video Acceleration (VA) video processing device.</p>


## -prototype

````
PFND3DDDI_DESTROYVIDEOPROCESSDEVICE DestroyVideoProcessDevice;

__checkReturn HRESULT APIENTRY DestroyVideoProcessDevice(
  _In_ HANDLE hDevice,
  _In_ HANDLE hVideoProcessor
)
{ ... }
````


## -parameters
<dl>

### -param <i>hDevice</i> [in]

<dd>
<p> A handle to the display device (graphics context).</p>
</dd>

### -param <i>hVideoProcessor</i> [in]

<dd>
<p> A handle to the DirectX VA video processing device that was created by the <a href="https://msdn.microsoft.com/3149c7d9-0bf7-4355-8f15-821cf6b92f0a">CreateVideoProcessDevice</a> function.</p>
</dd>
</dl>

## -returns
<p><b>DestroyVideoProcessDevice</b>  should return S_OK or an appropriate error result if it cannot successfully release resources for the DirectX VA decode device.</p>

## -remarks
<p>The <b>DestroyVideoProcessDevice</b> function notifies the driver to destroy the handle to the DirectX VA video processing device that the <a href="https://msdn.microsoft.com/3149c7d9-0bf7-4355-8f15-821cf6b92f0a">CreateVideoProcessDevice</a> function previously created. The driver can then release resources that are associated with the DirectX VA video processing device handle.</p>

<p>The <b>DestroyVideoProcessDevice</b> function notifies the driver to destroy the handle to the DirectX VA video processing device that the <a href="https://msdn.microsoft.com/3149c7d9-0bf7-4355-8f15-821cf6b92f0a">CreateVideoProcessDevice</a> function previously created. The driver can then release resources that are associated with the DirectX VA video processing device handle.</p>

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
<a href="https://msdn.microsoft.com/3149c7d9-0bf7-4355-8f15-821cf6b92f0a">CreateVideoProcessDevice</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544519">D3DDDI_DEVICEFUNCS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFND3DDDI_DESTROYVIDEOPROCESSDEVICE callback function%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
