---
UID: NE.d3d10umddi.D3D10_DDI_RESOURCE_MISC_FLAG
title: D3D10_DDI_RESOURCE_MISC_FLAG
author: windows-driver-content
description: Identifies miscellaneous information about a resource.
old-location: display\d3d10_ddi_resource_misc_flag.htm
old-project: display
ms.assetid: 1de11acf-1571-44ae-9bde-2b417bf615b7
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: SETRESULT_INFO, SETRESULT_INFO, *PSETRESULT_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3D10_DDI_RESOURCE_MISC_FLAG
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

# D3D10_DDI_RESOURCE_MISC_FLAG enumeration



## -description
<p>Identifies miscellaneous information about a resource. </p>


## -syntax

````
typedef enum D3D10_DDI_RESOURCE_MISC_FLAG { 
  D3D10_DDI_RESOURCE_AUTO_GEN_MIP_MAP                       = 0x00000001L,
  D3D10_DDI_RESOURCE_MISC_SHARED                            = 0x00000002L,
  D3D10_DDI_RESOURCE_MISC_DISCARD_ON_PRESENT                = 0x00000008L,
#if D3D11DDI_MINOR_HEADER_VERSION >= 1
  D3D11_DDI_RESOURCE_MISC_DRAWINDIRECT_ARGS                 = 0x00000010L,
  D3D11_DDI_RESOURCE_MISC_BUFFER_ALLOW_RAW_VIEWS            = 0x00000020L,
  D3D11_DDI_RESOURCE_MISC_BUFFER_STRUCTURED                 = 0x00000040L,
  D3D11_DDI_RESOURCE_MISC_RESOURCE_CLAMP                    = 0x00000080L,
#endif 
  D3D10_DDI_RESOURCE_MISC_REMOTE                            = 0x00000400L,
#if D3D11DDI_MINOR_HEADER_VERSION >= 3
  D3D11_1DDI_RESOURCE_MISC_RESTRICTED_CONTENT               = 0x00000800L,
  D3D11_1DDI_RESOURCE_MISC_RESTRICT_SHARED_RESOURCE_DRIVER  = 0x00001000L,
#endif 
#if D3D11DDI_MINOR_HEADER_VERSION >= 4
  D3DWDDM1_3DDI_RESOURCE_MISC_CROSS_ADAPTER                 = 0x00002000L,
  D3DWDDM1_3DDI_RESOURCE_MISC_TILED                         = 0x00004000L,
  D3DWDDM1_3DDI_RESOURCE_MISC_TILE_POOL                     = 0x00008000L,
#endif 
#if D3D11DDI_MINOR_HEADER_VERSION >= 5
  D3DWDDM2_0DDI_RESOURCE_MISC_HW_PROTECTED                  = 0x00010000L,
  D3DWDDM2_0DDI_RESOURCE_MISC_DISPLAYABLE_SURFACE           = 0x00020000L,
  D3DWDDM2_0DDI_RESOURCE_MISC_CONTAINS_HW_PROTECTED         = 0x00040000L,
#endif 
  
} D3D10_DDI_RESOURCE_MISC_FLAG;
````


## -enum-fields
<dl>

### -field D3D10_DDI_RESOURCE_AUTO_GEN_MIP_MAP

<dd>
<p>The resource can be used with the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-genmips.md">GenMips</a> function.</p>
</dd>

### -field D3D10_DDI_RESOURCE_MISC_SHARED

<dd>
<p>The resource can be shared by multiple devices and processes.</p>
</dd>

### -field D3D10_DDI_RESOURCE_MISC_DISCARD_ON_PRESENT

<dd>
<p>The resource is not required to persist across presentations. 
      </p>
<p>For more information about this value, see the Remarks section of the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-createresource.md">CreateResource(D3D10)</a> reference page.</p>
<p>Supported starting with Windows Server 2008, and Windows Vista with Service Pack 1 (SP1).</p>
</dd>

### -field D3D11_DDI_RESOURCE_MISC_DRAWINDIRECT_ARGS

<dd>
<p>The resource is a buffer that the runtime can use as the argument buffer in a call to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11ddi-drawindexedinstancedindirect.md">DrawIndexedInstancedIndirect</a>, <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11ddi-drawinstancedindirect.md">DrawInstancedIndirect</a>, or <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11ddi-dispatchindirect.md">DispatchIndirect</a> function.</p>
<p>Supported starting with Windows 7.</p>
</dd>

### -field D3D11_DDI_RESOURCE_MISC_BUFFER_ALLOW_RAW_VIEWS

<dd>
<p>The resource is a buffer on which the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11ddi-createshaderresourceview.md">CreateShaderResourceView(D3D11)</a> function can create a raw-format view. A raw-format view is created through a call to the driver's <b>CreateShaderResourceView(D3D11)</b> function with the D3D11_DDI_BUFFEREX_SRV_FLAG_RAW flag set in the <b>BufferEx</b> member of the <a href="..\d3d10umddi\ns-d3d10umddi-d3d11ddiarg-createshaderresourceview.md">D3D11DDIARG_CREATESHADERRESOURCEVIEW</a> structure. Raw-format views allow to read (and write in the case of unordered access view (UAV) objects) up to four DWORD values in one instruction.</p>
<p>Supported starting with Windows 7.</p>
<p>Supported in Windows 7 and later versions.</p>
</dd>

