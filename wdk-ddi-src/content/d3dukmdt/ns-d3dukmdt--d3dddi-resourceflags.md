---
UID: NS.d3dukmdt._D3DDDI_RESOURCEFLAGS
title: D3DDDI_RESOURCEFLAGS
author: windows-driver-content
description: The D3DDDI_RESOURCEFLAGS structure identifies the type of resources to create in a call to the driver's CreateResource function.
old-location: display\d3dddi_resourceflags.htm
old-project: display
ms.assetid: a466a158-dacf-42cc-b2ad-8af5b2c6c7d5
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DDDI_RESOURCEFLAGS, D3DDDI_RESOURCEFLAGS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dukmdt.h
req.include-header: D3dumddi.h, D3dkmddi.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DDDI_RESOURCEFLAGS
req.alt-loc: d3dukmdt.h
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

# D3DDDI_RESOURCEFLAGS structure



## -description
<p>The D3DDDI_RESOURCEFLAGS structure identifies the type of resources to create in a call to the driver's <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-createresource.md">CreateResource</a> function.</p>


## -syntax

````
typedef struct _D3DDDI_RESOURCEFLAGS {
  union {
    struct {
      UINT RenderTarget  :1;
      UINT ZBuffer  :1;
      UINT Dynamic  :1;
      UINT HintStatic  :1;
      UINT AutogenMipmap  :1;
      UINT DMap  :1;
      UINT WriteOnly  :1;
      UINT NotLockable  :1;
      UINT Points  :1;
      UINT RtPatches  :1;
      UINT NPatches  :1;
      UINT SharedResource  :1;
      UINT DiscardRenderTarget  :1;
      UINT Video  :1;
      UINT CaptureBuffer  :1;
      UINT Primary  :1;
      UINT Texture;
      UINT CubeMap  :1;
      UINT Volume  :1;
      UINT VertexBuffer  :1;
      UINT IndexBuffer  :1;
      UINT DecodeRenderTarget  :1;
      UINT DecodeCompressedBuffer  :1;
      UINT VideoProcessRenderTarget  :1;
      UINT CpuOptimized  :1;
      UINT MightDrawFromLocked  :1;
      UINT Overlay  :1;
      UINT MatchGdiPrimary  :1;
      UINT InterlacedRefresh  :1;
      UINT TextApi  :1;
      UINT RestrictedContent  :1;
      UINT RestrictSharedAccess  :1;
    };
    UINT   Value;
  };
} D3DDDI_RESOURCEFLAGS;
````


## -struct-fields
<dl>

### -field <b>RenderTarget</b>

<dd>
<p>Setting this member is equivalent to setting the first bit of the 32-bit <b>Value</b> member (0x00000001).</p>
</dd>

### -field <b>ZBuffer</b>

<dd>
<p>A UINT value that specifies whether the surface is the z-buffer. The z-buffer contains bit-depth information that is used to determine which pixels are visible and which are obscured. The z-buffer contains information that cannot be displayed.</p>
<p>Setting this member is equivalent to setting the second bit of the 32-bit <b>Value</b> member (0x00000002).</p>
</dd>

### -field <b>Dynamic</b>

<dd>
<p>A UINT value that specifies whether the surface is updated frequently. This bit-field flag cannot be used with the <b>HintStatic</b> bit-field flag.</p>
<p>Setting this member is equivalent to setting the third bit of the 32-bit <b>Value</b> member (0x00000004).</p>
</dd>

### -field <b>HintStatic</b>

<dd>
<p>A UINT value that specifies whether the surface is updated infrequently but still must allow access. This bit-field flag cannot be used with the <b>Dynamic</b> bit-field flag.</p>
<p>Setting this member is equivalent to setting the fourth bit of the 32-bit <b>Value</b> member (0x00000008).</p>
</dd>

### -field <b>AutogenMipmap</b>

