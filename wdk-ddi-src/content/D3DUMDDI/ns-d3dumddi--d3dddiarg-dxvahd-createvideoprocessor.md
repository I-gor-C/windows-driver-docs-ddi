---
UID: NS.d3dumddi._D3DDDIARG_DXVAHD_CREATEVIDEOPROCESSOR
title: D3DDDIARG_DXVAHD_CREATEVIDEOPROCESSOR
author: windows-driver-content
description: The D3DDDIARG_DXVAHD_CREATEVIDEOPROCESSOR structure describes a Microsoft DirectX Video Acceleration (DirectX VA) video processor to create.
old-location: display\d3dddiarg_dxvahd_createvideoprocessor.htm
ms.assetid: fafb1b1f-409d-4eab-a5dd-22fd1ab830d2
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: d3dumddi.h
req.include-header: D3dumddi.h
req.target-type: Windows
req.target-min-winverclnt: D3DDDIARG_DXVAHD_CREATEVIDEOPROCESSOR is supported beginning with the Windows 7 operating system.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DDDIARG_DXVAHD_CREATEVIDEOPROCESSOR
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
ms.keywords: D3DDDIARG_DXVAHD_CREATEVIDEOPROCESSOR, D3DDDIARG_DXVAHD_CREATEVIDEOPROCESSOR
req.iface: 
---

# D3DDDIARG_DXVAHD_CREATEVIDEOPROCESSOR structure



## -description
<p>The D3DDDIARG_DXVAHD_CREATEVIDEOPROCESSOR structure describes a Microsoft DirectX Video Acceleration (DirectX VA) video processor to create. </p>


## -syntax

````
typedef struct _D3DDDIARG_DXVAHD_CREATEVIDEOPROCESSOR {
  const GUID *pVPGuid;
  HANDLE     hVideoProcessor;
} D3DDDIARG_DXVAHD_CREATEVIDEOPROCESSOR;
````


## -struct-fields
<dl>

### -field <b>pVPGuid</b>

<dd>
<p>[in] A pointer to the GUID that represents a DirectX VA video processor to create. The Microsoft Direct3D runtime can call the user-mode display driver's <a href="https://msdn.microsoft.com/cf6c61ce-7b53-46d0-b3ff-ed5b2b964c65">GetCaps</a> function to query (D3DDDICAPS_DXVAHD_GETVPCAPS) for the capabilities of the video processors that the driver supports. Each <b>VPGuid</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff563109">DXVAHDDDI_VPCAPS</a> structure in the array that the driver's <b>GetCaps</b> returns specifies a video processor that the driver supports.  </p>
</dd>

### -field <b>hVideoProcessor</b>

<dd>
<p>[out] A handle to the video processor. The user-mode display driver must set this handle to a value that the Microsoft Direct3D runtime can use to identify the video processor in subsequent calls. </p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>D3DDDIARG_DXVAHD_CREATEVIDEOPROCESSOR is supported beginning with the Windows 7 operating system.</p>
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
<a href="https://msdn.microsoft.com/68a7c394-4b0f-4446-a54b-5aee6cf8a913">CreateVideoProcessor</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563109">DXVAHDDDI_VPCAPS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DDDIARG_DXVAHD_CREATEVIDEOPROCESSOR structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