### -field D3D11_DDI_RESOURCE_MISC_BUFFER_STRUCTURED

<dd>
<p>The resource is a buffer that has its memory sectioned into equally sized pieces (structures). The structure size of each piece is provided in the resource declaration. The drivers might be able to use this information to optimize memory layout.</p>
<p>Supported starting with Windows 7.</p>
</dd>

### -field D3D11_DDI_RESOURCE_MISC_RESOURCE_CLAMP

<dd>
<p>The resource must consider any resource clamp, which a call to the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11ddi-setresourceminlod.md">SetResourceMinLOD</a> function applies.</p>
<p>Supported starting with Windows 7.</p>
</dd>

### -field D3D10_DDI_RESOURCE_MISC_REMOTE

<dd>
<p>This value is for internal use only. Do not use. </p>
</dd>

### -field D3D11_1DDI_RESOURCE_MISC_RESTRICTED_CONTENT

<dd>
<p>The resource can contain protected content. This value should be used only if the driver and hardware support content protection.</p>
<p>Supported starting with Windows 8.</p>
</dd>

### -field D3D11_1DDI_RESOURCE_MISC_RESTRICT_SHARED_RESOURCE_DRIVER

<dd>
<p>The driver should restrict access to the shared surface. This value should be used only when a shared surface is created. The process that is creating the surface is always allowed to open the shared resource.</p>
<p>Supported starting with Windows 8.</p>
</dd>

### -field D3DWDDM1_3DDI_RESOURCE_MISC_CROSS_ADAPTER

<dd>
<p>The resource is a shared cross-adapter resource.</p>
<p>The user-mode display driver should record information about the cross-adapter resource in a private driver data structure. The display miniport driver can call the <a href="..\d3dkmddi\nc-d3dkmddi-dxgkcb-gethandledata.md">DxgkCbGetHandleData</a> function  to retrieve this private data.</p>
<p>The DirectX graphics kernel subsystem calls the <a href="display.dxgkddidescribeallocation">DxgkDdiDescribeAllocation</a> function to get information on the cross-adapter resource when it needs to open the resource on another adapter. The display miniport must ensure that this information is correct.</p>
<p>Supported starting with Windows 8.1.</p>
</dd>

### -field D3DWDDM1_3DDI_RESOURCE_MISC_TILED

<dd>
<p>The resource is tiled. </p>
<p>Supported starting with Windows 8.1.</p>
</dd>

### -field D3DWDDM1_3DDI_RESOURCE_MISC_TILE_POOL

<dd>
<p>The resource is a tile pool.  Must be a buffer with <a href="..\d3d10umddi\ne-d3d10umddi-d3d10-ddi-resource-usage.md">D3D10_DDI_RESOURCE_USAGE</a> usage type <b>D3D10_DDI_USAGE_DEFAULT</b>.</p>
<p>Supported starting with Windows 8.1.</p>
</dd>

### -field D3DWDDM2_0DDI_RESOURCE_MISC_HW_PROTECTED

<dd>
<p>The resource should be created such that it will be protected by the hardware. </p>
<p>Supported starting with Windows 10.</p>
</dd>

### -field D3DWDDM2_0DDI_RESOURCE_MISC_DISPLAYABLE_SURFACE

<dd>
<p>The resource contains a displayable surface.</p>
<p>Supported starting with Windows 10.</p>
</dd>

### -field D3DWDDM2_0DDI_RESOURCE_MISC_CONTAINS_HW_PROTECTED

<dd>
<p>The decoder input buffer contains encrypted protected content. The hardware does not need to protect these buffers (as they are encrypted), but the driver may need to allocate these buffers differently so they can efficiently interact with their decryption hardware.</p>
<p>Supported starting with Windows 10.</p>
</dd>

### -field 

<dd></dd>
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
<dt>D3d10umddi.h (include D3d10umddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-createresource.md">CreateResource(D3D10)</a>
</dt>
<dt>
<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11ddi-createshaderresourceview.md">CreateShaderResourceView(D3D11)</a>
</dt>
<dt>
<a href="..\d3d10umddi\ne-d3d10umddi-d3d10-ddi-resource-usage.md">D3D10_DDI_RESOURCE_USAGE</a>
</dt>
<dt>
<a href="..\d3d10umddi\ns-d3d10umddi-d3d10ddiarg-createresource.md">D3D10DDIARG_CREATERESOURCE</a>
</dt>
<dt>
<a href="..\d3d10umddi\ns-d3d10umddi-d3d11ddiarg-createshaderresourceview.md">D3D11DDIARG_CREATESHADERRESOURCEVIEW</a>
</dt>
<dt>
<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11ddi-dispatchindirect.md">DispatchIndirect</a>
</dt>
<dt>
<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11ddi-drawindexedinstancedindirect.md">DrawIndexedInstancedIndirect</a>
</dt>
<dt>
<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11ddi-drawinstancedindirect.md">DrawInstancedIndirect</a>
</dt>
<dt>
<a href="..\d3dkmddi\nc-d3dkmddi-dxgkcb-gethandledata.md">DxgkCbGetHandleData</a>
</dt>
<dt>
<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-genmips.md">GenMips</a>
</dt>
<dt>
<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11ddi-setresourceminlod.md">SetResourceMinLOD</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3D10_DDI_RESOURCE_MISC_FLAG enumeration%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