<dd>
<p>A UINT value that specifies whether the MIP-map sublevels for the surface are automatically generated.</p>
<p>Setting this member is equivalent to setting the fifth bit of the 32-bit <b>Value</b> member (0x00000010).</p>
</dd>

### -field <b>DMap</b>

<dd>
<p>A UINT value that specifies whether the surface is a displacement-map texture that the displacement-map sampler can sample in the tessellation unit.</p>
<p>Setting this member is equivalent to setting the sixth bit of the 32-bit <b>Value</b> member (0x00000020).</p>
</dd>

### -field <b>WriteOnly</b>

<dd>
<p>A UINT value that specifies whether the surface can only be written to. Read access from the surface might generate a general protection fault (GPF). If the surface is read from, the read results are not meaningful.</p>
<p>Setting this member is equivalent to setting the seventh bit of the 32-bit <b>Value</b> member (0x00000040).</p>
</dd>

### -field <b>NotLockable</b>

<dd>
<p>A UINT value that specifies whether the render target is lockable. This bit-field flag is set on the primary and the back buffers if the flipping chain is not lockable, or on any render target that is not lockable. The driver can then do background optimization. </p>
<p>Even if this flag is set, the surface can still be locked, so the driver must handle this situation. However, such locks are infrequent and are not expected to be fast.</p>
<p>The driver can also determine whether the depth or stencil buffer is lockable by the presence of this bit-field flag.</p>
<p>Setting this member is equivalent to setting the eighth bit of the 32-bit <b>Value</b> member (0x00000080).</p>
</dd>

### -field <b>Points</b>

<dd>
<p>A UINT value that specifies whether the surface contains vertex buffer data that can be used to render points and point sprites.</p>
<p>Setting this member is equivalent to setting the ninth bit of the 32-bit <b>Value</b> member (0x00000100).</p>
</dd>

### -field <b>RtPatches</b>

<dd>
<p>A UINT value that specifies whether the surface contains vertex buffer data that can be used to render rt-patches.</p>
<p>Setting this member is equivalent to setting the tenth bit of the 32-bit <b>Value</b> member (0x00000200).</p>
</dd>

### -field <b>NPatches</b>

<dd>
<p>A UINT value that specifies whether the surface contains vertex buffer data that can be used to render n-patches.</p>
<p>Setting this member is equivalent to setting the eleventh bit of the 32-bit <b>Value</b> member (0x00000400).</p>
</dd>

### -field <b>SharedResource</b>

<dd>
<p>A UINT value that specifies whether multiple devices and processes share the surface.</p>
<p>Setting this member is equivalent to setting the twelfth bit of the 32-bit <b>Value</b> member (0x00000800).</p>
</dd>

### -field <b>DiscardRenderTarget</b>

<dd>
<p>A UINT value that specifies whether the preservation of the surface is required. If the surface is used as a render target, its preservation is not required. </p>
<p>Setting this member is equivalent to setting the thirteenth bit of the 32-bit <b>Value</b> member (0x00001000).</p>
</dd>

### -field <b>Video</b>

<dd>
<p>A UINT value that specifies whether the surface is a render target that contains video data.</p>
<p>Note that several render targets can be created with this flag, and if two or more of these render targets belong to the same Microsoft Direct3D context, the driver determines that these render targets should all display the same video stream regardless of whether the render target surfaces are attached to each other.</p>
<p>Setting this member is equivalent to setting the fourteenth bit of the 32-bit <b>Value</b> member (0x00002000).</p>
</dd>

### -field <b>CaptureBuffer</b>

<dd>
<p>A UINT value that specifies whether the resource is a capture buffer.</p>
<p>Setting this member is equivalent to setting the fifteenth bit of the 32-bit <b>Value</b> member (0x00004000).</p>
</dd>

### -field <b>Primary</b>

<dd>
<p>A UINT value that specifies whether the surface is the primary surface--that is, whether the surface is currently visible to the user.</p>
<p>Setting this member is equivalent to setting the sixteenth bit of the 32-bit <b>Value</b> member (0x00008000).</p>
</dd>

