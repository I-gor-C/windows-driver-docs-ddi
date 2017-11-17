---
UID: NS.dxgiddi.DXGI_DDI_ARG_SETRESOURCEPRIORITY
title: DXGI_DDI_ARG_SETRESOURCEPRIORITY
author: windows-driver-content
description: The DXGI_DDI_ARG_SETRESOURCEPRIORITY structure describes parameters for setting the priority level of a resource.
old-location: display\dxgi_ddi_arg_setresourcepriority.htm
ms.assetid: 9d3f5687-bc49-4831-bf56-5d4201ed45de
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: dxgiddi.h
req.include-header: D3d10umddi.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGI_DDI_ARG_SETRESOURCEPRIORITY
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
ms.keywords: DXGI_DDI_ARG_SETRESOURCEPRIORITY, DXGI_DDI_ARG_SETRESOURCEPRIORITY
req.iface: 
---

# DXGI_DDI_ARG_SETRESOURCEPRIORITY structure



## -description
<p>The DXGI_DDI_ARG_SETRESOURCEPRIORITY structure describes parameters for setting the priority level of a resource. </p>


## -syntax

````
typedef struct DXGI_DDI_ARG_SETRESOURCEPRIORITY {
  DXGI_DDI_HDEVICE   hDevice;
  DXGI_DDI_HRESOURCE hResource;
  UINT               Priority;
} DXGI_DDI_ARG_SETRESOURCEPRIORITY;
````


## -struct-fields
<dl>

### -field <b>hDevice</b>

<dd>
<p>[in] A handle to the display device (graphics context) on which the driver sets the eviction-from-memory priority for a resource. The Direct3D runtime passes this handle to the driver in the <b>hDrvDevice</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff541664">D3D10DDIARG_CREATEDEVICE</a> structure when the runtime calls the driver's <a href="https://msdn.microsoft.com/c69eedb1-c975-412c-aa9f-cf64a702f937">CreateDevice(D3D10)</a> function to create the display device. </p>
</dd>

### -field <b>hResource</b>

<dd>
<p>[in] A handle to the resource to set the priority level for.</p>
</dd>

### -field <b>Priority</b>

<dd>
<p>[in] The priority level to set for the resource that the <b>hResource</b> member specifies. A resource's priority level can be set anywhere in the range from 0 through 0xFFFFFFFF.</p>
</dd>
</dl>

## -remarks
<p>The priority level that a resource is set at determines its eviction order from memory. A resource that is assigned a low priority is evicted before a resource with a high priority. If two resources have the same priority, the resource that was used more recently is kept in memory; the other resource is evicted.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff569657">SetResourcePriorityDXGI</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGI_DDI_ARG_SETRESOURCEPRIORITY structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
