---
UID: NS.dxgiddi.DXGI_DDI_ARG_ROTATE_RESOURCE_IDENTITIES
title: DXGI_DDI_ARG_ROTATE_RESOURCE_IDENTITIES
author: windows-driver-content
description: Describes a list of resources to rotate.
old-location: display\dxgi_ddi_arg_rotate_resource_identities.htm
old-project: display
ms.assetid: 904b16d1-44dc-4d7a-96cb-3fd82d378b24
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGI_DDI_ARG_ROTATE_RESOURCE_IDENTITIES, DXGI_DDI_ARG_ROTATE_RESOURCE_IDENTITIES
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: dxgiddi.h
req.include-header: D3d10umddi.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGI_DDI_ARG_ROTATE_RESOURCE_IDENTITIES
req.alt-loc: dxgiddi.h
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

# DXGI_DDI_ARG_ROTATE_RESOURCE_IDENTITIES structure



## -description
<p>Describes a list of resources to rotate. </p>


## -syntax

````
typedef struct DXGI_DDI_ARG_ROTATE_RESOURCE_IDENTITIES {
  DXGI_DDI_HDEVICE         hDevice;
  const DXGI_DDI_HRESOURCE *pResources;
  UINT                     Resources;
} DXGI_DDI_ARG_ROTATE_RESOURCE_IDENTITIES;
````


## -struct-fields
<dl>

### -field <b>hDevice</b>

<dd>
<p>[in] A handle to the display device (graphics context) on which the driver rotates resources. The Direct3D runtime passes this handle to the driver in the <b>hDrvDevice</b> member of the <a href="..\d3d10umddi\ns-d3d10umddi-d3d10ddiarg-createdevice.md">D3D10DDIARG_CREATEDEVICE</a> structure when the runtime calls the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-createdevice.md">CreateDevice(D3D10)</a> function to create the display device. </p>
</dd>

### -field <b>pResources</b>

<dd>
<p>[in] A pointer to an array of handles to the resources to rotate.</p>
<p>Beginning in Windows 8, the driver must support rotation of stereo back buffers.</p>
</dd>

### -field <b>Resources</b>

<dd>
<p>[in] The number of elements in the <i>pResources</i> array.  </p>
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
<p>Available in Windows Vista and later versions of the Windows operating systems.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Dxgiddi.h (include D3d10umddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="display.rotateresourceidentitiesdxgi">RotateResourceIdentitiesDXGI</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGI_DDI_ARG_ROTATE_RESOURCE_IDENTITIES structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