### -field <b>Texture</b>

<dd>
<p>A UINT value that specifies whether the surface can be used as a texture.</p>
<p>Setting this member is equivalent to setting the seventeenth bit of the 32-bit <b>Value</b> member (0x00010000).</p>
</dd>

### -field <b>CubeMap</b>

<dd>
<p>A UINT value that specifies whether the surface is a cubic-environment map. This bit-field flag requires that the <b>Texture</b> bit-field flag is set.</p>
<p>Setting this member is equivalent to setting the eighteenth bit of the 32-bit <b>Value</b> member (0x00020000).</p>
</dd>

### -field <b>Volume</b>

<dd>
<p>A UINT value that specifies whether the surface has depth, in addition to width and height--that is, whether the surface is a volume. This bit-field flag requires that the <b>Texture</b> bit-field flag is set.</p>
<p>Setting this member is equivalent to setting the nineteenth bit of the 32-bit <b>Value</b> member (0x00040000).</p>
</dd>

### -field <b>VertexBuffer</b>

<dd>
<p>A UINT value that specifies whether the surface is a vertex buffer (that is, stores vertices).</p>
<p>Setting this member is equivalent to setting the twentieth bit of the 32-bit <b>Value</b> member (0x00080000).</p>
</dd>

### -field <b>IndexBuffer</b>

<dd>
<p>A UINT value that specifies whether the surface is an index buffer (that is, stores indices).</p>
<p>Setting this member is equivalent to setting the twenty-first bit of the 32-bit <b>Value</b> member (0x00100000).</p>
</dd>

### -field <b>DecodeRenderTarget</b>

<dd>
<p>A UINT value that specifies whether the surface is used as a render target for Microsoft DirectX Video Acceleration (DirectX VA) decoding. </p>
<p>Setting this member is equivalent to setting the twenty-second bit of the 32-bit <b>Value</b> member (0x00200000).</p>
</dd>

### -field <b>DecodeCompressedBuffer</b>

<dd>
<p>A UINT value that specifies whether the surface contains compressed buffer information for DirectX VA decoding.</p>
<p>Setting this member is equivalent to setting the twenty-third bit of the 32-bit <b>Value</b> member (0x00400000).</p>
</dd>

### -field <b>VideoProcessRenderTarget</b>

<dd>
<p>A UINT value that specifies whether the surface is used as a render target for DirectX VA video processing.</p>
<p>Setting this member is equivalent to setting the twenty-fourth bit of the 32-bit <b>Value</b> member (0x00800000).</p>
</dd>

### -field <b>CpuOptimized</b>

<dd>
<p>A UINT value that specifies whether the CPU frequently accesses the resource.</p>
<p>The driver should place the resource in a memory pool that the CPU can quickly access (for example, AGP memory). The display miniport driver should flag the memory as cacheable by setting the <b>Cached</b> bit-field flag in the <b>Flags</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff560960">DXGK_ALLOCATIONINFO</a> structure when its <a href="display.dxgkddicreateallocation">DxgkDdiCreateAllocation</a> function is called. </p>
<p>The <b>CpuOptimized</b> flag is typically set for render targets (both stand-alone render targets and textures).</p>
<p>Setting this member is equivalent to setting the twenty-fifth bit of the 32-bit <b>Value</b> member (0x01000000).</p>
</dd>

### -field <b>MightDrawFromLocked</b>

<dd>
<p>A UINT value that specifies whether the driver is possibly requested to draw from a vertex buffer even if the vertex buffer is locked by the Direct3D runtime. This request means that the driver can, on occasion, receive calls to its <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-drawindexedprimitive.md">DrawIndexedPrimitive</a>, <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-drawindexedprimitive2.md">DrawIndexedPrimitive2</a>, <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-drawprimitive.md">DrawPrimitive</a>, and <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-drawprimitive2.md">DrawPrimitive2</a> functions where the vertex data is referenced within a locked vertex buffer that is marked with <b>MightDrawFromLocked</b>. The runtime must make these types of calls in scenarios in which it performs software transform and lighting (rather than hardware). These scenarios do not typically occur. </p>
<p>However, because the runtime locked the vertex buffer, the driver cannot call the <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-unlockcb.md">pfnUnlockCb</a> function before calling the <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-rendercb.md">pfnRenderCb</a> function. As a result, the driver must support the vertex buffer in a system or AGP memory segment; otherwise, the video memory manager rejects the rendering. The driver is not required to take any other special action because the runtime will not overwrite any data in the locked vertex buffer when the hardware actively renders from the vertex buffer. </p>
<p>Setting this member is equivalent to setting the twenty-sixth bit of the 32-bit <b>Value</b> member (0x02000000).</p>
</dd>

### -field <b>Overlay</b>

<dd>
<p>A UINT value that specifies whether the resource is an overlay.</p>
<p>Setting this member is equivalent to setting the twenty-seventh bit of the 32-bit <b>Value</b> member (0x04000000).</p>
</dd>

### -field <b>MatchGdiPrimary</b>

<dd>
<p>A UINT value that specifies whether the resource is a primary surface that matches all the properties of the current GDI primary surface that was created by using the <a href="https://msdn.microsoft.com/library/windows/hardware/ff546177">D3DKMDT_SHAREDPRIMARYSURFACEDATA</a> structure. For example, flipping from the matching primary surface to the current GDI primary surface and vice versa is possible.</p>
<p>Setting this member is equivalent to setting the twenty-eighth bit of the 32-bit <b>Value</b> member (0x08000000).</p>
</dd>

### -field <b>InterlacedRefresh</b>

<dd>
<p>A UINT value that specifies whether the resource is a primary surface that is meant to be used in an interlaced display mode.</p>
<p>Setting this member is equivalent to setting the twenty-ninth bit of the 32-bit <b>Value</b> member (0x10000000).</p>
</dd>

### -field <b>TextApi</b>

<dd>
<p>A UINT value that specifies whether the resource can be used for texture filtering or as an input stream source. If textures are created with the <b>TextApi</b> bit-field flag set, they cannot be used for texture filtering. If vertex buffers are created with the <b>TextApi</b> bit-field flag set, they cannot be used as input stream sources. The <b>TextApi</b> bit-field flag must be specified for vertex buffers and source surfaces that are used in calls to the <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-composerects.md">ComposeRects</a> function. </p>
<p>Setting this member is equivalent to setting the thirtieth bit of the 32-bit <b>Value</b> member (0x20000000).</p>
</dd>

### -field <b>RestrictedContent</b>

<dd>
<p>Supported in Windows 7 and later versions.</p>
<p>A UINT value that specifies whether the resource contains protected content. In most situations, an application has explicitly enabled content protection before the application creates a restricted resource. However, the application does not have to explicitly enable content protection if it creates a restricted fullscreen exclusive mode swapchain.</p>
<p>Setting this member is equivalent to setting the thirty-first bit of the 32-bit <b>Value</b> member (0x40000000).</p>
</dd>

### -field <b>RestrictSharedAccess</b>

<dd>
<p>Supported in Windows 7 and later versions.</p>
<p>A UINT value that specifies whether the runtime allows only specific processes  access to the shared resource. </p>
<p>Setting this member is equivalent to setting the thirty-second bit of the 32-bit <b>Value</b> member (0x80000000).</p>
</dd>

### -field <b>Value</b>

<dd>
<p>A 32-bit value that identifies the type of resource to create.</p>
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
<dt>D3dukmdt.h (include D3dumddi.h or D3dkmddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-createresource.md">CreateResource</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff542963">D3DDDIARG_CREATERESOURCE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DDDI_RESOURCEFLAGS structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
